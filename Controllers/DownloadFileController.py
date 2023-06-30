import ClientModels.DownloadFileModels
from Controllers.BaseController import BaseController
from BussinessLogic.DownloadFileBll import DownloadFileBll
from fastapi import Depends, APIRouter

from Models.DbDownloadFile import DbDownloadFile
from Utils.StaticValues import API_PATH


class DownloadFileController(BaseController):
    def __init__(self):
        self.bll = DownloadFileBll()
        self.router: APIRouter = APIRouter(
            prefix=API_PATH+"/download_file",
            tags=["download_file"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbDownloadFile()
        self.insert_model = ClientModels.DownloadFileModels.DownloadFileInsertModel
        self.update_model = ClientModels.DownloadFileModels.DownloadFileUpdateModel
        self.delete_model = ClientModels.DownloadFileModels.DownloadFileUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
