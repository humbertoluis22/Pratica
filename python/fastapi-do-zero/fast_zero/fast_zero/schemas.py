from pydantic import BaseModel,EmailStr,ConfigDict

class Message(BaseModel):
    message:str
    model_config = ConfigDict(from_attributes=True)


class UserSchema(BaseModel):
    user:str    
    email: EmailStr
    password: str

class UserDB(UserSchema):
    id : int

class UserPublic(BaseModel):
    id: int
    username:str    
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)

class UserList(BaseModel):
    users : list[UserPublic]

class Token(BaseModel):
    access_token:str
    token_type:str