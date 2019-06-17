from flask import Flask, jsonify, render_template, request
from Naaz import app
import os, dialogflow, json, pusher, requests

@app.route('/')
def index():
	return render_template('index.html', title='Naaz')