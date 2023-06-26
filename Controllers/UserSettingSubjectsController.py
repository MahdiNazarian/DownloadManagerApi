import ClientModels.UserSettingSubjectsModels
from Controllers.BaseController import BaseController
from BussinessLogic.UserSettingSubjectsBll import UserSettingSubjectBll
from fastapi import Depends, APIRouter

from Models.DbUserSettingSubjects import DbUserSettingSubjects


class UserSettingSubjectsController(BaseController):
    def __init__(self):
        self.bll = UserSettingSubjectBll()
        self.router: APIRouter = APIRouter(
            prefix="/user_setting_subjects",
            tags=["user_setting_subjects"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbUserSettingSubjects()
        self.insert_model = ClientModels.UserSettingSubjectsModels.UserSettingSubjectsInsertModel
        self.update_model = ClientModels.UserSettingSubjectsModels.UserSettingSubjectsUpdateModel
        self.delete_model = ClientModels.UserSettingSubjectsModels.UserSettingSubjectsUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
