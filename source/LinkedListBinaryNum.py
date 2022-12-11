@total_ordering
class LinkedListBinaryNum:
    def __init__(self, num=0):
        if not isinstance(num, int):
            raise TypeError("The number must be an int!")
        elif num < 0:
            raise ValueError('The number must be a positive int!')

        self.size = 0
        self.head = None

        byte_size = 8
        bin_num = bin(num).replace("0b", "")

        for i in range(len(bin_num), 0, -byte_size):
            min = i - byte_size if i - byte_size >= 0 else 0
            byte = bin_num[min:i]
            byte = byte.zfill(byte_size)
            self.add_MSB(byte)

    def add_MSB(self, byte):
        new_head = ByteNode(byte)
        old_head = self.head
        new_head.next = old_head
        self.head = new_head
        self.size += 1

    def __len__(self):
        return self.size

    def __str__(self):  # end user
        curr = self.head
        str = "|"
        while curr is not None:
            str += curr.get_byte() + "|"
            curr = curr.get_next()
        return str

    def __repr__(self):  # developer
        byte_msg = "Byte" if len(self) == 1 else "Bytes"
        msg = f"LinkedListBinaryNum with {self.size} {byte_msg}, Bytes map: "

        current_node = self.head
        while current_node is not None:
            msg += str(current_node)
            current_node = current_node.get_next()

        msg += str(current_node)

        return msg

    def __getitem__(self, item):
        if not isinstance(self, LinkedListBinaryNum):
            return TypeError

        if item <= -1 * self.size - 1 or self.size <= item:
            raise IndexError

        if item < 0:
            item += self.size

        i = 0
        curr = self.head
        while i < item:
            curr = curr.get_next()
            i += 1

        return curr.get_byte()

    # Order relations:
    def __eq__(self, other):
        if len(self) == len(other):
            for i in range(len(self)):
                if self[i] != other[i]:
                    return False
            return True
        return False

    def __gt__(self, other):
        for i in range(len(self)):
            if self[i] > other[i]:
                return True
            return False

    def __add__(self, other):
        min = self if len(self) < len(other) else other
        max = self if len(self) > len(other) else other
        to_add = len(max) - len(min)
        for i in range(to_add):
            min.add_MSB(ByteNode("00000000"))
        #print(f"1: {self}, 2: {other}")
        c_out = 0
        for i in range(len(max)-1,-1,-1):
            byte1, byte2 = self[i], other[i]
            #print(f"byte1: {byte1}, byte2: {byte2}")
            ans_byte = ""
            for bit in range(7, -1, -1):
                s  = int(byte1[bit]) + int(byte2[bit]) + int(c_out)
                if s == 0:
                    s = 0
                    c_out = 0
     
                elif s == 1:
                    s = 1
                    c_out = 0
                elif s == 2:
                    s = 0
                    c_out = 1
                elif s == 3:
                    s = 1
                    c_out = 1
                else:
                    print(f"ERORR in FA - s = {s}")
                ans_byte = str(s) + ans_byte
            # changes start here
            if i == len(max)-1:
                ans = LinkedListBinaryNum(int(ans_byte,2))   
            else:    
                ans.add_MSB(ans_byte)
            # end here
            print(ans)
        return ans

    def __sub__(self, other):
        # str1, str2 = normaliseString(str1, str2)
        # startIdx = 0
        # endIdx = len(str1) - 1
        # carry = [0] * len(str1)
        # result = ''
        #
        # while endIdx >= startIdx:
        #     x = int(str1[endIdx])
        #     y = int(str2[endIdx])
        #     sub = (carry[endIdx] + x) - y
        #
        #     if sub == -1:
        #         result += '1'
        #         carry[endIdx - 1] = -1
        #
        #     elif sub == 1:
        #         result += '1'
        #     elif sub == 0:
        #         result += '0'
        #     else:
        #         raise Exception('Error')
        #
        #     endIdx -= 1
        #
        # return result[::-1]
        pass

    def __radd__(self, other):
        pass