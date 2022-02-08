class DataExistException(Exception):
    def __init__(self, message='--Failed-- this action failed because some of the data exist in our DB.'
                               ' we cant create this user and object'):
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return '--Failed-- this action failed because some of the data exist in our DB.  we cant create this user and object'