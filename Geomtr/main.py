from input import Input
from logger import Logger
from parser import Parser
from tokenizer import Tokenizer
from converter import Converter
from datetime import datetime
import os
import time
import json


class Runner:  # main runner class, brings all functions of the program together
    def __init__(self):
        self.version = "0.0"
        self.release_date = "N/A"
        log_file_exists = os.path.isfile("log")
        user_settings_exits = os.path.isfile("user_data.json")
        if not log_file_exists:  # checks if there is a local log file, creates if there isn't
            logfile = open("log", "x")
            Logger.log(f"Create logfile", "main")
        if not user_settings_exits:
            user_settings_file_creation = open("user_data.json", "x")
            user_data = dict()
            user_data["username"] = os.getlogin()
            user_data["debug_mode"] = False
            user_data["history"] = []
            with open("user_data.json", "w") as f:
                json.dump(user_data, f, indent=4)
            Logger.log("Create user data file", "main")
            self.username = os.getlogin()
            self.debug_mode = False
            self.history = []
        else:
            with open("user_data.json", "r") as f:
                user_data = json.load(f)
            self.username = user_data["username"]
            self.debug_mode = user_data["debug_mode"]
            self.history = user_data["history"]

    def main(self):  # TODO: implement debug mode setting
        Logger.log("Starting main function.", "main")
        problem = Input.input_problem()  # input of problem
        valid = Input.validate(problem)  # initial validation of input

        parser = Parser()  # initialise parser
        if valid:
            sentence_list = Tokenizer.split_text(problem)  # split text into sentences
            for sentence in sentence_list:
                sentence = Tokenizer.split_sentence(sentence)  # split sentence into words

                object_kws = parser.find_objects(sentence)  # finding object keywords
                property_kws = parser.find_properties(sentence)  # finding property keywords

                valid = Converter.validate(object_kws, property_kws)  # additional logic validation

                if valid:
                    [objects, properties] = Converter.convert_objects(object_kws)  # converting keywords to classes
                    properties = Converter.convert_properties(property_kws, objects, properties)
                else:
                    print("Logic validation failed. Please edit the problem text and fix errors outlined above, then try again. ")

        else:
            print("Parsing failed. Please edit the problem text and fix errors outlined above, then try again. ")

        Logger.space()
        print()
        self.command_input()

    def history_display(self, arg):
        arg = arg[8:]
        if not arg.isnumeric():
            for problem in self.history:
                print(str(problem[0]) + " | " + problem[1][:40] + "... | " + problem[2])
            print("To see a problem fully, run 'history <problem_id>', for example 'history 3'. The ID of each problem is in the right column.")
        else:
            arg = int(arg)
            try:
                problem = self.history[arg-1]
                print(problem[1])
            except IndexError:
                print("Invalid problem ID. Please run 'history' to see all saved problems. ")

    def program_info(self):
        print(f"Version: {self.version}")
        print(f"Release Date: {self.release_date}")
        print("Author: FoxyCoder")
        print("")
        self.command_input()

    def program_start(self):
        print("Welcome to Geomtr. Use 'help' to get information on how to use the program.")
        self.command_input()

    def help(self):
        print("Geomtr is very simple to use. These are the commands it recognizes: ")
        print("help - display this message")
        print("start - run the main draw-diagram script")
        print("history - show your problem history")
        print("info - display version, release date etc. ")
        print("exit - close the program. ")
        print("Commands do not take arguments (additional information to run them); just type in the command, hit enter, and the system wil guide you. ")
        print("")
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
            case _:
                if command.startswith("history"):
                    self.history_display(command)
                else:
                    print("That's not a valid command. Run 'help' to see a list of them. \n")

        self.command_input()


runner = Runner()
Logger.space()
Logger.space()
Logger.freelog(f"Starting program at {datetime.now()}.")
Logger.space()
runner.program_start()


