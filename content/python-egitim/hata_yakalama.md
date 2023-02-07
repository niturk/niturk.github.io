+++
title = "Hata Yakalama"
date = "2023-01-23T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


Hiçbir kod hata vermesi için tasarlanmaz ancak bazı durumlarda hata olabilme olasılığı vardır. Genelde bu hatalar kullanıcı tarafından alınacak verilerden kaynaklanır. Örneğin siz kullanıcıdan adını yazmasını istiyorsunuz ama kullanıcı yazmadı veya string yerine sayılar kullandı işte bu tarz beklenmedik senaryolara önlem almak için hata yakalama yaparız. Bu hatalar genelde beklenmedik hatalardır.

Her hata bizim için kritik değildir. Önemli olan hata oluşabilecek yerleri yakalamak ve kodu devam ettirmektir. Yakalanmayan bir hata bırakılırsa programımız duracak ve çalışmaya devam edemeyecektir.

&nbsp;

### Terminoloji
- `exception` : Python'da hatalar için kullanılan özel bir objedir.
- `raising` : Bazı durumlarda hata oluşmuş gibi davranmak isteyebiliriz. Raising ile bu işlemi yapabiliyoruz.
- `exception handling` : Hata yakalama işlemidir.
- `unhandled exception` : Kodumuz tarafından yakalanmayan hatalardır, programımız python tarafından sonlandırılır.

&nbsp;

### Hataların Hiyerarşisi

Pythonda oluşan hataların bir hiyerarşisi vardır. Şimdiye kadar gördüğümüz hatalar vardı. Örneğin bir sayıyı 0'a bölmeye çalıştığımızda `ZeroDivisionError` hatasını alıyorduk. Aynı şekilde bir listede olmayan bir elemana erişmeye çalıştığımızda `IndexError` hatasını alıyorduk.  

İşte python kodumuzu tam olarak bu hatalara göre davranış sergilemesini sağlayabiliyoruz. Listede bir eleman olmadığında `IndexError` hatasını yakalayarak kullanıcıya bu index yok diye bir mesaj gösterip tekrar index seçmesini isteyebiliyoruz.  

`raising` ile de bu hataların birini oluşturabiliyoruz. Listede arama yapan bir kod için eğer bulamazsak `NotFoundError` şeklinde bir hata oluşturabiliriz. Böylece kodumuz bu hataya göre şekil alacaktır.  

Pythonda hataların hiyerarşisi vardır. `LookupError` hatasını ele alırsak, aslında `IndexError` ve `KeyError` gibi hataların üst sınıfıdır. Yani `IndexError` ve `KeyError` hatasını da `LookupError` hatası olarak yakalayabiliriz. Daha spesifik bir hata yakalamak istiyorsak `IndexError` veya `KeyError` hatasını yakalamamız gerekmektedir. Tüm hataların hiyerarşisinin en başında `Exception` bulunmaktadır.
Hangi hatanın oluşacağını öngöremiyorsanız öncelikle bu ciddi bir problemdir, çevik bir kod yazmıyorsunuz demektir ama bu durumda yakalamanız gereken hata `Exception` olacaktır.

Python hata hiyerarşisini [buradan](https://docs.python.org/3/library/exceptions.html#exception-hierarchy) inceleyebilirsiniz.

&nbsp;

### En Popüler Hata Türleri

- `SyntaxError` : Kodumuzda yazım hatası olduğunda oluşan hata türüdür.
- `ZeroDivisionError` : Bir sayıyı 0'a bölmeye çalıştığımızda oluşan hata türüdür.
- `IndexError` : Listede olmayan bir indexe erişmeye çalıştığımızda oluşan hata türüdür.
- `KeyError` : Sözlükte olmayan bir anahtara erişmeye çalıştığımızda oluşan hata türüdür.
- `ValueError` : Bir fonksiyona geçersiz bir değer verdiğimizde oluşan hata türüdür.
- `TypeError` : Bir fonksiyona geçersiz bir veri tipi verdiğimizde oluşan hata türüdür.
- `FileNotFoundError` : Bir dosya bulunamadığında oluşan hata türüdür.

&nbsp;

### EAFP ve LBYL Kavramları

Python'da hata yakalama işlemini yaparken iki yaklaşım vardır. Bunlar `EAFP` ve `LBYL` kavramlarıdır.

- `EAFP` : Easier to Ask for Forgiveness than Permission (İzin almak yerine affetmeyi tercih etmek) kavramıdır. Bu yaklaşımda öncelikle kodumuzu çalıştırıyoruz. Kodumuz çalışırken bir hata oluşursa bu hatayı yakalıyoruz. Bu yaklaşımı kullanmak için `try` ve `except` bloklarını kullanıyoruz. Pythonda bu yaklaşım tercih edilmektedir.

- `LBYL` : Look Before You Leap (Atlamadan Önce Bak) kavramıdır. Bu yaklaşımda öncelikle kodumuzun çalışması için gerekli şartları kontrol ediyoruz. Eğer şartlar sağlanıyorsa kodumuzu çalıştırıyoruz. Bu yaklaşımı kullanmak için `if` ve `else` bloklarını kullanıyoruz.

&nbsp;

#### Python Geliştiricileri Neden EAFP Tercih Ediyor

`EAFP` tercih edilmesinin sebebi aslında hızdan kaynaklanmaktadır. Bir döngü ile 1000 defa bölme işlemi yapacağınızı düşünün. `LBYL` yapılırsa her defasında `if` ile bölenin 0 olup olmadığınız kontrol ederseniz 1000 adet kontrol gerçekleştirecek ve kodunuzu yavaşlatacaksınız. Ancak `EAFP` yapılırsa böyle bir kontrol yapmadan kodunuzu çalıştırırsınız. Eğer bölen 0 ise hata alırsınız ve bu hatayı yakalarsınız. Eğer 5 adet 0 varsa 5 adet hata yakalamış olursunuz ancak 1000 adet `if` kontrolü yapmaktan kat kat hızlıdır.

Ayrıca bir kodu hata olmayacak gibi yazmak her zaman deterministik bir durum değildir. Gözden kaçırdığımız yerler bize problem olacaktır. Bu sebeplede `EAFP` yaklaşımı tercih edilmektedir.

### Hata Yakalama Akışı

- Hata oluşur.
    - `exception` nesnesi yaratılır.
    - Hata yakalama akışı başlatılır.
    - Eğer bu hata yakalama akışında birşey yapmazsak.
        - Program sonlanır.
    - Eğer bu hatayı yakalamak için hata yakalama yapısı kullandıysak.
        - Mümkünse hata yakalanmaya çalışılır.
        - Ardından;
            - Program sonlanmadan kodun çalışmasına devam edilebilir.
            - Hatanın devam etmesine izin verilerek bir üst hata yakalama yapısına gönderilebilir. Genelde kütüphane yazılıyorsa bu durum tercih edilir.
            - Yeni bir hata akışı başlatılabilir.

&nbsp;

## Hata Akışı Başlatma

Bazen hatanın yakalanması için bir hata akışı başlatmak isteyebiliriz. Bu durumda `raise` anahtar kelimesini kullanırız.
Daha önce `exception` nesnesinin pythonda tanımlı olduğundan bahsetmiştik. Bu yapıyı ileride anlatacağımız fonksiyonlar içerisinde kullanırız genelde ve fonksiyonu kullandığımız kod parçasında hata yakalama yapısı koyarız. 


```python
# Bir hata oluşturalım
hata = ValueError('Ad alanı en az 5 karakter olmalıdır.')
raise hata
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[1], line 3
          1 # Bir hata oluşturalım
          2 hata = ValueError('Ad alanı en az 5 karakter olmalıdır.')
    ----> 3 raise hata


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


### Hata Yakalama İçin Genel Öneriler

Genellikle her durum için hata ayıklama yapmayız. Paronayak bir şekilde yaklaşır kodumuzun her tarafında hata ayıklama yapısı kurarsak bu durum kodumuzun okunabilirliğini ve hızını azaltır. Aynı zamanda çok fazla kod yazmamıza sebep olur. Bazende hataların oluşmasına izin vererek bu hataları takip ederiz. Oluşan hataları analiz ederek kodumuzu iyileştiririz. Bu durumlara genellikle `bug` denir.

- Küçük kod parçalarında hata ayıklama yapısı kullanmalıyız. Olmuyorsa kodumuzu parçalara ayırmalıyız.
- Yakalanacak hataları genel değil olabildiğince özel hatalara indirgemeliyiz. Index sorgulaması yaparken `Exception` yerine `IndexError` kullanmalıyız. Böylece oluşabilecek farklı kategorideki hatalara göre farklı işlemler yapabiliriz.

## Hata Yakalama Yapısı

Hata yakalamak için `try` `except` yapısını kullanırız.

- Hata olabilecek kod parçalarını `try` bloğuna alırız.
- Hata oluşursa `except` bloğuna girer. Bu bloğada hata oluştuktan sonra yapılacak işlemleri yazabiliriz.


```python
# Try Except Örneği
a = 1
b = 0

try:
    sonuc = a / b
except ZeroDivisionError:
    print('Bir sayı sıfıra bölünemez.')
    sonuc = 'Tanımsız'
print(f'Sonuc : {sonuc}')
```

    Bir sayı sıfıra bölünemez.
    Sonuc : Tanımsız


> Yukarıdaki kod örneğimizde 0 a bölme hatası oluştu ancak hiçbir hata mesajı almadık çünkü hatayı yakaladık. Ardından sonuç değişkenini tanımsız olarak belirledik ve programımızı devam ettirdik.

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
    raise
```

### Aynı Anda Birden Fazla Hata Yakalama

Bazen bir kod parçasında birden fazla hata oluşabilir. Bu durumda `except` bloğuna birden fazla hata yazabiliriz.
Python uyumlu olan ilk hata tipi için `except` bloğu çalışır. Bu durumda diğer hata tipleri için `except` bloğu çalışmaz.


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

### Finaly Bloğu

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

