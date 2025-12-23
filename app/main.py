from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from data_interactor import DataInteractor

app = FastAPI()
data_interactor = DataInteractor()

class Contact(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

@app.get("/contacts")
def get_contacts():
    return data_interactor.get_all_contacts()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

