import json
import sys
import nltk
from nltk.corpus import stopwords
import string
from nltk.tokenize import RegexpTokenizer

stopwordsList = stopwords.words('english')

def getTweets(filename):
	corpus = open(filename)
	decoded_response = corpus.read()
	jsonData=json.loads(decoded_response)
	text = []
	for item in jsonData:
		name = item.get("text")
		text.append(name)

	tokenized_tweets = []
	tokenizer = RegexpTokenizer(r'\w+')

	for tweet in text:
		tweet = tokenizer.tokenize(tweet)
		tokenized_tweets.append(tweet)

	for tweet in tokenized_tweets:
		for token in tweet:
			if token.lower() in stopwordsList:
				tweet.remove(token)

	return tokenized_tweets
