class UserAlreadyExistException(Exception):
    def __init__(self, message=f' The username that you want to create is alrady exist '):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'