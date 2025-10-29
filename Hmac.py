import hmac
import hashlib

def create_hmac(key, message):
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

def verify_hmac(key, message, hmac_to_verify):
    generated_hmac = create_hmac(key, message)
    return hmac.compare_digest(generated_hmac, hmac_to_verify)

key = "secretkey"
message = "ZEBRA"
message_hmac = create_hmac(key, message)
print("HMAC:", message_hmac)

# بررسی صحت
(print("Verification:", verify_hmac(key, message, message_hmac)))  # True
