from LinkedListBinaryNum import LinkedListBinaryNum

class NumsManagment:
    def __init__(self, file_name):
        self.file_name = file_name

    def is_line_pos_int(self, st):
        if st > 0 and isinstance(st, int):
            return True
        return False

    def read_from_file_gen(self):