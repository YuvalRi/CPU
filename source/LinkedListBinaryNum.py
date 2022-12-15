#LSB = Least Significant Bit
#MSB = Most Significant Bit

class LinkedListBinaryNum:
    def __init__(self, num: int):
        '''
        Constructor function
        Input should be integer and positive
        '''
        if not isinstance(num, int):
            raise ValueError("Error! Input must be integer!")
        if num <= 0:
            raise ValueError("Error! Input must be positive!")

    def add_MSB(self, byte:  str):
        pass
        
