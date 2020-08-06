'''
Copyright 2020, Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle.
Licensed under GPLv3.0.
'''
from flask import jsonify
from .. import app, postgres
from ..parse_request import parse_request
from flask_cors import cross_origin

@app.route("/user/authorize", methods=["POST"])
@cross_origin()
def user_authorize():
	username, password = parse_request("username", "password")

	# This function is a stub just to demonstrate separate components

	return jsonify({"authorization": None})
