import os

from pydantic import Field

from YCvTools.schemas.base import BaseModel


class DataSet(BaseModel):
    image_dir: str = Field(
        ..., description="Path to the directory containing the images"
    )
    xml_dir: str = Field(
        ..., description="Path to the directory containing the xml files"
    )
    txt_dir: str = Field(
        ..., description="Path to the directory containing the txt files"
    )
    random_seed: int = Field(42, description="Seed for random number generator")

    @property
    def data_nums(self):
        return len(os.listdir(self.image_dir))

    @property
    def split_dataset(self, train_ratio: float = 0.8, val_ratio: float = 0.2):
        """
        划分数据集
        """
        assert train_ratio > 0
        assert val_ratio > 0
