# Osoba
```python
from testowaAnkieta.models import Osoba, Druzyna, MIESIAC
from testowaAnkieta.serializers import OsobaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

osoba = Osoba(imie='Klaudia', nazwisko='Drzazga', miesiac_urodzenia=3)        
osoba.save()

serializer = OsobaSerializer(osoba)                                    
serializer.data
#{'id': 6, 'imie': 'Klaudia', 'nazwisko': 'Drzazga', 'miesiac_urodzenia': 3, 'data_dodania': '2022-10-27', 'druzyna': None}

content = JSONRenderer().render(serializer.data)
content
#b'{"id":6,"imie":"Klaudia","nazwisko":"Drzazga","miesiac_urodzenia":3,"data_dodania":"2022-10-27","druzyna":null}'

import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = OsobaSerializer(data=data)  
deserializer.is_valid()
#True

deserializer.errors
#{}

deserializer.fields
#{'id': IntegerField(read_only=True), 'imie': CharField(required=True), 'nazwisko': CharField(required=True), 'miesiac_urodzenia': ChoiceField(choices=[(1, 'Styczen'), (2, 'Luty'), (3, 
#'Marzec'), (4, 'Kwiecien'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpien'), (9, 'Wrzesien'), (10, 'Pazdziernik'), (11, 'Listopad'), (12, 'Grudzien')], default=1), 'data_dodania': DateField(), 'druzyna': PrimaryKeyRelatedField(allow_null=True, queryset=<QuerySet [<Druzyna: Tygrysuchy PL>, <Druzyna: Miernotuchy PL>, <Druzyna: Rekinuchy DE>]>)}

repr(deserializer)
#"OsobaSerializer(data={'id': 7, 'imie': 'Klaudia', 'nazwisko': 'Drzazga', 'miesiac_urodzenia': 3, 'data_dodania': '2022-10-27', 'druzyna': None}):\n    id = IntegerField(read_only=True
#)\n    imie = CharField(required=True)\n    nazwisko = CharField(required=True)\n    miesiac_urodzenia = ChoiceField(choices=[(1, 'Styczen'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecien'
#), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpien'), (9, 'Wrzesien'), (10, 'Pazdziernik'), (11, 'Listopad'), (12, 'Grudzien')], default=1)\n    data_dodania = DateField()\n    druzyna = PrimaryKeyRelatedField(allow_null=True, queryset=<QuerySet [<Druzyna: Tygrysuchy PL>, <Druzyna: Miernotuchy PL>, <Druzyna: Rekinuchy DE>]>)"

deserializer.validated_data
#OrderedDict([('imie', 'Klaudia'), ('nazwisko', 'Drzazga'), ('miesiac_urodzenia', 3), ('data_dodania', datetime.date(2022, 10, 27)), ('druzyna', None)])

deserializer.save()
#<Osoba: Klaudia Drzazga>

deserializer.data
#{'id': 7, 'imie': 'Klaudia', 'nazwisko': 'Drzazga', 'miesiac_urodzenia': 3, 'data_dodania': '2022-10-27', 'druzyna': None}

```
# Druzyna
```python
from testowaAnkieta.models import Osoba, Druzyna, MIESIAC
from testowaAnkieta.serializers import DruzynaSerializer 
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

druzyna = Druzyna(nazwa="Kaczuchy", kraj="TV")
druzyna.save()

serializer = DruzynaSerializer(druzyna)   
serializer.data
#{'id': 4, 'nazwa': 'Kaczuchy', 'kraj': 'TV'}

content = JSONRenderer().render(serializer.data)
content
#b'{"id":4,"nazwa":"Kaczuchy","kraj":"TV"}'

import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = DruzynaSerializer(data=data) 
deserializer.is_valid()
#True

deserializer.errors
#{}

deserializer.fields
#{'id': IntegerField(read_only=True), 'nazwa': CharField(required=True), 'kraj': CharField(required=True)}

repr(deserializer)
#"DruzynaSerializer(data={'id': 4, 'nazwa': 'Kaczuchy', 'kraj': 'TV'}):\n    id = IntegerField(read_only=True)\n    nazwa = CharField(required=True)\n    kraj = CharField(required=True)"

deserializer.validated_data
#OrderedDict([('nazwa', 'Kaczuchy'), ('kraj', 'TV')])

deserializer.save()
#<Druzyna: Kaczuchy TV>

deserializer.data
#{'id': 5, 'nazwa': 'Kaczuchy', 'kraj': 'TV'}
```