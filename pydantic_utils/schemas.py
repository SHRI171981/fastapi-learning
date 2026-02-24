from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str 
    city: str
    age: int
    gender: str
    height: float
    weight: float
    bmi: float
    verdict: str


class CustomModel(BaseModel):
    name: str = Field(..., description="The name of the patient")
    email: EmailStr = Field(..., description="The email address of the patient")
    linkedin: Optional[AnyUrl] = Field(None, description="The LinkedIn profile URL of the patient")
    age: int = Field(..., description="The age of the patient", strict=True) # strict=True will prevent automatic conversion of types, ensuring that the input is strictly an integer
    weight: float = Field(..., description="The weight of the patient in kilograms")
    married: bool = Field(..., description="Marital status of the patient")
    allergies: Optional[List[str]] = Field(None, description="List of allergies the patient has", max_length=5)
    contact_details: Dict[str, str] = Field(..., description="Contact details of the patient, including phone and email")



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
    patient = CustomModel(**patient_data)
    print(patient.model_dump_json())