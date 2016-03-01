# -*- coding: utf-8 -*-


def mapper(parser, mapping):
    models = mapping['models']
    for model_name, fields in parser(models):
        for field in mapping[model_name]:
            model = models[model_name](*fields)
        yield model
