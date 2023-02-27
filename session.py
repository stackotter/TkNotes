class Session:
    user_id: int

    def __init__(self):
        pass

    def get_user_id(self) -> int:
        return self.user_id

    def set_user_id(self, new_user_id: int):
        self.user_id = new_user_id
