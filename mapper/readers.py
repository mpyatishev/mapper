# -*- coding: utf-8 -*-

from lxml import etree


def recursive_dict(element):
    return element.tag, dict(map(recursive_dict, element)) or element.text


def xml_reader(xml):
    return etree.parse(xml).getroot().iter()
