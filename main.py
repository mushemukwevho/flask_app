from flask import Flask, redirect, render_template, url_for, request

app=Flask(__name__)

app.route("/")
def home():
    return "It works"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)