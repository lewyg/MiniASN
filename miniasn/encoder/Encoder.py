def encode_bool(reader):
    bit = reader.read_bit()

    return bit == 1


def encode_bitstring(reader, len):
    bitstring = ''
    for i in range(len):
        bitstring += str(reader.read_bit())

    return bitstring


def encode_uint(reader, len):
    bits = []
    number = 0
    bit_position = 0

    for i in range(len):
        bits.append(reader.read_bit())

    for bit in reversed(bits):
        number += bit * 2 ** bit_position
        bit_position += 1

    return number
