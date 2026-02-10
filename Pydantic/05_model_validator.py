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

patient_info = {'name': 'Akshay Sharma', 'email': 'akshay@hdfc.com', 'age' : 65, 'weight': 55.2,'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890', 'emergency': '987-654-3210'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
# update_patient_data(patient1)

# ============================================================
# WHY MODEL VALIDATORS EXIST
# ============================================================
# Sometimes, validation depends on MULTIPLE fields.
#
# Example in this file:
# - If age > 60
# - emergency contact MUST exist
#
# Field validators cannot see other fields reliably.
# So we use @model_validator
#
# model_validator(mode='after'):
# - Runs AFTER all fields are validated
# - Has access to FULL model
#
# VERY IMPORTANT CONCEPT:
# "Individual fields may be valid,
#  but the object as a whole may be invalid."
#
# REAL-WORLD EXAMPLES:
# - If payment_method = "card", card_number is required
# - If user is minor, guardian info is required
#
# THINK OF IT AS:
# "Final approval before object is accepted"
# ============================================================
