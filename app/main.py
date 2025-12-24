from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from data_interactor import DataInteractor

app = FastAPI()
data_interactor = DataInteractor()

class Contact(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number
        }

@app.get("/contacts")
def get_contacts():
    return data_interactor.get_all_contacts()

@app.post("/contacts")
def create_contact(contact: Contact):
    contact_id = data_interactor.create_contact(contact.first_name, contact.last_name, contact.phone_number)
    return {"message": "Contact created successfully", "id": contact_id}

@app.put("/contacts/{id}")
def update_contact(id: int, contact: Contact):
    success = data_interactor.update_contact(id, contact.to_dict())
    if not success:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact updated successfully"}

@app.put("/contacts/{id}/field")
def update_contact_field(id: int, field_name: str, new_value: str):
    try:
        success = data_interactor.update_contact_person_by_field_selection(id, field_name, new_value)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
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

