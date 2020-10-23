from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/mail/", response_model=schemas.Email)
def create_mail(email: schemas.CreateEmail, db: Session = Depends(get_db)):
    db_email= crud.get_mail_by_subject(db, subject=email.subject)
    if db_email:
        raise HTTPException(status_code=400, detail="Subject already registered")
    return crud.create_email(db=db, email=email)



@app.get("/mails/", response_model=List[schemas.Email])
def get_mails(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    mails = crud.get_mails(db, skip=skip, limit=limit)
    return mails


@app.post("/mail/{mail_id}/receivers/")
def add_receivers_for_mail(
    mail_id: int, sender: schemas.SenderCreate, db: Session = Depends(get_db)
):
    mail_Senders = crud.create_email_receiver(db=db, receiver=sender, email_id=mail_id)

    return {"message": "receivers added successfully"}



@app.get("/mail/{mail_id}/receivers/", response_model=List[schemas.Sender])
def get_receivers_for_mail(
    mail_id: int, skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)
):

    return crud.get_mail_receivers(db, skip=skip, limit=limit, mail_id=mail_id)


@app.get("/mail/receivers/", response_model=List[schemas.Sender])
def get_receivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    receivers_data = crud.get_receivers(db, skip=skip, limit=limit)
   
    return receivers_data


@app.get("/mail/receivers/status", response_model=List[schemas.Email])
def get_mails_by_status(
    status: schemas.MailStaus, skip: int = 0, limit: int = 100,  db: Session = Depends(get_db)
):

    return crud.get_mail_by_status(db, skip=skip, limit=limit, status=status)