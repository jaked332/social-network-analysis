import random

from faker import Faker
from prettytable import PrettyTable

from node import User, Post, Comment

generator = Faker()

def generate_fake_users(num_users, min_age=18, max_age=65):
    users = []

    for _ in range(num_users):
        age = random.randint(min_age, max_age)
        gender = random.choice(['Male', 'Female', 'Non-binary'])

        real_name = None
        if gender == "Male":
            real_name = generator.name_male()    
        elif gender == "Female":
            real_name = generator.name_female()
        else:
            real_name = generator.name_nonbinary()

        user_name = real_name.lower()

        # Remove existing dot (e.g., Dr. or Mr.)
        user_name = user_name.replace('.', '')
        user_name = ".".join(user_name.split())

        workplace = generator.company()
        location = generator.city()

        current_user = User(user_name, real_name, age, gender, workplace, location)
        users.append(current_user)

    print(f"Generated {num_users} profiles.")
    return users

def generate_fake_posts(users, max_number_of_posts=3):
    posts = []

    for i, u in enumerate(users):
        post_count = random.randint(1, max_number_of_posts)
        for _ in range(post_count):
            generated_content = generator.text(max_nb_chars=100)
            timestamp = generator.date_time_this_year()

            # TODO: Make this more determinstic.
            current_post = Post(i + random.randint(1, 500), generated_content, u, timestamp)

            u.posts.append(current_post)
            posts.append(current_post)

    return posts

def generate_fake_comments(posts, users, max_comments_per_post):
    for post in posts:
        random_comment_count = random.randint(1, max_comments_per_post)
        for _ in range(random_comment_count):
            comment_str = generator.sentence()
            timestamp = generator.date_time_this_year()
            author = random.choice(users)
            current_comment = Comment(comment_str, author, timestamp)
            post.comments.append(current_comment)
            author.comments.append(current_comment)

def generate_fake_views(posts, users):
    for post in posts:
        viewer_count = random.randint(0, 5)
        viewers = random.sample(users, viewer_count)
        for viewer in viewers:
            post.viewers.append(viewer)
            viewer.viewed_posts.append(post)

def display_users(users, filename="./out/users.txt"):
    table = PrettyTable()
    table.field_names = ["User Name", "Real Name", "Age", "Gender", "Workplace", "Location"]

    for u in users:
        table.add_row([u.user_name, u.real_name, u.age, u.gender, u.workplace, u.location])
    
    with open(filename, "w") as file:
        file.write(str(table))

    print(f"Wrote the user base to {filename}")

def display_posts(posts, filename="./out/posts.txt"):
    table = PrettyTable()
    table.field_names = ["Author", "Timestamp", "Content"]

    for p in posts:
        table.add_row([p.author.user_name, p.timestamp, p.content])

    with open(filename, "w") as file:
        file.write(str(table))

    print(f"Wrote user posts to {filename}")

def display_comments(posts, filename="./out/comments.txt"):
    table = PrettyTable()
    table.field_names = ["Author", "Timestamp", "Comment", "Original Post"]

    for p in posts:
        for c in p.comments:
            table.add_row([c.author.user_name, c.timestamp, c.content, p.content])

    with open(filename, "w") as file:
        file.write(str(table))

    print(f"Wrote user comments to {filename}")
