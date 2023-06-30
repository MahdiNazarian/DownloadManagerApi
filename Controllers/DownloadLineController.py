import ClientModels.DownloadLineModels
from Controllers.BaseController import BaseController
from BussinessLogic.DownloadLineBll import DownloadLineBll
from fastapi import Depends, APIRouter

from Models.DbDownloadLine import DbDownloadLine
from Utils.StaticValues import API_PATH


class DownloadLineController(BaseController):
    def __init__(self):
        self.bll = DownloadLineBll()
        self.router: APIRouter = APIRouter(
            prefix=API_PATH+"/download_line",
            tags=["download_line"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbDownloadLine()
        self.insert_model = ClientModels.DownloadLineModels.DownloadLineInsertModel
        self.update_model = ClientModels.DownloadLineModels.DownloadLineUpdateModel
        self.delete_model = ClientModels.DownloadLineModels.DownloadLineUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
