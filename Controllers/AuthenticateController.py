from fastapi import APIRouter, HTTPException

from BussinessLogic.AuthenticateBll import AuthenticateBll
from ClientModels import UserAuthenticateModels
from ClientModels.ResponseModel import ResponseModel


class AuthenticateController:
    def __init__(self):
        self.bll = AuthenticateBll()
        self.router: APIRouter = APIRouter(
            prefix="/authenticate",
            tags=["authenticate"],
            responses={404: {"description": "Not found"}},
        )

        @self.router.post("/register_user")
        def register_user(register_data: UserAuthenticateModels.UserRegisterModel):
            if register_data is not None:
                if register_data.Password == register_data.Re_Password:
                    register_result = self.bll.user_register(register_data=register_data)
                    if register_result is not None:
                        return ResponseModel(status_code=200, message="User Registered Successfully", data=register_result)
                    else:
                        raise HTTPException(status_code=500, detail="User Register Failed")
                else:
                    raise HTTPException(status_code=500, detail="Password And Repeat Not Same")
            else:
                raise HTTPException(status_code=400, detail="No data entered")

        @self.router.post("/login")
        def login_user(login_data: UserAuthenticateModels.UserLoginModel):
            if login_data is not None:
                login_result = self.bll.user_login(login_data=login_data)
                if login_result is not None:
                    return ResponseModel(status_code=200, message="User loged in Successfully", data=login_result)
                else:
                    raise HTTPException(status_code=500, detail="User login Failed")
            else:
                raise HTTPException(status_code=400, detail="No data entered")
