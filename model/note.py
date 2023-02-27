from dataclasses import dataclass


@dataclass
class Note:
    _id: str
    author_id: int
    title: str
    content: str
