from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, ValidationInfo
from typing import List, Dict, Optional, Annotated


class CustomModel(BaseModel):
    name: str = Field(..., description="The name of the patient")
    email: EmailStr = Field(..., description="The email address of the patient")
    linkedin: Optional[AnyUrl] = Field(None, description="The LinkedIn profile URL of the patient")
    age: int = Field(..., description="The age of the patient", strict=True) # strict=True will prevent automatic conversion of types, ensuring that the input is strictly an integer
    weight: float = Field(..., description="The weight of the patient in kilograms")
    married: bool = Field(..., description="Marital status of the patient")
    allergies: Optional[List[str]] = Field(None, description="List of allergies the patient has", max_length=5)
    contact_details: Dict[str, str] = Field(..., description="Contact details of the patient, including phone and email")

    @field_validator('email')
    @classmethod
    def validate_email(cls, value, info: ValidationInfo):
        valid_domains = info.context.get('valid_domains', [])
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()  # Convert the name to uppercase

if __name__ == "__main__":
    patient_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "linkedin": "https://www.linkedin.com/in/johndoe",
        "age": 30,
        "weight": 70.5,
        "married": True,
        "allergies": ["Peanuts", "Shellfish"],
        "contact_details": {
            "phone": "123-456-7890",
            "email": "john.doe@example.com"
        }
    }
    allowed_domains: List[str] = ["example.com", "test.com"]
    patient = CustomModel.model_validate(patient_data, context={'valid_domains': allowed_domains})
    print(patient.model_dump_json())