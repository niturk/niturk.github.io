+++
title = "Modüller ve İmport"
date = "2023-01-27T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


Bazen bir dosyada çok fazla kod yazdığımızda aradığımız şeyi bulmakta ve yönetmekte zorlanırız.
Bu durumlarda kodumuzu farklı dosyalara ayırarak daha düzenli bir şekilde yazabiliriz. Bu dosyalara modüller denir.

# Built-in Objeler ve Fonksiyonlar

Python'da hazır olarak gelen objeler ve fonksiyonlar vardır. Bu objeler ve fonksiyonlar `built-in` modülü içerisinde yer alır. Bu modülü import etmeden kullanabiliriz.

`bool`, `int`, `float`, `str`, `list`, `tuple`, `dict`, `set`, `range`, `len`, `print`, `input`, `type`, `id`, `dir`, `help` gibi objeler ve fonksiyonlar `built-in` modülü içerisinde yer alır.

Bu fonksiyonların listesine [buradan](https://docs.python.org/3/library/functions.html) ulaşabilirsiniz.

&nbsp;

# Standart Kütüphaneler

Python'da hazır olarak gelen modüller vardır. Bu modüller `standart library` içerisinde yer alır. Bu modüllerin listesine [buradan](https://docs.python.org/3/library/index.html) ulaşabilirsiniz.

Bu modülleri kullanabilmek için import etmemiz gerekmektedir.

```python
import math
math.sqrt(9)
```

> Tüm modüller otomatik import edilmez çünkü bellekte yer kaplarlar. Bu yüzden sadece kullanacağımız modülleri import ederiz.

&nbsp;

## İmport Ederken Etiket Kullanımı

İmport etmek istediğimiz modül ismi uzun olabilir veya farklı bir isimde kullanmak istersek etiket kullanabiliriz.

```python
import math as m
m.sqrt(9)
```
&nbsp;

# Üçüncü Parti Kütüphaneler

Standart kütüphaneler bize bazen yeterli gelmemektedir. Standart kütüphaneler olabildiğince genel olmak zorundadır. Bu yüzden bazen daha özel amaçlar için üçüncü parti kütüphaneler kullanmak gerekebilir.
Bu kütüphaneleri önce kurar sonra import ederiz.

Bazı popüler üçüncü parti kütüphaneler:
- [numpy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [tensorflow](https://www.tensorflow.org/)
- [opencv](https://opencv.org/)

Bu kütüphaneler PYPI (Python Package Index) üzerinden indirilebilir. PYPI'ya [buradan](https://pypi.org/) ulaşabilirsiniz. Bu paketleri indirmek için `pip` kullanılır.

> Üçüncü parti kütüphane seçimi çok önemlidir. Bir kütüphaneyi kullanmaya karar verdiğimizde kontrol etmemiz gereken bazı adımlar vardır;
> - Araştırma yapılarak kullanıcıların kütüphane hakkındaki görüşleri öğrenilmelidir.
> - Geliştirilmeye devam edilip edilmediğine bakılmalıdır.
> - Dökümantasyonunun iyi olup olmadığına bakılmalıdır.
> - Kullanıcı kitlesinin geniş olup olmadığına bakılmalıdır.

> Her zaman üçüncü parti kütüphanelere ihtiyaç duymayız. Eğer yukarıdaki adımlarda kütüphane bizi tatmin etmiyorsa kendimiz yazmalıyız. Aksi halde bizim için acı dolu bir yolculuk başlayacaktır.

# Modül İçerisinden Fonksiyon ve Değişkenlerin İmport Edilmesi

Modül içerisindeki fonksiyon ve değişkenlerin import edilmesi için `from` anahtar kelimesi kullanılır.

```python
from math import sqrt
sqrt(9)
```
```python
from math import sqrt, pi
sqrt(9)
print(pi)
```
