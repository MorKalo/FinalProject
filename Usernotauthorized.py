class Usernotauthorized(Exception):
    def __init__(self, message='This user is not authorized to do this action'):
        #self.flight=flight
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return f' This user is not authorized to do this action '