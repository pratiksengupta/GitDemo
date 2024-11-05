import logging

def test_loggingDemo():
    logger=logging.getLogger(__name__)#(__name__)is for capturing the file name



    filehandler = logging.FileHandler('logfile.log')

    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)
    logger.debug("It's a debug message")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")