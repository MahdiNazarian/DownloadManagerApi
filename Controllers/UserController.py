from Controllers.BaseController import BaseController
from BussinessLogic.UserBll import UserBll
from fastapi import Depends, APIRouter


class UserController(BaseController):
    def __init__(self):
        self.bll = Depends(UserBll)
        self.router = APIRouter(
            prefix="/user",
            tags=["user"],
            responses={404: {"description": "Not found"}},
        )
        super().__init__(self.bll, self.router)
