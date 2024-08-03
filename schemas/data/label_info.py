from pydantic import Field

from schemas.base import BaseModel


class LabelInfo(BaseModel):
    label_format: str = Field(..., description="标签格式")
