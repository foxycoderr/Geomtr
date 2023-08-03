from logger import Logger


class Parser:  # parser that reads through the problem text and picks out key information
    def __init__(self):
        self.object_keywords = ["rectangle", "triangle", "point"]  # defining what to look for
        self.property_keywords = ["side", "angle"]

    def find_objects(self, sentence, dbm):
        """ Finds objects and their point names """
        Logger.log("Started object keyword find", "parser")

        keywords = []
        index = 0
        for word in sentence:
            if word in self.object_keywords:
                Logger.log(f"Found keyword {word}.", "parser")
                point_name = sentence[index+1]
                keywords.append([word, point_name])
            index += 1

        Logger.log("Object keywords parsed", "parser")
        Logger.log(keywords, "parser")

        return keywords

    def find_properties(self, sentence, dbm):
        """ Finds properties such as side lengths and angles of objects. """
        Logger.log("Started property keyword find", "parser")

        keywords = []
        index = 0
        for word in sentence:
            if word in self.property_keywords:
                Logger.log(f"Found property kw {word}", "parser")
                point_name = sentence[index+1]
                value = sentence[index+3]
                keywords.append([word, point_name, value])
            index += 1

        Logger.log("Property keywords parsed", "parser")
        Logger.log(keywords, "parser")
        if dbm: print("Parsing OK.")

        return keywords





