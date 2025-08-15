from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Requester(BaseModel):
    name: str
    email: str


class SummaryComment(BaseModel):
    body: str
    public: bool


class Author(BaseModel):
    role: str
    name: str
    email: Optional[str] = None


class Attachment(BaseModel):
    file_name: str


class DetailedComment(BaseModel):
    author: Author
    public: bool
    body: str
    created_at: datetime
    attachments: list[Attachment]


class Ticket(BaseModel):
    subject: str
    requester: Requester
    created_at: datetime
    comment: SummaryComment
    comments: list[DetailedComment]


class TicketData(BaseModel):
    tickets: list[Ticket]
