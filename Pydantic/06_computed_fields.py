from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    height: float # computed field(kgs)
    weight: float # meters
    married: bool = False # Defaul value
    allergies: List[str] # List[] is used for two-level validation
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi
        
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print('inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('BMI:', patient.bmi)
    print('updated')

patient_info = {'name': 'Akshay Sharma', 'email': 'akshay@hdfc.com', 'age' : 65, 'height': 1.75,'height':1.72, 'weight': 55.2,'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890'}}

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)