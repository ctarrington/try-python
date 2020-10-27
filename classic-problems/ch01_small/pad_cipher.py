from secrets import token_bytes
from typing import Tuple


def bytes_to_int(raw: bytes) -> int:
    return int.from_bytes(raw, 'big')


def encrypt(plain: str) -> Tuple[int, int]:
    plain_bytes = plain.encode()
    plain_int = bytes_to_int(plain_bytes)

    pad_int = bytes_to_int(token_bytes(len(plain_bytes)))
    encrypted_int = plain_int ^ pad_int  # xor

    return pad_int, encrypted_int


def decrypt(pad: int, encrypted: int) -> str:
    decrypted = pad ^ encrypted
    rounded_up_size = (decrypted.bit_length() + 7) // 8
    decrypted_bytes = decrypted.to_bytes(rounded_up_size, 'big')
    return decrypted_bytes.decode()


original = 'hi there'
key, message = encrypt(original)
recovered = decrypt(key, message)
print(original == recovered)
