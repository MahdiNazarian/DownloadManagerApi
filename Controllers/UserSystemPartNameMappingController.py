import ClientModels.UserSystemPartNameMappingModels
from Controllers.BaseController import BaseController
from BussinessLogic.UserSystemPartNameMappingBll import UserSystemPartNameMappingBll
from fastapi import Depends, APIRouter

from Models.DbUserSystemPartNameMapping import DbUserSystemPartNameMapping


class UserSystemPartNameMappingController(BaseController):
    def __init__(self):
        self.bll = UserSystemPartNameMappingBll()
        self.router: APIRouter = APIRouter(
            prefix="/user_system_part_name_mapping",
            tags=["user_system_part_name_mapping"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbUserSystemPartNameMapping()
        self.insert_model = ClientModels.UserSystemPartNameMappingModels.UserSystemPartNameMappingInsertModel
        self.update_model = ClientModels.UserSystemPartNameMappingModels.UserSystemPartNameMappingUpdateModel
        self.delete_model = ClientModels.UserSystemPartNameMappingModels.UserSystemPartNameMappingUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
