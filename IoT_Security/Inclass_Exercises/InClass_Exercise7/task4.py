# Demonstration of known-plaintext attack when the same keystream is reused
import os

# Two plaintexts of equal length (required for this simple demo)
P1 = b'HELLO123'   # attacker knows or guesses this
P2 = b'SECRET42'   # target message attacker wants to recover

# Attacker and sender mistakenly reuse the same keystream K
K = os.urandom(len(P1))    # keystream (should NEVER be reused in real systems)

# Sender encrypts both messages with same keystream
C1 = bytes([p ^ k for p, k in zip(P1, K)])
C2 = bytes([p ^ k for p, k in zip(P2, K)])

# --- Attacker side (knows P1 and C1) ---
# Recover keystream:
K_recovered = bytes([p ^ c for p, c in zip(P1, C1)])   # K_recovered == K

# Use recovered keystream to decrypt C2:
P2_recovered = bytes([c ^ k for c, k in zip(C2, K_recovered)])

# Print results (binary and ascii)
def bstr(x): return ' '.join(format(b, '08b') for b in x)

print("P1 (ASCII)        :", P1)
print("P1 (binary)       :", bstr(P1))
print("C1 (binary)       :", bstr(C1))
print("Recovered K (bin) :", bstr(K_recovered))
print()
print("C2 (binary)       :", bstr(C2))
print("P2 recovered (ASCII):", P2_recovered)
print("P2 recovered (binary):", bstr(P2_recovered))

# Verify correctness
print("\nKeystream match?   ", K_recovered == K)
print("P2 match?          ", P2_recovered == P2)
