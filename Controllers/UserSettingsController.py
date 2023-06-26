import ClientModels.UserSettingsModels
from Controllers.BaseController import BaseController
from BussinessLogic.UserSettingsBll import UserSettingsBll
from fastapi import Depends, APIRouter

from Models.DbUserSettings import DbUserSettings


class UserSettingsController(BaseController):
    def __init__(self):
        self.bll = UserSettingsBll()
        self.router: APIRouter = APIRouter(
            prefix="/user_settings",
            tags=["user_settings"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbUserSettings()
        self.insert_model = ClientModels.UserSettingsModels.UserSettingsInsertModel
        self.update_model = ClientModels.UserSettingsModels.UserSettingsUpdateModel
        self.delete_model = ClientModels.UserSettingsModels.UserSettingsUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
