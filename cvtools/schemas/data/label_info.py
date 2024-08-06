from pydantic import Field

from cvtools.schemas.base import BasicModel


class LabelInfo(BasicModel):
    label_format: str = Field(..., description="标签格式")
