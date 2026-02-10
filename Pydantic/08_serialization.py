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

# ============================================================
# WHAT THIS FILE IS REALLY ABOUT
# ============================================================
# This file teaches how a Pydantic model is converted
# into a dictionary or JSON in a CONTROLLED way.
#
# Serialization means:
# "Take a Pydantic object and convert it into plain data
#  (dict / JSON) that can be sent outside Python"
#
# ------------------------------------------------------------
# STEP 1: NESTED MODELS RECAP
# ------------------------------------------------------------
# Address is a separate BaseModel.
# Patient contains Address as a field.
#
# This means:
# - Patient is NOT flat data
# - It has a nested structure
#
# Pydantic understands this hierarchy automatically.
#
# ------------------------------------------------------------
# STEP 2: DEFAULT VALUES DURING SERIALIZATION
# ------------------------------------------------------------
# gender: str = 'Male'
#
# Here, gender is NOT provided while creating patient_dict.
# But Pydantic still assigns:
# gender = 'Male'
#
# Important concept:
# DEFAULT values become part of the model automatically.
#
# ------------------------------------------------------------
# STEP 3: CREATING THE MODEL INSTANCE
# ------------------------------------------------------------
# patient1 = Patient(**patient_dict)
#
# At this point:
# - Validation is done
# - Defaults are applied
# - Nested Address is fully validated
#
# patient1 is now a "clean, trusted object"
#
# ------------------------------------------------------------
# STEP 4: BASIC SERIALIZATION
# ------------------------------------------------------------
# model_dump()
# → Converts the model into a Python dictionary
#
# model_dump_json()
# → Converts the model into a JSON string
#
# Key idea:
# "Serialization removes Pydantic and leaves pure data"
#
# ------------------------------------------------------------
# STEP 5: PARTIAL SERIALIZATION (include / exclude)
# ------------------------------------------------------------
# model_dump(include={'name', 'age'})
# → Only selected fields are included
#
# model_dump(exclude={'name', 'age'})
# → Selected fields are removed
#
# Nested exclusion:
# model_dump(exclude={'address': ['state']})
# → Removes only 'state' from address
#
# This is VERY powerful for APIs:
# - Hide sensitive data
# - Send only required fields
#
# ------------------------------------------------------------
# STEP 6: exclude_unset=True (VERY IMPORTANT)
# ------------------------------------------------------------
# temp = patient1.model_dump(exclude_unset=True)
#
# Meaning:
# - Only include fields that were explicitly provided
# - Exclude defaulted values
#
# In this file:
# - gender was NOT provided by user
# - gender is excluded from output
#
# This helps in:
# - PATCH APIs
# - Partial updates
# - Clean payloads
#
# ------------------------------------------------------------
# FINAL MENTAL MODEL
# ------------------------------------------------------------
# Validation happens ONCE (while creating model)
# Serialization can happen MANY times
#
# Pydantic gives FULL CONTROL over:
# - What data goes out
# - How nested data looks
# - Whether defaults are included or not
#
# ------------------------------------------------------------
# ONE-LINE TAKEAWAY
# ------------------------------------------------------------
# "Pydantic models are for safety inside Python,
#  serialization is for communication outside Python."
# ============================================================
