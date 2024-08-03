from cvtools.schemas.data.train_dataset import DataSet


class TestDataset:

    @staticmethod
    def fake_dataset():
        dataset = DataSet(
            image_dir="./test_data", label_dir="", txt_dir="", random_seed=42
        )
        return dataset

    @staticmethod
    def test_data_num():
        dataset = TestDataset.fake_dataset()
        assert dataset.data_nums == 1

    @staticmethod
    def test_label_file_parser():
        dataset = TestDataset.fake_dataset()
        train_list, val_list = dataset.split_dataset(train_ratio=0.7, val_ratio=0.3)
        assert len(train_list) + len(val_list) == 1
