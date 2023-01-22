+++
title = "Döngüler"
date = "2023-01-05T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


Döngüler en çok kullanılan yapılardan biridir. Döngüleri bir kodu tekrar tekrar yazmadan tekrar etmek için kullanırız.
İki çeşit döngü vardır.
- Sonlu döngüler, belirli bir sayıda tekrar etmek için kullanılır.
- Sonsuz döngüler, bir koşul sağlandığı sürece tekrar etmek için kullanılır. Dolayısıyla burada karar yapısıyla birlikte bir kullanım var.

Bu iki çeşit için pythonda deterministik olanlar için `for` döngüsünü, deterministik olmayanlar içinde `while` döngüsünü kullanırız.

## Range Fonksiyonu

range tekrarlanabilir bir objedir. Talep ettikçe size bir sayı verir.

- range objesi bir sayıdan başlar ve bir sayıya kadar gider.
- tüm liste bellekte tutulmaz. Talep ettikçe size bir sayı üretir.
- bellek verimli kullanılır.
- range objesi sonlu bir objedir. sonsuz bir obje değildir.

### range() Fonksiyonunun Kullanımı

Range fonksiyonu 3 şekilde kullanılır. Kullanımı sekans veri tiplerindeki slice işlemine benzerdir.

- range(10) 0'dan 10'a kadar sayılar üretir. Tek parametre ile kullanıldığında sadece bitiş değeri verilir.
- range(1,10) 1'den 10'a kadar sayılar üretir. İki parametre ile kullanıldığında başlangıç ve bitiş değeri verilir.
- range(1,10,2) 1'den 10'a kadar 2'şer 2'şer sayılar üretir. Üç parametre ile kullanıldığında başlangıç, bitiş ve artış değeri verilir.


```python
# Bir range oluşturalım ve printleyelim.
r = range(10)
print(r)
```

    range(0, 10)


> range fonksiyonunun içeriği yazılmadı çünkü henüz ortada bir sayı listesi yok sayıların tek tek üretilmesi gerekiyordu. Bellek bu şekilde daha verimli kullanılır. Sayılar sadece gerektiğinde üretilir.


```python
# Sayıları kullanmak için range objesini tuple veya listeye dönüştürmeliyiz.
r = range(10)
print(list(r))
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


&nbsp;
## For Döngüsü

For döngüsü tekrarlanabilir sonlu objeler üzerinde dönen bir döngüdür. Bu objelerin içindeki elemanları tek tek dolaşır. Her bir eleman için `for` içerisine yazılan kod bloğu çalışır. Obje içerisindeki tüm elemanlar bittiğinde for döngüsünden çıkılır ve normal kod akışına devam edilir.


```python
# For döngüsü örneği
for x in [1, 2]:
    print(x)
print('bitti.')
```

    1
    2
    bitti.


> for döngüsü içerisindeki kod bloğu bir tab kadar girintili olmalıdır. Pythonda daha önce gördüğümüz karar yapılarından buna artık alışmış olmanız gerekiyor.  
Yukarıdaki `for` döngümüzde x liste içerisinde dönerek önce `1` daha sonra `2` değerini alıyor ve kod bloğu buna göre çalıştırılıyor, bu sebeple ekranda `1` ve `2` değerleri yazılıyor. Döngü bittiğinde döngüden çıkışıyor ve ekrana `bitti` yazılıyor.


```python
# Range fonksiyonunu kullanarak for döngüsü örneği
for x in range(4, 6):
    alan = x * x
    print(alan)
print('bitti.')
```

    16
    25
    bitti.


> Tüm python yapıları iç içe kullanılabilir bir döngü içerisine döngü, karar yapıları veya tam tersi istediğiniz kadar sınırsız bir şekilde 1 tab girinti yaparak tüm yapıları kullanabilirsiniz. Tecrübeli kod geliştiricileri, 3 ten fazla girinti yapıyorsanız muhtemelen kötü bir kod yazıyorsunuz yorumunu yapmaktadır.

### Enumerate Fonksiyonu Kullanımı

`enumerate` fonksiyonu bir döngü içerisinde döngü sayacını kullanmak için kullanılır. Bu sayede döngü içerisindeki her bir elemanın kaçıncı eleman olduğunu öğrenebiliriz.

Bir liste içerisinde negatif olan sayıları `0` yapmak istediğimizi düşünelim. Burada döngüleri kullanmamız gerekiyor çünkü eleman döngüsüz yapsaydık her eleman için manuel bir if kodu yazmamız gerekirdi. Bulduğumuz elemanı düzeltmek içinde index numarasına ihtiyacımız var `enumerate` fonksiyonu burada çok işimize yarayacak gibi duruyor.


```python
# enumerate ile for döngüsü örneği
data = [1, -2, 3, -4, 5]
for index, eleman in enumerate(data):
    if eleman < 0:
        data[index] = 0
print(data)
```

    [1, 0, 3, 0, 5]


&nbsp;
## While Döngüsü

While döngüsü bir koşul sağlandığı sürece dönen bir döngüdür. Koşul sağlandığı sürece döngü içerisindeki kod bloğu çalışır. Koşul sağlanmazsa döngüden çıkılır ve normal kod akışına devam edilir.

> Koşul sağlandığı sürece döngü sonsuza kadar çalışır. Sonsuz döngü oluşturabilme riski bulunmaktadır. Bu yüzden while döngüsü kullanırken dikkatli olmak gerekir.


```python
# While döngüsü örneği
x = 1
while x < 3:
    print(x)
    x += 1
print('bitti.')
```

    1
    2
    bitti.


&nbsp;
## Continue,Break ve Else Anahtar Kelimeleri Kullanımı

### Continue Anahtar Kelimesi

Bazen döngüde gelen elemana göre veya bir duruma göre kod bloğunu çalıştırmak istemeyiz ama döngünün bir sonraki elemana geçmesini isteriz. Bu durumda `continue` anahtar kelimesini kullanırız.

Örneğin sadece tek basamaklı sayıları yazdıran bir kod yazalım. Çift basamaklılar için `continue` anahtar kelimesini kullanacağız.


```python
# Sadece tek basamaklı sayıları yazdıralım.
sayilar = [1, 20, 3, 40, 55, 60, 7, 80, 99, 100]
for sayi in sayilar:
    if sayi > 9:
        continue
    print(sayi)
print('bitti.')
```

    1
    3
    7
    bitti.



```python
# continue çok kullanılmaz. Çünkü kodun okunabilirliğini azaltır.
# Bu örnekte continue kullanılmadan da aynı sonucu elde edebiliriz.
sayilar = [1, 20, 3, 40, 55, 60, 7, 80, 99, 100]
for sayi in sayilar:
    if sayi < 10:
        print(sayi)
print('bitti.')
```

    1
    3
    7
    bitti.


> Zorunda kalmadıkça kullanmamak gerekir. Çünkü kodun okunabilirliğini azaltır.

### Break Anahtar Kelimesi

Bazen döngüde gelen elemana göre veya bir duruma göre hem kod bloğunu çalıştırmak istemeyiz hemde döngüyü sonlandırmak isteyebiliriz. Bu durumda `break` anahtar kelimesini kullanırız.

Bir yazı içerisinde `python` kelimesini arattığınızı düşünün ve döngü içerisinde kelime bulundu bu durumda döngüye devam etmek istenmez `break` anahtar kelimesi ile döngüden çıkılır.


```python
# Break örneği 2. sayı 9 dan büyük yazılmadan döngüden çıkılacak.
sayilar = [1, 20, 3, 40, 55, 60, 7, 80, 99, 100]
for sayi in sayilar:
    if sayi > 9:
        break
    print(sayi)
print('bitti.')
```

    1
    bitti.



```python
# Break while sonsuz döngüsünü kırabilen bir yapıdır.
x = 1
while True:
    print(x)
    x += 1
    if x > 3:
        break
print('bitti.')
```

    1
    2
    3
    bitti.


### Else Anahtar Kelimesi

`for` döngüsünde `else` yapısı kullanılabilir. `else` yapısı `for` döngüsünde `break` anahtar kelimesi kullanılmadığı sürece çalışır. `break` anahtar kelimesi kullanıldığı zaman `else` yapısı çalışmaz.

```python
for i in range(5):
    <code block 1>
else: # break kullanılmadıysa bu kod bloğu çalışır
    <code block 2>
```

<code block 2> nin çalışması için for döngüsünden normal bir şekilde çıkılması gerekmektedir.


```python
# Break ile bir liste içerisinde arama
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bulundu = False
for el in liste:
    if el == 'python':
        bulundu = True
        print('Bulundu')
        break

if not bulundu:
    print('Bulunamadı')
```

    Bulunamadı



```python
# Şimdi aynı örneği else kullanarak daha güzel ve okunaklı yazalım.
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for el in liste:
    if el == 'python':
        print('Bulundu')
        break
else:
    print('Bulunamadı')
```

    Bulunamadı


> Python dilinde okunabilirliği yüksek kodlar yazmak çok önemlidir. Pratik yaparak bu konuda kendinizi geliştirebilirsiniz.
