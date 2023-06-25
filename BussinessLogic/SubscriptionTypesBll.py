from typing import Annotated

from fastapi import Depends

from BussinessLogic.BaseBll import BaseBll
from Repositories.SubscriptionTypesRepository import SubscriptionTypesRepository


class SubscriptionTypesBll(BaseBll):
    def __init__(self):
        self.repository = SubscriptionTypesRepository()
        super().__init__(repository=self.repository)

