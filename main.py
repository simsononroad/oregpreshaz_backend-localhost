#!/srv/www/gyuris.hu/op.gyuris.hu/.venv/bin/python
from flask import *
import time
from flask import Flask, request, render_template, redirect, url_for, flash, session, jsonify
#import database
import hashlib
import sqlite3
import datetime
import hashlib
from datetime import datetime
import csv


localhost = Flask(__name__)
localhost.secret_key="asd"

@localhost.route("/")
def sql_command():
    con = sqlite3.connect("db/login.db")
    cur = con.cursor()
    return render_template("index.html")

@localhost.route("/execute_select", methods=["POST"])
def execute_select():
    con = sqlite3.connect("db/login.db")
    cur = con.cursor()
    command_in_html = request.form["command_select"]
    ans = cur.execute(command_in_html)
    flash(ans.fetchall())
    return redirect(url_for("sql_command"))

@localhost.route("/execute", methods=["POST"])
def execute():
    con = sqlite3.connect("db/login.db")
    cur = con.cursor()
    command_in_html = request.form["command"]
    cur.execute(command_in_html)
    con.commit()
    return redirect(url_for("sql_command"))

if __name__ == "__main__":
    localhost.run(debug=True)
