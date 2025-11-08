from enums import JobStatus  # your custom enum
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from schemas import SocialModal, BlogModel
from bson import ObjectId


class ContentJobOut(BaseModel):
    id: str = Field(..., alias="_id")
    @validator("id", pre=True)
    def objectid_to_str(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v
    status: JobStatus
    context: Optional[str] = None
    error: Optional[str] = None
    user_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        allow_population_by_field_name = True


class ContentWithJobs(BaseModel):
    id: str
    userId: str
    link: str
    title: str = None
    created_at: datetime
    updated_at: datetime
    blogs: Optional[List[BlogModel]] = None
    raw_text: Optional[str] = None
    tags: Optional[List[str]] = None
    is_active: bool = True
    socials: Optional[List[SocialModal]] = None
    jobs: List[ContentJobOut] = []

    class Config:
        allow_population_by_field_name = True

class PaginatedContentWithJobs(BaseModel):
    total: int
    items: List[ContentWithJobs]