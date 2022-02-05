class LoginToken:

    def __init__(self, id, name, role):
        self._id=id
        self._name=name
        self._role=role

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def role(self):
        return self._role

