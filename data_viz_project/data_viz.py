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
polarity_list = []
subjectivity_list = []
polarity_total = 0
subjectivity_total = 0
tweets_string = ""

for twt in tweet_data:
    tweets_string += twt["text"]

    twt_tb = TextBlob(twt["text"])
    polarity_list.append(twt_tb.sentiment.polarity)
    polarity_total += twt_tb.sentiment.polarity
    subjectivity_list.append(twt_tb.sentiment.subjectivity)
    subjectivity_total += twt_tb.sentiment.subjectivity

polarity_avg = polarity_total/len(polarity_list)
subjectivity_avg = subjectivity_total/len(subjectivity_list)

print("\nThe average polarity is: {avg}\n".format(avg=polarity_avg))
print("The average subjectivity is: {avg}\n".format(avg=subjectivity_avg))

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

tweets_blob = TextBlob(tweets_string)
word_count = tweets_blob.word_counts
common_words = ["and", "about", "the", "http"]
filtered_words = {}

for word in word_count:
    if word.isalpha() and word not in common_words:
        if word.lower() in filtered_words:
            filtered_words[word.lower()] += 1
        else:
            filtered_words[word.lower()] = 1

wordcloud = WordCloud().generate_from_frequencies(filtered_words)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
