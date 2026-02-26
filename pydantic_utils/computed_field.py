from pydantic import BaseModel, Field, EmailStr, AnyUrl, computed_field, ValidationInfo
from typing import List, Dict, Optional, Annotated


class CustomModel(BaseModel):
    name: str = Field(..., description="The name of the patient")
    height: float = Field(..., description="The height of the patient in centimeters")
    weight: float = Field(..., description="The weight of the patient in kilograms")

    @computed_field
    @property
    def bmi(self) -> float:
        height_in_meters = self.height / 100
        bmi_value = self.weight / (height_in_meters ** 2)
        return round(bmi_value, 2)
    

if __name__ == "__main__":
    patient_data = {
        "name": "John Doe",
        "height": 180.0,
        "weight": 75.0
    }
    patient = CustomModel(**patient_data)
    print(patient.model_dump_json())