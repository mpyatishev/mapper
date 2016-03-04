# -*- coding: utf-8 -*-


def mapper(reader, parser, mapping):
    models = mapping['models']
    model_fields = mapping['fields']
    for model, fields in map(parser,
                             filter(lambda e: e.name in mapping['models'], reader)):
        klass = models[model]
        klass_fields = model_fields[model]
        params = {}
        for field, value in fields.items():
            if field in klass_fields:
                params[klass_fields[field]] = value

        yield klass(**params)
