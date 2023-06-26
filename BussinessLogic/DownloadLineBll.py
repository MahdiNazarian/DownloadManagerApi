from BussinessLogic.BaseBll import BaseBll
from Repositories.DownloadLineRepository import DownloadLineRepository


class DownloadLineBll(BaseBll):
    def __init__(self):
        self.repository = DownloadLineRepository()
        super().__init__(repository=self.repository)

