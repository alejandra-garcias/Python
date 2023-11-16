from fastapi import APIRouter,HTTPException,Depends,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from  passlib.context import CryptContext
from datetime import datetime,timedelta

ALGORITHM = 'HS256'
ACCESS_TOKEN_DURATION = 1
SECRET = "hjbfybrhb23434984895843958njfdgjng72y4"
  
router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl='login')
crypt = CryptContext(schemes=["bcrypt"])

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

@router.post('/login')
async def login(form:OAuth2PasswordRequestForm = Depends()):
    user_db= users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="usuario no es correcto")
    user = search_user_db(form.username)

    acces_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)

    expire = datetime.utcnow() + acces_token_expiration
    access_token = {"sub":user.username,'exp':expire}
    
    return {"acces_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM) ,"token_type":"bearer"}

def search_user(username:str):
    if username in users_db:
        return UserDb(**users_db[username])
    
def search_user_db(username:str):
    if username in users_db:
        return User(**users_db[username])
    


async def auth_user(token: str = Depends(oauth2)):
    excepcion = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticacion invalidas",headers={"www.authenticate":"Bearer"})
    try:
        username = jwt.decode(token,SECRET,algorithms=[ALGORITHM]).get('sub')
        if username is None:
            raise excepcion
    except JWTError:
        raise excepcion
    
    return search_user(username)




    
async def curren_user(user: User = Depends(auth_user)):

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="USUARIO INACTIVO",
            headers={"www.authenticate":"Bearer"})

    return user