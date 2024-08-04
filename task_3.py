# Import necessary packages
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from data import generate_fake_users

stopWords = set(STOPWORDS)

print(stopWords)

# Function used to make a list of dictionaries of user's as key and their list of attributes as value (age, gender, region).
# [{“userName1” : [attribute1, attribute2, attribute3]}, ...]
# Let's say we can only allow people who are 18 and older

#Function used to make a list of dictionaries of user's name as key and a list of string words as value.

# Function used to make of list of dictionaries of words as key and frequency as their integer values another dictionary 
# which has a userName as key and list of people who have used that word as value :
#  [{“word1” : frequency}, ...]

