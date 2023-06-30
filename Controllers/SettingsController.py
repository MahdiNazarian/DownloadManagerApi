import ClientModels.SettingsModels
from Controllers.BaseController import BaseController
from BussinessLogic.SettingsBll import SettingsBll
from fastapi import Depends, APIRouter

from Models.DbSettings import DbSettings
from Utils.StaticValues import API_PATH


class SettingsController(BaseController):
    def __init__(self):
        self.bll = SettingsBll()
        self.router: APIRouter = APIRouter(
            prefix=API_PATH+"/settings",
            tags=["settings"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbSettings()
        self.insert_model = ClientModels.SettingsModels.SettingsInsertModel
        self.update_model = ClientModels.SettingsModels.SettingsUpdateModel
        self.delete_model = ClientModels.SettingsModels.SettingsUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
