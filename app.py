from asyncio import tasks
from tkinter.font import names
from flask import Flask, render_template
from classes import Contact
app = Flask(__name__)

# **** 1*****
# @app.route('/')
# def hello_world():
#     return "Hello world!"

# ****3****
# @app.route('/')
# def name():
#     return render_template("index.html", name="murat", date="29.08.2023")

# ****4****
# @app.route('/')
# def loop():
#     return render_template("index.html", names=["murat", "tal", "alik"])

# ****5****


# @app.route('/')
# def contact():
#     return render_template("contact.html", contact=Contact(name="murat", phone="0544443", email="mmmm@mmm.gmail.com"))


@app.route('/')
def dict():
    return render_template("task.html", tasks=[
        {"name": "Go to Work", "Date": "2023-1-1", "assigend": "murat"},
        {"name": "Walk with dog", "Date": "2024-4-4", "assigend": "tal"},
        {"name": "clean house", "Date": "2022-5-5", "assigend": "alik"},
    ])
