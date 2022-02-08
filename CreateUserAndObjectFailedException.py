class CreateUserAndObjectFailedException(Exception):
    def __init__(self, message='--Failed-- this action failed. we cant create this user and object'):
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return f'--Failed-- this action failed. we cant create this user and object '