from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool = False # Defaul value
    allergies: List[str] # List[] is used for two-level validation
    contact_details: Dict[str, str]
    
    @model_validator(mode='after') 
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model
        
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print('inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name': 'Akshay Sharma', 'email': 'akshay@hdfc.com', 'age' : 7, 'weight': 55.2,'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
# update_patient_data(patient1)