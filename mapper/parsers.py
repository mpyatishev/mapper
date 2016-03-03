# -*- coding: utf-8 -*-


from collections import defaultdict


def feed_parser(models, model_fields):
    def parser(elem):
        result = (elem.name, elem.fields)
        for child in elem.children:
            result = result + tuple(parser(child))
        yield result
        # f = defaultdict(list)
        # res = None
        # in_elem = False

        # if elem.name in check_list:
        #     if res:
        #         yield res
        #         res = None
        #         f = defaultdict(list)
        #         in_elem = False
        #     f.update(elem.fields)
        #     res = (check_list[elem.name], f)
        #     in_elem = True
        #     check_fields = model_fields[elem.name]
        # elif in_elem and elem.name in check_fields:
        #     if elem.text and elem.name not in f:
        #         f[elem.name] = elem.text
        #     else:
        #         f[elem.name] = list(f[elem.name]).append(elem.text)

    return parser
