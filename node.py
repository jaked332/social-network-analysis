from dataclasses import dataclass, field
from typing import List, Any

@dataclass
class User:
    user_name: str
    real_name: str
    age: int
    gender: str
    workplace: str
    location: str
    posts: List['Post'] = field(default_factory=list)
    comments: List['Comment'] = field(default_factory=list)
    viewed_posts: List['Post'] = field(default_factory=list)

@dataclass
class Post:
    uid: int
    content: str
    author: User
    timestamp: Any
    viewers: List[User] = field(default_factory=list)
    comments: List['Comment'] = field(default_factory=list)

@dataclass
class Comment:
    content: str
    author: User
    timestamp: Any
