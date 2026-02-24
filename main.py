from fastapi import FastAPI, Path, Query, HTTPException
import json

app = FastAPI()


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


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

# uvicorn main:app --reload