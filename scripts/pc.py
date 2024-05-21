class program_counter():
    def __init__(self, address):
        self.address = address
        self.next = self.address + 4

    def set_addr(self, new_address, offset):
        self.address = new_address
        self.next = self.address + offset

    def next(self, opcode, offset):
        if len(bin(offset)) > 12:
            raise offset

        if self.address < 2**31:
            if opcode == 0b1100011:
                self.set_addr(self.next, offset)
            else:
                self.set_addr(self.next, 4)
        else:
            self.set_addr(0, 4)

    