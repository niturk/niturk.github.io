+++
title = "Temel Python'a Giriş - 1"
date = "2022-12-28T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


Bu bölümde temel python kod eğitimine başlıyoruz.  

Bölüm kapsamında odaklanacağımız konular;
- Temel python veri tipleri `int`, `float`, `boolean`
- Nesne kavramına giriş
- Temel operatörler ile işlemler `+`, `-`, `*`, `/`, `**`, `%`, `//`
- Temel karşılaştırma operatörleri `==`, `!=`, `>`, `<`, `>=`, `<=`
- Temel mantıksal operatörler `and`, `or`, `not`
- Temel operatör öncelikleri

> Bu eğitim mühendislik öğrencileri için hazırlanmaktadır. Temel seviyede bilgisayar bilimi bilgisi gerekmektedir!

&nbsp;

## Temel Veri Tipleri

Yazılım dillerinde verilerin her zaman bir tipi olmak zorundadır. Bu gercek hayatta da bu şekildedir.
- Ahmet bir kişidir.
- Fırın bir mağazadır.
- Banka hesabım bir sayıdır.
- Bir kitabın sayfa sayısı bir sayıdır.
- `ders.pdf` dosyası bir pdf dosyasıdır.
- Durum yapıları bir veri tipidir. `True`, `False` ile ifade edilir vardır yada yoktur.
    - Pythonda biz bunlara `boolean` veri tipi diyoruz.
    - İki değer alabiliyor `True` ve `False`.
    - `Ben artık bir python geliştiricisiyim` ifadesi `True` değerini alır. Doğru çünkü artık bir python geliştiricisisiniz.
    - `Köpeğim miyavlıyor` ifadesi `False` değerini alır. Yanlış çünkü köpekler miyavlamaz.

bu örnekleri çoğaltmak mümkün.

&nbsp;


### Integer (Tam Sayılar) Veri Tipi

- `int` veri tipi tam sayıları ifade eder. `0`, `1`, `100`, `-100` gibi değerler alır.
- Pythonda `int` veri tipi için herhangi bir büyüklük limiti yoktur. Limit sahip olduğunuz bellektir.
- Pythonda sayıları direk tanımlayabilirsiniz, `100`, `-100` veya matematik işlemi sonucu elde edilebilir. `1 + 1`, `1 * 2` gibi.
- Okunabilirliği artırmak için sayıları `_` ile ayırabiliriz. `100_000_000`, `1_000_000_000` gibi.


```python
# Int örnek 
a = 5      # int tanımlaması
b = 3      # int tanımlaması
c = a + b  # toplama işlemi
print(c)   # ekrana yazdırma
```

    8


&nbsp;
### Float (Ondalıklı Sayılar) Veri Tipi

- `float` veri tipi ondalıklı sayıları ifade eder. `3.14`, `-1.3` gibi değerler alır.
- `int` veri tipiyle hemen hemen tüm özellikleri aynıdır. Ancak `float` ondalıklı sayılar oluşturmanıza olanak verir.
- Okunabilirliği artırmak için sayıları `_` ile ayırabiliriz. `1_234.567_890` gibi.
- Ancak dikkat edilmesi gerekir, sayılar için virgülden sonrası yazılırsa veriniz `float` olur. 
    - `1` -> `int` veri tipidir
    - `1.0` -> `float` veri tipidir 
- Float her zaman tam olarak ifade edilemez. Bu yüzden bazı sayılar `float` olarak ifade edilemez. `0.1` gibi. Bunun sebebi bilgisayarların ikili sayı sistemi kullanmasıdır.
    - `0.1 + 0.1 + 0.1 == 0.3` ifadesinin sonucu bu sebeple `false` dönecektir.
    - `float` veri tipi için bu problem tüm yazılım dillerinde mevcuttur.
    - Eğer ondalıklı sayılarla işlem yapacaksanız örneğin bir banka uygulaması yazacaksanız kullanmanız gereken veri tipi `decimal` veri tipidir.





```python
# Format fonksiyonu ile 0.1 sayısını 25 basamaklı olarak yazdırma
format(0.1, '.25f')
```




    '0.1000000000000000055511151'



Gördüğünüz gibi 0.1 değerinin ikili sayı sisteminde ifade etmek için sonsuz sayıda basamak gerekmektedir. Hiçbir zaman tam olarak 0.1 i ifade edemeyiz. Ancak yakınsayabiliyoruz!

![Float Representation](float_representation.png)


```python
# Format fonksiyonu ile 0.125 sayısını 25 basamaklı olarak yazdırma
format(0.125, '.25f') # Ondalık gösterimi 1/8 dir.  
                      # Tam olarak bölünebilen sayılar ondalık gösterimde 
                      # sorun çıkarmaz.
```




    '0.1250000000000000000000000'



> Dolayısıyla `float` sayılarla işlem yaparken sonuçlar hatalı olabilmektedir. Bu yüzden `float` veri tipi kullanırken dikkatli olunmalıdır.

&nbsp;


```python
# 0.1 + 0.1 + 0.1 == 0.3 ifadesi bize False döndürür. Ancak beklenen sonuç True olmalıdır.
0.1 + 0.1 + 0.1 == 0.3 # False
```




    False



&nbsp;


```python
# Format fonksiyonu ile 0.1+0.1+0.1 sayısını ve 0.3 sayısını 25 basamaklı olarak yazdırma
print(format(0.1 + 0.1 + 0.1, '.25f')) # 0.3000000000000000444089210
print(format(0.3, '.25f')) # 0.2999999999999999888977698
```

    0.3000000000000000444089210
    0.2999999999999999888977698


&nbsp;
## Nesne Kavramına Giriş

Nesne kavramı python için çok önemlidir. Diğer dillerden farklı olarak pythonda tüm veri tipleri nesnelerdir. Bu nedenle pythonda her şey bir nesnedir.

Nesnelerin iki özelliği bulunur;
1. Durum (State) -> Nesnenin durumunu ifade eder. Örneğin bir kitabın sayfa sayısı, bir kişinin adı, bir banka hesabının bakiyesi gibi.
2. Metodlar (Fonksiyonlar) -> Nesnenin yapabileceği işlemleri ifade eder. Örneğin bir kitabın sayfa sayısını arttırma, bir kişinin adını değiştirme, bir banka hesabının bakiyesini arttırma gibi.

> Nesnelerin durumunu ve metodlarını bir arada tutmak için `kapsülleme(encapsulation)` kullanılır.

Nesneleri yazılım alanında gerçek dünya nesnelerini tanımlamak için kullanırız. Siz bir inşaat uygulaması geliştirmek istiyorsanız. Temel nesneler yeterli olmayacaktır. Uygulamaya özgü nesneler oluşturmanız gerekiyor. Örneğin `Bina`, `Kat`, `Daire`, `Oda`, `Duvar`, `Pencere`, `Kapı` gibi. Bu nesnelerin durumları ve metodları olmalıdır. Örneğin `Bina` nesnesinin durumu `kat_sayisi`, `katlar`, `bina_adi` gibi. `Bina` nesnesinin metodları ise `kat_ekle`, `kat_sil`, `bina_adi_degistir` gibi.

&nbsp;
### Integer Bir Nesnedir

`int` bir nesnedir. Sayıları tutar ama python için sayılarda bir nesnedir. Sayının değeri `durum` belirtir.
Pythonda iki sayıyı topladığınızda ise metod çağrısı olur ve toplama işlemi gerçekleşir.  
Python 10 + 100 için `__add__` metodunu çağrır ve 110 değerini döndürür.


```python
# bir örnek yapalım
(10).__add__(100) # 10 + 100 için aslında `__add__` metodunu çağırılır.
```




    110



&nbsp;
### Float Bir Nesnedir

Aynı şekilde `float` da bir nesnedir. Sayının değeri `durum` belirtir. Metodlarda `int` veri tipiyle aynıdır.
Bazı ek metodlar vardır. Örneğin `float` bir sayıyı matematiksel olarak kesirli olarak yazdırabiliriz. Bunun için `as_integer_ratio` metodunu kullanırız.


```python
(0.125).as_integer_ratio() # 1/8 sayısının kesirli gösterimi
```




    (1, 8)



&nbsp;
### Python'da Her Şey Bir Nesnedir

> **Pythonda her şey bir nesnedir!** Bu cümleyi eğitim boyunca birkaç kez kullanacağız unutmayalım :)

Nesnelerin durum ve metodları vardı biz bunlara nitelik(`attributes`) diyoruz. Peki bu niteliklere nasıl ulaşacağız.
Sayıların sadece bir durumu vardı, `int` için sadece sayı değeri. Ancak gerçek dünya örneklerinde birden çok durum olabiliyor.
Bir araba nesnesi için durumları `marka`, `model`, `yıl`, `renk` gibi. Bu durumları `nitelik` olarak tanımlarız. Bu niteliklere erişmek için `.` operatörünü kullanırız.  
Örneğin `araba.marka` diyerek arabanın markasını alabiliriz.

Metodlar için de aynı şekilde `.` operatörünü kullanırız.  
Örneğin `araba.korna_cal()` diyerek arabanın markasını değiştirebiliriz. Dikkat edilmesi gereken nokta burada bir çağrı(`call`) yapmak için `()` kullanıyoruz. Eğer kullanmazsanız metod çalışmaz.

&nbsp;

### Değişebilirlik(Mutability) ve Değişmezlik(Immutability) Kuramı

Python'da nesnelerin değişebilirlik durumunu `mutability` diyoruz. Değişmezlik durumunu ise `immutability` diyoruz. Bu iki kavramı anlamak python kodu yazarken hata yapmamak için çok önemlidir. Bir nesnenin bir niteliği değişebilir ise `mutable` bir nesnedir. Değişmez ise `immutable` bir nesnedir.

`İmmutable` veri tipleri:
- `int`
- `float`
- `bool`
- `str`
- ...

`Mutable` veri tipleri:
- `list`
- `dict`
- `set`
- ...

&nbsp;
Değiştirilemez demek aslında diğer yazılım dillerindeki `const` yapısı ile karıştırılmamalıdır. Python'da `const` yapısı yoktur. Ancak `immutable` veri tipleri değiştirilemez. Bu veri tipleri üzerinde değişiklik yapmak istediğinizde yeni bir nesne oluşturulur.

> Bu konu ilerleyen derslerde daha ayrıntılı olarak ele alınacaktır.
