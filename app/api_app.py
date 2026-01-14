from fastapi import FastAPI,HTTPException,Depends
from sqlmodel import Session
from app.db import create_db_and_tables,get_session,Notes

app=FastAPI()


# initialize the db
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
# path parameter for listing the note title
@app.post("/notes/")
def create_note(
    note: Notes,
    session: Session = Depends(get_session)
):
    session.add(note)
    session.commit()
    session.refresh(note)
    return note

#root dir
@app.get("/")
def root():
    return {"working":"yes"}
# health endpoint
@app.get("/health",status_code=200)
def health_check():
    return {"status":"running"}