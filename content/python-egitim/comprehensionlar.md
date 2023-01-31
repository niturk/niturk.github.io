+++
title = "Comprehensionlar"
date = "2023-01-22T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


Comprehensionlar pythonda listeleri, sözlükleri ve setleri döngü kullanarak basitçe oluşturmak için kullanılan bir yöntemdir. Kullanımı döngü kullanımına çok benzer.

> Basit veriler için çok kullanışlıdır ancak karmaşa arttıkça kodun okunabilirliği aniden azalır. Dikkatli olmak gerekir. Unutmayalım ki kısa kodlar yazmak her zaman iyi bir şey değildir. Kodumuzun okunabilirliği bizim için her zaman birinci sıradadır.

&nbsp;

## Listelerde Comprehension

Elimizde bir sayı demeti (tuple) olsun ve biz bu sayıların karelerinden oluşan bir liste oluşturmak istesek. Bunu iki yöntemle yapabiliriz.

- 1. Yöntem şimdiye kadar öğrendiğimiz yöntemlerle yapabiliriz.



```python
# Mevcut yöntemlerle tuple içindeki sayıların karesinin listesi
sayilar = (1, 2, 3, 4, 5)
liste = []
for sayi in sayilar:
    liste.append(sayi**2)
print(liste)
```

    [1, 4, 9, 16, 25]



```python
# List Comprehension ile tuple içindeki sayıların karesinin listesi
sayilar = (1, 2, 3, 4, 5)
liste = [sayi**2 for sayi in sayilar]
print(liste)
```

    [1, 4, 9, 16, 25]


Aslında for döngüzü yazarak listeye eleman eklemiyoruzda bir listenin içerisine for döngüsüyle tek satırda eleman ekliyoruz. Bu yöntemde listeyi oluşturmak için önce bir boş liste oluşturuyoruz ve ardından for döngüsüyle bu listeye eleman ekliyoruz.

`[deger for deger in demet]` şeklinde bir ifade yazıyoruz. Karar yapılarındaki üçlü koşul ifadesine benzer bir yapı var.

Şimdi bu yönteme birde karar yapısı ekleyelim.


```python
# 1. Yöntem: Sadece çift sayıların karesinin listesi mevcut yöntemlerle
sayilar = (1, 2, 3, 4, 5)
liste = []
for sayi in sayilar:
    if sayi % 2 == 0:
        liste.append(sayi**2)
print(liste)
```

    [4, 16]



```python
# 2. Yöntem: Sadece çift sayıların karesinin listesi list comprehension ile
sayilar = (1, 2, 3, 4, 5)
liste = [sayi**2 for sayi in sayilar if sayi % 2 == 0]
print(liste)
```

    [4, 16]


> Her iki kod birbirinin tamamen aynısı. Yine aynı şekilde aslında for döngüsüyle ve if karar yapısıyla tek satırda eleman ekliyoruz.  
`[deger for deger in demet if koşul]`

> List comprehension, for döngüsü ile yazılan normal koda göre daha hızlıdır!

&nbsp;

## Sözlüklerde ve Setlerde Comprehension

Listeler için yaptığımız şeyleri sözlükler ve setler için de yapabiliriz. Sadece `[]` yerine `{}` kullanıyoruz.

- Sözlükler için `{anahtar:deger for anahtar,deger in demet}`
- Setler için `{deger for deger in demet}`


```python
# Bildiğimiz yöntemlerle bir sözlük oluşturalım.

urunler = ["elma", "armut", "muz", "kiraz"]
fiyatlar = [5, 6, 7, 0]
sozluk = {}
for i in range(len(urunler)):
    if fiyatlar[i] > 0:
        sozluk[urunler[i]] = fiyatlar[i]
print(sozluk)
```

    {'elma': 5, 'armut': 6, 'muz': 7}



```python
# Comprehension ile aynı sözlüğü oluşturalım.
urunler = ["elma", "armut", "muz", "kiraz"]
fiyatlar = [5, 6, 7, 0]
sozluk = {urunler[i]: fiyatlar[i] for i in range(len(urunler)) if fiyatlar[i] > 0}
print(sozluk)
```

    {'elma': 5, 'armut': 6, 'muz': 7}



```python
# Bildiğimiz yöntemlerle bir set oluşturalım.
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ciftler = set()
for sayi in sayilar:
    if sayi % 2 == 0:
        ciftler.add(sayi)
print(ciftler)
```

    {2, 4, 6, 8, 10}



```python
# Comprehension ile aynı seti oluşturalım.
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ciftler = {sayi for sayi in sayilar if sayi % 2 == 0}
print(ciftler)
```

    {2, 4, 6, 8, 10}



```python
# Bir listedeki sayıların çift olanlarını bulalım ve listemizdeki elemanları benzersiz yapalım.
sayilar = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]
ciftler = {sayi for sayi in sayilar if sayi % 2 == 0}
sayilar2 = list(ciftler)
print(sayilar2)
```

    [2, 4, 6, 8, 10]

