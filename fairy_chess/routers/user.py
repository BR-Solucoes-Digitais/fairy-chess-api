from fastapi import APIRouter, Depends, HTTPException

from fairy_chess.config import get_token_header, HTTPExceptionResponses

router = APIRouter(
    prefix="/users",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses=HTTPExceptionResponses.NOT_FOUND,
)

@router.post("/", responses=HTTPExceptionResponses.FORBIDEN)
async def post_user():
    return {[{"username": "Rick"}, {"username": "Morty"}]}

@router.get("/", responses=HTTPExceptionResponses.FORBIDEN)
async def get_user():
    return [{"username": "Rick"}, {"username": "Morty"}]