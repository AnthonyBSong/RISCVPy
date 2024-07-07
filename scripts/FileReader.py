class AssemblyFileReader:
    def __init__(self, file_path):
        """Initializes the AFR object with the filepath
        and opens the file. Sets current_line (the index of 
        the line that will be read) to 0. Stores the total number
        of lines in the file."""
        self.file_path = file_path
        self.file = open(file_path, 'r')
        self.current_line = 0
        self.total_lines = self.count_lines()

    def count_lines(self):
        "Counts the number of lines in the file."
        with open(self.file_path, 'r') as f:
            return sum(1 for i in f)
        
    def read_next_line(self):
        """Reads the next line of the file and returns it.
        If all lines have been read, returns None. 
        Keeps track of the current position. 
        WILL READ BLANK LINES."""
        if self.current_line < self.total_lines:
            self.file.seek(0)
            for i in range(self.current_line):
                self.file.readline()
            line = self.file.readline()
            self.current_line += 1
            return line.strip()
        else:
            return None
    
    def read_all(self):
        """Reads the entire file. Returns it as a 
        single string."""
        self.file.seek(0)
        return ''.join(self.file.readlines()).strip()
    
    def reset(self):
        """Resets the current line counter."""
        self.current_line = 0
    
    def delete(self):
        """To ensure the file gets closed."""
        self.file.close()
