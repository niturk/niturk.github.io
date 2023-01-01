+++
title = "Temel Python'a Giriş - 3"
date = "2022-12-30T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


## Karşılaştırma Operatörleri

Eşitlik operatörü `==` iki nesneyi karşılaştırır ve eşitse `True` değilse `False` cevabını verir.
İşlem sırasında python `__eq__` fonksiyonunu çağırır ve işlemi bu fonksiyonun sonucuna göre yapar.
- `10 == 10`  >  `10.__eq__(10)` fonksiyonu çağırılır ve sonuç `True` döner.
- `10 == 20` sonucu `False` olur.

Eşit değil operatörü `!=` iki nesneyi karşılaştırır ve eşit değilse `True` eşitse `False` cevabını verir.
İşlem sırasında python `__ne__` fonksiyonunu çağırır ve işlemi bu fonksiyonun sonucuna göre yapar.
- `10 != 10` > `10.__ne__(10)` fonksiyonu çağırılır ve sonuç `False` döner.
- `10 != 20` sonucu `True` olur.

Diğer karşılaştırma operatörleri;
- `>` (Büyüktür) `10 > 5` sonucu `True` olur.
- `<` (Küçüktür) `10 < 20` sonucu `False` olur.
- `>=` (Büyük Eşittir) `10 >= 10` sonucu `True` olur.
- `<=` (Küçük Eşittir) `10 <= 20` sonucu `True` olur.
- `is` (Nesne Eşitliği) `10` bir int nesnesi `10.0` bir float nesnesidir. `10 is 10.0` sonucu `False` olur. Çünkü bir int nesnesi bir float nesnesi değildir. Ancak `10 == 10.0` sonucu `True` olur. Çünkü değerleri aynıdır.

İki karşılaştırma operatörünü özel olarak ele almak gerekiyor. `is` iki nesnenin aynı nesne olup olmadığına bakarken `==` sadece o nesnelerin değerlerini karşılaştırır. Örnek vermek gerekirse. İki kişininde adı `Ahmet` olabilir, ancak bu aynı kişi oldukları anlamına gelmez.
Eğer aynı kişi olup olmadıklarını sorgulamak istiyorsak `is` kullanırız, eğer sadece adları aynı mı diye bakmak istiyorsak `==` kullanırız.


> `float` ile ilgili özel durumu hatırlayalım;
```python
0.1 + 0.1 + 0.1 == 0.3 # True olması gerekirken False oluyordu. Dikkat edin.
```

Bir şey daha deneyelim;


```python
a = 256
b = 256
print(a is b) # True

a = 257
b = 257
print(a is b) # False
```

    True
    False


Nasıl yani a ve b 256 iken `is` sorgusu `True` oluyor. Ama sayı değerleri 257 olduğunda `False` oluyor. Sanırım pythonda bir bug var!
Aslında öyle değil. Python geliştiricileri 1-256 arasında olan sayılar sık kullanıldığı için python başlatıldığında bu sayıları belleğe yükler. Ve siz bu sayıları tanımladığınızda aslında yeni nesne oluşturmazsınız aynı nesneleri kullanırsınız. Hadi bu bellekteki adresleri karşılaştırarak bunun nasıl çalıştığını görelim.  

Bellekteki nesnenin referans numarasını `id` fonksiyonu ile sorgularız.


```python
a = 256
b = 256
print(id(a), id(b))

a = 257
b = 257
print(id(a), id(b))
```

    139870646313168 139870646313168
    139870580485200 139870580480368


Gördüğünüz gibi ilk `print` sonucunda a ve b nin referans numarası aynı dolayısıyla `is` karşılaştırması `True` dönüyor. Fakat ikinci `print` sonucunda a ve b nin referans numarası farklı olduğu için `is` karşılaştırması `False` dönüyor.

> Sayılar için `is` karşılaştırma operatörünün kullanılması önerilmemektedir. Hataya çok açıktır.

&nbsp;

### Diğer Karşılaştırma Operatörleri

Kullanabileceğimiz birkaç karşılaştırma operatörü daha mevcut. Bunlar;
- `in` (İçeriyor mu) `10 in [10, 20, 30]` sonucu `True` olur.
- `not in` (İçermiyor mu) `10 not in [10, 20, 30]` sonucu `False` olur.

Pythonda verileri zaman zaman bir liste içinde tutarız ve aradığımız veri liste içerisinde mi sık sık sorgularız. Bu operatörler oldukça kullanışlıdır. Karşınıza çok çıkacaktır.

## Boolean Operatörleri

- Boolean'nın iki değeri vardı `True` ve `False`.
- Bunlara ek olarak üç adet operatör daha mevcut. Bunlar;
    - `and` (Ve) `True and True` sonucu `True` olur.
    - `or` (Veya) `True or False` sonucu `True` olur.
    - `not` (Değil) `not True` sonucu `False` olur.

Bu operatörleri bir sonraki konumuz olan koşullu ifadelerde çok sık kullanırız. Bir den fazla karşılaştırma operatörünü birleştirmek için kullanırız. 
&nbsp;

### and Operatörü

Matematikteki mantıksal ve ile aynı işlevi görür. İki karşılaştırma operatörünün sonucu `True` ise `and` operatörünün sonucu `True` olur. Aksi halde `False` döner. Akılda kalıcı olması için çarpım işlemi yapıyor gibi düşünebilirsiniz(`False` yutan eleman.).

| **A** | **B** |   | **A and B** |
|:-----:|:-----:|:-:|:-----------:|
|  True |  True |   |   **True**  |
|  True | False |   |  **False**  |
| False |  True |   |  **False**  |
| False | False |   |  **False**  |

```python
10 < 20 and 20 < 30 # True
10 < 20 and 20 > 30 # False
```

Sadece sayılarda geçerli değil, Örneğin bir login sistemi tasarlıyorsunuz. Login olurken iki bilgiye ihtiyacınız var. `E-mail` ve `Şifre`. Aynı anda ikisininde doğru olması gerektiği için burada `and` operatörünü kullanabiliriz.
&nbsp;

### not Operatörü

Matematikteki mantıksal değil ile aynı işlevi görür. Bir karşılaştırma operatörünün sonucu `True` ise `not` operatörünün sonucu `False` olur. Yani tam tersini yapar.

| **A** |   | **not A** |
|:-----:|:-:|:---------:|
|  True |   | **False** |
| False |   |  **True** |

```python
not 10 < 20 # False
not 10 > 20 # True
```
&nbsp;

### or Operatörü

İki karşılaştırma operatöründen birisi `True` ise `or` operatörünün sonucu `True` olur. Aksi halde `False` döner. Akılda kalması için toplama yapıyormuş gibi düşünebilirsiniz. (`True` 1 `False` 0 olarak düşünün.)

| **A** | **B** |   | **A or B** |
|:-----:|:-----:|:-:|:----------:|
|  True |  True |   |  **True**  |
|  True | False |   |  **True**  |
| False |  True |   |  **True**  |
| False | False |   |  **False** |

&nbsp;

### Kısa Yol Hesaplamaları

Python `and` ve `or` operatörlerinin kısa yol hesaplamaları yapar.  

- `and` operatöründe ilk değer `False` dönerse ikinci karşılaştırma hesaplanmaz ve sonuç otomatik olarak `False` döner.
- `or` operatöründe ilk değer `True` dönerse ikinci karşılaştırma hesaplanmaz ve sonuç otomatik olarak `True` döner.

```python
10 > 20 and 20 < 30 # False (10 > 20 False olduğu için ikinci karşılaştırma hesaplanmaz.)
10 < 20 or 20 > 30 # True (10 < 20 True olduğu için ikinci karşılaştırma hesaplanmaz.)
```
> Bu yüzden kod yazarken daha hızlı çalışmasını istiyorsanız öncelikli sorgulamayı bu operatörlerin sol tarafına yazmalısınız!

Bir örnek yapalım.


```python
a = 20
b = 0

a / b > 1 # karşılaştırması yapmak istiyorsunuz. 
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    Cell In[26], line 4
          1 a = 20
          2 b = 0
    ----> 4 a / b > 1 # karşılaştırması yapmak istiyorsunuz. 


    ZeroDivisionError: division by zero


sıfırla bölme hatası aldık. Unutmayın hiçbir sayı sıfıra bölünemez!
&nbsp;

Sıfıra bölme hatası almamak için ne yapabiliriz ?  
Yukarıdaki kod yerine aşağıdaki şekilde yazabilirsiniz. `b!=0` sorgusu `False` dönerse ikinci karşılaştırma hesaplanmaz ve `ZeroDivisionError` hatası almayız.


```python
a = 20
b = 0
b != 0 and a / b > 1
```




    False


