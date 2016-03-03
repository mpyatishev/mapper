# -*- coding: utf-8 -*-


from models import (
    Event,
    Place,
    Schedule,
)


feed_mapping = {
    'models': {
        'event': Event,
        'place': Place,
        'session': Schedule,
    },
    'fields': {
        'event': {
            'id': 'foreign_id',
            'age_restricted': 'age',
        }
    },
}
