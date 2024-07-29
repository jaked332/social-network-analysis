# This module defines the different node types.

class User:
    def __init__(
        self,
        user_name,
        real_name,
        age,
        gender,
        workplace,
        location):

        self.user_name = user_name
        self.real_name = real_name
        self.age = age
        self.gender = gender
        self.workplace = workplace
        self.location = location
        self.connection = []
        self.posts = []
        self.comments = []
        self.viewed_posts = []

    def __str__(self):
        return (
            f"Username: {self.user_name} - "
            f"Real Name: {self.real_name} - "
            f"Age: {self.age} - "
            f"Gender: {self.gender} - "
            f"Workplace: {self.workplace} - "
            f"Location: {self.location} -"
            f"# of Posts: {len(self.posts)}")

class Post:
    def __init__(
        self, 
        uid,
        content,
        author,
        timestamp):
    
        self.uid = uid
        self.content = content
        self.author = author
        self.timestamp = timestamp
        self.viewers = []
        self.comments = []

class Comment:
    def __init__(
        self,
        content,
        author,
        timestamp):

        self.content = content
        self.author = author
        self.timestamp = timestamp
