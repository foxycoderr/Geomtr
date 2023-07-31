from logger import Logger


class Tokenizer:
    @staticmethod
    def split_text(text):
        text = text.lower()
        sentence_list = text.split(".")
        Logger.log("Split text", "tokenizer")
        return sentence_list

    @staticmethod
    def split_sentence(sentence):
        sentence = sentence.strip()
        words_list = sentence.split(" ")
        Logger.log("Split sentence", "tokenizer")
        return words_list
