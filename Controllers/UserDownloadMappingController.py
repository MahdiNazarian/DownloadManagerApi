import ClientModels.UserDownloadMappingModels
from Controllers.BaseController import BaseController
from BussinessLogic.UserDownloadMappingBll import UserDownloadMappingBll
from fastapi import Depends, APIRouter

from Models.DbUserDownloadMapping import DbUserDownloadMapping
from Utils.StaticValues import API_PATH


class UserDownloadMappingController(BaseController):
    def __init__(self):
        self.bll = UserDownloadMappingBll()
        self.router: APIRouter = APIRouter(
            prefix=API_PATH+"/user_download_mapping",
            tags=["user_download_mapping"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbUserDownloadMapping()
        self.insert_model = ClientModels.UserDownloadMappingModels.UserDownloadMappingInsertModel
        self.update_model = ClientModels.UserDownloadMappingModels.UserDownloadMappingUpdateModel
        self.delete_model = ClientModels.UserDownloadMappingModels.UserDownloadMappingUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
