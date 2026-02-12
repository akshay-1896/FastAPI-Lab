from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
import json
from typing import Annotated, Literal
from pydantic import BaseModel, Field, computed_field

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City of residence')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in meters')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kilograms')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height **2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal weight'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'

def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)

    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)


@app.get("/")
def hello():
    return {'message': 'Patient Management System API'}


@app.get("/about")
def about():
    return {'message': 'This API is designed to manage patient records efficiently.'}


@app.get("/view")
def view():
    data = load_data()
    return data


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='The ID of the patient to retrieve', example='P001')):
    # load data from JSON file
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='Sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400, detail=f'Invalid field selected from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400, detail='Order must be either asc or desc')

    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_data


@app.post('/create')
def create_patient(patient: Patient): #patient is a variable of type Patient (Pydantic model)
    # load data from JSON file
    data = load_data()

    # check if patient ID already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient ID already exists')

    # if doesn't exist, add the new patient to the database(JSON file)
    data[patient.id] = patient.model_dump(exclude={'id'})

    # save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'Patient created successfully', 'patient_id': patient.id})
