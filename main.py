import uvicorn
from fastapi import FastAPI
from Controllers.UserController import UserController
from DbContext.DbContext import engine
from DbContext.MigrationController import MigrationController

MigrationController().start_migrate()

app = FastAPI()

user_controller = UserController()

app.include_router(user_controller.router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, reload=True, access_log=False)
