from flask import current_app as app
from flask import render_template, request
from app.models import Message
from time import strftime
import random
import requests
from utils.combine_outputs import combine

MESSAGE_HISTORY = []
@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        current_time = strftime("%A, %b %d, %Y at %I:%M:%S %p IST")
        json = {"text": request.form["message"]}

        res = requests.get("http://localhost:5000/api/traditionalmlapi", json = json)
        traditional_pred = res.json()["prediction"]

        res = requests.get("http://localhost:5000/api/lstmapi", json = json)
        lstm_pred = res.json()["prediction"]

        isSafe, message = combine(traditional_pred, lstm_pred, 0)

        isSafe = not isSafe

        if isSafe:
            message = request.form["message"]

        new_message = Message(text = message, datetime = current_time, isSafe = isSafe)
        MESSAGE_HISTORY.append(new_message)
    return render_template("index.html", messages = MESSAGE_HISTORY)