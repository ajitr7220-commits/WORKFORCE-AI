from backend.app.auth.password import hash_password, verify_password

password = "Ajit@123"
hashed = hash_password(password)

print("Hashed:", hashed)
print("verify:", verify_password(password, hashed))