from BussinessLogic.BaseBll import BaseBll
from Repositories.UserSubscriptionRepository import UserSubscriptionRepository


class UserSubscriptionBll(BaseBll):
    def __init__(self):
        self.repository = UserSubscriptionRepository()
        super().__init__(repository=self.repository)

