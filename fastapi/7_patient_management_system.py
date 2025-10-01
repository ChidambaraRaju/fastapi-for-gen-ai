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

import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
        
    return data

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