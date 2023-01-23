import logging


def test_logging():

    log = logging.getLogger(__name__)
    logfile = logging.FileHandler('logfile.log')
    log.addHandler(logfile)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :  %(message)s")
    logfile.setFormatter(formatter)
    log.setLevel(logging.INFO)
    log.debug("prints debug statement")
    log.info("print info statement")
    log.error("print error statement")
    log.warning("print warnign statement")
    log.critical("print critical statement")