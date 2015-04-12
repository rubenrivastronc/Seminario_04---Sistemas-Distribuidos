
#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Antonio Miguel'
import twitter
import io
import json

def oauth_login():
    CONSUMER_KEY = 'ancCuk3dToDorjHMglgpkxMTa'
    CONSUMER_SECRET = 'MXSJJhkoLicw6kN8XwEsfKSfZ5Di6eOu6DJ3cdRy7n8cUbIBQ7'
    OAUTH_TOKEN = '269370297-iRLe1iLxJCY10jkBStZvbu4bc0FEoUkhfQkF6hF1'
    OAUTH_TOKEN_SECRET = 'f6PJNA0qX3AM1DM0fJkgeDUYhjp5b6RFK5OQ0qFITZVsz'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

def load_json(filename):
    with io.open('{0}.json'.format(filename),'r', encoding='utf-8') as f:
        return f.read()

