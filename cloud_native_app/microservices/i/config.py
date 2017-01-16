# coding=utf-8

import configparser

# Initialise global variable
logger = None
i = None


def initialise_i():
    """Define i global object so it can be called from anywhere."""
    global i
    i = I()


class I(object):
    def __init__(self):
        self.NAME = "Microservice i"
        self.VERSION = "0.1"
        #
        # Configuration file
        self.conf_file = iConfiguration("i.conf")
        #self.mysql = mysql.connector.connect(host=self.conf_file.get_sql_hostname(), \
         #                                    user=self.conf_file.get_sql_username(), \
         #                                    password=self.conf_file.get_sql_password(), \
          #                                   database=self.conf_file.get_sql_database())


class iConfiguration(object):

    def __init__(self, configuration_file):
        self.config = configparser.ConfigParser(allow_no_value=True)
        self.config.read(configuration_file)

    def get_i_port(self):
        return self.config.get("i", "port")

    def get_sql_hostname(self):
        return self.config.get("sql", "hostname")

    def get_sql_username(self):
        return self.config.get("sql", "username")

    def get_sql_password(self):
        return self.config.get("sql", "password")

    def get_sql_database(self):
        return self.config.get("sql", "database")

    def get_i_debug(self):
        return self.config.get("i", "debug")
