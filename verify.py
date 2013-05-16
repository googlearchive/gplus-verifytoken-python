#!/usr/bin/python
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Simple server to demonstrate token verification."""

__author__ = 'cartland@google.com (Chris Cartland)'

import json
import random
import string

from flask import Flask
from flask import make_response
from flask import render_template
from flask import request

import httplib2
from oauth2client.client import verify_id_token
from oauth2client.crypt import AppIdentityError


APPLICATION_NAME = 'Google+ Python Token Verification'


app = Flask(__name__)
app.secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits)
                         for x in xrange(32))


# Update client_secrets.json with your Google API project information.
# Do not change this assignment.
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']


@app.route('/', methods=['GET'])
def index():
  """Render index.html."""
  # Set the Client ID and Application Name in the HTML while serving it.
  response = make_response(
      render_template('index.html',
                      CLIENT_ID=CLIENT_ID,
                      APPLICATION_NAME=APPLICATION_NAME))
  response.headers['Content-Type'] = 'text/html'
  return response


@app.route('/verify', methods=['POST'])
def verify():
  """Verify an ID Token or an Access Token."""

  id_token = request.args.get('id_token', None)
  access_token = request.args.get('access_token', None)

  token_status = {}

  id_status = {}
  if id_token is not None:
    # Check that the ID Token is valid.
    try:
      # Client library can verify the ID token.
      jwt = verify_id_token(id_token, CLIENT_ID)
      id_status['valid'] = True
      id_status['gplus_id'] = jwt['sub']
      id_status['message'] = 'ID Token is valid.'
    except AppIdentityError:
      id_status['valid'] = False
      id_status['gplus_id'] = None
      id_status['message'] = 'Invalid ID Token.'
    token_status['id_token_status'] = id_status

  access_status = {}
  if access_token is not None:
    # Check that the Access Token is valid.
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    if result.get('error') is not None:
      # This is not a valid token.
      access_status['valid'] = False
      access_status['gplus_id'] = None
      access_status['message'] = 'Invalid Access Token.'
    elif result['issued_to'] != CLIENT_ID:
      # This is not meant for this app. It is VERY important to check
      # the client ID in order to prevent man-in-the-middle attacks.
      access_status['valid'] = False
      access_status['gplus_id'] = None
      access_status['message'] = 'Access Token not meant for this app.'
    else:
      access_status['valid'] = True
      access_status['gplus_id'] = result['user_id']
      access_status['message'] = 'Access Token is valid.'
    token_status['access_token_status'] = access_status
  
  response = make_response(json.dumps(token_status, 200))
  response.headers['Content-Type'] = 'application/json'
  return response


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=4567)
