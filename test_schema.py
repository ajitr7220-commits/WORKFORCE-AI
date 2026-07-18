from backend.app.schemas.auth import RegisterRequest

user = RegisterRequest(
    organization_name="ABC Hospital",
    name="Ajit Rout",
    email="ajit@example.com",
    password="Ajit@1234"
)

print(user)