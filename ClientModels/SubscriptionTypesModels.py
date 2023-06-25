from pydantic import BaseModel


class SubscriptionTypesInsertModel(BaseModel):
    Name: str
    Price: int


class SubscriptionTypesUpdateModel(SubscriptionTypesInsertModel):
    Id: int | None = None
    GuId: str | None = None
    Deleted: bool | None = None
