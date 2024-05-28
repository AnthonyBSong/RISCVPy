from typing import Any
from NotSignal import NotSignalException
import string

class Signal(object):
    def __init__(self, _signal, _msb):
        self.signal = [0] * 32

        # conversion of binary literal, _signal, to a signal
        self.set(_signal, _msb)

    def invariant(self):
        if len(self.signal) != 32:
            raise NotSignalException('Check to make sure your input is a signal')
        for i in range(len(self.signal)):
            if (self.signal[i] == 0) or (self.signal[i] == 1):
                pass
            else:
                raise NotSignalException('Check to make sure your input is a signal')
    
    def __str__(self):
        to_ret = "0b"
        for bit in self.signal:
            to_ret = to_ret + str(bit)
        return to_ret

    def set(self, new_signal : int, msb : int):
        temp = list.copy(self.signal)
        ctr = 31
        while new_signal != 0:
            self.signal[ctr] = (new_signal % 2)
            new_signal = new_signal // 2
            ctr -= 1
        for i in range(0, ctr + 1):
            if msb == 1: # negative
                self.signal[i] = 1
            else: # positive
                self.signal[i] = 0
        try: # checks to make sure new signal is legal
            self.invariant()
        except NotSignalException as exception: # if not, goes back to old signal which is
            print(exception)
            self.signal = temp # guarenteed to be legal by invariant
            
    def __getitem__(self, index) -> int: # begin inclusive, end non-inclusive
        if type(index) == int:
            return bin(self.signal[31-index])
        else: 
            to_ret = 0
            print(31 - index.stop, 31 - index.start - 1)
            for i in range(31 - index.stop, 31 - index.start - 1, -1):
                to_ret += self.signal[i] * (2 ** (31 - i))
            return bin(to_ret)
    

if __name__ == "__main__":
    x = Signal(0b000000101010101110, 1)
    print(x[0])
    print(x[2:0])