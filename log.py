from loguru import logger
import time
import sys

def calc(a, b):
    result = a + b
    logger.info("Params {} + {} = {}".format(a, b, result))
    start = time.time()
    end = time.time()
    prog_time = end - start
    logger.info("Time = {}".format(prog_time))
    return result

logger.add("file.log", rotation="10 MB")
calc(10, 20)

