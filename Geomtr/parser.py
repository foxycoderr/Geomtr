from logger import Logger


class Parser:
    def __init__(self):
        self.keywords = ["rectangle", "triangle", "point"]

    def find_keywords(self, sentence):
        Logger.log("Started keyword find", "parser")

        keywords = []
        index = 0
        for word in sentence:
            if word in self.keywords:
                Logger.log(f"Found keyword {word}.", "parser")
                point_name = sentence[index+1]
                keywords.append([word, point_name])

            index += 1

        Logger.log("Keywords parsed", "parser")
        Logger.log(keywords, "parser")



