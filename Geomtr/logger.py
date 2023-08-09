from datetime import datetime


class Logger:  # operates with the log file

    @staticmethod
    def log(log_text, module):  # quickly log something; supposed to be used in other modules as Logger.log("message", "module_name")
        logfile = open("log", "a")
        timestamp = datetime.now()
        log_text = f"{module}-{timestamp}: {log_text} \n"
        logfile.write(log_text)
        logfile.close()

    @staticmethod
    def read_log():  # opens and returns the whole log
        logfile = open("log", "r")
        text = logfile.read()
        logfile.close()
        return text

    @staticmethod
    def blank_line():  # adds a blank line to the log
        logfile = open("log", "a")
        logfile.write("\n")
        logfile.close()

    @staticmethod
    def plain_log(log_text):  # allows plaintext logging (without mandatory date and source module of normal log func)
        logfile = open("log", 'a')
        logfile.write(log_text)
        logfile.close()

    @staticmethod
    def clear_log():  # clears logs
        logfile = open("log", "w")
        logfile.write("")
        logfile.close()

    @staticmethod
    def log_length():  # returns number of lines in log
        logfile = open("log", "r")
        log = list(logfile.read())
        count = 0
        for symbol in log:
            if symbol == "\n":
                count += 1
                logfile.close()
        return count+1
