from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool = False # Defaul value
    allergies: List[str] # List[] is used for two-level validation
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@example.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError(f'Email domain must be one of {valid_domains}')

        return value
    
    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()
    
    # @field_validator('age', mode='before') # returns the value before type coercion
    @field_validator('age', mode='after') # returns the value after type coercion which is always the default behavior
    @classmethod
    def age_validator(cls, value):
        if 0 < value <= 100:
            return value
        raise ValueError('Age must be between 1 and 100')
        
        
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print('inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name': 'Akshay Sharma', 'email': 'akshay@hdfc.com', 'age' : 23, 'weight': 55.2,'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
# update_patient_data(patient1)