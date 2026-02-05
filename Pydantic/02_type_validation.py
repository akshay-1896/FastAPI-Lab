from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool = False # Defaul value
    allergies: Optional[List[str]] = None # List[] is used for two-level validation
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print('inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name': 'Akshay', 'age' : 23, 'weight': 55.2, 'contact_details': {'email': 'akshay@example.com', 'phone': '123-456-7890'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
# update_patient_data(patient1)