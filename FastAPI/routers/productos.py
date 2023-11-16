from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404:{"message":"No encontrado"}})

products_list =["producto 1","producto 2","producto 3","producto 4","producto 5",]

@router.get("/")
async def product():
    return products_list

@router.get("/{id}")
async def product(id:int):
    return products_list