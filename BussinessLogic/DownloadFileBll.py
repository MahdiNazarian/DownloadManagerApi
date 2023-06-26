from BussinessLogic.BaseBll import BaseBll
from Repositories.DownloadFileRepository import DownloadFileRepository


class DownloadFileBll(BaseBll):
    def __init__(self):
        self.repository = DownloadFileRepository()
        super().__init__(repository=self.repository)

