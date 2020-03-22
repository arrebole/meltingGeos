
class Province:
    def __init__(self, code: str, name: str):
        self.type = "province"
        self.code = code
        self.name = name
    
    def __str__(self) ->str:
        return f"(type: '{self.type}'', code: '{self.code}'', name: '{self.name}')"
    
    def __repr__(self) ->str:
        return f"(type: '{self.type}'', code: '{self.code}'', name: '{self.name}')"
    

class City:
    def __init__(self, code: str, name: str):
        self.type = "city"
        self.code = code
        self.name = name
    
    def __str__(self) ->str:
        return f"(type: '{self.type}'', code: '{self.code}'', name: '{self.name}')"
    
    def __repr__(self) ->str:
        return f"(type: '{self.type}'', code: '{self.code}'', name: '{self.name}')"


class Area:
    def __init__(self, code: str, name: str):
        self.type = "area"
        self.code = code
        self.name = name
    
    def __str__(self) ->str:
        return f"(type: '{self.type}'', code: '{self.code}'', name: '{self.name}')"
    
    def __repr__(self) ->str:
        return f"(type: '{self.type}'', code: '{self.code}'', name: '{self.name}')"


class Street:
    def __init__(self, code: str, name: str):
        self.type = "street"
        self.code = code
        self.name = name
    
    def __str__(self) ->str:
        return f"(type: '{self.type}'', code: '{self.code}'', name: '{self.name}')"
    
    def __repr__(self) ->str:
        return f"(type: '{self.type}'', code: '{self.code}'', name: '{self.name}')"


class Village:
    def __init__(self, code: str, name: str):
        self.type = "villages"
        self.code = code
        self.name = name
    
    def __str__(self) ->str:
        return f"(type: '{self.type}'', code: '{self.code}'', name: '{self.name}')"
    
    def __repr__(self) ->str:
        return f"(type: '{self.type}'', code: '{self.code}'', name: '{self.name}')"