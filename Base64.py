import base64

def base64_encode(text):
    message_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('utf-8')

def base64_decode(encoded_text):
    base64_bytes = encoded_text.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('utf-8')

message = "ZEBRA"
encoded = base64_encode(message)
decoded = base64_decode(encoded)

print("Encoded:", encoded)
print("Decoded:", decoded)
