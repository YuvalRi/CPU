from LinkedListBinaryNum import LinkedListBinaryNum

class NumsManagment:
    def __init__(self, file_name):
        '''
        A contructor function which recieves the name
        of the file as a string and save it as a field
        in the class.
        '''
        self.file_name = file_name

    def is_line_pos_int(self, st):
        '''
        A function that checks if a line in the given file
        represents an integer and positive number 
        '''
        if st > 0 and isinstance(st, int):
            return True
        return False

    def read_from_file_gen(self):
        '''
        A function that returns a generator which
        in each iteration returns binary representation of each number
        in the file
        '''
        file = open("file_name.txt")
        for line in file.readlines():
            x = LinkedListBinaryNum(int(line))
            yield x
        