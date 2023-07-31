from logger import Logger


class Input:

    @staticmethod
    def input_problem():
        problem = input("Please paste or type your problem here... ")
        print("Problem received. Please wait...")
        Logger.log("Problem text put in", "input")
        return problem

    @staticmethod
    def validate(text):
        print("Validating problem text... ")
        Logger.log("Started text validation", "input")
        text = list(text)

        valid = True
        errors = []
        for symbol in text:
            symbol_ascii_code = ord(symbol)
            if symbol_ascii_code < 32 or symbol_ascii_code > 126:
                valid = False
                errors.append(f"Symbol '{symbol}' does not appear to be an English letter, number, or punctuation sign.")
                Logger.log("Found issue in validation", "input")

        if valid is True:
            print("Problem validated, no issues found. Proceeding to parse...")
            Logger.log("Validation OK", "input")
        else:
            print("Problem text appears to be invalid. Following issues were found: ")
            for error in errors:
                print(error)
            Logger.log("Validation fail", "input")

        return valid

