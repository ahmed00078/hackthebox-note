import string

def decryption(ct):
    pt = []
    for char in ct:
        # Find the multiplicative inverse of  123 modulo  256
        inverse = pow(123, -1,  256)
        # Reverse the operations: subtract  18, multiply by the inverse, and take modulo  256
        pt.append((char -  18) * inverse %  256)
    return bytes(pt)

# Convert the hexadecimal string back to bytes
ct_hex = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
ct_bytes = bytes.fromhex(ct_hex)

# Decrypt the bytes
pt = decryption(ct_bytes)
print(pt)
