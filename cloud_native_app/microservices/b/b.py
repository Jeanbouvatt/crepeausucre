#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Service B """

import base64
import logging
from logging.handlers import RotatingFileHandler
import pprint
import time
import sys
import os
from flask import Flask
from flask import jsonify
from flask import request
import config

# Initialise Flask
app = Flask(__name__)
app.debug = True

# Affect app logger to a global variable so logger can be used elsewhere.
config.logger = app.logger


@app.route("/get_button/<id>")
def get_button(id):

    try:
        config.logger.info("*** Start processing id %s ***", id)

        data = {"msg": "ok", "html":config.b.conf_file.get_w_protocol()+"://"+config.b.conf_file.get_w_hostname()+\
                                    ":" + config.b.conf_file.get_w_port() + "/" + config.b.conf_file.get_w_route() + "/" + str(id)}
        resp = jsonify(data)
        resp.status_code = 200

        config.logger.info("*** End processing id %s ***", id)        
        add_headers(resp)
        return resp
    except:        
        data = {"msg": "bug"}
        resp = jsonify(data)
        resp.status_code = 500
        return resp



@app.route("/shutdown", methods=["POST"])
def shutdown():
    """Shutdown server"""
    shutdown_server()
    config.logger.info("Stopping %s...", config.b.NAME)
    return "Server shutting down..."


@app.route("/", methods=["GET"])
def api_root():
    """Root url, provide service name and version"""
    data = {
        "Service": config.b.NAME,
        "Version": config.b.VERSION
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
    if (config.b.conf_file.get_b_debug().title() == 'True'):
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
    app_logfile = "b.log"

    # Change diretory to script one
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except FileNotFoundError:
        pass

    # Define a PrettyPrinter for debugging.
    pp = pprint.PrettyPrinter(indent=4)

    # Initialise apps
    config.initialise_b()

    # Configure Flask logger
    configure_logger(app.logger, app_logfile)

    config.logger.info("Starting %s", config.b.NAME)
    app.run(port=int(config.b.conf_file.get_b_port()), host='0.0.0.0')
