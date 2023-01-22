+++
title = "Karar Yapıları"
date = "2022-12-31T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


Karar yapıları programlamanın temel yapı taşlarından birisidir. Yazdığımız kodlarda bazen duruma göre sonuç üretmemiz gerekebiliyor. İşte bu anlarda kullanacağımız yapı karar yapılarıdır. Örneğin yazacağımız uygulamamızda üyelere özel bir alan olsun. Bu alana kimlerin erişip kimlerin erişemeyeceğine karar vermemiz gerekecektir bu noktada bu yapıyı kullanabiliyoruz. Neredeyse tüm programlama dillerinde `if` `else` `elif` şeklindedir bu yapılar.

- `if` kullanıcı doğru bilgileri girdiyse
    - sisteme girmesine izin ver
- `else` bilgilerde yanlışlık varsa
    - sisteme girmesine izin verme ve hata mesajı göster.

en basit şekliyle kullanımı bu şekildedir. Gerçek hayattan bir örnekte vermek gerekirse hepimiz atmlerden para çekmişizdir. Atmye eğer bakiyenizden daha düşük bir miktar para çekeceğinizi söylerseniz size bu parayı verir ancak bakiyenizden veya günlük para çekme limitinden daha fazla bir miktar tuşlarsanız size bu parayı vermez ve neden vermeyeceğini hata mesajıyla ekranda yazar.

## If / Else Karar Yapısı

### If Koşulu

```python
if (koşul):
    (koşulun sağlanması durumunda çalışacak kod bloğu)
    ...
```

Python dilinde kod blokları boşluk ile oluşturulur. Diğer yazılım dillerine aşinaysanız satır sonlarında kullanılan `;` ve kod bloklarının `{}` sembolleri ile başladığını biliyorsunuzdur. Python'da bu tarz semboller kullanılmaz. Bir kod parçası yukarıdaki şekilde `if` koşuluna bağlı olarak çalışacaksa daha önceden belirlenmiş sayıdaki boşluk ile içerden yazılır. Böylece koda bakıldığında hangi satırların `if` koşuluna bağlı olarak çalışacağı görülür.Koşul sonucunun `True` olması gerekmektedir aksi halde bu kod satırları pas geçilir. Boşluk sayısı genelde 4 veya 8 olmaktadır. Her satır için 4 boşluk verdiğiniz sürece çalışacaktır. Eğer boşluk sayısını bir satır için bile farklı verecek olsanız kodunuz hata verecektir. Unutulmaması gereken bir diğer nokta `if` koşul yapısında koşuldan sonra `:` iki nokta koyularak kod bloğunun başlatılmasıdır. Python için bundan sonra göreceğimiz tüm özel yapılarda `:` iki nokta sembolü kullanılmaktadır. Nesne, fonksiyon, koşullar ve döngüler bunlardan bazılarıdır.


```python
# Örnek
cekilecek_miktar = 300
bakiye = 400

if cekilecek_miktar <= bakiye:
    print('Paranız hazırlanıyor, lütfen bekleyiniz.')
```

    Paranız hazırlanıyor, lütfen bekleyiniz.


Birkaç deneme yaparak hızlıca kavrayabilirsiniz. Çekilecek miktar bakiyeden fazla olursa `if` koşuluna bağlanan `Paranız hazırlanıyor...` mesajı ekranda görünmeyecektir. Python koşul sağlanmadığı için bu kod bloğunu dikkate almayacaktır.

### Else Koşulu

Bazı durumlarda koşulun yanlış olduğu zamanlar içinde farklı bir kod çalıştırmanız gerekiyor. 'else' yapısı 'if' olmadan tek başına kullanılamıyor. Anlam olarak değilse anlamı taşıyor. Yani bir koşulunuz var doğru olmadığında ne olacağını `else` bloğuna yazıyoruz.

```python
if (koşul) :
    (koşul sağlanırsa çalışacak kod bloğu)
else :
    (koşul sağlanmazsa çalışacak kod bloğu)
```

Aslında hiç else olmadan koşul 2 defa kontrol edilerek sadece `if` kullanılarak yapabilirdik bunu. 2 tane `if` yazardık koşulu sağlaması durumda olması gereken kodları bir diğer `if` koşulun sağlanmaması durumu için olabilirdi ancak kod okunabilirliği ve düzeni için pek hoş olmazdı bu durum. Ayrıca koşul iki defa kontrol edilirdi ki buda verimsizlik anlamına gelirdi.


```python
bakiye = 300
cekilecek_miktar = 400

if cekilecek_miktar <= bakiye:
    print('Paranız hazırlanıyor, lütfen bekleyiniz.')
else:
    print('Yetersiz bakiye!')
```

    Yetersiz bakiye!


### İç İçe Karar Yapıları

Öğrendiğimiz bu karar yapılarını sınırsız bir şekilde iç içe kullanabiliyoruz. Kural her zaman her blok için aynı olması gerekmektedir.

> Kaliteli bir kod için en fazla 3 adet iç içe yapı kullanılmalıdır. Daha fazla iç içe yapı kullanmaya başladıysanız muhtemelen kötü bir kod yazmaya başladınız gözden geçirmekte fayda var.


```python
hesap_durumu = True
bakiye = 300
cekilecek_miktar = 250

if hesap_durumu == True and cekilecek_miktar <= bakiye:
    print('Paranız hazırlanıyor, lütfen bekleyiniz.')

    if bakiye - cekilecek_miktar <= 100:
        print('Bakiyeniz 100 tl nin altina düştü!')
else:
    print('Hesap bloklanmış veya yetersiz bakiye!')
```

    Paranız hazırlanıyor, lütfen bekleyiniz.
    Bakiyeniz 100 tl nin altina düştü!


Örneğimizde iki `if` yapısını iç içe kullandık. Para çekilmesi ve bakiyenin 100 tl altına düşmesi durumunda extra bir kod bloğu ekledik. Bu içe içe yapıları python programlama dilinde bulunan tüm yapılarda kullanabilirsiniz. Aynı şekilde `else` kod bloğunada bazı eklemeler yapabilirdik örneğin bakiye yetersiz olsada avans isteyerek müşterimizin para çekmesini sağlayabilirdik.

> Bu tarz karar yapılarının kodlarını yazarken kafanızda kod olarak düşünmeyin. Gerçek hayatta o atm de siz olsaydınız işlemleri hangi aşamada yapardınız? Bu senaryoyu kafanızda kurun ve koda daha sonra dökün. Karmaşık karar yapılarında direk kod üzerinde çalışmak bir çok hataya sebep olmaktadır.

### Elif Koşulu

Bazen koşulumuzun birden fazla durumu olabilir. Alt alta birçok `if` ve `else` kullanmaktansa `elif` yapısını kullanırız.
Aşağıdaki kod parçasında koşullardan ilk doğru olanın kod parçası çalışır eğer hiçbiri doğru değilse `else` bloğu çalışır.
Bu yapıdaki `elif` koşulu sınırsız şekilde eklenebilir.
```python
if (koşul):
    (koşul doğruysa bu kod parçası çalışır)
elif (diğer koşul):
    (diğer koşul doğruysa bu kod parçası çalışır)
elif ( ...):
    (...)
else:
    (hiçbir koşul sağlanmıyorsa bu kod parçası çalışır.)
```


```python
#Örnek
sinav_notu = 90

if sinav_notu >= 90:
    print('Notunuz A')
elif sinav_notu >= 80:
    print('Notunuz B')
elif sinav_notu >= 70:
    print('Notunuz C')
else:
    print('Dersten kaldiniz!')
```

    Notunuz A


Artık `elif` yapısını bildiğimize göre atm uygulamasını tekrar daha güzel şekilde yazabiliriz.


```python
hesap_durumu = True
bakiye = 300
cekilecek_miktar = 250

if hesap_durumu == False:
    print('Hesabınız bloke edilmiştir, lütfen bankanız ile iletişime geçiniz!')

elif cekilecek_miktar <= bakiye:
    print('Paranız hazırlanıyor, lütfen bekleyiniz.')

    if bakiye - cekilecek_miktar <= 100:
        print('Bakiyeniz 100 tl nin altına düştü!')
else:
    print('Yetersiz bakiye!')


```

    Paranız hazırlanıyor, lütfen bekleyiniz.
    Bakiyeniz 100 tl nin altına düştü!


### Üçlü Koşul Operatörü

Standart `if/else` koşul yapısından daha kısa bir şekilde üçlü koşul yapısı kullanılabilir. Her durum için geçerli olmaya bile değer atama koşulları için kullanılabilir.

```python
deger1 if koşul else deger2
```

Bu yapıda eğer koşul doğruysa deger1 değeri yanlışsa deger2 değeri döndürülür.

Bir örnek yapalım, aşağıda bedel değişkenine göre hacim değişkenine değer atayan bir kod parçası mevcut.

```python
bedel = 100
if bedel < 100:
    hacim = 10
else:
    hacim = 1
```

Bu kod parçasını üçlü koşul operatörü ile daha kısa bir şekilde yazabiliriz.

```python
hacim = 10 if bedel < 100 else 1
```

Diğer bir örnek;


```python
# a/b bölme işlemi yapan kod parçası
a = 10
b = 5
sonuc = a / b if b != 0 else 'Hata'
print(sonuc)
```

    2.0

