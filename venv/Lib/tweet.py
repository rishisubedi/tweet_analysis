# This apps will do the sentiment analysis of the recent tweets in my user account

import tweepy
from textblob import textblob


consumerKey= 'dNLzQHqyAm6LgDotscnrOZm0Z'

consumerSecret='IOHhTZxkuU7T100VkpzxkXHaRyXLTAij42022WzqXaOll3qsXi '

accessToken= '1342197739-YcVWjU2FCknhZvVbZVKtG3RfnMWwNUCw3gyyM55 '

accessTokenSecret= 'z2Q6ZfRaURvgz2JqqY3B0hJVi6WBqY3fOkKPK6039DHEu'

# Authentication module
makeauth = tweepy.OAuthHandler(consumerKey, consumerSecret)

makeauth.set_access_token(accessToken,accessTokenSecret)