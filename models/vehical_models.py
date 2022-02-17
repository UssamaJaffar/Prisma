from pydantic import BaseModel
from typing import Optional

class CarBrand(BaseModel):
    name: str
    logo: Optional[str] = None
    description: Optional[str] = None

class CarModel(BaseModel):
    name: str
    description: str
