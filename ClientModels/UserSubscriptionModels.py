from pydantic import BaseModel
import datetime


class UserSubscriptionInsertModel(BaseModel):
    UserId: int
    SubscriptionTypeId: int
    active: bool
    SubscriptionBuyDate: datetime.datetime
    SubscriptionEndDate: datetime.datetime


class UserSubscriptionUpdateModel(UserSubscriptionInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None
