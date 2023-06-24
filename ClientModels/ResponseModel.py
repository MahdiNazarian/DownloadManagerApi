from pydantic import BaseModel


class ResponseModel(BaseModel):
    status_code: int
    message: str | None = None
    data: list | set | dict | frozenset | tuple | object | str | int | bool | float | None = None
