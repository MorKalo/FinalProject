class NameNeedToBeDifrentException(Exception):
    def __init__(self, message='the same name cant be for two or more object '):
        #self.flight=flight
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return f'the same name cant be for two or more object: {self.message} '