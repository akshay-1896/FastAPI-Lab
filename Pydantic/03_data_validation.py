from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Patient Name', description='The full name of the patient in less than 50 characters', examples=['Nitish Kumar', 'Sonia Gandhi'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)] # strict=True ensures that type coercion is not allowed
    # married: bool = False # Defaul value
    married: Annotated[bool, Field(default=None, description='Marital status of the patient')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)] # List[] is used for two-level validation
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print('inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name': 'Akshay', 'email': 'akshay@gmail.com', 'linkedin_url': 'https://www.linkedin.com/in/akshay', 'age' : 23, 'weight': 55.2, 'contact_details': {'phone': '123-456-7890'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
# update_patient_data(patient1)