from .db import DBCreator

class Geos:
    def __init__(self):
        self.databases = DBCreator()

    def search(self, key: str, depth = 1):
        res = []
        for db in self.databases:
            for i in db.findAll(key, depth):
                res.append(i)
        return res
        