import sys

value_to_code_map = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}
code_to_value_map = {value: key for key, value in value_to_code_map.items()}

def encode(raw):
    encoded = 1 # add sentinel at left
    for letter in raw:
        encoded <<= 2
        code = value_to_code_map[letter]
        encoded |= code

    return encoded

def decode(encoded):
    characters = []

    bit_length = encoded.bit_length() - 1  # ignore sentinel
    for index in range(0, bit_length, 2):
        value = encoded & 3
        characters.append(code_to_value_map[value])
        encoded >>= 2

    return ''.join(list(reversed(characters)))

original = 'ACGT' * 10000
original_size = sys.getsizeof(original)
compressed = encode(original)
compressed_size = sys.getsizeof(compressed)

uncompressed = decode(compressed)
print(original == uncompressed)

compression_ratio = compressed_size / original_size
print('original {}, compressed: {} compression_ratio: {}'.format(original_size, compressed_size, compression_ratio))

