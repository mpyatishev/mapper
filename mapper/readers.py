# -*- coding: utf-8 -*-

from collections import namedtuple

from lxml import etree


# namedtuple в последствии можно будет заменить на класс
# без необходимости переделки зависимого кода
Element = namedtuple('Element', ('name', 'attrib', 'text'))


def xml_reader(xml):
    root = etree.iterparse(xml)
    for _, elem in root:
        yield Element(elem.tag, elem.attrib, elem.text)
