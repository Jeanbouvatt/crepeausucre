#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Service I """

import base64
import logging
from logging.handlers import RotatingFileHandler
import pprint
import time
import sys
import os
import mysql.connector 
from flask import Flask
from flask import jsonify
from flask import request
import config

# Initialise Flask
app = Flask(__name__)
app.debug = True

# Affect app logger to a global variable so logger can be used elsewhere.
config.logger = app.logger


@app.route("/login/<id>")
def api_login(id):

    """Check if user <id> is registered"""
    config.logger.info("*** Start processing id %s ***", id)

    mysql_connector = mysql.connector.connect(host=config.i.conf_file.get_sql_hostname(), \
                                             user=config.i.conf_file.get_sql_username(), \
                                             password=config.i.conf_file.get_sql_password(), \
                                             database=config.i.conf_file.get_sql_database())

    cursor = mysql_connector.cursor()

    cursor.execute("SELECT COUNT(*) FROM users WHERE users.id = " + str(id))
    response = cursor.fetchall()
    if response[0][0] == 1:
        config.logger.info("*** %s is in the database ***", id)
        data = {"msg": "ok"}
        resp = jsonify(data)
        resp.status_code = 200
    else:
        config.logger.info("*** %s is unknown ***", id)
        data = {"msg": "pas ok"}
        resp = jsonify(data)
        resp.status_code = 401

    cursor.close()
    mysql_connector.close()

    config.logger.info("*** End processing id %s ***", id)        
    add_headers(resp)
    return resp


@app.route("/shutdown", methods=["POST"])
def shutdown():
    """Shutdown server"""
    shutdown_server()
    config.logger.info("Stopping %s...", config.i.NAME)
    return "Server shutting down..."


@app.route("/", methods=["GET"])
def api_root():
    """Root url, provide service name and version"""
    data = {
        "Service": config.i.NAME,
        "Version": config.i.VERSION
    }

    resp = jsonify(data)
    resp.status_code = 200

    resp.headers["AuthorSite"] = "https://github.com/Jeanbouvatt/crepeausucre"

    add_headers(resp)
    return resp

def shutdown_server():
    """shutdown server"""
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()


def configure_logger(logger, logfile):
    """Configure logger"""
    formatter = logging.Formatter(
        "%(asctime)s :: %(levelname)s :: %(message)s")
    file_handler = RotatingFileHandler(logfile, "a", 1000000, 1)

    # Add logger to file
    if (config.i.conf_file.get_i_debug().title() == 'True'):
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')


if __name__ == "__main__":
    # Vars
    app_logfile = "i.log"

    # Change diretory to script one
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except FileNotFoundError:
        pass

    # Define a PrettyPrinter for debugging.
    pp = pprint.PrettyPrinter(indent=4)

    # Initialise apps
    config.initialise_i()

    # Configure Flask logger
    configure_logger(app.logger, app_logfile)

    config.logger.info("Starting %s", config.i.NAME)
    app.run(port=int(config.i.conf_file.get_i_port()), host='0.0.0.0')
