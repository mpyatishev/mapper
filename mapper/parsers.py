# -*- coding: utf-8 -*-


from collections import defaultdict


def feed_parser(reader):
    def parser(check_list):
        fields = defaultdict(list)
        for elem in reader:
            if elem.tag in check_list:
                fields.update(*elem.attrib)
                yield (elem.tag, fields)
                fields = defaultdict(list)
            elif elem.text:
                fields[elem.tag] = elem.text
    return parser
