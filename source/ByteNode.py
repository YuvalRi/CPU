class ByteNode:
    def __init__(self, byte: str):
        '''
        Construction function
        '''
        if not isinstance(byte, str):
            raise ValueError("Error! byte must be of type string")
        if len(str) != 8:
            raise ValueError("Error! byte length must be eight")
        if '0' or '1' not in str and len(set(str)) > 2:
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
