from input import Input
from logger import Logger
from parser import Parser
from tokenizer import Tokenizer
from converter import Converter, Point
from coordinator import Coordinator
from datetime import datetime
import os
import time
import json


class Runner:  # main runner class, brings all functions of the program together
    def __init__(self):
        self.version = "0.0"  # program attributes
        self.release_date = "N/A"
        log_file_exists = os.path.isfile("log")  # check if log file exists
        user_data_exists = os.path.isfile("user_data.json")  # check is user data file exists
        if not log_file_exists:  # checks if there is a local log file, creates if there isn't
            logfile = open("log", "x")
            Logger.log(f"Create logfile", "main")
        if not user_data_exists:
            user_settings_file_creation = open("user_data.json", "x")
            user_data = dict()
            user_data["username"] = os.getlogin()  # add the data upon file creation
            user_data["debug_mode"] = False
            user_data["history"] = []
            with open("user_data.json", "w") as f:
                json.dump(user_data, f, indent=4)
            Logger.log("Create user data file", "main")
            self.username = os.getlogin()  # save new data into class attributes
            self.debug_mode = False
            self.history = []
        else:
            self.update_class_data()  # check docs for this func below

    def update_class_data(self):  # called when use data is updated
        with open("user_data.json", "r") as f:
            user_data = json.load(f)
        self.username = user_data["username"]  # update class attributes according to the settings file
        self.debug_mode = user_data["debug_mode"]
        self.history = user_data["history"]
        f.close()

    def main(self):  # main function of the program (diagram drawing)
        if Logger.log_length() > 50:
            Logger.clear_log()

        Logger.log("Starting main function.", "main")
        dbm = self.debug_mode
        problem = Input.input_problem(dbm)  # input of problem

        if problem == "exit":
            print("Exiting problem input.")
            self.command_input()

        if dbm:  # this variable is passed to almost every function, if it's true, some logs get printed into the console as well as the logfile
            print("Debug mode is turned on; debugging logs will be printed. Run 'debug' to toggle it.")
        valid = Input.validate(problem, dbm)  # initial validation of input

        parser = Parser()  # initialise parser
        if valid:
            sentence_list = Tokenizer.split_text(problem)  # split text into sentences
            for sentence in sentence_list:
                sentence = Tokenizer.split_sentence(sentence)  # split sentence into words

                object_kws = parser.find_objects(sentence, dbm)  # finding object keywords
                property_kws = parser.find_properties(sentence, dbm)  # finding property keywords

                valid = Converter.validate(object_kws, property_kws, dbm)  # additional logic validation

                if valid:
                    [objects, properties] = Converter.convert_objects(object_kws, dbm)  # converting keywords to classes
                    [properties, objects] = Converter.convert_properties(property_kws, objects, properties, dbm)

                    # Creation of coordinates by default off for now due to incompleteness of the module
                    # Errors may arise if uncommented
                    coordinates = Coordinator.create_coordinates(objects, properties)

                    """ ❗❗❗ Make sure this next part stays the last thing after drawing diagram. ❗❗❗ """

                    with open("user_data.json", "r") as f:
                        data = json.load(f)

                    history = data["history"]  # update history
                    date = f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year}"
                    history.append([str(len(history)+1), problem, date])

                    with open("user_data.json", "w") as f:
                        json.dump(data, f, indent=4)
                    f.close()

                    self.update_class_data()  # update class attributes
                else:
                    print("Logic validation failed. Please edit the problem text and fix errors outlined above, then try again. ")

        else:
            print("Parsing failed. Please edit the problem text and fix errors outlined above, then try again. ")

        Logger.blank_line()
        self.command_input()  # ready for next command

    def debug_toggle(self):  # toggles debug mode
        with open("user_data.json", "r") as f:
            data = json.load(f)
        data["debug_mode"] = not data["debug_mode"]

        if data["debug_mode"]:
            toggle = "on"
        else:
            toggle = "off"
        print(f"Debug mode turned {toggle}.")

        with open("user_data.json", "w") as f:
            json.dump(data, f)
        self.update_class_data()  # update class attributes

    def history_display(self, arg):  # prints history
        arg = arg[8:]
        if not arg.isnumeric():  # if no ID arg is given, just display list
            print("ID " + " | " + "Problem Text" + 38*" " + " | " + "Date")  # top row
            print(63*"-")  # separator
            for problem in self.history:  # lengthening or shortening
                index = str(problem[0])
                if len(index) < 3:
                    index = index + " "*(3-len(index))
                if len(index) > 3:  # TODO: get rid of this over 999 thing
                    index = "over 999"  # this is ugly sorry :(

                problem_text = problem[1]  # next block of code makes the preview exactly 50 chars
                if len(problem_text) > 47:
                    problem_text = problem_text[:47] + "..."
                if len(problem_text) < 47:
                    problem_text += " "*(50-len(problem_text))

                date = problem[2]

                print(index + " | " + problem_text + " | " + date)  # prints row
            print()
            print("To see a description fully, run 'history <problem_id>', for example 'history 3'. ")
        else:  # if problem ID is given
            arg = int(arg)
            try:
                problem = self.history[arg-1]
                print(problem[1])  # return full problem
            except IndexError:
                print("Invalid problem ID. Please run 'history' to see all saved problems. ")

    def program_info(self):
        print(f"Version: {self.version}")
        print(f"Release Date: {self.release_date}")
        print("Author: FoxyCoder")
        self.command_input()

    def program_start(self):
        print("Welcome to Geomtr. Use 'help' to get information on how to use the program.")
        self.command_input()

    def help(self):
        print("Geomtr is very simple to use. These are the commands it recognizes: ")
        print("help - display this message")
        print("start - run the main draw-diagram script")
        print("history - show your diagram description history")
        print("info - display version, release date etc. ")
        print("debug - toggle debug mode")
        print("exit - close the program. ")
        print("Commands do not take arguments (additional information to run them); just type in the command, hit enter, and the system wil guide you. ")
        self.command_input()

    @staticmethod
    def exit():
        print("Thank you for using Geomtr. This window will close automatically in 3 seconds. ")
        time.sleep(3)
        exit(0)

    def command_input(self):  # command is called after the use of any other command, creates the terminal-like UI
        command = input(">>> ").lower().strip()

        match command:
            case "help":
                self.help()
            case "start":
                self.main()
            case "info":
                self.program_info()
            case "exit":
                self.exit()
            case "debug":
                self.debug_toggle()
            case _:
                if command.startswith("history"):
                    self.history_display(command)
                else:
                    print("That's not a valid command. Run 'help' to see a list of them. \n")

        self.command_input()


runner = Runner()
Logger.blank_line()
Logger.blank_line()
Logger.plain_log(f"Starting program at {datetime.now()}.")
Logger.blank_line()
runner.program_start()


