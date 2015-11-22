# coding: utf-8

from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def housemakeing_index():
	return "Welcome to housemakeing!"

if __name__ == "__main__":
    app.run()
