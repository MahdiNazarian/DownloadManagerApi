import ClientModels.RoleSystemPartNameMappingModels
from Controllers.BaseController import BaseController
from BussinessLogic.RoleSystemPartNameMappingBll import RoleSystemPartNameMappingBll
from fastapi import Depends, APIRouter

from Models.DbRoleSystemPartNameMapping import DbRoleSystemPartNameMapping
from Utils.StaticValues import API_PATH


class RoleSystemPartNameMappingController(BaseController):
    def __init__(self):
        self.bll = RoleSystemPartNameMappingBll()
        self.router: APIRouter = APIRouter(
            prefix=API_PATH+"/role_system_part_name_mapping",
            tags=["role_system_part_name_mapping"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbRoleSystemPartNameMapping()
        self.insert_model = ClientModels.RoleSystemPartNameMappingModels.SystemPartNameMappingInsertModel
        self.update_model = ClientModels.RoleSystemPartNameMappingModels.SystemPartNameMappingUpdateModel
        self.delete_model = ClientModels.RoleSystemPartNameMappingModels.SystemPartNameMappingUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
