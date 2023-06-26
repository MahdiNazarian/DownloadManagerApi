import uvicorn
from fastapi import FastAPI

from Controllers.TimingController import TimingController
from Controllers.UserController import UserController
from Controllers.SubscriptionTypesController import SubscriptionTypesController
from Controllers.UserSubscriptionController import UserSubscriptionController
from Controllers.UserSettingSubjectsController import UserSettingSubjectsController
from Controllers.UserSettingsController import UserSettingsController
from DbContext.DbContext import engine
from DbContext.MigrationController import MigrationController

MigrationController().start_migrate()

app = FastAPI()

user_controller = UserController()
subscription_types_controller = SubscriptionTypesController()
user_subscription_controller = UserSubscriptionController()
user_setting_subjects_controller = UserSettingSubjectsController()
user_settings_controller = UserSettingsController()
timing_controller = TimingController()

app.include_router(user_controller.router)
app.include_router(subscription_types_controller.router)
app.include_router(user_subscription_controller.router)
app.include_router(user_setting_subjects_controller.router)
app.include_router(user_settings_controller.router)
app.include_router(timing_controller.router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, reload=True, access_log=False)
