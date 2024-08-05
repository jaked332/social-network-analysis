# Import necessary packages
import random
import matplotlib.pyplot as plt
import names
from data import (
    generate_fake_users,
    generate_fake_posts,
    generate_fake_comments,
    generate_fake_views)
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

stopWords = set(STOPWORDS)

# Function used to make a list of dictionaries of user's as key and their list of attributes as value (age, gender, region).
# [{“userName1” : [attribute1, attribute2, attribute3]}, ...]
def generateUsers(userNum = 3, minAge = 5, maxAge = 100):
    createdUsers = []
    counter = 0

    for users in userNum:
        age = random.randint(minAge, maxAge)
        gender = random.choice(['Male', 'Female', 'Non-binary'])
        userName = names.get_full_name(gender)
        region = random.choice(["Africa", "Asia", "Central America", "Europe", "Middle East", "North America", "Pacific", "South America"])

        # Conditionals, or user attributes, that needs to be met so that words can be included in the wordcloud.
        if (age >= criteria['age']) and (gender == criteria['gender']) and (region == criteria['region']):
            currentUser = {userName : [age, gender, region]}
            createdUsers.append(currentUser)
            counter += 1
    
    print(f"Generated {counter} profiles out of {userNum} generated users.")
    return createdUsers

# Function is used to make a dictionary of words as the key and frequency count as their value.
def generateWordFrequencyDict(posts):
    wordFrequency = {}
    wordSplit = posts[word].split
    for word in wordSplit:
        wordFrequency[word] = wordFrequency.get(word, 0) + 1

## Couldn't finish
#def descendingQuickSort(dictionary, left, right):



# Criteria that must be met so that it is included in the wordcloud.
criteria = {
            'age' : 18,
            'gender' : 'Male',
            'region' : 'North America'
            }

# Generate new users with their attributes
newUsers = generateUsers(5, 10, 65)

# Get the list of fake posts, it will be a tuple.
generateFakePosts = generate_fake_posts(newUsers,4)
# A string that will hold all the sentences of generateFakePosts.
allPosts = ""
# For loop of only getting the sentences of generateFakePosts
for post in range(len(generateFakePosts)):
    allPosts += generateFakePosts[post][1]
    allPosts += " "

# Get the dictionary of every word and their frequency.
wordFrequencyDict = generateWordFrequencyDict(allPosts)

# We want to get the list of all sentences in 
descendingSort = descendingQuickSort(wordFrequencyDict)
