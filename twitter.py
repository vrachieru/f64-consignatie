#!/usr/bin/env python
 
from tweepy import OAuthHandler, API

class Twitter():
  def __init__(self, config = None):
    auth = OAuthHandler(unicode(config.consumerKey), unicode(config.consumerSecret))
    auth.set_access_token(unicode(config.accessToken), unicode(config.accessTokenSecret))
    self._api = API(auth)

  def tweet(self, message):
    self._api.update_status(message.encode('utf-8'))
 