+++
title = "Sekans Veri Tipleri - 1"
date = "2023-01-01T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


Sekanslar sıralı obje koleksiyonlarıdır. Birden fazla birbiri ile bağlantılı verileri sıralı olarak tutmaya ihtiyaç duyarız. Bu verilerin sıralanmaya ihtiyacı vardır. Bu sıraya `index` adı verilir. Pythonda index `0` dan sayılmaya başlar.

Bu durumda `n` elemanlı bir sekans için;

- ilk eleman `0` indexine sahiptir.
- ikinci eleman `1` indexine sahiptir.
- son eleman `n-1` indexine sahiptir.

Bu sekans veri tipleri homojen veya heterojen yapıda olabilir. Homojen yapıda olması için aynı veri tiplerinden bir sekans oluşturulmalıdır. Heterojen yapıda olması için farklı veri tiplerinden bir sekans oluşturulmalıdır.

Sekans veri tipleri;
- Lists (Listeler) -> değişebilir heterojen sekans veri tipi
- Tuples (Demetler) -> değişmez heterojen sekans veri tipi
- Strings (Stringler) -> değişmez homojen sekans veri tipi

&nbsp;

## Listeler (Lists)

- Listeleri veri tutan bir konteyner gibi düşünebilirsiniz.
- Listeler içerisinde farklı veri tipleri barındırabilir.
- Listeler içerisindeki verileri değiştirebiliriz.
- Listeler içerisindeki verileri sıralı olarak tutarlar. Bu yüzden indexleri vardır.
- Listeleri `[]` parantezlerini kullanarak oluşturabiliriz.
- Listeleri `list()` fonksiyonu ile de oluşturabiliriz.
- Listeler veri tipi bir objedir.
- Listelerin metodları vardır. Bu metodları kullanarak listeler üzerinde işlemler yapabiliriz.



```python
# Listeleri [] parantezlerini kullanarak oluşturabiliriz.
liste = [1, 2, 3, 4, 5]
print(liste)
print("Type:", type(liste))
```

    [1, 2, 3, 4, 5]
    Type: <class 'list'>



```python
# Listeler farklı tipte elemanlarda tutabilir.
liste = [1, 2, 3.14, True]
print(liste)
```

    [1, 2, 3.14, True]



```python
# Listeler içerisinde bile liste olabilir.
liste = [1, 2, 3, [4, 5, 6]]
print(liste)
```

    [1, 2, 3, [4, 5, 6]]



```python
# Listedeki elemanlara index ile ulaşabiliriz.
liste = [1, 2, 3, 4, 5]
print(liste[0])
print(liste[1])
```

    1
    2



```python
# Index negatif değerler alabilir. Bu durumda sondan başlanır.
liste = [1, 2, 3, 4, 5]
print(liste[-1])
print(liste[-2])
```

    5
    4


> Listedeki bir elemana ulaşırken eleman sayısından daha büyük bir index kullanırsak `IndexError` hatası alırız.


```python
# `len` fonksiyonunu kullanarak listedeki eleman sayısına ulaşabiliriz.
liste = [1, 2, 3, 4, 5]
print(len(liste))
```

    5


### Boş Liste Oluşturmak

Bazen örnek kodları incelerken boş listelerin oluşturulduğunu göreceğiz. Bu boş listeleri `[]` ile oluşturabiliriz. Ama `list()` fonksiyonunu kullanarak da boş bir liste oluşturabiliriz. Bunun sebebi daha sonra bu listeye eleman ekleneceğidir. Doğru bir kullanım şeklidir. Bu listenin eleman sayısı `0` olacaktır.

### Liste Elemanlarını Değiştirmek

Bir önceki konuda liste elemanlarına index numaralarından ulaşabildiğimizden bahsetmiştik. Aynı şekilde bu elemanları değiştirebiliriz.


```python
# Liste elemanlarını değiştirebiliriz.
liste = [1, 2, 3, 4, 5]
liste[0] = 10
print(liste)
```

    [10, 2, 3, 4, 5]


&nbsp;
## Demetler (Tuples)

Tuple `list` veri tipine çok benzer.

- Tuple bir konteynerdır.
- Tuple içerisinde farklı veri tipleri barındırabilir.
- Tuple içerisindeki verileri değiştiremezsiniz.
- Tuple içerisindeki verileri sıralı olarak tutarlar. Bu yüzden indexleri vardır.
- Tuple `()` parantezlerini kullanarak oluşturabiliriz.
- Tuple `tuple()` fonksiyonu ile de oluşturabiliriz.
- Tuple veri tipi bir objedir.
- Tuple, listelerden farklı olarak bir defa yaratılır ve değiştirilemez.



```python
# Tuple'ları () parantezlerini kullanarak oluşturabiliriz.
t = (1, 2, 3, 4, 5)
print(t)
print("Type:", type(t))
```

    (1, 2, 3, 4, 5)
    Type: <class 'tuple'>



```python
# Tuple olustururken parantez kullanmak zorunda değiliz. Sadece virgül kullanarak da oluşturabiliriz.
t = 1, 2, 3, 4, 5
print(t)
print("Type:", type(t))
```

    (1, 2, 3, 4, 5)
    Type: <class 'tuple'>



```python
# Tuple'lar farklı tipte elemanlarda tutabilir.
t = (1, 2, 3.14, True)
print(t)
```

    (1, 2, 3.14, True)



```python
# Tuple'lar içerisinde bile tuple olabilir.
t = (1, 2, 3, (4, 5, 6))
print(t)
```

    (1, 2, 3, (4, 5, 6))



```python
# Tuple'ların elemanlarına index ile ulaşabiliriz.
t = (1, 2, 3, 4, 5)
print(t[0])
print(t[1])
```

    1
    2



```python
# `len` fonksiyonunu kullanarak tuple'ların eleman sayısına ulaşabiliriz.
t = (1, 2, 3, 4, 5)
print(len(t))
```

    5


> Tuple içerisindeki bir elemana ulaşırken eleman sayısından daha büyük bir index kullanırsak `IndexError` hatası alırız.

> Tuple içerisindeki bir elemanı değiştirmeye çalışırsak `TypeError` hatası alırız. Listeler gibi değiştirilemezler yeniden oluşturmak gereklidir.  
`t[0] = 1` kodu çalıştırıldığında `TypeError` hatası alırız.


```python
# Ancak tuple içerisinde list varsa list değiştirilebilir olduğu için listin elemanları değiştirilebilir.
t = (1, 2, 3, [4, 5, 6])
t[3][0] = 10
print(t)
```

    (1, 2, 3, [10, 5, 6])


> Boş bir tuple oluşturulması pek kullanışlı değildir. Çünkü tuple içerisindeki elemanları değiştiremeyeceğimizden dolayı boş bir tuple oluşturmak pek mantıklı değildir.


```python
# Bir listeyi tuple'a çevirebiliriz.
liste = [1, 2, 3, 4, 5]
t = tuple(liste)
print(t)
```

    (1, 2, 3, 4, 5)



```python
# Aynı şekilde bir tupleyi bir listeye çevirebiliriz.
t = (1, 2, 3, 4, 5)
liste = list(t)
print(liste)
```

    [1, 2, 3, 4, 5]


&nbsp;
## Stringler (Strings)

- Stringler karakter dizileridir.
- Stringler içerisinde sadece karakterler barındırabilir.
- Stringler içerisindeki karakterleri değiştiremezsiniz.
- Stringler içerisindeki karakterleri sıralı olarak tutarlar. Bu yüzden indexleri vardır.
- Stringler `''` veya `""` tırnak işaretleri kullanarak oluşturabiliriz.
- Stringler `str()` fonksiyonu ile de oluşturabiliriz.
- String veri tipi bir objedir.


```python
# Stringleri '' veya "" parantezlerini kullanarak oluşturabiliriz.
s = "Python"
print(s)
```

    Python


> Kodunuzun özenli olması açısından her zaman aynı tırnak işaretlerini kullanmalısınız. Örneğin `''` tırnak işaretlerini kullanıyorsanız tüm stringleri `''` tırnak işaretleri ile oluşturmalısınız. Aksi takdirde kodunuzun okunabilirliği azalacaktır.  
Boş bir string oluşturmak için `''` veya `""` kullanabilirsiniz.


```python
# String içerisinde tek tırnak kullanmak istiyorsanız çift tırnak ile string oluşturabilirsiniz.
s = "Python'da stringler çok kullanışlıdır."
print(s)
```

    Python'da stringler çok kullanışlıdır.



```python
# Aynı şeyi kaçış karakteri ile de yapabiliriz. Bu durumda stringi oluşturmak için tek tırnak kullanabiliriz.
s = 'Python\'da stringler çok kullanışlıdır.'
print(s)
```

    Python'da stringler çok kullanışlıdır.



```python
# String eleman sayısına `len` fonksiyonu ile ulaşabiliriz.
s = "Python"
print(len(s))
```

    6



```python
# Stringlerdeki karakterlere index ile ulaşabiliriz.
s = "Python"
print(s[0])
print(s[1])
```

    P
    y


> Listeler ve demetlerde olduğu gibi stringlerde de bir elemana ulaşırken eleman sayısından daha büyük bir index kullanırsak `IndexError` hatası alırız.


```python
# Stringleri liste veya tuple'a çevirebiliriz.
s = "Python"
liste = list(s)
print(liste)
```

    ['P', 'y', 't', 'h', 'o', 'n']



```python
# String oluştururken bir karakteri tekrarlamak için * operatörünü kullanabiliriz.
s = "Python " * 5
print(s)
```

    Python Python Python Python Python 

