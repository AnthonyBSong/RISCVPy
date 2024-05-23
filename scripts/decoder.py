from ImmediateError import ImmediateError # type: ignore

class Decoder:
    def __init__(self):
        pass

    def decode(self, instruction):
        type = self.parse_op(instruction)

        print(f"Instruction type: {type}")

    def parse_op(self, instruction) -> str:
        op_code = instruction[len(instruction)-7: len(instruction)]

        print(f"op code: {op_code}")

        if op_code == "0110011":
            return "R"
        elif op_code == "0010011":
            return "I"
        elif op_code == "0100011":
            return "S"
        elif op_code == "0110111" or op_code == "0010111":
            return "U"

if __name__ == '__main__':
    instruction_add = "0b0000000xxxxxyyyyy000zzzzz0110011"
    instruction_addi = "0bxxxxxxxxxxxxyyyyy000zzzzz0010011"

    print(len(instruction_add))

    decoder = Decoder()

    decoder.decode(instruction_add)
    decoder.decode(instruction_addi)