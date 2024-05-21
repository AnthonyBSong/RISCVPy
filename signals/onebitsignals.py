import NotSignal

class OneBitSignal():
    def __init__(self, signal):
        self.signal = signal

        # invariant
        if not (self.signal == 0 or self.signal == 1):
            raise NotSignal

    
    
