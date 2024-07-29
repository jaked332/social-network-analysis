from typing import List

import networkx as nx
import matplotlib.pyplot as plt

from data import (
    generate_fake_users,
    generate_fake_posts,
    generate_fake_comments,
    generate_fake_views)

from node import User, Post, Comment

def filter_interesting_users(users: List[User], criteria: dict):
    filtered_users = []
    for user in users:
        match = True
        for key, value in criteria.items():
            if key == 'posts_count' and len(user.posts) <= value:
                match = False
            elif key == 'comments_count' and len(user.comments) <= value:
                match = False
            elif key == 'views_counts' and sum(
                len(post.viewers) for post in user.posts) <= value:
                match = False
            elif key == 'age' and not eval(f'user.age {value}'):
                match = False
        if match:
            filtered_users.append(user)
    return filtered_users

def visualize_social_network(users: List[User], interesting_users):
    G = nx.DiGraph()

    for user in users:
        # Take only the first letter of first name and first letter of
        # the last name for vis. So jon.smith becomes j.s
        truncated_label = user.user_name.split('.')
        truncated_label = truncated_label[0][0] + truncated_label[1][0]

        G.add_node(user.user_name, label=truncated_label, color='blue')

    # Adding post nodes and connecting them with authors and viewers
    for user in users:
        for post in user.posts:
            content = post.uid
            G.add_node(content, label=content, color='green')
            G.add_edge(user.user_name, content, color='green')
            for viewer in post.viewers:
                G.add_edge(content, viewer.user_name, color='red')
    
    # Now let's highlight the interesting users making them "red"
    for user in interesting_users:
        G.nodes[user.user_name]['color'] = 'red'

    pos = nx.spring_layout(G)

    node_colors = [G.nodes[node]['color'] for node in G.nodes()]
    edge_colors = [G.edges[edge]['color'] for edge in G.edges()]

    nx.draw(
        G, pos, with_labels=True, labels=nx.get_node_attributes(G, 'label'),
        node_color=node_colors, edge_color=edge_colors, node_size=500, arrows=True)
    plt.show()



userbase = generate_fake_users(10)
posts = generate_fake_posts(userbase, 2)
comments = generate_fake_comments(posts, userbase, 2)
views = generate_fake_views(posts, userbase)


criteria = {
    'age': '< 30',
    'views_counts': 2
}

interesting_users = filter_interesting_users(userbase, criteria)
print(f"Found {len(interesting_users)} interesting users")

# print(f"Interesting Users:")
# for user in interesting_users:
#     print(user)

visualize_social_network(userbase, interesting_users)
