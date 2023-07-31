from input import Input
from logger import Logger
from parser import Parser
from tokenizer import Tokenizer
from datetime import datetime
import os


class Runner:
    def __init__(self):
        self.version = "0.0"
        log_file_exists = os.path.isfile("log")
        if log_file_exists is False:
            logfile = open("log", "x")

    @staticmethod
    def main():
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


runner = Runner()
Logger.space()
Logger.space()
Logger.freelog(f"Starting program at {datetime.now()}.")
Logger.space()
runner.main()


