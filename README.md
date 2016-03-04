# mapper
Тестовое задание для KudaGo

Пример работы с модулем можно посмотреть в example.
Запустить пример:
```
./runexample.sh
```

Сопоставления моделей и полей задается словарем:
```
{
	'models': {
		'event': Event,
		'place': Place,
		'session': Schedule,
	},
	'fields': {
		'event': {
			'id': 'foreign_id',
			'title': 'title'
		},
		'place': {
			'id': 'foreign_id',
			'type': 'type',
			'url': 'url'
		},
		'session': {
			'date': 'date',
			'time': 'time',
			'timetill': 'timetill',
			'event': 'event_id',
			'place': 'place_id',
		}
	}
}
```
