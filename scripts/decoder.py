from ImmediateError import ImmediateError # type: ignore

class Decoder:
    def decode(self, instruction):
        type = self.parse_op(instruction)

        print(f"Instruction type: {type}")

    def invalid_instruction(self, instruction, opcode):
        print(f"Given instruction {instruction} does not have a valid opcode\nInvalid opcode: {opcode}")
        quit()

    def parse_op(self, instruction) -> str:
        opcode = instruction[len(instruction)-7: len(instruction)]

        print(f"op code: {opcode}")

        if opcode == "0110011":
            return "R"
        elif opcode == "0010011" or opcode == "0000011" or opcode == "1100111" or opcode == "1110011":
            return "I"
        elif opcode == "0100011":
            return "S"
        elif opcode == "0110111" or opcode == "0010111":
            return "U"
        else:
            self.invalid_instruction(instruction, opcode)

if __name__ == '__main__':
    instruction_add = "0b0000000xxxxxyyyyy000zzzzz0110011"
    instruction_addi = "0bxxxxxxxxxxxxyyyyy000zzzzz0010011"
    instruction_invalid = "0bxxxxxxxxxxxxyyyyy000zzzzz0011111"
    instruction_stype = "0bxxxxxxxxxxxxxxxxxxxxxxxxx0100011"

    decoder = Decoder()

    decoder.decode(instruction_add)
    print()
    decoder.decode(instruction_addi)
    print()
    decoder.decode(instruction_invalid)