def signed_int(byte_one: int, byte_two: int):
    return byte_one + 256 * byte_two


def grab_byte(byte: int, bit: int):
    return byte & 1 << bit != 0

def extract_by_range(data, start_bit, stop_bit):
    x = data[0] + 256 * data[1] + 256**2 * data[2] + 256**3 * data[3] + 256**4 * data[4] + 256**5 * data[5] + 256**6 * data[6] + 256**7 * data[7]
    base_mask = 2 ** (stop_bit - start_bit) - 1
    mask = base_mask << start_bit
    return (mask & x) >> start_bit
