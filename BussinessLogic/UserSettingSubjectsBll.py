from BussinessLogic.BaseBll import BaseBll
from Repositories.UserSettingSubjectsRepository import UserSettingSubjectRepository


class UserSettingSubjectBll(BaseBll):
    def __init__(self):
        self.repository = UserSettingSubjectRepository()
        super().__init__(repository=self.repository)

