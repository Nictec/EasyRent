labor_choices = (
    ('L', 'Licht'),
    ('T', 'Ton'),
    ('R', 'rigging'),
    )



TYPE_CHOICES = (
    ('R', 'Rental'),
    ('FS', 'Full Service'),
)


STATUS_CHOICES = (
    ('OK', 'Geladen'),
    ('im Lager', 'Im Lager'),
	('Abgeschlossen', 'Abgeschlossen')
)


order_choices = (
    ('Res', 'reserviert'),
	('R', 'bereit'),
	('IP', 'in bearbeitung'),
    ('F', 'abgeschlossen')
)
