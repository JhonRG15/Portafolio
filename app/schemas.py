from pydantic import BaseModel, HttpUrl
from typing import List, Optional

'''class MetadataResponse(BaseModel):
    id: Optional[str]
    title: Optional[str]
    duration: Optional[int]
    thumbnail: Optional[HttpUrl]
    channel: Optional[str]
    uploader: Optional[str]
    upload_date: Optional[str]
    view_count: Optional[int]
    like_count: Optional[int]
    entries: Optional[List]'''

class YTVideo(BaseModel):
    url: HttpUrl
