from fastapi import APIRouter,HTTPException,Depends,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router=APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl='login')

class User(BaseModel):
    username:str
    full_name:str
    email:str
    disabled:bool

#usuario de base de datos que extiende de usuario
class UserDb(User):
    password:str

users_db={
    "mouredev": {
        "username":"mouredev",
        "full_name":"Brais Moure",
        "email":"braismoure@mouredev.com",
        "disabled":False,
        "password":"123456"
    },
     "mouredev2": {
        "username":"mouredev2",
        "full_name":"Brais Moure2",
        "email":"braismoure@mouredev2.com",
        "disabled":True,
        "password":"456123"
    }
    
}

def search_user(username:str):
    if username in users_db:
        return UserDb(**users_db[username])
    
def search_user_db(username:str):
    if username in users_db:
        return User(**users_db[username])
    

async def curren_user(token: str = Depends(oauth2)):
    user =  search_user_db(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticacion invalidas",headers={"www.authenticate":"Bearer"})
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="USUARIO INACTIVO",
            headers={"www.authenticate":"Bearer"})

    return user

    
@router.post('/login')
async def login(form:OAuth2PasswordRequestForm = Depends()):
    user_db= users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="usuario no es correcto")
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="la contraseña no es correcta")
    return {"acces_token": user.username ,"token_type":"bearer"}


@router.get("/users/me")
async def me(user: User = Depends(curren_user)):
    return user
    

