import hashlib

# Create a hash
data = "Password123".encode('utf-8')
hash_object = hashlib.sha256(data)
hex_dig = hash_object.hexdigest()

print(f"SHA-256 Hash: {hex_dig}")

# Salted hash
salt = "randomsalt".encode('utf-8')
salted_data = salt + data
hash_object = hashlib.sha256(salted_data)
hex_dig = hash_object.hexdigest()
print(f"Salted SHA-256 Hash: {hex_dig}")
