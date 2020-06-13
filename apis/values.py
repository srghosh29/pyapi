from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"value1": "Foo"}, {"value2": "Bar"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "current user"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}