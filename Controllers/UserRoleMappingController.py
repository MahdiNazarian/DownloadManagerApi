import ClientModels.UserRoleMappingModels
from Controllers.BaseController import BaseController
from BussinessLogic.UserRoleMappingBll import UserRoleMappingBll
from fastapi import Depends, APIRouter

from Models.DbUserRoleMapping import DbUserRoleMapping


class UserRoleMappingController(BaseController):
    def __init__(self):
        self.bll = UserRoleMappingBll()
        self.router: APIRouter = APIRouter(
            prefix="/user_role_mapping",
            tags=["user_role_mapping"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbUserRoleMapping()
        self.insert_model = ClientModels.UserRoleMappingModels.UserRoleMappingInsertModel
        self.update_model = ClientModels.UserRoleMappingModels.UserRoleMappingUpdateModel
        self.delete_model = ClientModels.UserRoleMappingModels.UserRoleMappingUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
