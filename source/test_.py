from ByteNode import ByteNode
import pytest

def test_byte_node():
    bn = ByteNode('10011000')
    assert bn.get_next() is None

    bn = ByteNode('10011000')
    assert bn.__repr__() == "[10011000]=>"
    bn2 = ByteNode('11111111')
    bn2.set_next(bn)
    assert bn2.get_next().get_byte() == '10011000'

# since the given string contain '2', we expect to get an error 
def test_ByteNode_1():
    with pytest.raises(ValueError):
        ByteNode('1020102')

# since the length of the given string 
# is bigger than 8, we expect to get an error 
def test_ByteNode_2():
    with pytest.raises(ValueError):
        ByteNode('100010111111')

# since the given input is of type 'int', we expect to get an error 
def test_ByteNode_3():
    with pytest.raises(ValueError):
        ByteNode(10001011)



