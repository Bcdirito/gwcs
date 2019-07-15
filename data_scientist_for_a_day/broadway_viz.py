import broadway
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

production_list = broadway.get_shows()
show_info = []

for p in production_list:
    show_info.append(p["Show"])

musical_titles = {}
play_titles = {}
special_titles = {}

for s in show_info:
    show_name = s["Name"]
    if s["Type"] == "Musical":
        if show_name in musical_titles:
            musical_titles[show_name] += 1
        else:
            musical_titles[show_name] = 1
    elif s["Type"] == "Play":
        if show_name in play_titles:
            play_titles[show_name] += 1
        else:
            play_titles[show_name] = 1
    else:
        if show_name in special_titles:
            special_titles[show_name] += 1
        else:
            special_titles[show_name] = 1

def generate_cloud(dic):
    wordcloud = WordCloud().generate_from_frequencies(dic)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

generate_cloud(musical_titles)
generate_cloud(play_titles)
generate_cloud(special_titles)
