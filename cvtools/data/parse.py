from xml.etree import ElementTree

from cvtools.schemas.data.coord import Point
from cvtools.schemas.data.label_info import ImageInfo, InstanceBBox, LabelInfo


class LabelFileParser:

    @staticmethod
    def xml_parser(xml_path: str) -> LabelInfo:
        """
        parse xml label file
        :param xml_path: xml file path
        :return: label info
        """
        tree = ElementTree.parse(xml_path)
        root = tree.getroot()
        instance_bbox_list = []
        image_size = root.find("size")
        image_height = int(image_size.find("height").text)
        image_weight = int(image_size.find("width").text)
        image_channel = int(image_size.find("depth").text)
        image_info = ImageInfo(
            image_weight=image_weight,
            image_height=image_height,
            image_channel=image_channel,
        )
        for obj in root.iter("object"):
            cls_name = str(obj.find("name").text)
            xml_bbox = obj.find("bndbox")
            xmin = int(xml_bbox.find("xmin").text)
            ymin = int(xml_bbox.find("ymin").text)
            xmax = int(xml_bbox.find("xmax").text)
            ymax = int(xml_bbox.find("ymax").text)
            instance_bbox_list.append(
                InstanceBBox(
                    left_top=Point(x=xmin, y=ymin),
                    right_bottom=Point(x=xmax, y=ymax),
                    label=cls_name,
                )
            )

        label_info = LabelInfo(instance_list=instance_bbox_list, image_info=image_info)
        return label_info
