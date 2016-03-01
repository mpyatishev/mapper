# -*- coding: utf-8 -*-


from collections import defaultdict

from mapper import mapper
from mapper.parsers import feed_parser
from mapper.readers import xml_reader

from mappings import feed_mapping

source = 'test.xml'
reader = xml_reader(source)
parser = feed_parser(reader)

for model in mapper(parser, feed_mapping):
    if hasattr(model, 'save'):
        model.save()
