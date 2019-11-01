import os

from flask import Flask, render_template, request, jsonify, redirect, session, url_for
from flask_oauthlib.client import OAuth, OAuthException
import pandas as pd

import math
import json

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/upload' , methods=['POST'])
def volunteer_sign_up():
	return 



if __name__ == '__main__':
	app.run(debug=True, port=55 )
