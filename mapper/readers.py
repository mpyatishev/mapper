# -*- coding: utf-8 -*-

from collections import namedtuple

from lxml import etree


# namedtuple в последствии можно будет заменить на класс
# без необходимости переделки зависимого кода
Element = namedtuple('Element', ('name', 'text', 'fields', 'children'))


def xml_reader(xml):
    root = etree.parse(xml).getroot()
    def reader(root):
        for elem in root.iter():
            text = elem.text
            text = text.strip() if text else None
            yield Element(elem.tag, text=text, fields=elem.attrib,
                        children=reader(elem))
    return reader(root)
