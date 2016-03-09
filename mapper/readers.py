# -*- coding: utf-8 -*-

from collections import namedtuple

from lxml import etree


# namedtuple в последствии можно будет заменить на класс
# без необходимости переделки зависимого кода
Element = namedtuple('Element', ('name', 'text', 'fields', 'children'))


def xml_reader(xml):
    """ Функция последовательно читает xml-файл, преобразуя его элементы
    во внутренний класс Element

    arguments:
        xml -- путь к файлу

    return:
        генератор
    """
    root = etree.parse(xml).getroot()

    def reader(root):
        return (Element(elem.tag, text=elem.text.strip() if elem.text else None,
                        fields=elem.attrib, children=reader(elem))
                for elem in root.iter())
    return reader(root)
