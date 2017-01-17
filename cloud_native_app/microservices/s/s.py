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
import sqlite3
from flask import Flask
from flask import jsonify
from flask import request
import config

# Initialise Flask
app = Flask(__name__)
app.debug = True

# Affect app logger to a global variable so logger can be used elsewhere.
config.logger = app.logger


@app.route("/get_status/<id>")
def get_status(id):

    try:
        config.logger.info("*** Start processing id %s ***", id)

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        response = [[0]]

        try:
            c.execute("CREATE TABLE played (id INT)")
        except:
            pass

        c.execute("SELECT * FROM played WHERE played.id = " + str(id))
        response = c.fetchone()

        if response != None:
            config.logger.info("*** %s already played ***", id)
            data = {"msg": "deja joue"}
            resp = jsonify(data)
            resp.status_code = 401
        else:
            config.logger.info("*** %s has not played yet ***", id)
            data = {"msg": "Pas encore joue"}
            resp = jsonify(data)
            resp.status_code = 200

        conn.commit()
        conn.close()

        config.logger.info("*** End processing id %s ***", id)        
        add_headers(resp)
        return resp
    except:
        resp = jsonify({"msg": "bug"})
        resp.status_code = 500
        return resp

@app.route("/set_status/<id>")
def set_status(id):
    try:
        config.logger.info("*** Start processing id %s ***", id)

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        response = [[0]]

        try:
            c.execute("CREATE TABLE played (id INT)")
        except:
            pass

        c.execute("INSERT INTO played VALUES (" + str(id) + ")")
        response = c.fetchall()
        conn.commit()
        conn.close()
        resp = jsonify({"msg":"set status to 1 ok"})
        resp.status_code = 200
        config.logger.info("*** End processing id %s ***", id)        
        add_headers(resp)
        return resp
    except:        
        resp = jsonify({"msg": "bug"})
        resp.status_code = 500
        return resp




@app.route("/shutdown", methods=["POST"])
def shutdown():
    """Shutdown server"""
    shutdown_server()
    config.logger.info("Stopping %s...", config.s.NAME)
    return "Server shutting down..."


@app.route("/", methods=["GET"])
def api_root():
    """Root url, provide service name and version"""
    data = {
        "Service": config.s.NAME,
        "Version": config.s.VERSION
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
    if (config.s.conf_file.get_s_debug().title() == 'True'):
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
    app_logfile = "s.log"

    # Change diretory to script one
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except FileNotFoundError:
        pass

    # Define a PrettyPrinter for debugging.
    pp = pprint.PrettyPrinter(indent=4)

    # Initialise apps
    config.initialise_s()

    # Configure Flask logger
    configure_logger(app.logger, app_logfile)

    config.logger.info("Starting %s", config.s.NAME)
    app.run(port=int(config.s.conf_file.get_s_port()), host='0.0.0.0')
