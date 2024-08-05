# Import necessary packages
import random
#from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#import matplotlib.pyplot as plt
import secrets
import names

#stopWords = set(STOPWORDS)

#print(stopWords)

# Function used to make a list of dictionaries of user's as key and their list of attributes as value (age, gender, region).
# [{“userName1” : [attribute1, attribute2, attribute3]}, ...]
def createUsers(userNum = 3, minAge = 5, maxAge = 100):
    createdUsers = []

    for users in userNum:
        age = random.randint(minAge, maxAge)
        gender = random.choice(['Male', 'Female', 'Non-binary'])
        userName = names.get_full_name(gender)
        region = random.choice(["Africa", "Asia", "Central America", "Europe", "Middle East", "North America", "Pacific", "South America"])

        currentUser = {}
# Function used to make a list of dictionaries of user's name as key and a list of string words as value.

# Function used to make of list of dictionaries of words as key and frequency as their integer values another dictionary 
# which has a userName as key and list of people who have used that word as value :
#  [{“word1” : frequency}, ...]

