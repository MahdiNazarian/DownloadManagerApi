from BussinessLogic.BaseBll import BaseBll
from Repositories.UserDownloadMappingRepository import UserDownloadMappingRepository


class UserDownloadMappingBll(BaseBll):
    def __init__(self):
        self.repository = UserDownloadMappingRepository()
        super().__init__(repository=self.repository)

