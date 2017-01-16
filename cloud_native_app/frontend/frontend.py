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
import requests
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


@app.route("/<id>")
def api_login(id):

    """Check if user <id> is registered"""
    config.logger.info("*** Start processing id %s ***", id)

    html_result = ""

    # Get i
    try:
        r = requests.get("http://localhost:8091/login/"+str(id))
        if r.status_code == 200:
            html_result += "<p>Bienvenue from I</p>"
        else:
            html_result += "<p>Unknown user</p>"
    except:
        html_result += "<p>I not responding</p>"

    # Get s
    try:
        r = requests.get("http://localhost:8092/status/"+str(id))
        if r.status_code == 200:
            html_result += "<p>You haven't played already</p>"
        else:
            html_result += "<p>You have already played</p>"
    except:
        html_result += "<p>S not responding</p>"

    # Get b
    try:
        r = requests.get("http://localhost:8093/button"+str(id))
        if r.status_code == 200:
            html_result += ""

    return html_result


@app.route("/shutdown", methods=["POST"])
def shutdown():
    """Shutdown server"""
    shutdown_server()
    config.logger.info("Stopping %s...", config.frontend.NAME)
    return "Server shutting down..."


@app.route("/", methods=["GET"])
def api_root():
    """Root url, provide service name and version"""
    data = {
        "Service": config.frontend.NAME,
        "Version": config.frontend.VERSION
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
    if (config.frontend.conf_file.get_debug().title() == 'True'):
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
    app_logfile = "frontend.log"

    # Change diretory to script one
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except FileNotFoundError:
        pass

    # Define a PrettyPrinter for debugging.
    pp = pprint.PrettyPrinter(indent=4)

    # Initialise apps
    config.initialise_frontend()

    # Configure Flask logger
    configure_logger(app.logger, app_logfile)

    config.logger.info("Starting %s", config.frontend.NAME)
    app.run(port=int(config.frontend.conf_file.get_port()), host='0.0.0.0')
