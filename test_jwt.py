from backend.app.auth.jwt import create_access_token , decode_access_token


token = create_access_token(
    {
        "sub": 'ajit@example.com'
    }
)

print("Token:")
print(token)

payload = decode_access_token(token)

print("\nDecoded payload:")
print(payload)