import time


def generate_unique_name():
    """This method should be static"""
    return "repository" + str(time.time()).replace(".", "-")
