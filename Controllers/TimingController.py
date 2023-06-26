import ClientModels.TimingModels
from Controllers.BaseController import BaseController
from BussinessLogic.TimingBll import TimingBll
from fastapi import Depends, APIRouter

from Models.DbTiming import DbTiming


class TimingController(BaseController):
    def __init__(self):
        self.bll = TimingBll()
        self.router: APIRouter = APIRouter(
            prefix="/timing",
            tags=["timing"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbTiming()
        self.insert_model = ClientModels.TimingModels.TimingInsertModel
        self.update_model = ClientModels.TimingModels.TimingUpdateModel
        self.delete_model = ClientModels.TimingModels.TimingUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
