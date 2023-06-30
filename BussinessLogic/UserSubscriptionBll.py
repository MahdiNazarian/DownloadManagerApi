from BussinessLogic.BaseBll import BaseBll
from Repositories.UserSubscriptionRepository import UserSubscriptionRepository


class UserSubscriptionBll(BaseBll):
    def __init__(self):
        self.repository = UserSubscriptionRepository()
        super().__init__(repository=self.repository)

    def get_user_active_subs_by_user_id(self, user_id: int):
        return self.repository.get_user_active_subs_by_user_id(user_id)
