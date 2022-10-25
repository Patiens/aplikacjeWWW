from testowaAnkieta.models import Osoba, Druzyna

Osoba.objects.all()

Osoba.objects.get(id__exact=3)

Osoba.objects.filter(imie__contains='A')

Osoba.objects.filter(druzyna__isnull=False).order_by().values('druzyna__nazwa').distinct()

#dla lepszej czytelnosci z petla for
for o in Osoba.objects.filter(druzyna__isnull=False).order_by().values('druzyna__nazwa').distinct():
    print(o)

Druzyna.objects.order_by('-nazwa')

o = Osoba(imie="Piotr", nazwisko="Piotrowski", miesiac_urodzenia="4")

o.save()
