class NotSignal(Exception):
    def __init__(self, messsage):
        self.message = messsage