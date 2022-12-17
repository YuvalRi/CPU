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
        my_str = binary.zfill(((8 - remnant) + len(binary)))
        self.head = ByteNode(my_str[:8])
        self.size = (len(my_str))/8
        curr_pos = self.head
        for j in range(self.size - 1):
            pos = ByteNode(my_str[8*j:8*j + 8])
            curr_pos.next = pos
            curr_pos = pos
        

        # my_str2 = [my_str[i:i+8] for i in range(0, len(my_str), 8)]
        # for ele in my_str2[:len(my_str2)-1]:
        #     print(ByteNode(ele), end =" ")
        # print(f"{ByteNode(my_str2[len(my_str2)-1])}None")


    def add_MSB(self, byte:  str):
        pass 


if __name__ == "__main__":
    # binary = bin(256)[2:]
    # remnant = len(binary) % 8
    # my_str = binary.zfill(((8 - remnant) + len(binary)))
    # head = ByteNode(my_str[:8])
    # size = (len(my_str)) / 8 
    # my_str2 = [my_str[i:i+8] for i in range(0, len(my_str), 8)]
    # for ele in my_str2[:len(my_str2)-1]:
    #     print(ByteNode(ele), end =" ")
    # print(f"{ByteNode(my_str2[len(my_str2)-1])}None")
    # print(head)
    # print(size)
