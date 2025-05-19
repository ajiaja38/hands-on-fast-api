from pydantic import BaseModel
from uuid import UUID, uuid4

class User(BaseModel):
  id: UUID
  name: str
  age: int
  address: str
  phoneNumber: str
  
class CreateUser(BaseModel):
  name: str
  age: int
  address: str
  phoneNumber: str