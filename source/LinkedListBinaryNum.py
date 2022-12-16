from ByteNode import ByteNode
import math
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
        if num < 0:
            raise ValueError("Error! Input must be positive!")
        binary = bin(num)[2:]
        remnant = len(binary) % 8
        if remnant != 0:
            my_str = binary.zfill(((8 - remnant) + len(binary)))
        else:
            my_str = binary
        self.head = ByteNode(my_str[:8])
        size = ((8 - remnant) + len(binary))/ 8


    def add_MSB(self, byte:  str):
        pass 
        
