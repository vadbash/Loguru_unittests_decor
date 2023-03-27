import requests
from loguru import logger
import time

#finish output
def link_site(link):
    url = f"{link}"
    res = requests.get(url)
    logger.info(f"Link = {link}, response = {res}")
    return res

#logger params
logger.add("file.log", rotation="10 MB")
start = time.time()
#test link
link_site("https://github.com/")
end = time.time()
prog_time = end - start
logger.info("Time = {}".format(prog_time))

