""" Tokenizer """
from logger import Logger


class Tokenizer:
    """ Very simple class to split text and sentences, probably not very necessary. """

    @staticmethod
    def split_text(text):
        """ Splits problem text into sentences. """
        text = text.lower()
        sentence_list = text.split(".")
        Logger.log("Split text", "tokenizer")
        return sentence_list

    @staticmethod
    def split_sentence(sentence):
        """ Splits sentences into words. """
        sentence = sentence.strip()
        words_list = sentence.split(" ")
        Logger.log("Split sentence", "tokenizer")
        return words_list
