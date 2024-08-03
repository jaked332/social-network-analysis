from typing import List

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from data import (
    generate_fake_users,
    generate_fake_posts,
    generate_fake_comments,
    generate_fake_views)

from node import User

def filter_interesting_users(users: List[User], criteria: dict):
    filtered_users = []

    for user in users:
        match = True
        
        if 'comments_count' in criteria:
            if criteria['comments_count'][0] == '>' and len(user.comments) <= criteria['comments_count'][1]:
                match = False
            if criteria['comments_count'][0] == '<' and len(user.comments) >= criteria['comments_count'][1]:
                match = False

        if 'post_count' in criteria:
            if criteria['post_count'][0] == '>' and len(user.posts) <= criteria['post_count'][1]:
                match = False
            if criteria['post_count'][0] == '<' and len(user.posts) >= criteria['post_count'][1]:
                match = False

        if 'views_count' in criteria:
            total_views = sum(len(post.viewers) for post in user.posts)
            if criteria['views_count'][0] == '>' and total_views <= criteria['views_count'][1]:
                match = False
            if criteria['views_count'][0] == '<' and total_views >= criteria['views_count'][1]:
                match = False

        if 'age' in criteria:
            if criteria['age'][0] == '>' and user.age <= criteria['age'][1]:
                match = False
            if criteria['age'][0] == '<' and user.age >= criteria['age'][1]:
                match = False

        if 'gender' in criteria and user.gender != criteria['gender']:
            match = False

        if match:
            filtered_users.append(user)

    return filtered_users

def visualize_interesting_network(users: List[User], interesting_users):
    G = nx.DiGraph()

    for user in users:
        # Take only the first letter of first name and first letter of
        # the last name for vis. So jon.smith becomes j.s
        truncated_label = user.user_name.split('.')
        truncated_label = truncated_label[0][0] + truncated_label[1][0]

        G.add_node(user.user_name, label=truncated_label,
            color='blue', size=len(user.posts) * 300 + 300)

    # Adding post nodes and connecting them with authors and viewers
    for user in users:
        for post in user.posts:
            G.add_node(post.uid, label=str(post.uid), color='green', size=300)
            G.add_edge(user.user_name, post.uid, color='green', label="Authored")
            for viewer in post.viewers:
                view_count = len(post.viewers)
                # Keeping label an empty string to not clutter the vis
                G.add_edge(post.uid, viewer.user_name, color='red', label="")

    # Now let's highlight the interesting users making them "red"
    for user in interesting_users:
        G.nodes[user.user_name]['color'] = 'red'

    pos = nx.spring_layout(G)

    node_colors = [G.nodes[node]['color'] for node in G.nodes()]
    node_sizes = [G.nodes[node].get('size', 300) for node in G.nodes()]

    edge_colors = [G.edges[edge]['color'] for edge in G.edges()]
    edge_labels = nx.get_edge_attributes(G, 'label')

    nx.draw(
        G, pos, with_labels=True, labels=nx.get_node_attributes(G, 'label'), alpha=0.7,
        node_color=node_colors, edge_color=edge_colors, node_size=node_sizes, arrows=True)

    nx.draw_networkx_edge_labels(G, pos, edge_labels={k: v for k, v in edge_labels.items() if v})

    user_patch = mpatches.Patch(color='blue', label='User')
    post_patch = mpatches.Patch(color='green', label='Post')
    interesting_patch = mpatches.Patch(color='red', label='Interesting User')
    plt.legend(handles=[user_patch, post_patch, interesting_patch])

    plt.show()


# Generate fake data.
userbase = generate_fake_users(10)
posts = generate_fake_posts(userbase, 2)
comments = generate_fake_comments(posts, userbase, 2)
views = generate_fake_views(posts, userbase)

criteria = {
    'age': ('<', 35),
    'gender': 'Female',
    'comments_count': ('>', 1)
}

interesting_users = filter_interesting_users(userbase, criteria)
print(f"Found {len(interesting_users)} interesting users")

visualize_interesting_network(userbase, interesting_users)
