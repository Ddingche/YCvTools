import os

from pydantic import Field, field_validator

from cvtools.schemas.base import BasicModel


class DataSet(BasicModel):
    image_dir: str = Field(
        ..., description="Path to the directory containing the images"
    )
    label_dir: str = Field(
        ..., description="Path to the directory containing the label files"
    )
    txt_dir: str = Field(
        ..., description="Path to the directory containing the txt files"
    )
    random_seed: int = Field(42, description="Seed for random generator")

    @field_validator("image_dir")
    def image_dir_validator(cls, v):
        assert os.path.isdir(v), "Image directory does not exist"
        assert len(os.listdir(v)) > 0, "Image directory is empty"

    @field_validator("label_dir")
    def label_dir_validator(cls, v):
        assert os.path.isdir(v), "Label directory does not exist"
        assert len(os.listdir(v)) > 0, "Label directory is empty"

    @field_validator("txt_dir")
    def txt_dir_validator(cls, v):
        assert os.path.isdir(v), "txt directory does not exist"
        assert len(os.listdir(v)) > 0, "txt directory is empty"
