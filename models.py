from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class TicketCategory(Enum):
    AUTHENTICATION = "Authentication issues"
    PAYMENT = "Payment issues"
    PROMOTIONS = "Promotional issues"
    RETURNS = "Returns and exchanges"
    PRODUCT_QUALITY = "Product quality and incorrect shipments"
    SHIPPING_TRACKING = "Shipping and tracking issues"
    ORDER_MODIFICATION = "Order modifications and cancellations"
    OTHER = "Other"


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
