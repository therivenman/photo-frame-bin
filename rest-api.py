#!/usr/bin/env python

import subprocess
from flask import Flask,jsonify,request

"""
Display power service
"""

status_app='display-status'
control_app='display-power'

app = Flask(__name__)

# Helper functions

def getDisplayPowerStatus():
    stdout = subprocess.check_output(status_app).strip('\n')
    json = { 'display' : int(stdout) }
    return json

def setDisplayPower(state):
    cmd = [ control_app, str(state) ]
    proc = subprocess.Popen(cmd)
    exit_code = proc.wait()
    return exit_code

# Error handling

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# REST API

@app.route('/', methods=['GET'])
def home():
    return "Get status at /status [GET]\nChange state at /control [PUT] [0/1]"

@app.route('/status', methods=['GET'])
def getDisplayPower():
    return jsonify(getDisplayPowerStatus())

@app.route('/control/<int:state>', methods=['PUT'])
def modifyDisplayPower(state):

    # validate state

    if state < 0 or state > 1:
        raise InvalidUsage('Invalid state')

    if setDisplayPower(state) is not 0:
        return "ERROR: Failed to set display power"

    return jsonify(getDisplayPowerStatus())

if __name__ == '__main__':
	app.run(debug=False, host="0.0.0.0", port=8000)

