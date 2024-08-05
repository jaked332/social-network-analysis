# Import necessary packages
import random
import matplotlib.pyplot as plt
import names
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

# Function used to make of list of dictionaries of words as key and frequency as their integer values another dictionary 
# which has a userName as key and list of people who have used that word as value :
#  [{“word1” : frequency}, ...]
def generateUserPosts(users, maxNumPost = 3):
    
    for user in (len(users) - 1):

# Criteria that must be met so that it is included in the wordcloud.
criteria = {
            'age' : 18,
            'gender' : 'Male',
            'region' : 'North America'
            }

# Generate new users with their attributes
newUsers = generateUsers(5, 10, 65)
