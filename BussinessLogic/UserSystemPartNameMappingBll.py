from BussinessLogic.BaseBll import BaseBll
from Repositories.UserSystemPartNameMappingRepository import UserSystemPartNameMappingRepository


class UserSystemPartNameMappingBll(BaseBll):
    def __init__(self):
        self.repository = UserSystemPartNameMappingRepository()
        super().__init__(repository=self.repository)

