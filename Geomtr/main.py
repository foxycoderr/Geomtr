from input import Input
from logger import Logger
from parser import Parser
from tokenizer import Tokenizer
from datetime import datetime
import os
import time


class Runner:
    def __init__(self):
        self.version = "0.0"
        self.release_date = "N/A"
        log_file_exists = os.path.isfile("log")
        if log_file_exists is False:
            logfile = open("log", "x")

    def main(self):
        Logger.log("Starting main function", "main")
        print("Initiating problem parsing and drawing...")
        problem = Input.input_problem()
        valid = Input.validate(problem)

        parser = Parser()
        if valid:
            sentence_list = Tokenizer.split_text(problem)
            for sentence in sentence_list:
                sentence = Tokenizer.split_sentence(sentence)

                parser.find_keywords(sentence)

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
        print("main - run the main parse-and-draw-diagram script")
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

    def command_input(self):
        command = input(">>> ")

        match command:
            case "help":
                self.help()
            case "main":
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


