class UserAlreadyExistException(Exception):
    def __init__(self, username, email, message="The user that you want to create is alrady exist "):
        self.username=username
        self.email=email
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'UserAlreadyExistException: {self.message}'