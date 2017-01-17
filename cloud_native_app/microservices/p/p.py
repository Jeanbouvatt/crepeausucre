#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Service W define the price won by a customer"""

import base64
import logging
from logging.handlers import RotatingFileHandler
import pprint
import os
import sqlite3 
import time
import subprocess
import sys
from flask import Flask
from flask import jsonify
from flask import request
import config

# Initialise Flask
app = Flask(__name__)
app.debug = True

# Affect app logger to a global variable so logger can be used elsewhere.
config.logger = app.logger


@app.route("/get_price/<id>")
def get_price(id):
    try:
        """Send the price of the user"""

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        try:
            c.execute("CREATE TABLE users (id INT, image TEXT)")
        except:
            pass

        c.execute("SELECT image FROM users WHERE users.id = " + str(id))
        response = c.fetchone()
        data = 0
        if response == None:
            data = {"msg": "noprice"}
        else:
            data = {"msg": response[0]}
        resp = jsonify(data)
        resp.status_code = 200

        conn.commit()
        conn.close()
        add_headers(resp)
        return resp
    except:
        resp = jsonify({"msg": "bug"})
        resp.status_code = 500
        return resp

@app.route("/set_price/<id>/<price>")
def set_price(id, price):
    try:
        """Set the price of the user"""
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        try:
            c.execute("CREATE TABLE users (id INT, image TEXT)")
        except:
            pass

        c.execute("DELETE FROM users WHERE users.id = " + str(id))
        c.execute("INSERT INTO users VALUES(" + str(id) + ",'" + price + "')")
        conn.commit()
        conn.close()
        data = {"msg": "ok"}
        resp = jsonify(data)
        add_headers(resp)
        resp.status_code = 200
        return resp
    except:
        resp = jsonify({"msg": "bug"})
        resp.status_code = 500
        return resp

@app.route("/shutdown", methods=["POST"])
def shutdown():
    """Shutdown server"""
    shutdown_server()
    config.logger.info("Stopping %s...", config.p.NAME)
    return "Server shutting down..."


@app.route("/", methods=["GET"])
def api_root():
    """Root url, provide service name and version"""
    data = {
        "Service": config.p.NAME,
        "Version": config.p.VERSION
    }

    resp = jsonify(data)
    resp.status_code = 200

    resp.headers["AuthorSite"] = "https://github.com/uggla/openstack_lab"

    add_headers(resp)
    return resp


def listprices(path):
    onlyfiles = [f for f in os.listdir(path)
                 if os.path.isfile(os.path.join(path, f))]
    return onlyfiles


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
    if (config.p.conf_file.get_p_debug().title() == 'True'):
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
    app_logfile = "p.log"

    # Change diretory to script one
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except FileNotFoundError:
        pass

    # Define a PrettyPrinter for debugging.
    pp = pprint.PrettyPrinter(indent=4)

    # Initialise apps
    config.initialise_p()

    # Configure Flask logger
    configure_logger(app.logger, app_logfile)

    config.logger.info("Starting %s", config.p.NAME)
    app.run(port=int(config.p.conf_file.get_p_port()), host='0.0.0.0')
