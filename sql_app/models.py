from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base




class Emails(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)
    subject = Column(String)
    msg = Column(String)
    status = Column(String, default="pending")
    senders = relationship("Sender", back_populates="emails")

class Sender(Base):
    __tablename__ = "sender"

    id = Column(Integer, primary_key=True, index=True)
    receiver = Column(String, nullable=True)
    email_id = Column(Integer, ForeignKey("emails.id"))

    emails = relationship("Emails", back_populates="senders")