def xor_encrypt_decrypt(text, key):
    result = ""
    for char in text:
        result += chr(ord(char) ^ key)
    return result

message = "MAHBOD"
key = 1324

encrypted = xor_encrypt_decrypt(message, key)
decrypted = xor_encrypt_decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
