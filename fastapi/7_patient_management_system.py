from fastapi import FastAPI, Path, HTTPException, Query
'''
Path() can be used to provide metadata, validation rules, and documentation hints for path parameters in the API endpoints
Title, Description, Example, ge, gt, le, lt, Min_length, Max_length, regex

HTTPException is a built in exception in FastAPI used to return custom HTTP error responses when something goes wrong in the API
Instead of returning a normal JSON or crashing the server, you can gracefully raise an error with:
    - a proper HTTP status code (like 404, 400, 403)
    - a custom error message
    - (optional) extra headers

Query() is a utility function provided by FastAPI to declare, validate, and document query parameters in your API endpoints.
It allows us to 
    - Set default values
    - Enforce validation rules
    - Add metadata like description, title, examples
'''
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json


app = FastAPI()

class Patient(BaseModel):
    
    id: Annotated[str, Field(..., description= "ID of the patient", examples=["P001"])]
    name: Annotated[str, Field(..., description= "Name of the patient")]
    city: Annotated[str, Field(..., description= "City where the patient is living")]
    age: Annotated[int, Field(..., gt=0, lt=100, description= "Age of the patient")]
    gender: Annotated[Literal["male", "female", "others"], Field(..., description= "gender of the patient")]
    height: Annotated[float, Field(..., gt=0, description= "Height of the patient in mtrs")]
    weight: Annotated[float, Field(..., gt=0, description= "Weight of the patient in KG")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Normal"
        else:
            return "Obese"

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(None, description= "Name of the patient")]
    city: Annotated[Optional[str], Field(None, description= "City where the patient is living")]
    age: Annotated[Optional[int], Field(None, gt=0, lt=100, description= "Age of the patient")]
    gender: Annotated[Optional[Literal["male", "female", "others"]], Field(None, description= "gender of the patient")]
    height: Annotated[Optional[float], Field(None, gt=0, description= "Height of the patient in mtrs")]
    weight: Annotated[Optional[float], Field(None, gt=0, description= "Weight of the patient in KG")]


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
        
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient record"}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="ID of the patient in the DB", example="P001")):
    # load the patient data
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code= 404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="sort on the basis of height, weight or bmi"), order: str = Query("asc", description="sort in asc or desc order")): 
    # ... means that query param is madatory,
    # 'asc' is the default value and order is optional
    valid_fields_sortby = ["height", "weight", "bmi"]
    valid_fields_order = ["asc", "desc"]
    
    if sort_by not in valid_fields_sortby:
        raise HTTPException(status_code=400, detail=f"Invalid sortby, select from {valid_fields_sortby}")
    
    if order not in valid_fields_order:
        raise HTTPException(status_code=400, detail=f"Invalid order, select from {valid_fields_order}")
    
    data = load_data()
    
    is_reverse = True if order == "desc" else False
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse=is_reverse)
    
    return sorted_data

@app.post("/create")
def create_patient(patient: Patient):
    
    # load the data
    data = load_data()
    
    # check if the patient already exist
    if patient.id in data:
        raise HTTPException(status_code= 400, detail= "Patient already exist")
    
    # add new patient
    data[patient.id] = patient.model_dump(exclude= ["id"])
    
    # save the new record
    save_data(data)
    
    return JSONResponse(status_code=201, content={"message": "Patient record created successfully"})

@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient_update: PatientUpdate):
    
    # load the data
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    existing_patient_info = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset=True)
    
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value
    
    # existing_patient_info -> pydantic object -> update bmi + verdict
    existing_patient_info["id"] = patient_id
    pydantic_patient_obj = Patient(**existing_patient_info)
    
    # pydantic object -> dict
    existing_patient_info = pydantic_patient_obj.model_dump(exclude=["id"])
    data[patient_id] = existing_patient_info
    
    # save the data
    save_data(data)
    
    return JSONResponse(status_code= 200, content={"message": "Patient updated"})

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    
    #load the data
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code= 404, detail= "Patient not found")
    
    del data[patient_id]
    
    save_data(data)
    
    return JSONResponse(status_code= 200, content={"message": "Patient deleted"})