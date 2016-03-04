# -*- coding: utf-8 -*-


from mapper.mapper import mapper
from mapper.parsers import feed_parser
from mapper.readers import xml_reader

from mappings import mapping

source = 'test.xml'
reader = xml_reader(source)
parser = feed_parser(mapping['fields'])

for model in mapper(reader, parser, mapping):
    if hasattr(model, 'save') and callable(model.save):
        model.save()
