from pydantic import BaseModel

class Address(BaseModel):
    
    street: str
    city: str
    state: str
    pincode: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address # Nested model


address_dict = {'street': '123 Main St', 'city': 'Jaipur', 'state': 'Rajasthan', 'pincode': '302015'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Akshay Sharma', 'gender': 'male', 'age': 23, 'address': address1}

patient1 = Patient(**patient_dict)

# print(patient1)
print(patient1.name)
print(patient1.age)
print(patient1.address.city)

# ============================================================
# WHY NESTED MODELS ARE IMPORTANT
# ============================================================
# Real-world objects are not flat.
#
# A patient has:
# - name
# - age
# - address (which itself has fields)
#
# Address is its OWN model.
# Patient simply USES it.
#
# Pydantic automatically:
# - Validates Address
# - Embeds it inside Patient
#
# BIG BENEFIT:
# - Clean structure
# - Easy access: patient.address.city
#
# THINK OF THIS AS:
# "Models inside models"
# ============================================================
