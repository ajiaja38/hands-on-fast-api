from fastapi import APIRouter, HTTPException
from service.user_service import UserService
from schema.response_entity import ResponseEntity
from model.User import User, CreateUser

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/", response_model=ResponseEntity[User], status_code=201)
def create_user(user: CreateUser) -> ResponseEntity[User]:
    try:
      new_user = UserService.add_user(user)
      print(new_user)
      return ResponseEntity(code=201, status="Created", message="User created successfully", data=new_user)
    except ValueError as e:
      raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=ResponseEntity[list[User]])
def get_all_users() -> ResponseEntity[list[User]]:
    try:
      users = UserService.get_all_users()
      return ResponseEntity(code=200, status="OK", message="Users retrieved successfully", data=users)
    except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))

@router.get("/{id}", response_model=ResponseEntity[User])
def get_user_by_id(id: int) -> ResponseEntity[User]:
    try:
      user = UserService.get_user_by_id(id)
      return ResponseEntity(code=200, status="OK", message="User retrieved successfully", data=user)
    except ValueError as e:
      raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))
