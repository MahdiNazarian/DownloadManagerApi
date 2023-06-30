import datetime
import hashlib

from BussinessLogic.RoleBll import RoleBll
from BussinessLogic.UserBll import UserBll
from BussinessLogic.UserRoleMappingBll import UserRoleMappingBll
from BussinessLogic.UserSessionsBll import UserSessionsBll
import ClientModels.UserAuthenticateModels
from Models.DbRole import DbRole
from Models.DbUser import DbUser
from Models.DbUserRoleMapping import DbUserRoleMapping
from Models.DbUserSessions import DbUserSessions


class AuthenticateBll:
    def __init__(self):
        self.user_bll = UserBll()
        self.role_bll = RoleBll()
        self.user_role_mapping_bll = UserRoleMappingBll()
        self.user_sessions_bll = UserSessionsBll()

    def user_register(self, register_data: ClientModels.UserAuthenticateModels.UserRegisterModel):
        user_insert_data = DbUser(
            Email=register_data.Email,
            FirstName=register_data.FirstName,
            LastName=register_data.LastName,
            IsEmailConfirmed=True,
            PhoneNumber=register_data.PhonNumber,
            IsPhoneNumberConfirmed=True,
            Password=hashlib.md5(register_data.Password.encode('utf-8')).hexdigest()
        )
        inserted_user: DbUser = self.user_bll.insert_data(user_insert_data)
        register_role: DbRole = self.role_bll.get_role_by_name("Register")
        user_role_mapping_insert_data = DbUserRoleMapping(
            UserId=inserted_user.Id,
            RoleId=register_role.Id
        )
        inserted_user_role_mapping = self.user_role_mapping_bll.insert_data(user_role_mapping_insert_data)
        return {"registered_user": inserted_user, "user_role_mapping": inserted_user_role_mapping}

    def user_login(self, login_data: ClientModels.UserAuthenticateModels.UserLoginModel):
        user_data: DbUser = self.user_bll.get_user_by_email_phone_number(login_data.EmailOrPhoneNumber)
        if user_data is not None:
            if user_data.Password == (hashlib.md5(login_data.Password.encode('utf-8')).hexdigest()):
                user_insert_session = DbUserSessions(
                    UserId=user_data.Id,
                    Token=hashlib.md5("{0}{1}{2}{3}{4}".format(
                        user_data.Email,
                        user_data.PhoneNumber,
                        user_data.FirstName,
                        user_data.LastName,
                        user_data.Password).encode('utf-8')).hexdigest(),
                    ExpireDate=datetime.datetime.now() + datetime.timedelta(days=10) if login_data.remember_me else datetime.datetime.now() + datetime.timedelta(hours=24)
                )
                inserted_session = self.user_sessions_bll.insert_data(user_insert_session)
                return inserted_session
            else:
                return None
        else:
            return None
