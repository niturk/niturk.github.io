+++
title = "Fonksiyonlar"
date = "2023-01-25T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


Fonksiyonlar en işlevsel yapılardan biridir. Kod tekrarını önlemek için ve kompleks olan kodları parçalara bölmek için ihtiyacımız vardır. Fonksiyon çağrıları yaparken argüman ve parametreler kullanırız. Teknik olarak ikiside aynı şeydir ve sık sık birbirine karıştırılır.
- Fonksiyon yaratırken parametreleri kullanırız.
- Fonksiyon çağrıları yaparken argümanları kullanırız.

> Fonksiyonlar her python nesnesi olduğu gibi bir nesnedir ve değişkene atanır.
Fonksiyonların durum, kod ve parametreleri vardır. Ayrıca çağrı yapılabilecek bir nesnedir.

# Çağrılabilen Nesneler

`()` parantez ile çağrılabilen nesnelere çağrılabilir nesneler diyoruz. Fonksiyonlar bu nesnelere en iyi örneklerden biridir.


```python
# Fonksiyon Yaratma
def fonksiyon_adi():
    return True
```


```python
def merhaba_yaz():
    print("Merhaba")
merhaba_yaz()
```

    Merhaba


> `return` ifadesi ile fonksiyonun sonucunu döndürürüz. `return` yazılmaz ise fonksiyon `None` döndürür.


```python
# Return Örneği
def sayi_bul():
    return 5
sayi = sayi_bul()
print(sayi)
```

    5



```python
# Karmaşık bir örnek
from datetime import datetime
def simdiki_zaman_utc():
    return datetime.utcnow().isoformat()

sonuc = simdiki_zaman_utc()
print(sonuc)
```

    2023-02-06T20:10:06.674891


# Parametreli Fonksiyonlar

Fonksiyonlar parametre alarak çalışabilir ve bu parametrelere göre çalışma şeklini değiştirebilir.


```python
def toplama(a, b):
    return a + b

sonuc = toplama(5, 6)
print(sonuc)
```

    11


## Fonksiyon Parametresi Olarak *(Yıldız) Kullanımı

Fonksiyonlara belirsiz bir sayıda parametre göndermek için kullanırız. Bu parametreler bir tuple içinde saklanır.


```python
# Fonksiyon parametresi olarak *
def toplama(*args):
    return sum(args)
sonuc = toplama(5, 6, 7, 8, 9)
print(sonuc)
```

    35


## Fonksiyon Parametrelerinde Varsayılan Değerler

Fonksiyon parametrelerine varsayılan değerler atayabiliriz. Bu sayede fonksiyon çağrıları yaparken parametreleri belirtmek zorunda kalmayız.


```python
# Fonksiyonlarda varsayılan değerler
def toplama(a, b, c=0):
    return a + b + c

sonuc = toplama(5, 6)
print(sonuc)
```

    11


> Fonksiyon parametrelerinde varsayılan değerlerin sırası önemlidir ve varsayılan parametrelerden sonra normal parametre kullanılamaz. Varsayılan değerlerin sırası değiştirilirse hata alırız. Örneğin `def func(a, b=1, c=2)` şeklinde tanımlanmış bir fonksiyon var. Bu fonksiyonu `func(1, 2, 3)` şeklinde çağırdığımızda `a=1, b=2, c=3` olur. Ancak `func(1, c=3)` şeklinde çağırdığımızda `a=1, b=1, c=3` olur. Çünkü `c` parametresi varsayılan değerini kullanmaz.

## Fonksiyon Parametrelerinde ** (Çift Yıldız) Kullanımı

Fonksiyonlara belirsiz bir sayıda parametre göndermek için kullanırız. Bu parametreler bir dictionary içinde saklanır.


```python
# Fonksiyon parametrelerinde **kwargs
def toplama(**kwargs):
    return sum(kwargs.values())

sonuc = toplama(a=5, b=6, c=7)
print(sonuc)
```

    18


# Lambda Fonksiyonu

Lambda fonksiyonları tek satırlık fonksiyonlardır. Lambda fonksiyonları bir değişkene atanır ve bu değişken üzerinden çağrılır. Lambda fonksiyonları `return` ifadesi kullanılmadan yazılır.


```python
# Örnek Lambda Kodu
toplama = lambda a, b: a + b
sonuc = toplama(5, 6)
print(sonuc)
```

    11

