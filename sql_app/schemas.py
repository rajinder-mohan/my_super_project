from typing import List, Optional
from enum import Enum
from pydantic import BaseModel




class MailStaus(str, Enum):
    value_a = "send"
    value_b = "pending"


class SenderBase(BaseModel):
    receiver: str


class SenderCreate(BaseModel):
    receivers_list: List[str]

class Sender(SenderBase):
    id: int
    
    class Config:
        orm_mode = True



class CreateEmail(BaseModel):
    sender: str
    subject: str
    msg: str

class Email(CreateEmail):
    id: int
    status: str
    senders: List[Sender] = []

    class Config:
        orm_mode = True