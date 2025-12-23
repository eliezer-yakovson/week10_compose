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

@app.post("/contacts")
def create_contact(contact: Contact):
    contact_id = data_interactor.create_contact(contact.first_name, contact.last_name, contact.phone_number)
    return {"message": "Contact created successfully", "id": contact_id}

@app.put("/contacts/{id}")
def update_contact(id: int, contact: Contact):
    success = data_interactor.update_contact(id, contact.first_name, contact.last_name, contact.phone_number)
    if not success:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact updated successfully"}

@app.delete("/contacts/{id}")
def delete_contact(id: int):
    success = data_interactor.delete_contact(id)
    if not success:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

