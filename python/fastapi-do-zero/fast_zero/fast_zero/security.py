from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()

def get_password_hash(password:str):
    return pwd_context.hash(password) # gera um hash de uma senha 

def verify_password(plain_password : str, hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)