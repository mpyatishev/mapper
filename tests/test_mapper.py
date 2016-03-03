# -*- coding: utf-8 -*-

import os
import os.path
import unittest

from io import BytesIO
from collections.abc import Generator
from unittest import mock

from mapper.mapper import mapper
from mapper.readers import xml_reader
from mapper.parsers import feed_parser


class TestMapper(unittest.TestCase):
    def setUp(self):
        self.source = os.path.join(os.path.dirname(__file__), 'data', 'test.xml')
        self.mapping = {}

    def test_mapper_returns_generator(self):
        m = mapper(mock.MagicMock(), self.mapping)

        self.assertIsInstance(m, Generator)

    def test_xml_reader_returns_generator(self):
        reader = xml_reader(self.source)

        self.assertIsInstance(reader, Generator)

    def test_feed_parser_returns_generator(self):
        parser = feed_parser(mock.MagicMock())

        self.assertIsInstance(parser, Generator)

    def test_mapper_returns_model_with_filled_params(self):
        Event = mock.MagicMock()
        mapping = {
            'models': {
                'event': Event
            },
            'fields': {
                'event': {
                    'id': 'incoming_id',
                    'title': 'title',
                    'image': 'images',
                },
                'place': {
                    'id': 'incoming_id',
                    'title': 'title',
                }
            }
        }

        source = """<?xml version="1.0" encoding="utf8"?>
<feed version="1.1">
  <events>
    <event id="93492" price="true" type="concert">
      <title><![CDATA[Kodaline]]></title>
      <age_restricted>18+</age_restricted>
      <tags>
        <tag>18+</tag>
        <tag>концерт</tag>
        <tag>рок и рок-н-ролл</tag>
      </tags>
      <gallery>
        <image href="http://test.kudago.com/media/images/event/00/69/0069659af8601e1d1560886ae9dd75b1.jpg"/>
      </gallery>
      <text><![CDATA[]]></text>
    </event>
  </events>
</feed>"""

        reader = xml_reader(BytesIO(source.encode()))
        mapped_models = mapper(reader, mapping)

        model = next(mapped_models)

        self.assertEquals(model.incoming_id, 93492)

    def test_parser_returns_dict(self):
        Event = mock.MagicMock()
        Tag = mock.MagicMock()
        Image = mock.MagicMock()
        mapping = {
            'models': {
                'event': Event,
            },
            'fields': {
                'event': ('id', 'title', 'text', 'age_restricted')
            }
        }

        source = """<?xml version="1.0" encoding="utf8"?>
<feed version="1.1">
  <events>
    <event id="93492" price="true" type="concert">
      <title><![CDATA[Kodaline]]></title>
      <age_restricted>18+</age_restricted>
      <tags>
        <tag>18+</tag>
        <tag>концерт</tag>
        <tag>рок и рок-н-ролл</tag>
      </tags>
      <gallery>
        <image href="http://test.kudago.com/media/images/event/00/69/0069659af8601e1d1560886ae9dd75b1.jpg"/>
      </gallery>
      <text><![CDATA[]]></text>
    </event>
  </events>
</feed>"""

        reader = xml_reader(BytesIO(source.encode()))
        parser = feed_parser(mapping['models'], mapping['fields'])
        d = next(next(map(parser, filter(lambda e: e.name in mapping['models'], reader))))

        expected = (Event, {
            'id': '93492',
            'price': 'true',
            'type': 'concert',
            'title': 'Kodaline',
            'age_restricted': '18+',
            'text': ''
        })

        # 'tag': ['18+', 'концерт', 'рок и рок-н-ролл'],
        # 'image': [{
        #     'href': 'http://test.kudago.com/media/images/event/00/69/0069659af8601e1d1560886ae9dd75b1.jpg'
        # }],

        print(d, expected)
        self.assertEquals(d, expected)


if __name__ == '__main__':
    unittest.main()
