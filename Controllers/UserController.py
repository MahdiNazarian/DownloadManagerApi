from typing import Annotated

import ClientModels.UserModels
from Controllers.BaseController import BaseController
from BussinessLogic.UserBll import UserBll
from fastapi import Depends, APIRouter

from Models.DbUser import DbUser


class UserController(BaseController):
    def __init__(self):
        self.bll = UserBll()
        self.router: APIRouter = APIRouter(
            prefix="/user",
            tags=["user"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbUser()
        self.insert_model = ClientModels.UserModels.UserInsertAndUpdateModel
        self.update_model = ClientModels.UserModels.UserInsertAndUpdateModel
        self.delete_model = ClientModels.UserModels.UserInsertAndUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
