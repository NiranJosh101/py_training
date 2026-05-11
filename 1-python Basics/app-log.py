import logging


## config. logging
logging.basicConfig(
    # filename='app1.log',
    # filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s  %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True,
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger101=logging.getLogger("ArithmethicApp")

def add(a,b):
    result=a+b

    logger101.debug(f"Multiplying {a}+{b}, {result}")
    return result

def subtract(a,b):
    result=a-b

    logger101.debug(f"Multiplying {a}-{b}, {result}")
    return result

def multiply(a,b):
    result=a*b

    logger101.debug(f"Multiplying {a}*{b}, {result}")
    return result

def divide(a,b):
    try:
        result=a/b

        logger101.debug(f"Multiplying {a}/{b}, {result}")
        return result
    except ZeroDivisionError:
        logger101.error("Division by zero error")
        return None
    

add(10,15)
subtract(15,10)
multiply(10,7)
divide(20,0)