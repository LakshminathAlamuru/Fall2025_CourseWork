import random

def generate_keystream(key, length):
    """Generates a pseudorandom keystream using the given key."""
    random.seed(key)  # initialize PRNG with the seed
    keystream = bytes([random.randint(0, 255) for _ in range(length)])
    return keystream

def encrypt(plaintext: bytes, key: int) -> bytes:
    """Encrypt plaintext using XOR with a generated keystream."""
    keystream = generate_keystream(key, len(plaintext))
    ciphertext = bytes([p ^ k for p, k in zip(plaintext, keystream)])
    return ciphertext

def decrypt(ciphertext: bytes, key: int) -> bytes:
    """Decrypt ciphertext (same operation as encryption)."""
    return encrypt(ciphertext, key)

# Example data
key = 0b01011101  # Seed for PRNG
plaintext = b'\xB5'  # 0b10110101 as one byte

# Encryption
ciphertext = encrypt(plaintext, key)

# Decryption
decrypted_text = decrypt(ciphertext, key)

print("Plaintext (bits) :", format(plaintext[0], '08b'))
print("Ciphertext (bits):", format(ciphertext[0], '08b'))
print("Decrypted (bits) :", format(decrypted_text[0], '08b'))
