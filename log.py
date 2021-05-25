import logging

def log_def_start(name):
    logging.basicConfig(filename='log.log',level=logging.DEBUG)
    logging.debug(f'    {name}--start!')

def log_def_over(name):
    logging.basicConfig(filename='log.log', level=logging.DEBUG)
    logging.debug(f'    {name}--over!')