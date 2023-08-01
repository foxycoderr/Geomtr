from input import Input
from logger import Logger
from parser import Parser
from tokenizer import Tokenizer
from converter import Converter
from datetime import datetime
import os
import time


class Runner:  # main runner class, brings all functions of the program together
    def __init__(self):
        self.version = "0.0"
        self.release_date = "N/A"
        log_file_exists = os.path.isfile("log")
        if log_file_exists is False:  # checks if there is a local log file, creates if there isn't
            logfile = open("log", "x")

    def main(self):
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
                print("That's not a valid command. Run 'help' to see a list of them. \n")

        self.command_input()


runner = Runner()
Logger.space()
Logger.space()
Logger.freelog(f"Starting program at {datetime.now()}.")
Logger.space()
runner.program_start()


