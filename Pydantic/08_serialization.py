from pydantic import BaseModel

class Address(BaseModel):
    
    street: str
    city: str
    state: str
    pincode: str

class Patient(BaseModel):

    name: str
    # gender: str
    gender: str = 'Male' # Default value
    age: int
    address: Address # Nested model


address_dict = {'street': '123 Main St', 'city': 'Jaipur', 'state': 'Rajasthan', 'pincode': '302015'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Akshay Sharma', 'age': 23, 'address': address1}

patient1 = Patient(**patient_dict)

# print(patient1)
# print(patient1.name)
# print(patient1.age)
# print(patient1.address.city)

# temp = patient1.model_dump() # to serialize the model into a dictionary
# temp = patient1.model_dump_json() # to serialize the model into a JSON string
# temp = patient1.model_dump(include={'name', 'age'})
# temp = patient1.model_dump(exclude={'name', 'age'})
# temp = patient1.model_dump(exclude={'address': ['state']})
temp = patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))