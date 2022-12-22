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
        if len(binary) % 8 != 0:
            my_str = binary.zfill(((8 - remnant) + len(binary)))
        else:
            my_str = binary.zfill(((len(binary))))
        self.head = ByteNode(my_str[:8])
        self.size = (len(my_str))//8
        curr_pos = self.head
        for j in range(1, self.size):
            pos = ByteNode(my_str[8*j:8*j + 8])
            curr_pos.next = pos
            curr_pos = pos

    def add_MSB(self, byte:  str):
        '''
        A function that adds a MSB node to LinkedListBinaryNum
        '''
        new_byte = ByteNode(byte)
        new_byte.next = self.head
        self.head = new_byte
        self.size += 1

    def __repr__(self):
        '''
        A function that returns a string with all nodes 
        that consists the binary representation
        '''
        curr_pos = self.head
        st = ''
        while curr_pos != None:
            st += curr_pos.__repr__()
            curr_pos = curr_pos.get_next()
        st += 'None'
        if self.size == 1:
            return f"LinkedListBinaryNum with 1 Byte, Bytes map: {st}" 
        return f"LinkedListBinaryNum with {self.size} Bytes, Bytes map: {st}" 
        
    def __str__(self):
        '''
        A function that returns a representive string
        where bytes divided by "|" 
        '''
        curr_pos = self.head
        st = '|'
        while curr_pos != None:
            st += curr_pos.byte + '|'
            curr_pos = curr_pos.get_next()
        return st

        
            
        
        
        