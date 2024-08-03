from cvtools.schemas.data.label_info import LabelInfo


class LabelFileParser:
    # TODO: @yechun 结合各主流标注软件的格式，实现解析器和数据结构
    @staticmethod
    def xml_parser(xml_path) -> LabelInfo:
        """
        parse xml label file
        :param xml_path: xml file path
        :return: label info
        """
        label_info = LabelInfo(label_format="")
        return label_info
