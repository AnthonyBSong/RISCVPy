from enum import Enum

# class Opcode(Enum):
#     add = 0b0110011
#     sub = 0b0110011
#     xor
#     orand
#     sll
#     srl
#     sra
#     slt
#     sltu


class Binary():
    def __init__(self, number: int):
        self.number = bin(number)
        self.listNum = list(str(self.number))[2:]
        self.lsb = int(self.listNum[-1])
    
    def __getitem__(self, index: slice):
        return int(''.join(self.listNum[index]))

def main():
    exInst = 0b1100110111000010000010000000000 # add x15, x1, x2
    exInst2 = 0b1100110111000010000010000000010 # sub x15, x1, x2

    # binNum = Binary(0b11000101)
    # print(binNum[1:]) # prints 1000101
    # print(binNum[3:5]) # prints 0 (00)
    # print(binNum.lsb) # prints 1

    exInstBin = Binary(exInst)
    print(f"Opcode = {exInstBin[0:7]}")
    print(f"rd = {exInstBin[7:12]}")
    print(f"funct3 = {exInstBin[12:15]}")
    print(f"rs1 = {exInstBin[15:20]}")
    print(f"rs2 = {exInstBin[20:25]}")
    print(f"funct7 = {exInstBin[25:32]}")

if __name__ == '__main__':
    main()


    
