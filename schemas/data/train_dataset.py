import glob
import os
import random
from typing import List, Tuple

from pydantic import Field

from YCvTools.schemas.base import BaseModel # type: ignore


class DataSet(BaseModel):
    image_dir: str = Field(
        ..., description="Path to the directory containing the images"
    )
    label_dir: str = Field(
        ..., description="Path to the directory containing the label files"
    )
    txt_dir: str = Field(
        ..., description="Path to the directory containing the txt files"
    )
    random_seed: int = Field(42, description="Seed for random number generator")

    @property
    def data_nums(self):
        return len(os.listdir(self.image_dir))

    @property
    def split_dataset(
        self, train_ratio: float = 0.8, val_ratio: float = 0.2
    ) -> Tuple[List, List]:
        random.seed(self.random_seed)
        """
        划分数据集
        :param train_ratio: 训练集比例
        :param val_ratio: 验证集比例
        :return: 训练集和验证集的文件名列表
        """
        assert train_ratio > 0
        assert val_ratio > 0
        image_filename_list = glob.glob(self.image_dir + "/*")
        train_image_filename_list = []
        val_image_filename_list = []
        for image_filename in image_filename_list:
            flag = random.random()
            if flag < train_ratio:
                train_image_filename_list.append(image_filename)
            else:
                val_image_filename_list.append(image_filename)
        return train_image_filename_list, val_image_filename_list
