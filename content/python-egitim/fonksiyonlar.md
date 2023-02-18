+++
title = "Fonksiyonlar"
date = "2023-01-25T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


Fonksiyonlar en işlevsel yapılardan biridir. Şimdiye kadar kullandığımız `print`, `type`, `len` gibi yapıların tamamı fonksiyondu.
Aynı şekilde biz kendi fonksiyonlarımızıda yaratabiliriz. Fonksiyonlara, kod tekrarını önlemek ve kompleks olan kodları parçalara bölmek için ihtiyacımız vardır.  
Fonksiyon çağrıları yaparken argüman ve parametreler kullanırız. Teknik olarak ikiside aynı şeydir ve sık sık birbirine karıştırılır.
- Fonksiyon yaratırken parametreleri kullanırız.
- Fonksiyon çağrıları yaparken argümanları kullanırız.

> Fonksiyonlar her python nesnesi olduğu gibi bir nesnedir.
Fonksiyonların durum, kod ve parametreleri vardır. Ayrıca çağrı yapılabilen bir nesnedir.

&nbsp;

## Çağrılabilen Nesneler

Bir nesnenin sonuna `()` parantez eklersek onu çağırmış oluruz. Fonksiyonlar bu nesnelere en iyi örneklerden biridir.
```python
print("Merhaba")
```
Bu kodu çalıştırdığımızda `print` fonksiyonunu `Merhaba` argümanı ile çağırmış oluyoruz ve fonksiyon görevini yerine getirerek ekrana `Merhaba` yazdırıyor.

&nbsp;

## Özel Fonksiyonlar

Fonksiyonlar `def` özel kelimesi ile yaratılırlar. `def` kelimesinin anlamı `define` yani tanımlamak anlamına gelir.
Fonksiyon yaratılırken bir isim verilir. Bu isim fonksiyonun çağrılmasında kullanılır. Fonksiyonun içindeki kodlar fonksiyon çağrıldığında çalıştırılır.
```python
def fonksiyon_adi():
    print("Merhaba")
```

&nbsp;  
Fonksiyonlar bir değer döndürmek zorundadır. Fonksiyonlar bir değer döndürürse bu değer `return` anahtar kelimesi ile döndürülür.
`return` kullanılmazsa fonksiyon varsayılan olarak `None` değerini döndürür.

```python
def fonksiyon_adi():
    return "Merhaba"
```

&nbsp;  
Fonksiyon adı fonksiyona sembol olarak atanır. a = 5 dediğimizde `a` değişkenine int 5 değerinin atandığı gibi bir fonksiyon oluştuğunda `fonksiyon_adi` değişkenine fonksiyonun adresi atanır.


```python
def bes_ata():
    return 5
a = bes_ata()
print(a)
```

    5


&nbsp;

Her fonksiyon çağrısında bir sözlük yaratılır. Bu sözlük fonksiyonun parametrelerini ve argümanlarını tutar. Bu sözlüğe fonksiyon içerisinden `locals()` fonksiyonu ile erişebiliriz.


```python
def toplama(a, b):
    toplam = a + b
    sozluk = locals()
    print(sozluk)
toplama(5, 6)
```

    {'a': 5, 'b': 6, 'toplam': 11}


> Bu sözlük fonksiyon sonlandığında silinir.
&nbsp;

## Parametreli Fonksiyonlar

Fonksiyonlar parametre alarak çalışabilir ve bu parametrelere göre çalışma şeklini değiştirebilir. Unutmamamız gereken bu parametrelerin sıralı olduğudur. Tanımlandığı sırayla değer alırlar.


```python
def toplama(a, b):
    return a + b

sonuc = toplama(5, 6)
print(sonuc)
```

    11


> Fonksiyon parametrelerinin varsayılan değerleri belirtilmezse fonksiyon çağrısı yapılırken bu parametreler verilmelidir. Aksi halde hata alırız.

&nbsp;

### Dinamik Sıralı Parametreler | `*args`

Fonksiyon parametreleri her zaman sabit olmak zorunda değildir. Bazen farklı sayıda parametre almak isteyebiliyoruz. Örneğin tüm parametreleri toplayan bir fonksiyon yazmak istesek. Bu durumda parametre sayısını bilmemiz mümkün değildir. Eğer fonksiyon parametrelerine `*args` yıldız koyarsak sınırsız sayıda parametre alabiliriz.

- `*args` parametrelerini bir demet(tuple) olarak alır.
- `args` parametre ismi zorunlu değildir. Ancak genelde `args` kullanılır.


```python
# Fonksiyon parametresi olarak *
def toplama(a, *args):
    return a + sum(args)
sonuc = toplama(5, 6, 7, 8, 9)
print(sonuc)
```

    35


> `*args` yerine aslında liste kullanabilirdik. Fonksiyonumuz parametre olarak liste alırsa istediğimiz kadar eleman gönderebiliriz. Ancak `*args` kullanmak daha pratik ve okunaklıdır.


```python
# Fonksiyon parametresi olarak *
def fonksiyon(a, *args, c):
    print(f'a={a} | args={args} | c={c}')
fonksiyon(5, 6, 7, 8, 9, c=10)
```

    a=5 | args=(6, 7, 8, 9) | c=10


&nbsp;
### Fonksiyon Parametrelerinde Varsayılan Değerler

Fonksiyon parametrelerine varsayılan değerler atayabiliriz. Bu durumda fonksiyon çağrısı yaparken parametreyi belirtmezsek varsayılan değer kullanılır.


```python
# Fonksiyonlarda varsayılan değerler
def yaz(msg="Merhaba"):
    print(msg)
yaz()
yaz("Python")
```

    Merhaba
    Python


> Fonksiyon parametrelerinde siralama önemlidir. Varsayılanı olan parametreden sonra normal parametre kullanamazsınız. Varsayılanı olan parametreler, diğer parametrelerden sonra yazılmalıdır.  
Örneğin `def func(a, b=1, c=2)` şeklinde tanımlanmış bir fonksiyon var.  
Bu fonksiyonu `func(5, 6, 7)` şeklinde çağırdığımızda `a=5, b=6, c=7` olur.  
Ancak `func(5, c=6)` şeklinde çağırdığımızda `a=5, b=1, c=6` olur.

&nbsp;


```python
def function(a, b=5, *args):
    return  f'a={a}, b={b}, args={args}'
print(f'f(1)        ->  {function(1)}')
print(f'f(1, 2)     ->  {function(1, 2)}')
print(f'f(1, 2, 3)  ->  {function(1, 2, 3)}')
```

    f(1)        ->  a=1, b=5, args=()
    f(1, 2)     ->  a=1, b=2, args=()
    f(1, 2, 3)  ->  a=1, b=2, args=(3,)


&nbsp;
### Dinamik İsimli Parametreler | `**kwargs`

Fonksiyonlarda isimli dinamik parametreleri almak için `**kwargs` kullanılır. Bu parametreler bir sözlük(dict) olarak alınır. `kwargs` parametre ismi zorunlu değildir. Ancak genelde `kwargs` kullanılır. Bu parametrelerin tamamı normal sıralı parametrelerden sonra yazılmalıdır.

Bir parametreyi isimli olarak göndermeye zorlamak için `*` kullanılır.


```python
# a parametresi anahtar=değer şeklinde gönderilmek zorundadir.
def fonksiyon(a, *, b):
    print(f'a={a} | b={b}')

fonksiyon(5, b=10)
```

    a=5 | b=10


Zorunlu isim parametrelerine varsayılan değer verilebilir. Bu durumda isimli parametre gönderilmezse varsayılan değer kullanılır.


```python
# b varsayılan değer olarak tanımlanabilir.
def fonksiyon(a, *, b=10):
    print(f'a={a} | b={b}')

fonksiyon(5) # Sıralı parametre verilirse yine hata verir.s
```

    a=5 | b=10



```python
# Fonksiyon parametrelerinde **kwargs tüm parametreler isimli olarak gönderilmek zorundadır.
def toplama(**kwargs):
    return sum(kwargs.values())

sonuc = toplama(a=5, b=6, c=7)
print(sonuc)
```

    18


&nbsp;

Özetlemek gerekirse;
- `*args` sıralı dinamik parametreler için kullanılır
- `**kwargs` isimli dinamik parametreler için kullanılır



```python
def fonksiyon(a, b, *args, c, d=7, **kwargs):
    print(f'a={a} | b={b} | args={args} | c={c} | d={d} | kwargs={kwargs}')
fonksiyon(1, 2, 3, 4, 5, c=6, e=8, f=9)
```

    a=1 | b=2 | args=(3, 4, 5) | c=6 | d=7 | kwargs={'e': 8, 'f': 9}


- `a, b` zorunlu sıralı parametredir
- `args` sıralı olarak verilen tüm parametreleri alır
- `c` zorunlu isimli parametredir (c=değer) şeklinde yazılmalıdır
- `d` opsiyonel isimli parametredir. Varsayılan değeri 7'dir
- `kwargs` isimli olarak verilen tüm parametreleri alır

&nbsp;

## Lambda Fonksiyonu

Lambda fonksiyonları aslında bildiğimiz fonksiyonlardır.
- `def` anahtar kelimesi yerine `lambda` kullanılır.
- `lambda` fonksiyonları tek satırlıktır ve fonksiyon objesi döndürürler.
- Python `lambda` fonksiyonları için değişken atamaz sadece fonksiyonu oluşturur. Biz değişkene atamak istediğimizde `lambda` fonksiyonunu bir değişkene atarız.
- Anonim fonksiyonlar olarak adlandırılırlar.

&nbsp;

### Lambdanın Yapısı

```python
lambda parametre1, parametre2, ... : işlem
```

&nbsp;


```python
# Örnek Lambda Fonksiyonu
msg = lambda: "Merhaba"
print(msg())
```

    Merhaba



```python
# Örnek Lambda Toplama Fonksiyonu
toplama = lambda a, b: a + b
sonuc = toplama(5, 6)
print(sonuc)
```

    11

