__author__ = 'Reza'
import json
import pandas as pd
import matplotlib.pyplot as plt
import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets_data = []
tweets_file = open("stream.txt", "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

tweets_by_lang = tweets['lang'].value_counts()

tweets['iphone'] = tweets['text'].apply(lambda tweet: word_in_text('iphone', tweet))
tweets['sony'] = tweets['text'].apply(lambda tweet: word_in_text('xperia', tweet))
tweets['htc'] = tweets['text'].apply(lambda tweet: word_in_text('htc', tweet))

prg_langs = ['iphone', 'sony', 'htc']
tweets_by_prg_lang = [tweets['iphone'].value_counts()[True], tweets['sony'].value_counts()[True], tweets['htc'].value_counts()[True]]

x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: iphone vs. sony vs. htc (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.1 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()



#
# fig, ax = plt.subplots()
# ax.tick_params(axis='x', labelsize=15)
# ax.tick_params(axis='y', labelsize=10)
# ax.set_xlabel('Languages', fontsize=15)
# ax.set_ylabel('Number of tweets' , fontsize=15)
# ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
# tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

plt._show()