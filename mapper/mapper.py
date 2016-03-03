# -*- coding: utf-8 -*-

from collections import defaultdict


def extract_params(element, fields):
    result = {}
    for field in filter(lambda k: k in fields, element.fields):
        result[fields[field]] = element.fields[field]
    return result


def mapper(reader, mapping):
    models = mapping['models']
    for element in reader:
        if element.name in models:
            model_name = element.name
            model = models[model_name]
            model_fields = mapping['fields'][model_name]

            params = defaultdict(list, **extract_params(element, model_fields))

            for child in reader:
                if child.name in model_fields:
                    params[child.name].append(extract_params(child, model_fields))

            yield model(**params)
