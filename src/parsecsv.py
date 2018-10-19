import logging
from src.logexception.logframework import GenericLogger
from src.logexception.exceptionhandler import CustomInputError, MyZeroDivisionException, DataNotValidException
from src.config.config import PROJECT_DIR


def parse_csv_and_get_columns(filename, error_type):
    logger.info("Read the file")
    csv_file = open(filename, 'r')
    if csv_file is None:
        raise CustomInputError
    logger.info("Read lines from file")
    lines = csv_file.readlines()
    logger.debug(lines)
    logger.info("Loop through lines")
    for line in lines:
        logger.debug(line)
        val = line.split(",")
        if error_type == 0:
            try:
                test_str_div = val[0] / val[11]
                logger.debug(test_str_div)
            except TypeError:
                raise DataNotValidException
                pass
        if error_type == 1:
            try:
                logger.debug("The value at index 11 is {}".format(val[11]))
                test_zero_div = (int(val[0]) / int(val[11]))
                logger.debug(test_zero_div)
            except ZeroDivisionError:
                raise MyZeroDivisionException


if __name__ == "__main__":
    GenericLogger()
    logger = logging.getLogger(__name__)
    parse_csv_and_get_columns(PROJECT_DIR + "/data/test.csv", 1)