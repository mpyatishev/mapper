# -*- coding: utf-8 -*-


def feed_parser(model_fields):
    """Функция производит разбор последовательности состоящей из Element
    в соответствии с определенными для модели полями.

    arguments:
        model_fields -- последовательность, содержащия определенныя для модели поля

    return:
        parser -- функция-парсер
    """
    def parser(elem):
        """
        return:
            кортеж из названия объекта (ключ в model_fields) и словаря параметров.
            Например:
                ('event', {'id': '2323', 'type': 'concert'})
        """
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
