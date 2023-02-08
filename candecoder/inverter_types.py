def signed_int(byte_one: int, byte_two: int):
    return byte_one + 256 * byte_two


def grab_byte(byte: int, bit: int):
    return byte & 1 << bit != 0
