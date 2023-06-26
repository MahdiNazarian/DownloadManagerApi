from BussinessLogic.BaseBll import BaseBll
from Repositories.TimingRepository import TimingRepository


class TimingBll(BaseBll):
    def __init__(self):
        self.repository = TimingRepository()
        super().__init__(repository=self.repository)

