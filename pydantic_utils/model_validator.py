from pydantic import BaseModel, Field, EmailStr, AnyUrl, model_validator, ValidationInfo
from typing import List, Dict, Optional, Annotated


class CustomModel(BaseModel):
    name: str = Field(..., description="The name of the patient")
    password: str = Field(..., description="The password of the patient")
    confirm_password: str = Field(..., description="The confirmation of the password")

    @model_validator(mode='after')
    @classmethod
    def validate_passwords(cls, model):
        password = model.password
        confirm_password = model.confirm_password
        if password != confirm_password:
            raise ValueError("Password and confirm password do not match")
        return model
    
if __name__ == "__main__":
    patient_data = {
        "name": "John Doe",
        "password": "secret13",
        "confirm_password": "secret123"
    }
    patient = CustomModel.model_validate(patient_data)
    print(patient.model_dump_json())