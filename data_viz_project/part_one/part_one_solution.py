'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
import matplotlib.pyplot as plt

from textblob import TextBlob

#Get the JSON data
tweetFile = open("../TwitterData/tweets_small.json", "r")
tweet_data = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polarity_list = []
subjectivity_list = []

polarity_total = 0
subjectivity_total = 0

for twt in tweet_data:

    twt_tb = TextBlob(twt["text"])

    sentiments = twt_tb.sentiment

    polarity_list.append(sentiments.polarity)
    polarity_total += sentiments.polarity
    subjectivity_list.append(sentiments.subjectivity)
    subjectivity_total += sentiments.subjectivity


polarity_avg = polarity_total/len(polarity_list)
subjectivity_avg = subjectivity_total/len(subjectivity_list)

print("\nThe average polarity is: {avg}\n".format(avg=polarity_avg))
print("The average subjectivity is: {avg}\n".format(avg=subjectivity_avg))
