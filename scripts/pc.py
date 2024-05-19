class program_counter():
    global instruction_size # placeholder, need to think of 
                            # how we will deal with this
    instruction_size = 4

    def __init__(self, address):
        self.address = address
        self.next = self.address + instruction_size
    
    def __next__(self):
        if self.address < 2**31:
            temp = self.address
            self.address = self.next
            self.next = self.address + instruction_size
            return temp
        else:
            self.address, self.next = 0, self.address + instruction_size
