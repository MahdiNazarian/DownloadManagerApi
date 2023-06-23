from pydantic import BaseModel


class ResponseModel(BaseModel):
    status_code: int
    message: str | None = None
    data: any
