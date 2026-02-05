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