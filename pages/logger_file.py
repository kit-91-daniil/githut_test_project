from loguru import logger


logger.add("logs/debug/debug.log", format="{time:YY-MM-DD HH:mm:ss} {level:<6} {message} ",
           level="DEBUG", rotation="1 day", compression="zip")
logger.add("logs/error/error.log", format="{time:YY-MM-DD HH:mm:ss} {level:<6} {message} ",
           level="ERROR", rotation="1 day", compression="zip")


def logger_expect_true(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if result:
            logger.info(f"function -- {function.__name__:<30} --parameters args: "
                        f"{args[1:]} ")
        else:
            logger.debug(f"function -- {function.__name__:<30} -- parameters args: {args[1:]}")
        return result

    return wrapper


def logger_expect_no_error(function):
    def wrapper(*args, **kwargs):
        logger.info(f"Start TEST function -- {function.__name__:<30} --parameters args: "
                    f"{args[1:]} ")
        try:
            result = function(*args, **kwargs)
        except TypeError:
            pass
        except Exception as e:
            logger.error(f"TEST function -- {function.__name__:<30} -- parameters args: {args[1:]} "
                         f"-- {e}")
        else:
            logger.info(f"End TEST function -- {function.__name__:<30} --parameters args: "
                        f"{args[1:]} ")
            return result

    return wrapper

