# -*- coding: utf-8 -*-


def feed_parser(reader):
    def parser(check_list):
        fields = {}
        for elem in reader:
            if elem.tag in check_list:
                fields.update(*elem)
                yield (elem.tag, fields)
                fields = {}
            elif elem.text:
                fields[elem.tag] = elem.text
    return parser
