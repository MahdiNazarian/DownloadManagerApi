import uvicorn
from fastapi import FastAPI

from Controllers.TimingController import TimingController
from Controllers.UserController import UserController
from Controllers.SubscriptionTypesController import SubscriptionTypesController
from Controllers.UserSubscriptionController import UserSubscriptionController
from Controllers.UserSettingSubjectsController import UserSettingSubjectsController
from Controllers.UserSettingsController import UserSettingsController
from Controllers.DownloadLineController import DownloadLineController
from Controllers.DownloadFileController import DownloadFileController
from Controllers.UserDownloadMappingController import UserDownloadMappingController
from Controllers.RoleController import RoleController
from Controllers.SystemPartNameController import SystemPartNameController
from Controllers.RoleSystemPartNameMappingController import RoleSystemPartNameMappingController
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
download_line_controller = DownloadLineController()
download_file_controller = DownloadFileController()
user_download_mapping_controller = UserDownloadMappingController()
role_controller = RoleController()
system_part_name_controller = SystemPartNameController()
role_system_part_name_mapping_controller = RoleSystemPartNameMappingController()

app.include_router(user_controller.router)
app.include_router(subscription_types_controller.router)
app.include_router(user_subscription_controller.router)
app.include_router(user_setting_subjects_controller.router)
app.include_router(user_settings_controller.router)
app.include_router(timing_controller.router)
app.include_router(download_line_controller.router)
app.include_router(download_file_controller.router)
app.include_router(user_download_mapping_controller.router)
app.include_router(role_controller.router)
app.include_router(system_part_name_controller.router)
app.include_router(role_system_part_name_mapping_controller.router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, reload=True, access_log=False)
