from model.User import User, CreateUser
from uuid import uuid4

users_db: list[User] = []

class UserService:
  @staticmethod
  def add_user(user: CreateUser) -> User:
    new_User: User = User(id=uuid4(), name=user.name, age=user.age, address=user.address, phoneNumber=user.phoneNumber)

    if not new_User:
      raise ValueError("User not created")
    
    users_db.append(new_User)
    return new_User
  
  @staticmethod
  def get_all_users() -> list[User]:
    return users_db
  
  @staticmethod
  def get_user_by_id(id: int) -> User:
    user = next((user for user in users_db if user.id == id), None)
    
    if not user:
      raise ValueError("User not found")
    
    return user