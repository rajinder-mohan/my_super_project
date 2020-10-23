from sqlalchemy.orm import Session

from . import models, schemas


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item


def get_mail_by_subject(db: Session, subject: str):
    return db.query(models.Emails).filter(models.Emails.subject == subject).first()

def create_email(db: Session, email: schemas.CreateEmail):
    db_email = models.Emails(sender=email.sender, subject=email.subject, msg=email.msg)
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email


def create_email_receiver(db: Session, receiver: schemas.SenderCreate, email_id: int):
    db_objects = []
    for receiver_obj in receiver.receivers_list:
  
        db_receiver = models.Sender(receiver=receiver_obj, email_id=email_id)
        db_objects.append(db_receiver)
    db.bulk_save_objects(db_objects)
    db.commit()
 
    return db_objects


def get_mails(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Emails).offset(skip).limit(limit).all()

def get_receivers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sender).offset(skip).limit(limit).all()

def get_mail_receivers(db: Session, mail_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Sender).filter(models.Sender.email_id == mail_id).offset(skip).limit(limit).all()


def get_mail_by_status(db: Session, status: schemas.MailStaus, skip: int = 0, limit: int = 100):
    return db.query(models.Emails).filter(models.Emails.status == status).offset(skip).limit(limit).all()