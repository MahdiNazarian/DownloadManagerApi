import ClientModels.SubscriptionTypesModels
from Controllers.BaseController import BaseController
from BussinessLogic.SubscriptionTypesBll import SubscriptionTypesBll
from fastapi import Depends, APIRouter

from Models.DbSubscriptionTypes import DbSubscriptionTypes
from Utils.StaticValues import API_PATH


class SubscriptionTypesController(BaseController):
    def __init__(self):
        self.bll = SubscriptionTypesBll()
        self.router: APIRouter = APIRouter(
            prefix=API_PATH+"/subscription_types",
            tags=["subscription_types"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbSubscriptionTypes()
        self.insert_model = ClientModels.SubscriptionTypesModels.SubscriptionTypesInsertModel
        self.update_model = ClientModels.SubscriptionTypesModels.SubscriptionTypesUpdateModel
        self.delete_model = ClientModels.SubscriptionTypesModels.SubscriptionTypesUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)