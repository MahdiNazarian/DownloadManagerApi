import ClientModels.RoleModels
from Controllers.BaseController import BaseController
from BussinessLogic.RoleBll import RoleBll
from fastapi import Depends, APIRouter

from Models.DbRole import DbRole


class RoleController(BaseController):
    def __init__(self):
        self.bll = RoleBll()
        self.router: APIRouter = APIRouter(
            prefix="/role",
            tags=["role"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbRole()
        self.insert_model = ClientModels.RoleModels.RoleInsertModel
        self.update_model = ClientModels.RoleModels.RoleUpdateModel
        self.delete_model = ClientModels.RoleModels.RoleUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
