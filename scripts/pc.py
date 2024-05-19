class program_counter():
    global instruction_size # placeholder, need to think of 
                            # how we will deal with this.
    instruction_size = 4

    def __init__(self, address, _opcode, _immediate): # immediate is 12 bits
        self.address = address
        self.next = self.address + instruction_size
        self._opcode = _opcode
        self._immediate = _immediate
    
    def __iter__(self):
        return self.address

    def __next__(self):
        return self.next()
    
    def set_addr(self, new_address):
        self.address = new_address
        self.next = self.address + instruction_size

    def next(self):
        if self.address < 2**31:
            temp = self.address
            self.set_addr(self.next)
            # returns current & next addresses
            return temp, self.address
        raise StopIteration()