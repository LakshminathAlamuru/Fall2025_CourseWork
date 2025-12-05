import os

def generate_keystream(length: int) -> bytes:
    """Generate a secure pseudorandom keystream using OS CSPRNG."""
    return os.urandom(length)  # cryptographically secure random bytes

def encrypt(plaintext: bytes, keystream: bytes) -> bytes:
    """Encrypt plaintext using XOR with the keystream."""
    return bytes([p ^ k for p, k in zip(plaintext, keystream)])

def decrypt(ciphertext: bytes, keystream: bytes) -> bytes:
    """Decrypt ciphertext (same operation as encryption)."""
    return encrypt(ciphertext, keystream)

# Example plaintext
plaintext = b"HELLO"  # 5 bytes of plaintext

# Step 1: Generate secure keystream of equal length
keystream = generate_keystream(len(plaintext))

# Step 2: Encrypt plaintext
ciphertext = encrypt(plaintext, keystream)

# Step 3: Decrypt ciphertext (using same keystream)
decrypted_text = decrypt(ciphertext, keystream)

# Display results
print("Plaintext     :", plaintext)
print("Keystream (hex):", keystream.hex())
print("Ciphertext (hex):", ciphertext.hex())
print("Decrypted Text :", decrypted_text)
