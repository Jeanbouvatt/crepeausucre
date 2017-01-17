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



@app.route("/create/<id>/<name>/<email>")
def api_create(id,name,email):
    try:
        """Create user <id>"""

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        response = [[0]]

        try:
            c.execute("CREATE TABLE users (id INT, nom TEXT, email TEXT)")
        except:
            pass

        c.execute("SELECT * FROM users WHERE users.id = " + str(id))
        response = c.fetchone()
        if response == None:
            c.execute("INSERT INTO users VALUES(" + str(id) + ",'" + str(name) + "','" + str(email) + "')")

        data = {"msg": "ok"}
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


@app.route("/login/<id>")
def api_login(id):

    try:
        """Check if user <id> is registered"""
        config.logger.info("*** Start processing id %s ***", id)

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        response = [[0]]

        try:
            c.execute("CREATE TABLE users (id INT, nom TEXT, email TEXT)")
            api_create(0,"Default user","default@gmail.com")
            api_create(1,"Jean Bvt","jean@gmail.com")
            api_create(2,"Salim Abc","salim@gmail.com")
            api_create(3,"Matthias Bp","matthias@gmail.com")
            api_create(4,"Robin Tgh","robin@gmail.com")
            api_create(5,"Yolo","Yola")
        except:
            pass

        c.execute("SELECT * FROM users WHERE users.id = " + str(id))
        response = c.fetchone()

        if response != None:
            config.logger.info("*** %s is in the database ***", id)
            data = {"msg": "ok","id": response[0], "name": response[1],"email": response[2]}
            resp = jsonify(data)
            resp.status_code = 200
        else:
            config.logger.info("*** %s is unknown ***", id)
            data = {"msg": "pas ok"}
            resp = jsonify(data)
            resp.status_code = 401

        conn.commit()
        conn.close()

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
