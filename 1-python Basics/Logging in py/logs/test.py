from logger import logging

def add(a,b):

    logging.debug("The addition operation is taking place")
    return a+b


logging.debug("The addtion function is called")
logging.error("This is to test it works")
add(10,15)