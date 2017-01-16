# coding=utf-8

import configparser
import mysql.connector 

# Initialise global variable
logger = None
frontend = None


def initialise_frontend():
    """Define frontend global object so it can be called from anywhere."""
    global frontend
    frontend = Frontend()


class Frontend(object):
    def __init__(self):
        self.NAME = "Frontend"
        self.VERSION = "0.1"
        #
        # Configuration file
        self.conf_file = iConfiguration("frontend.conf")


class iConfiguration(object):

    def __init__(self, configuration_file):
        self.config = configparser.ConfigParser(allow_no_value=True)
        self.config.read(configuration_file)

    def get_port(self):
        return self.config.get("frontend", "port")

    def get_debug(self):
        return self.config.get("frontend", "debug")

