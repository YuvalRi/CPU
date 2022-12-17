from ByteNode import ByteNode
from LinkedListBinaryNum import LinkedListBinaryNum

def test_byte_node():
    bn = ByteNode('10011000')
    assert bn.get_next() is None

    bn = ByteNode('10011000')
    assert bn.__repr__() == "[10011000]=>"
    bn2 = ByteNode('11111111')
    bn2.set_next(bn)
    assert bn2.get_next().get_byte() == "10011000"


def tests_init_linked_list_binary_num():
    bn1 = LinkedListBinaryNum(0)
    assert bn1.__repr__() == "LinkedListBinaryNum with 1 Byte, Bytes map: [00000000]=>None"
    bn1 = LinkedListBinaryNum(255)
    assert bn1.__repr__() == "LinkedListBinaryNum with 1 Byte, Bytes map: [11111111]=>None"
    bn1 = LinkedListBinaryNum(4294967296)
    assert bn1.__repr__() == "LinkedListBinaryNum with 5 Bytes, Bytes map: [00000001]=>[00000000]=>[00000000]=>[00000000]=>[00000000]=>None"
    for i in range(2**8 - 1):
        bn1 = LinkedListBinaryNum(i)
        assert bn1.__repr__() == f"LinkedListBinaryNum with 1 Byte, Bytes map: [{bin(i)[2:].zfill(8)}]=>None"
    
    for i in range(2**8, 2**16 - 1):
        bn1 = LinkedListBinaryNum(i)
        assert bn1.__repr__() == f"LinkedListBinaryNum with 2 Bytes, Bytes map: [{bin(i)[2:].zfill(16)[:8]}]=>[{bin(i)[2:].zfill(16)[8:]}]=>None"

def test_add_msb():
    bn1 = LinkedListBinaryNum(0)
    assert bn1.__repr__() == "LinkedListBinaryNum with 1 Byte, Bytes map: [00000000]=>None"

    import random
    st = ""
    for i in range(30):
        byte =  ''.join(random.choices(['0', '1'], k=8))
        bn1.add_MSB(byte)
        st = f"[{byte}]=>" + st
        assert bn1.__repr__() == f"LinkedListBinaryNum with 1 Byte, Bytes map: {st}[00000000]=>None"


def test_str_func():
    bn = LinkedListBinaryNum(0)
    res_str = "00000000|"
    import random
    for i in range(50):
        byte = ''.join(random.choices(['0', '1'], k=8))
        bn.add_MSB(byte)
        res_str = f"{byte}|" + res_str
        assert bn.__str__() == f"|{res_str}"

def test_get_item():
    bn = LinkedListBinaryNum(12345678901234567890)
    st = bn.__str__()
    lst = st.split("|")[1:-1]
    for i in range(len(lst) - 1):
        assert bn[i] == lst[i]
        assert bn[i] == bn[- bn.size + i]
        
