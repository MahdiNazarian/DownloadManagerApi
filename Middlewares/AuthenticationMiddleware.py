from fastapi import Request, Response

from BussinessLogic.RoleBll import RoleBll
from BussinessLogic.RoleSystemPartNameMappingBll import RoleSystemPartNameMappingBll
from BussinessLogic.UserBll import UserBll
from BussinessLogic.UserLoginsBll import UserLoginsBll
from BussinessLogic.UserRoleMappingBll import UserRoleMappingBll
from BussinessLogic.UserSessionsBll import UserSessionsBll
from BussinessLogic.UserSubscriptionBll import UserSubscriptionBll
from BussinessLogic.UserSystemPartNameMappingBll import UserSystemPartNameMappingBll
from ClientModels.ResponseModel import ResponseModel
from Models import DbUserSubscription
from Models.DbRole import DbRole
from Models.DbRoleSystemPartNameMapping import DbRoleSystemPartNameMapping
from Models.DbUser import DbUser
from Models.DbUserLogins import DbUserLogins
from Models.DbUserRoleMapping import DbUserRoleMapping
from Models.DbUserSessions import DbUserSessions


class AuthenticationMiddleware:
    def __init__(self):
        self.user_bll = UserBll()
        self.role_bll = RoleBll()
        self.user_role_mapping_bll = UserRoleMappingBll()
        self.user_sessions_bll = UserSessionsBll()
        self.role_system_part_name_mapping_bll = RoleSystemPartNameMappingBll()
        self.user_system_part_name_mapping_bll = UserSystemPartNameMappingBll()
        self.user_subscription_bll = UserSubscriptionBll()
        self.user_logins_bll = UserLoginsBll()

    async def __call__(self, request: Request, call_next):
        user_name = request.headers.get("UserName")
        token = request.headers.get("Token")
        url = request.url.path
        guest_role: DbRole = self.role_bll.get_role_by_name("Guest")
        subscriptor_role: DbRole = self.role_bll.get_role_by_name("Subscriptor")

        guest_system_part_names: list[DbRoleSystemPartNameMapping] = self.role_system_part_name_mapping_bll.get_role_system_part_name_mapping_by_role_id(guest_role.Id)

        if url.startswith("/api/") is not True:
            response = await call_next(request)
            return response

        for system_part in guest_system_part_names:
            if url.startswith(system_part.SystemPartName.Url):
                response = await call_next(request)
                return response

        if token is None or user_name is None:
            return Response(status_code=403, content="please login to continue", media_type="text/plain")

        user_data: DbUser = self.user_bll.get_user_by_email_phone_number(user_name)
        if user_data is None:
            return Response(status_code=403, content="please login to continue", media_type="text/plain")

        user_login_attempts: list[DbUserLogins] = self.user_logins_bll.get_user_login_attempts_by_user_id_desc(user_data.Id)
        failed_login_counter = 0
        if user_login_attempts is not None:
            for login_attempt in user_login_attempts:
                if login_attempt.LoginResult is False:
                    failed_login_counter = failed_login_counter + 1
                    if failed_login_counter > 5:
                        return Response(status_code=429, content="Too Many Requests", media_type="text/plain")
                else:
                    break

        last_user_session: DbUserSessions = self.user_sessions_bll.get_user_sessions_by_user_id(user_data.Id)
        if last_user_session is None:
            return Response(status_code=403, content="please login to continue", media_type="text/plain")

        if last_user_session.Token != token:
            return Response(status_code=403, content="please login to continue", media_type="text/plain")

        user_roles: list[DbUserRoleMapping] = self.user_role_mapping_bll.get_user_role_mapping_by_user_id(user_data.Id)
        for user_role in user_roles:
            role_system_part_names: list[DbRoleSystemPartNameMapping] = self.role_system_part_name_mapping_bll.get_role_system_part_name_mapping_by_role_id(user_role.Role.Id)
            for system_part in role_system_part_names:
                if url.startswith(system_part.SystemPartName.Url):
                    response = await call_next(request)
                    return response

        user_active_subs: list[DbUserSubscription.DbUserSubscriptions] = self.user_subscription_bll.get_user_active_subs_by_user_id(user_data.Id)
        if len(user_active_subs) > 0:
            subscriptor_system_part_names: list[DbRoleSystemPartNameMapping] = self.role_system_part_name_mapping_bll.get_role_system_part_name_mapping_by_role_id(subscriptor_role.Id)
            for system_part in subscriptor_system_part_names:
                if url.startswith(system_part.SystemPartName.Url):
                    response = await call_next(request)
                    return response

        return Response(status_code=403, content="Unauthorized", media_type="text/plain")
