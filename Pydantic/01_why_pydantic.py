def insert_patient_data(name, age):

    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age can't be negative")
        else:
            print(name)
            print(age)
            print('inserted into database')
    else:
        raise TypeError("Invalid data types for name or age")
    
def update_patient_data(name, age):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('updated')
    else:
        raise TypeError("Invalid data types for name or age")
    
    
insert_patient_data('Akshay', 30)

# ============================================================
# WHY THIS FILE EXISTS
# ============================================================
# Before learning Pydantic, it is very important to understand
# the PROBLEM it is trying to solve.
#
# In this file, we are validating data using NORMAL PYTHON.
#
# Look at insert_patient_data():
# - We are manually checking:
#     type(name) == str
#     type(age) == int
# - Then we are manually checking:
#     age < 0
#
# This approach looks okay for 2 fields,
# BUT imagine if we add:
# - email
# - phone number
# - address
# - marital status
#
# Every function will need:
# - repeated type checks
# - repeated error handling
#
# PROBLEMS WITH THIS APPROACH:
# 1. Validation code is repeated again and again
# 2. Logic is mixed with business code
# 3. Hard to scale for real applications
# 4. Very difficult to use in APIs
#
# IMPORTANT REALIZATION:
# "Data validation should be CENTRALIZED, not scattered"
#
# THIS FILE SETS THE BASE:
# - It shows HOW we used to validate data
# - It prepares our mind for WHY Pydantic is better
#
# After this file, we stop validating data manually
# and let Pydantic do the heavy lifting.
# ============================================================
