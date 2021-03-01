from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def adminRegister():
    return render_template("register.html")

