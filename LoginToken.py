class LoginToken:

    def __init__(self, id, name, role):
        self.id=id
        self.name=name
        self.role=role

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)