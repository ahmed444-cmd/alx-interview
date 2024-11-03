#!/usr/bin/python3
"""UTF-8 encoding standards Validation"""


def get_leading_set_bits(num):
    """Returns the count of consecutive leading 1-bits"""
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """Checks if the given data set is a valid UTF-8 encoding"""
    bits_count = 0
    for i in range(len(data)):
        if bits_count == 0:
            bits_count = get_leading_set_bits(data[i])
            '''Defines a 1-byte UTF-8 format (0xxxxxxx)'''
            if bits_count == 0:
                continue
            '''UTF-8 encoding allows characters to be 1 to 4 bytes long'''
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            '''Determines if the byte structure is 10xxxxxx'''
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bits_count -= 1
    return bits_count == 0
