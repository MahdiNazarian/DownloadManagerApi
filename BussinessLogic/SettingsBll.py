from BussinessLogic.BaseBll import BaseBll
from Repositories.SettingsRepository import SettingsRepository


class SettingsBll(BaseBll):
    def __init__(self):
        self.repository = SettingsRepository()
        super().__init__(repository=self.repository)

