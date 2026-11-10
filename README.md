# FastAPI Learning: Patient Records API

## Problem statement

Learning FastAPI and Pydantic means going beyond "hello world" to a real data API: validating input, computing derived values, updating records safely and returning proper errors.

## Solution

A patient records REST API built with FastAPI. Patients are stored in a JSON file, and Pydantic models validate every request, calculate each patient's BMI and verdict automatically, and control what the API returns. A separate folder holds focused examples of the Pydantic features used.

## Tech stack

Python, FastAPI, Pydantic, Uvicorn.

## Features

- **CRUD endpoints** to list, view, create, update and delete patients
- **Sorting** by height, weight or BMI, in ascending or descending order
- **Validated input** with typed fields, path and query parameter descriptions
- **Computed fields**: BMI and health verdict derived from height and weight
- **Partial updates** through a separate update model where every field is optional
- **Proper errors** with 404 responses for missing patients
- **Pydantic examples**: field validators, model validators, computed fields, nested models and exporting models

## Future steps

- Replace the JSON file with a database
- Authentication
- Pagination and filtering
- Automated tests

## Getting started

```bash
pip install fastapi uvicorn pydantic
uvicorn main:app --reload
```

Open http://localhost:8000/docs for the interactive API documentation.
