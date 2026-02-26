from fastapi import FastAPI, Path, Query, HTTPException
from fastapi.responses import JSONResponse
from schemas import Patient, PatientUpdate
import json

app = FastAPI()
    

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)

@app.get("/")
def hello():
    return {"message": "Hello, World!"}


@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}


@app.get("/view")
def view():
    data = load_data()
    return {"data": data}


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get('/sort')
def sort_patients(
        sort_by: str = Query(..., description="Sort on the basis of height, weight, BMI"),
        order_by: str = Query(default="ascending", description="Order of sorting: ascending or descending")
    ):
    data = load_data()
    
    valid_sort = ["height", "weight", "BMI"]
    valid_order = ["ascending", "descending"]

    if sort_by not in valid_sort:
        raise HTTPException(status_code=400, detail=f"Invalid sort_by value. Must be one of {valid_sort}")
    if order_by not in valid_order:
        raise HTTPException(status_code=400, detail=f"Invalid order_by value. Must be one of {valid_order}")
    sort_des = True if order_by == "descending" else False
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=sort_des)
    return {"sorted_data": sorted_data}


@app.post('/create')
def create_patient(patient: Patient):
    # Load existing data
    data = load_data()

    # check exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")

    # add new patient
    data[patient.id] = patient.model_dump(exclude={"id"})
    save_data(data)

    # return success message    
    return JSONResponse(status_code=201, content={"message": "Patient created successfully", "patient_id": patient.id})


@app.put('/update/{patient_id}')
def update_patient(patient_id: str, updated_patient: PatientUpdate):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Update patient data
    patient_data = data[patient_id]
    for field, value in updated_patient.model_dump(exclude_unset=True).items():
        # exclude_unset=True -> ensures that only provided fields are updated
        if field in patient_data:
            patient_data[field] = value

    # Save updated data
    data[patient_id] = patient_data
    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Patient updated successfully", "patient_id": patient_id})


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Delete patient
    del data[patient_id] # Remove the patient from the data dictionary
    save_data(data)

    return JSONResponse(status_code=204, content={}) # No content

# uvicorn main:app --reload