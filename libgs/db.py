from typing import List
from .model import Province, City, Area, Street, Village
import sqlite3


# DB 接口
class Interface():
    def findAll(self):
        pass

# GeosDB
class GeosDB(Interface):
    def __init__(self, db: sqlite3.Connection):
        self._db = db
    
    # provinces 省级查询
    def provinces(self, key:str):
        data = self.execSelect(f"SELECT code,name FROM province WHERE name LIKE '%{key}%'")
        return [Province(code=item[0], name=item[1]) for item in data]
    
    # cities 市级查询
    def cities(self, key: str):
        data = self.execSelect(f"SELECT code,name FROM city WHERE name LIKE '%{key}%'")
        return [City(code=item[0], name=item[1]) for item in data]
    
    # areas 县界查询
    def areas(self, key:str):
        data = self.execSelect(f"SELECT code,name FROM area WHERE name LIKE '%{key}%'")
        return [Area(code=item[0], name=item[1]) for item in data]

    # streets 乡级查询
    def streets(self, key:str):
        data = self.execSelect(f"SELECT code,name FROM street WHERE name LIKE '%{key}%'")
        return [Street(code=item[0], name=item[1]) for item in data]

    # villages 村级查询
    def villages(self, key:str):
        data = self.execSelect(f"SELECT code,name FROM street WHERE name LIKE '%{key}%'")
        return [Village(code=item[0], name=item[1]) for item in data]
    
    def commad(self)->List:
        return [
            self.provinces,
            self.cities,
            self.areas,
            self.streets,
            self.villages
        ]

    def execSelect(self, selectSql:str):
        cursor = self._db.cursor()
        cursor.execute(selectSql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def findAll(self, key: str, depth:int):
        result = []
        commad = self.commad()
        for i in range(depth):
            for res in commad[i](key):
                result.append(res)
        return result


def DBCreator() ->List[Interface]:
    return [
        GeosDB(sqlite3.connect('./db/china.sqlite'))
    ]

__all__ = ["DBCreator"]