from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def aes_encrypt(key, plaintext):
    iv = os.urandom(16)  # Initialization vector تصادفی 16 بایت
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return iv + ciphertext  # iv را به ابتدای پیام رمزگذاری شده می‌چسبانیم

def aes_decrypt(key, ciphertext):
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()
    return plaintext.decode()

key = os.urandom(32)  # کلید 256 بیتی تصادفی
message = "MAHBOD"

encrypted_msg = aes_encrypt(key, message)
print("Encrypted (bytes):", encrypted_msg)

decrypted_msg = aes_decrypt(key, encrypted_msg)
print("Decrypted:", decrypted_msg)
