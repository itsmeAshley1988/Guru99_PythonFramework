import logging

class LogGen:

    @staticmethod
    # creating a method
    def loggen():
        logging.basicConfig(filename=".//Logs//testLogs.log", format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger