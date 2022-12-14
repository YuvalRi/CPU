class ByteNode:
    def __init__(self, byte: str):
        '''
        Construction function
        '''
        if not isinstance(byte, str):
            raise ValueError("Error! byte must be of type string")
        if len(byte) != 8:
            raise ValueError("Error! byte length must be eight")
        for c in byte:
            if c != '1' and c != '0':
                raise ValueError("Error! byte inculdes only '0' or '1'")
        self.byte = byte
        self.next = None
    
    def get_byte(self):
        '''
        A function that returns 'byte' field.
        '''
        return self.byte

    def get_next(self):
        '''
        A function that returns 'next' field.
        '''
        return self.next

    def set_next(self, next):
        '''
        A function that updates 'next' field into next parameter.
        '''
        self.next = next
    
    def __repr__(self):
        return f"[{self.byte}]=>"

if __name__ == "__main__":
    bn = ByteNode(byte='10011000')
    print(bn)
    bn2 = ByteNode('11111111')
    bn2.set_next(bn)
    print(bn2.get_next().get_byte())