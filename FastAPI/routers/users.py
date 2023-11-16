from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests

#uvicorn users:app --reload

router = APIRouter()

@router.get("/usersjson")
async def usersjson():
    return [{'id':3,'name':'Alejandra','surname':'Garcia',"url":"https://github.com/alejandra-garcias","age":23},
            {'id':4,'name':'Linkedin','surname':'Alejandra',"url":"https://www.linkedin.com/in/alejandra-garcia-sanchez-2513a212a/","age":23}]

# Para no tener que rellenar uno por uno vamos a crear la entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url : str
    age: int

user_list = [User(id=1,name="Alejandra",surname='Garcia',url="https://github.com/alejandra-garcias",age=23),
         User(id=2,name="Linkedin",surname='Garcia',url="https://github.com/alejandra-garcias",age=23)]

@router.get("/users")
async def users():
    return user_list

#Por path:http://127.0.0.1:8000/user/1
@router.get("/user/{id}")
async def user(id:int):
    return search_user(id)
    

#Por query = http://127.0.0.1:8000/userquery?id=1, si quiero seugir concatenando seria un &, el signo de interrogacion solo en la primera query

@router.get("/user") #funcionaria tambien quitando el query, lo dejo por fines educativos
async def user(id:int):
    return search_user(id)

def search_user(id:int):
    user = filter(lambda user: user.id == id, user_list)
    try:
        return list(user)[0]
    except:
        return {'error':'Usuario no encontrado'}
    


@router.post("/user/",response_model=User,status_code=201) ## el codigo de success
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail='El usuario ya existe') ##codigo de error
    else:
        user_list.append(user)
        return user
    

@router.put("/user/")    
async def user(user:User):
    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index]=user
            return user


@router.delete("/user/{id}")
async def user(id:int):
    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            return "El usuario ha sido eliminado"


