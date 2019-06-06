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
tweetFile = open("./TwitterData/tweets_small.json", "r")
tweet_data = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
# Part One & Two:
# polarity_list = []
# subjectivity_list = []

# Part One:
# polarity_total = 0
# subjectivity_total = 0

# Part Three:
# tweets_string = ""

pos_tweets = ""
neg_tweets = ""
neut_tweets = ""
for twt in tweet_data:

    # Part Three:
    # tweets_string += twt["text"]

    # Parts One, Two, & Three:
    # twt_tb = TextBlob(twt["text"])

    sentiments = TextBlob(twt["text"]).sentiment

    if sentiments.polarity > 0.2:
        pos_tweets += twt["text"]
    elif sentiments.polarity < -0.2:
        neg_tweets += twt["text"]
    else:
        neut_tweets += twt["text"]

    # Part One:
    # polarity_list.append(twt_tb.sentiment.polarity)
    # polarity_total += twt_tb.sentiment.polarity
    # subjectivity_list.append(twt_tb.sentiment.subjectivity)
    # subjectivity_total += twt_tb.sentiment.subjectivity

# Part One:
# polarity_avg = polarity_total/len(polarity_list)
# subjectivity_avg = subjectivity_total/len(subjectivity_list)

# print("\nThe average polarity is: {avg}\n".format(avg=polarity_avg))
# print("The average subjectivity is: {avg}\n".format(avg=subjectivity_avg))

# Part Two:
# Polarity Histogram
# plt.hist(polarity_list, bins=[-1, -0.5, 0.0, 0.5, 1])
# plt.xlabel("Polarities")
# plt.ylabel("Number of Tweets")
# plt.title("Polarity Histogram")
# plt.axis([-1.1, 1.1, 0, 100])
# plt.grid(True)
#
# print("Polarities Histogram ready to be viewed")
#
# plt.show()
#
# # Sentimentality Histogram
# plt.hist(subjectivity_list, bins=[-1, -0.5, 0.0, 0.5, 1])
# plt.xlabel("Subjectivities")
# plt.ylabel("Number of Tweets")
# plt.title("Subjectivities Histogram")
# plt.axis([-1.1, 1.1, 0, 100])
# plt.grid(True)
#
# print("\nSubjectivities Histogram ready to be viewed\n")
#
# plt.show()

# Part Three:
# tweets_blob = TextBlob(tweets_string)

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

def create_figure(dict, plotnum, title):
    wordcloud = WordCloud().generate_from_frequencies(dict)
    plt.subplot(plotnum)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.title(title)
    plt.axis("off")

plt.figure(1)

create_figure(get_filtered_dictionary(TextBlob(pos_tweets)), 131, "Positive Tweets")
create_figure(get_filtered_dictionary(TextBlob(neg_tweets)), 132, "Negative Tweets")
create_figure(get_filtered_dictionary(TextBlob(neut_tweets)), 133, "Neutral Tweets")

# Part Three:
# wordcloud = WordCloud().generate_from_frequencies(filtered_words)
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()

plt.show()
