from pydantic import BaseModel, Field
from typing import Optional,List
from enum import Enum
from datetime import datetime


# To get dynamic values, use the Field parameter

class Language(str, Enum):
    PY = "python"
    JAVA = "java"
    GO = "go"

class Comment(BaseModel):
    text : Optional[str] = None

class Blog(BaseModel):
    title: str = Field(min_length=10)
    description: Optional[str] = None
    is_active: bool
    language: Language = Language.JAVA
    created_at: datetime = Field(default_factory=datetime.now)
    comments : Optional[List[Comment]]


first_blog= Blog(title= "My title", is_active= True)
print(first_blog)

import time
time.sleep(5)

second_blog= Blog(title= "My title", is_active= True)
print(second_blog)

# You can easily get the json of it by doing first_blog.json()
