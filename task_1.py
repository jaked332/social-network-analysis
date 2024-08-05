from typing import List

import networkx as nx
import plotly.graph_objects as go
from networkx.algorithms.centrality import degree_centrality

# Creating Graph
G = nx.DIGraph()

# Adding Fake Users
users = ['user1', 'user2', 'user3']
posts = ['post1', 'post2', 'post3']
views = [('user1', 'post1'), ('user2', 'post1'), ('user1', 'post2')]
comments = [('user1', 'post1'), ('user3', 'post2')]

for user in users:
    G.add_node(user, type = 'user')

for post in posts:
    G.add_node(post, type='post', comments=0, views=0)

for user,post in views:
    g.add_edge(user, post)
    G.nodes[post]['views'] += 1

for user,post in comments:
    g.add_edge(user, post)
    G.nodes[post]['comments'] += 1


# Finding Importance
def finding_importance(G):
    a = 0.5
    b = 0.5
    for post in posts:
        post_node = G.nodes[post]
        post_node['importance_score'] = a * post_node['comments'] + beta * post_node['views']


finding_importance(G):

# Graph Visualization
    
pos = nx.spring_layout(G)
edge_x = []
edge_y = []

for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(none)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(none)

node_x = []
node_y = []
node_text = []
node_size = []

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(f"{node}: {G.nodes[nodes].get('importance')}")
    node_size.append(30 * (G.nodes[node].get('importance_score', 0) + 1))


fig = go.figure(data=[go.Scatter(x = edge_x, y = edge_y, mode = 'lines', line = dict(color='gray')), 
                     go.Scatter(x = node_x, y = node_y, mode = 'markers+text', text = node_text, textposition = "bottom center", marker = dict(size = node_size, color = 'blue'))])
fig.show()

#all I could Add





