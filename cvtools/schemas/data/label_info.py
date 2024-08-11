from typing import List

from pydantic import Field

from cvtools.schemas.base import BasicModel
from cvtools.schemas.data.coord import Bbox


class InstanceBBox(Bbox):
    label: str = Field(..., description="实例标签")


class ImageInfo(BasicModel):
    image_weight: int = Field(..., description="图像宽度")
    image_height: int = Field(..., description="图像高度")
    image_channel: int = Field(..., description="图像通道数")


class LabelInfo(BasicModel):
    instance_list: List[InstanceBBox] = Field(default=[], description="实例列表")
    image_info: ImageInfo = Field(..., description="图像信息")
