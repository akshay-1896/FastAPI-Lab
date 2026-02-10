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

# ============================================================
# WHAT THIS FILE TEACHES
# ============================================================
# This file shows the FIRST BIG SUPERPOWER of Pydantic:
# 👉 Automatic type validation using BaseModel
#
# Instead of passing raw variables (name, age),
# we now pass a SINGLE object: Patient
#
# Look at the Patient class:
# - name: str
# - age: int
# - weight: float
#
# This means:
# "Whenever someone creates a Patient object,
#  these rules MUST be followed"
#
# VERY IMPORTANT POINT:
# Validation happens AT OBJECT CREATION:
# patient1 = Patient(**patient_info)
#
# If data is invalid:
# - Program stops immediately
# - Clear error is raised
#
# DEFAULT VALUES:
# married: bool = False
# → If user does not send married, False is assumed
#
# OPTIONAL FIELDS:
# allergies: Optional[List[str]]
# → allergies can be None OR a list of strings
#
# BIG CONCEPTUAL SHIFT:
# Earlier → Functions validated data
# Now     → Models validate data
#
# WHY THIS IS EASY TO LEARN:
# - No if/else
# - No manual type checks
# - Just define rules once
#
# MENTAL MODEL:
# "Patient class is a gatekeeper.
#  Only valid data is allowed inside."
# ============================================================
