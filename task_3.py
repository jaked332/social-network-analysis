# Import necessary packages
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

stopWords = set(STOPWORDS)

print(stopWords)

# 
# Layout of List of Dictionaries:
# ["name" : ["word" : frequency, "word" : frequency]
