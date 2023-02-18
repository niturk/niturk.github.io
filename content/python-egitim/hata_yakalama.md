+++
title = "Hata Yakalama"
date = "2023-01-23T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


Yazılım dillerinde hatalar özel yapılardır. Kodumuz beklenmedik bir şekilde çalıştığında hata mesajı alırız. Ancak her zaman beklenmedik durumlar olmaz. Bazende hataların olacağını biliriz ve programımızın çökmemesi için hata mesajlarını yakalar ve programımızı devam ettiririz.

&nbsp;

### Terminoloji
- `exception` : Python'da hatalar için kullanılan özel bir objedir.
- `raising` : Hata oluşturmak için kullanılan özel bir ifadedir.
- `exception handling` : Hata yakalama işlemidir.
- `unhandled exception` : Kodumuz tarafından yakalanmayan hatalardır, programımız python tarafından sonlandırılır.

&nbsp;

### Hataların Hiyerarşisi

Pythonda oluşan hataların bir hiyerarşisi vardır. Bir sayıyı 0'a bölmeye çalıştığımızda `ZeroDivisionError` hatasını alıyorduk. Aynı şekilde bir listede olmayan bir elemana erişmeye çalıştığımızda `IndexError` hatasını alıyorduk. Bu hataları yakalayarak programımızın çalışmasını devam ettirebiliriz.  

`LookupError` hatasını ele alırsak, aslında `IndexError` ve `KeyError` gibi hataların üst sınıfıdır. Yani `IndexError` ve `KeyError` hatasını da `LookupError` hatası olarak yakalayabiliriz. Daha spesifik bir hata yakalamak istiyorsak `IndexError` veya `KeyError` hatasını yakalamamız gerekmektedir. Tüm hataların hiyerarşisinin en başında `Exception` bulunmaktadır.
Hangi hatanın oluşacağını öngöremiyorsanız öncelikle bu ciddi bir problemdir, çevik bir kod yazmıyorsunuz demektir ama bu durumda yakalamanız gereken hata `Exception` olacaktır.

Python hata hiyerarşisini [buradan](https://docs.python.org/3/library/exceptions.html#exception-hierarchy) inceleyebilirsiniz.

`raising` ile de bu hataların birini oluşturabiliyoruz. Listede arama yapan bir kod için eğer bulamazsak `NotFoundError` şeklinde bir hata oluşturabiliriz. Böylece kodumuz bu hataya göre şekil alacaktır.  

&nbsp;

### En Popüler Hata Türleri

- `SyntaxError` : Kodumuzda yazım hatası olduğunda oluşan hata türüdür.
- `ZeroDivisionError` : Bir sayıyı 0'a bölmeye çalıştığımızda oluşan hata türüdür.
- `IndexError` : Listede olmayan bir indexe erişmeye çalıştığımızda oluşan hata türüdür.
- `KeyError` : Sözlükte olmayan bir anahtara erişmeye çalıştığımızda oluşan hata türüdür.
- `ValueError` : Bir fonksiyona geçersiz bir değer verdiğimizde oluşan hata türüdür.
- `TypeError` : Bir fonksiyona geçersiz bir veri tipi verdiğimizde oluşan hata türüdür.
- `FileNotFoundError` : Bir dosya bulunamadığında oluşan hata türüdür.  

Standart hataların listesine [buradan](https://docs.python.org/3/library/exceptions.html) ulaşabilirsiniz.

&nbsp;

### EAFP ve LBYL Kavramları

Hata yakalamak için kullanılan iki yaklaşım vardır. Bunlar `EAFP` ve `LBYL` kavramlarıdır.

- `EAFP` : Easier to Ask for Forgiveness than Permission (İzin almak yerine affetmeyi tercih etmek) kavramıdır. Bu yaklaşımda öncelikle kodumuzu çalıştırıyoruz. Kodumuz çalışırken bir hata oluşursa bu hatayı yakalıyoruz. Bu yaklaşımı kullanmak için `try` ve `except` bloklarını kullanıyoruz. **Pythonda bu yaklaşım tercih edilmektedir.**

&nbsp;

- `LBYL` : Look Before You Leap (Atlamadan Önce Bak) kavramıdır. Bu yaklaşımda öncelikle kodumuzun çalışması için gerekli şartları kontrol ediyoruz. Eğer şartlar sağlanıyorsa kodumuzu çalıştırıyoruz. Bu yaklaşımı kullanmak için `if` ve `else` bloklarını kullanıyoruz.

&nbsp;

#### Python Geliştiricileri Neden EAFP Tercih Ediyor

`EAFP` tercih edilmesinin sebebi daha hızlı olmasıdır.  
Bir döngü ile 1000 defa bölme işlemi yapacağınızı düşünün; 
- `LBYL` 'de her işlemde `if` ile bölenin 0 olup olmadığınız kontrol ederseniz 1000 adet kontrol gerçekleşecektir.
- `EAFP` yapılırsa böyle bir kontrol yapmadan kodunuzu çalıştırırsınız. Eğer bölen 0 ise hata alırsınız ve bu hatayı yakalarsınız. Eğer 5 adet 0 varsa 5 adet hata yakalamış olursunuz ancak 1000 adet `if` kontrolü yapmaktan kat kat hızlıdır.

> Ayrıca bir kodu hata olmayacak gibi yazmak her zaman deterministik bir durum değildir. Gözden kaçırdığımız yerler bize problem olacaktır. Bu sebeplede `EAFP` yaklaşımı tercih edilmektedir.

&nbsp;

### Hata Yakalama Akışı

- Hata oluşur.
    - `exception` nesnesi yaratılır ve akış başlar.
    - Eğer bu hata yakalama akışında birşey yapmazsak.
        - Program sonlanır.
    - Eğer bu hatayı yakalamak için hata yakalama yapısı kullandıysak.
        - Mümkünse hata yakalanmaya çalışılır.
        - Ardından;
            - Program sonlanmadan kodun çalışmasına devam edilebilir.
            - Hatanın devam etmesine izin verilerek bir üst hata yakalama yapısına gönderilebilir.
            - Yeni bir hata akışı başlatılabilir.

&nbsp;

## Hata Akışı Başlatma

Sıklıkla hata akışı başlatmaya ihtiyaç duyarız. Bu durumda `raise` anahtar kelimesini kullanırız.


```python
# Bir hata oluşturalım
raise ValueError('Ad alanı en az 5 karakter olmalıdır.')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[18], line 2
          1 # Bir hata oluşturalım
    ----> 2 raise ValueError('Ad alanı en az 5 karakter olmalıdır.')


    ValueError: Ad alanı en az 5 karakter olmalıdır.


> `raise` anahtar kelimesi ile bir hata fırlatıldığında eğer bu hata yakalanmazsa programını sonlandırılır. Eğer pythonda hata yapısını kullanacaksanız ne yaptığınızı bildiğinizden emin olmanız gerekmektedir.


```python
# kullanıcıdan adını alalım eğer 5 karakterden az girerse ValueError fırlatalım.
ad = input('Adınız: ')
if len(ad) < 5:
    raise ValueError(f'Ad alanı en az 5 karakter olmalıdır.{ad} uygun değildir.')
print(f'Merhaba {ad}')
```

    Merhaba Nikita


&nbsp;
### Hata Yakalama İçin Genel Öneriler

Genellikle her durum için hata ayıklama yapmayız. Paronayak bir şekilde yaklaşır kodumuzun her tarafında hata ayıklama yapısı kurarsak bu durum kodumuzun okunabilirliğini ve hızını azaltır. Aynı zamanda çok fazla kod yazmamıza sebep olur. Bazende hataların oluşmasına izin vererek bu hataları takip ederiz. Oluşan hataları analiz ederek kodumuzu iyileştiririz. Bu durumlara genellikle `bug` denir.

- Küçük kod parçalarında hata ayıklama yapısı kullanmalıyız. Olmuyorsa kodumuzu parçalara ayırmalıyız.
- Yakalanacak hataları genel değil olabildiğince özel hatalara indirgemeliyiz. Index sorgulaması yaparken `Exception` yerine `IndexError` kullanmalıyız. Böylece oluşabilecek farklı kategorideki hatalara göre farklı işlemler yapabiliriz.

&nbsp;

## Hata Yakalama Yapısı

Hata yakalamak için `try` `except` yapısını kullanırız.

- Hata olabilecek kod parçalarını `try` bloğuna alırız.
- Hata oluşursa `except` bloğu çalışır. Bu bloğa hata oluştuktan sonra yapılacak işlemleri yazabiliriz.


```python
# Try Except Örneği
a,b = 10,0
try:
    sonuc = a / b
except ZeroDivisionError as ex:
    print(f'Hata : {ex}')
    sonuc = 'Tanımsız'
print(f'Sonuc : {sonuc}')
```

    Hata : division by zero
    Sonuc : Tanımsız


> Yukarıdaki kod örneğimizde 0 a bölme hatası oluştu ancak hiçbir hata mesajı almadık çünkü hatayı yakaladık. Ardından sonuç değişkenini tanımsız olarak belirledik ve programımızı devam ettirdik.

&nbsp;

### Hata Yakalama ve Yeniden Hata Fırlatma

Bazen yakaladığımız bir hatadan sonra aynı hatayı veya farklı bir hatayı fırlatmak isteyebiliyoruz.
Bunu iki sebepten yapabiliyoruz;
- Bazen ilgili kod bölümünde yapabileceğimiz bir işlem yoktur. Bu durumda hata fırlatmak isteyebiliriz.
- Hatayı daha anlaşılır bir hata mesajı ile fırlatmak isteyebiliriz.


```python
# Örneğin tekrar hata fırlatmayı kayıt almak için kullanabiliyoruz.
try:
    pass
except Exception as ex:
    log(ex)
    raise ValueError('Hata oluştu.')
```

&nbsp;
### Aynı Anda Birden Fazla Hata Yakalama

Bazen bir kod parçasında birden fazla hata oluşabilir. Bu durumda `except` bloğuna birden fazla hata yazabiliriz.
Pythonda uyumlu olan ilk hata tipi için `except` bloğu çalışır. Bu durumda diğer hata tipleri için `except` bloğu çalışmaz.


```python
try:
    pass
except IndexError as ex:
    pass
except ValueError as ex:
    pass
except Exception as ex:
    pass
```

&nbsp;
### Finally Bloğu

`finally` bloğunu hata olsun veya olmasın çalışması istenen bölümdür. Genelde kesin çalışması gereken kod parçaları için kullanılır. Örneğin dosya veya database bağlantısının kapatılması çok kritik bir işlemdir.


```python
try:
    pass
except (IndexError, ValueError) as ex:
    pass
finally:
    print('Her durumda çalışır.')
```

    Her durumda çalışır.

