from BussinessLogic.BaseBll import BaseBll
from Repositories.SystemPartNameRepository import SystemPartNameRepository


class SystemPartNameBll(BaseBll):
    def __init__(self):
        self.repository = SystemPartNameRepository()
        super().__init__(repository=self.repository)

