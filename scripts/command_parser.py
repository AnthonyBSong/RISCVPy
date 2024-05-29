

class CommandParser():
    def __init__(self):
        pass

    def parse_string(self, s: str):
        arr = (s.replace(",", "")).split(" ")

        print(arr)


if __name__ == "__main__":
    cp = CommandParser()

    cp.parse_string("add rd, rs1, rs2")
    cp.parse_string("li x1, 5")
