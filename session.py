from typing import Optional


class Session:
    user_id: Optional[int]
    current_note_id: Optional[int]

    def __init__(self):
        self.user_id = None
        self.current_note_id = None

    def get_user_id(self) -> Optional[int]:
        return self.user_id

    def set_user_id(self, new_user_id: Optional[int]):
        self.user_id = new_user_id

    def get_current_note_id(self) -> Optional[int]:
        return self.current_note_id

    def set_current_note_id(self, new_current_note_id: Optional[int]):
        self.current_note_id = new_current_note_id
