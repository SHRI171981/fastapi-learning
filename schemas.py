from pydantic import BaseModel, Field, ValidationInfo, field_validator, computed_field


class Patient(BaseModel):
    id: str = Field(..., description="The unique identifier for the patient")
    name: str = Field(..., description="The name of the patient")
    age: int = Field(..., description="The age of the patient")
    gender: str = Field(..., description="The gender of the patient")
    height: float = Field(..., description="The height of the patient in centimeters")
    weight: float = Field(..., description="The weight of the patient in kilograms")
    
    # field validations
    @field_validator("age")
    @classmethod
    def validate_age(cls, age: int) -> int:
        if age < 0:
            raise ValueError("Age must be a positive integer")
        return age

    @field_validator("gender")
    @classmethod
    def validate_gender(cls, gender: str) -> str:
        if gender.lower() not in ["male", "female", "other"]:
            raise ValueError("Gender must be 'Male', 'Female', or 'Other'")
        return gender
    
    @field_validator("height")
    @classmethod
    def validate_height(cls, height: float) -> float:
        if height <= 0:
            raise ValueError("Height must be a positive number")
        return height
    
    @field_validator("weight")
    @classmethod
    def validate_weight(cls, weight: float) -> float:
        if weight <= 0:
            raise ValueError("Weight must be a positive number")
        return weight

    @computed_field
    @property
    def BMI(self) -> float:
        height_in_meters = self.height / 100
        return round(self.weight / (height_in_meters ** 2), 2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        bmi = self.BMI
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"


class PatientUpdate(BaseModel):
    id: str = Field(None, description="The unique identifier for the patient")
    name: str = Field(None, description="The name of the patient")
    age: int = Field(None, description="The age of the patient")
    gender: str = Field(None, description="The gender of the patient")
    height: float = Field(None, description="The height of the patient in centimeters")
    weight: float = Field(None, description="The weight of the patient in kilograms")
    
    # field validations
    @field_validator("age")
    @classmethod
    def validate_age(cls, age: int) -> int:
        if age < 0:
            raise ValueError("Age must be a positive integer")
        return age

    @field_validator("gender")
    @classmethod
    def validate_gender(cls, gender: str) -> str:
        if gender.lower() not in ["male", "female", "other"]:
            raise ValueError("Gender must be 'Male', 'Female', or 'Other'")
        return gender
    
    @field_validator("height")
    @classmethod
    def validate_height(cls, height: float) -> float:
        if height <= 0:
            raise ValueError("Height must be a positive number")
        return height
    
    @field_validator("weight")
    @classmethod
    def validate_weight(cls, weight: float) -> float:
        if weight <= 0:
            raise ValueError("Weight must be a positive number")
        return weight

    @computed_field
    @property
    def BMI(self) -> float:
        height_in_meters = self.height / 100
        return round(self.weight / (height_in_meters ** 2), 2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        bmi = self.BMI
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
