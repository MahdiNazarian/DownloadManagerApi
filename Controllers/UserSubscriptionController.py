import ClientModels.UserSubscriptionModels
from Controllers.BaseController import BaseController
from BussinessLogic.UserSubscriptionBll import UserSubscriptionBll
from fastapi import Depends, APIRouter

from Models.DbUserSubscription import DbUserSubscriptions


class UserSubscriptionController(BaseController):
    def __init__(self):
        self.bll = UserSubscriptionBll()
        self.router: APIRouter = APIRouter(
            prefix="/user_subscription",
            tags=["user_subscription"],
            responses={404: {"description": "Not found"}},
        )
        self.db_model_instance = DbUserSubscriptions()
        self.insert_model = ClientModels.UserSubscriptionModels.UserSubscriptionInsertModel
        self.update_model = ClientModels.UserSubscriptionModels.UserSubscriptionUpdateModel
        self.delete_model = ClientModels.UserSubscriptionModels.UserSubscriptionUpdateModel
        super().__init__(self.bll, self.router, self.db_model_instance, self.insert_model, self.update_model, self.delete_model)
