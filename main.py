import uvicorn
from fastapi import FastAPI
from Controllers.UserController import UserController
from Controllers.SubscriptionTypesController import SubscriptionTypesController
from Controllers.UserSubscriptionController import UserSubscriptionController
from DbContext.DbContext import engine
from DbContext.MigrationController import MigrationController

MigrationController().start_migrate()

app = FastAPI()

user_controller = UserController()
subscription_types_controller = SubscriptionTypesController()
user_subscription_controller = UserSubscriptionController()

app.include_router(user_controller.router)
app.include_router(subscription_types_controller.router)
app.include_router(user_subscription_controller.router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, reload=True, access_log=False)
