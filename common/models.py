from typing import Optional

from pydantic import BaseModel


class Initiative(BaseModel):
    id: int
    category: str
    title: str
    description: str
    latitude: float
    longitude: float
    milestone: str
    price: float
    current_funds: float
    contractor_present: bool
    image_url: str
    author_id: int
    creation_date: str
    reports: int
    document_url: str
    wallet: Optional[str] = None
    funding_url: Optional[str] = None


class EditInitiative(BaseModel):
    category: Optional[str]
    title: Optional[str]
    description: Optional[str]
    milestone: Optional[str]
    price: Optional[float]
    contractor_present: Optional[bool]
    image_url: Optional[str]
    document_url: Optional[str]
    wallet: Optional[str]
    funding_url: Optional[str]


class BlogItem(BaseModel):
    id: int
    title: str
    description: str
    creation_date: str
    image_url: str
    initiative: int


class EditBlogItem(BaseModel):
    title: Optional[str]
    description: Optional[str]
    image_url: Optional[str]


class Payment(BaseModel):
    initiative_id: int
    author_id: Optional[int] = None
    payment: int
