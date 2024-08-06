# -*- coding: utf-8 -*-
"""
@Time ： 2024/8/3 下午11:41
@Auth ： yechun
"""
from typing import List

from pydantic import Field

from cvtools.schemas.base import BasicModel


class Point(BasicModel):
    x: float = Field(default=0.0, description="x axis value")
    y: float = Field(default=0.0, description="y axis value")


class Bbox(BasicModel):
    left_top: Point = Field(default=Point(x=0.0, y=0.0), description="left top point")
    right_bottom: Point = Field(
        default=Point(x=0.0, y=0.0), description="right bottom point"
    )

    @property
    def left(self) -> float:
        return self.left_top.x

    @property
    def right(self) -> float:
        return self.right_bottom.x

    @property
    def top(self) -> float:
        return self.left_top.y

    @property
    def bottom(self) -> float:
        return self.right_bottom.y

    @property
    def ltrb(self) -> List[float]:
        return [
            self.left,
            self.top,
            self.right,
            self.bottom,
        ]

    @property
    def xywh(self) -> List[float]:
        return [
            self.center_x,
            self.center_y,
            self.width,
            self.height,
        ]

    @property
    def center_x(self) -> float:
        return (self.left + self.right) / 2

    @property
    def center_y(self) -> float:
        return (self.top + self.bottom) / 2

    @property
    def width(self) -> float:
        return self.right - self.left

    @property
    def height(self) -> float:
        return self.bottom - self.top
