'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
import matplotlib.pyplot as plt

from textblob import TextBlob
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("../TwitterData/tweets_small.json", "r")
tweet_data = json.load(tweetFile)
tweetFile.close()

tweets_string = ""

pos_tweets = ""
neg_tweets = ""
neut_tweets = ""

for twt in tweet_data:

    tweets_string += twt["text"]

    # twt_tb = TextBlob(twt["text"])
    #
    # sentiments = TextBlob(twt["text"]).sentiment
    #
    # if sentiments.polarity > 0.2:
    #     pos_tweets += twt["text"]
    # elif sentiments.polarity < -0.2:
    #     neg_tweets += twt["text"]
    # else:
    #     neut_tweets += twt["text"]
    #
    # polarity_list.append(twt_tb.sentiment.polarity)
    # polarity_total += twt_tb.sentiment.polarity
    # subjectivity_list.append(twt_tb.sentiment.subjectivity)
    # subjectivity_total += twt_tb.sentiment.subjectivity


tweets_blob = TextBlob(tweets_string)
common_words = ["and", "about", "the", "http", "automation"]


def get_filtered_dictionary(blob):
    filtered_words = {}
    word_count = blob.word_counts
    for word in word_count:
        if word.isalpha() and word.lower() not in common_words:
            if word.lower() in filtered_words:
                filtered_words[word.lower()] += 1
            else:
                filtered_words[word.lower()] = 1

    return filtered_words

# def create_figure(dict, plotnum, title):
#     wordcloud = WordCloud().generate_from_frequencies(dict)
#     plt.subplot(plotnum)
#     plt.imshow(wordcloud, interpolation="bilinear")
#     plt.title(title)
#     plt.axis("off")
#
# plt.figure(1)
#
# create_figure(get_filtered_dictionary(TextBlob(pos_tweets)), 131, "Positive Tweets")
# create_figure(get_filtered_dictionary(TextBlob(neg_tweets)), 132, "Negative Tweets")
# create_figure(get_filtered_dictionary(TextBlob(neut_tweets)), 133, "Neutral Tweets")

#
wordcloud = WordCloud().generate_from_frequencies(get_filtered_dictionary(tweets_blob)
)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# plt.show()
