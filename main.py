from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Phone(BaseModel):
    TypeID: int
    CountryCode: int
    Operator: int
    Number: int

class Contact(BaseModel):
    ID: int
    Username: str
    GivenName: str
    FamilyName: str
    Phone: List[Phone]
    Email: List[str]
    Birthdate: str


class Group(BaseModel):
    ID: int
    Title: str
    Description: str
    Contacts: List[int]


@app.post("/api/v1/contact")
async def create_contact(contact: Contact):
    return contact

@app.get("/api/v1/contact")
async def read_contacts():
    return Contact(
        ID=0,
        Username="",
        GivenName="",
        FamilyName="",
        Phone=[],
        Email=[],
        Birthdate=""
    )

@app.put("/api/v1/contact")
async def update_contact(contact: Contact):
    return contact

@app.delete("/api/v1/contact/{contact_id}")
async def delete_contact(contact_id: int):
    return {"message": f"Контакт с ID {contact_id} удален"}


@app.post("/api/v1/group")
async def create_group(group: Group):
    return group

@app.get("/api/v1/group")
async def read_groups():
    return []

@app.put("/api/v1/group")
async def update_group(group: Group):
    return group

@app.delete("/api/v1/group/{group_id}")
async def delete_group(group_id: int):
    return {"message": f"Группа с ID {group_id} удалена"}

#dockerfile - инструкция по сборке образа, где исходным образом берётся Python 3.12
#Compose.yaml - сборка образа и запуск контейнеров из этих образов
#docker-compose up --build
#docker-compose down
#http://localhost:8080/api/v1/contact