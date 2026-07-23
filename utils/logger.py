import logging

def get_logger(name: str):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

        fileHandler = logging.FileHandler("logs/api.log")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

    return logger