from datetime import datetime


class Logger:
    """ Operates with the log file. """

    @staticmethod
    def log(log_text, module):
        logfile = open("log", "a")
        timestamp = datetime.now()
        log_text = f"{module}-{timestamp}: {log_text} \n"
        logfile.write(log_text)
        logfile.close()

    @staticmethod
    def read_log():
        logfile = open("log", "r")
        text = logfile.read()
        logfile.close()
        return text

    @staticmethod
    def space():
        logfile = open("log", "a")
        logfile.write("\n")
        logfile.close()

    @staticmethod
    def freelog(log_text):
        logfile = open("log", 'a')
        logfile.write(log_text)
        logfile.close()

