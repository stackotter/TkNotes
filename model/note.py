from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class Note:
    id_: Optional[int]
    author_id: int
    title: str
    content: str

    @classmethod
    def from_row(cls, row: dict[str, Any]) -> "Note":
        return Note(
            row["id"],
            row["author_id"],
            row["title"],
            row["content"]
        )

    def to_row(self) -> dict[str, Any]:
        return {
            "id": self.id_,
            "author_id": self.author_id,
            "title": self.title,
            "content": self.content
        }
