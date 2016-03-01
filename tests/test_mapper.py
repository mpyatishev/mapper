# -*- coding: utf-8 -*-

import os
import os.path
import unittest

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


if __name__ == '__main__':
    unittest.main()
