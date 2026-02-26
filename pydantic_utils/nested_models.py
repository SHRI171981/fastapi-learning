from pydantic import BaseModel, Field, EmailStr, AnyUrl, computed_field, ValidationInfo
from typing import List, Dict, Optional, Annotated


class Address(BaseModel):
    street: str = Field(..., description="The street address of the patient")
    city: str = Field(..., description="The city of the patient")
    state: str = Field(..., description="The state of the patient")
    zip_code: str = Field(..., description="The zip code of the patient")

class CustomModel(BaseModel):
    name: str = Field(..., description="The name of the patient")
    address: Address = Field(..., description="The address of the patient") # Nested model for the patient's
    

if __name__ == "__main__":
    patient_data = {
        "name": "John Doe",
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip_code": "12345"
        }
    }
    patient = CustomModel.model_validate(patient_data)
    print(patient.model_dump_json())