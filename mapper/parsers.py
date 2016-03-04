# -*- coding: utf-8 -*-


def feed_parser(model_fields):
    def parser(elem):
        result = dict(text=elem.text, **elem.fields)
        fields = model_fields[elem.name]
        for child in elem.children:
            cname = child.name
            if cname in fields:
                if not child.fields:
                    data = child.text
                else:
                    data = dict(**child.fields)
                    if child.text:
                        data['value'] = child.text
                if data is None:
                    continue
                if cname in result and result[cname]:
                    try:
                        result[cname].append(data)
                    except AttributeError:
                        result[cname] = [result[cname], data]
                else:
                    result[cname] = data
        return elem.name, result
    return parser
