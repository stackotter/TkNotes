from db.file_db import FileDb


class Model:
    _db: FileDb

    def __init__(self, db: FileDb):
        self._db = db
