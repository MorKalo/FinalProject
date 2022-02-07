class FlightNotFoundException(Exception):
    def __init__(self,  message='We didnt find flight with this ID'):
        #self.flight=flight
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return f'We didnt find flight with this ID. '