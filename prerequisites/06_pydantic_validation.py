from pydantic import BaseModel, validator, root_validator

class CreateUser(BaseModel):
    email: str
    password: str
    confirm_password: str

    @validator("email")
    def validate_email(cls, value):
        if "admin" in value:
            raise ValueError("This email is not allowed")
        return value
    
    @root_validator()
    def validate_password(cls, values):
        password = values.get("password")
        confirm_password = values.get("confirm_password")

        if password != confirm_password:
            raise ValueError("The two passwords should match")
        return values

# Validator for one single field
# Root Validator has access to all field values


CreateUser(email="test@fastapicourse.com", password="123", confirm_password="123")
