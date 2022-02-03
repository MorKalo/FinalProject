class NoMoreTicketsForFlightsException(Exception):
    def __init__(self, message='No more tickets are available for this flight'):
        #self.flight=flight
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return f'No more tickets are available for flight number: {self.message} '