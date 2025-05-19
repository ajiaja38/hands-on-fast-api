from typing import Generic, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class ResponseMessage(BaseModel):
  code: int
  status: str
  message: str

class ResponseEntity(ResponseMessage, Generic[T]):
  data: Optional[T] = None