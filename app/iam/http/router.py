from fastapi import APIRouter

router = APIRouter()

@router.post("/", status_code=201)
async def handle_register():
    return "register"

@router.get("/", status_code=200)
async def handle_sign_in():
    return "sign in"

@router.delete("/", status_code=201)
async def handle_sign_out():
    return "sign out"