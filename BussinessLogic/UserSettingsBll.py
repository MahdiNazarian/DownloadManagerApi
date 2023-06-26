from BussinessLogic.BaseBll import BaseBll
from Repositories.UserSettingsRepository import UserSettingsRepository


class UserSettingsBll(BaseBll):
    def __init__(self):
        self.repository = UserSettingsRepository()
        super().__init__(repository=self.repository)

