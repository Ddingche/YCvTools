from pydantic import Field

from cvtools.schemas.base import BaseModel


class LabelInfo(BaseModel):
    label_format: str = Field(..., description="标签格式")
