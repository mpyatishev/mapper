# -*- coding: utf-8 -*-


from models import (
    Event,
    Place,
    Schedule,
)


mapping = {
    'models': {
        'event': Event,
        'place': Place,
        'session': Schedule,
    },
    'fields': {
        'event': {
            'id': 'foreign_id',
            'age_restricted': 'age',
            'price': 'price',
            'type': 'type',
            'title': 'title',
            'text': 'text',
            'tag': 'tags',
            'image': 'images'
        },
        'place': {
            'id': 'foreign_id',
            'type': 'type',
            'title': 'title',
            'address': 'address',
            'cooridinates': 'coordinates',
            'phone': 'phones',
            'work_time': 'work_times',
            'tag': 'tags',
            'metro': 'metros',
            'image': 'images',
            'text': 'text',
            'url': 'url'
        },
        'session': {
            'date': 'date',
            'time': 'time',
            'timetill': 'timetill',
            'event': 'event_id',
            'place': 'place_id',
        }
    },
}
