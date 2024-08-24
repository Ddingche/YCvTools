# -*- coding: utf-8 -*-
"""
@Time ： 2024/8/11 下午2:26
@Auth ： yechun
"""
import cv2

from cvtools.data.parse import LabelFileParser


class TestLabelFileParser:

    @staticmethod
    def build_test_data():
        image = cv2.imread(
            ".\\tests\\asset\\dog&cat.jpg"
        )
        xml_path = (
            ".\\tests\\asset\\dog&cat.xml"
        )
        return xml_path, image

    @staticmethod
    def test_xml_parser():
        xml_path, image = TestLabelFileParser.build_test_data()
        label_info = LabelFileParser.xml_parser(xml_path=xml_path)
        assert len(label_info.instance_list) == 2

        assert label_info.instance_list[0].label == "cat"
        assert label_info.instance_list[0].left_top.x == 355
        assert label_info.instance_list[0].left_top.y == 893
        assert label_info.instance_list[0].right_bottom.x == 1437
        assert label_info.instance_list[0].right_bottom.y == 2362

        assert label_info.instance_list[1].label == "dog"
        assert label_info.instance_list[1].left_top.x == 1214
        assert label_info.instance_list[1].left_top.y == 107
        assert label_info.instance_list[1].right_bottom.x == 3452
        assert label_info.instance_list[1].right_bottom.y == 2328

        assert label_info.image_info.image_weight == image.shape[1]
        assert label_info.image_info.image_height == image.shape[0]
        assert label_info.image_info.image_channel == image.shape[2]
