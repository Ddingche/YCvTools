from datetime import datetime

import pytz
from arrow import Arrow
from pydantic import BaseModel

class BasicModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda t: t.astimezone(pytz.timezone("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S"),  # type: ignore # noqa: E501
            Arrow: Arrow.format,
        }
