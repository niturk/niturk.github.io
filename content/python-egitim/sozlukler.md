+++
title = "Sözlükler"
date = "2023-01-20T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


Sözlükler pythonda en önemli veri yapılarından birisidir. Ancak objeler bile aslında sözlüktür. Objelerin özellikleri ve metodları sözlüklerle objeye ilişkilendirilirler. Görmesek bile aslında python kodu yazarken her zaman sözlüklerle çalışıyoruz.

Kullanıma uygun birkaç örnek vermek gerekirse;

Bir telefon rehberi düşünün telefon ve kime ait olduğu tutulur,
DNS servisinin çalışma biçimine bakıldığında web adresi ve IP adresi ilişkisi vardır,
Okuduğumuz bir kitabın içindekiler bölümünde sayfa numaraları ile konular ilişkilidir. İşte tüm bu uygulamalar sözlükler sayesinde gerçekleştirilir.

&nbsp;

## İlişkisel Veriler

Sözlüklerde anahtar ve değer ilişkisi vardır. Daha önce listeleri öğrenmiştik sözlükleri listelerle gerçekleştirelim ve daha sonra sözlüklerin özelliklerini inceleyelim.


```python
anahtarlar = ["a", "b", "c", "d"]
degerler = [1, 2, 3, 4]
```

Yukarıda iki adet liste oluşturduk. Birinde anahtarları tutuyoruz diğerinde değerlerini. Şimdi `a` anahtarı için değeri bulalım.


```python
index = anahtarlar.index("a")
print(degerler[index])
```

    1


`a` anahtarının indexini bulduk ve değerler listesindeki aynı indexe sahip değeri aldık. Biraz zor yoldan oldu ama sözlükler sayesinde daha kolay bir şekilde aynı şeyi yapabiliyoruz.

> Tabi sözlüklere ihtiyacımız yok diyebiliriz bu durumda ancak bu yöntemlerin çok verimsiz olduğunu unutmayın. Listelerde arama yapmanız gerekicek ve bu işlem uzun sürebilir. Sözlükler sayesinde bu işlem çok daha hızlı ve kolay oluyor.

&nbsp;

## Hash Haritaları (Hash Maps)

Sözlüklerin çalışma mantığı hash haritalarıdır. Hash haritaları anahtarları ve değerleri ilişkilendirmek için kullanılır. Anahtar bulmak için özel bir yöntem kullanıldığı için değer bulma hızı anahtar sayısına bağlı değildir. Bu yüzden sözlüklerde anahtar kelimeler hashlenebilen bir veri türünde olmalıdır.

- Stringler hashlenebilir.
- Sayısal veri tipleri hashlenebilir.
- Demetler hashlenebilir (eğer tüm elemanları hashlenebilirse).
- Listeler hashlenemez (mutable objeler hashlenemez).

&nbsp;


```python
# Hash fonksiyonu örneği
sayi = hash(100) # integer
metin = hash("100") # string
print(sayi, metin)
```

    100 -768187606974356583


> Sizde bir liste oluşturun ve hash fonksiyonuna gönderin. Göreceksiniz ki hata alırsınız.

&nbsp;

## Sözlüklerin Özellikleri

- Sözlükler anahtar ve değer ilişkisi vardır ve bunlar python objesidir.
- Anahtarlar haslenebilir ve benzersiz olmalıdır. Birden fazla aynı anahtarı tanımlayamazsınız.
- Değerler herhangi bir veri türü olabilir, sınırlama yoktur.
- Sözlüklerin tipi `dict` dir.
- Sözlükler sekans olmadığı için indekslenemezler. Değere anahtar ile ulaşılır. Listeler ve demetler gibi değillerdir.
- Teknik olarak sözlüklerde sıralama söz konusu değildir. (Python 3.6 ile artık sıralı.)
- Sözlükler mutable objelerdir. Yani değiştirilebilirler.
- Sözlükler `{}` ile tanımlanır. Anahtar ve değerleri `:` ile ayırırız, daha sonra `,' ile bir sonraki anahtar değer çiftlerini yazabiliriz.


```python
# Örnek bir sözlük
sozluk = {"a": 1, "b": 2, "c": 3, "d": 4}
print(sozluk)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4}


&nbsp;
### Bir Sözlük İçerisinde Değer Bulma

Sözlüklerin indexi yoktur. Değerlere anahtar ile ulaşılır. Sözlüklerin anahtarlarına `[]` ile ulaşabiliriz. Eğer anahtar sözlükte yoksa hata alırız.


```python
# Sözlükteki bir anahtarın değerine erişmek
sozluk = {"a": 1, "b": 2, "c": 3, "d": 4}
print(sozluk["b"])
```

    2


&nbsp;
### Bir Sözlük İçerisinde Değer Değiştirme

Sözlükler mutable objelerdir. Değerleri değiştirebiliriz. Eğer sözlükte olmayan bir anahtarı değiştirmeye çalışırsak hata alırız.


```python
# Örnek bir sözlük içerisinde değer değiştirme
sozluk = {"a": 1, "b": 2, "c": 3, "d": 4}
sozluk["b"] = 10
print(sozluk)
```

    {'a': 1, 'b': 10, 'c': 3, 'd': 4}


&nbsp;
### Bir Sözlüğe Yeni Bir Anahtar Değeri Ekleme

Sözlüklere yeni bir anahtar değer çifti ekleyebiliriz. Eğer anahtar varsa değerini güncellemiş oluruz yoksa yeni bir anahtar değer çifti eklenir.


```python
# Örnek bir sözlük içerisine yeni eleman ekleme
sozluk = {"a": 1, "b": 2, "c": 3, "d": 4}
sozluk["e"] = 5
print(sozluk)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


&nbsp;
### Bir Sözlükten Bir Anahtar Değeri Silme

Sözlüklerden anahtar değer çiftleri silinebilir. Eğer sözlükte olmayan bir anahtarı silmeye çalışırsak hata alırız.


```python
# Örnek bir sözlük içerisinden eleman silme
sozluk = {"a": 1, "b": 2, "c": 3, "d": 4}
del sozluk["b"]
print(sozluk)
```

    {'a': 1, 'c': 3, 'd': 4}


&nbsp;
### Sözlüklerle Sıkça Yapılan Hatalar

En sık karşılaşılabilecek hata `KeyError` hatasıdır. Bu hatayı iki şekilde alabiliriz.

- Sözlükte olmayan bir anahtarı kullanmaya çalıştığımızda.
- Sözlükte olmayan bir anahtarı silmeye çalıştığımızda.

Diğer alabileceğimiz hata ise `TypeError` hatasıdır. Bu hatayı hashlenemeyen bir veri tipini anahtar olarak kullanmaya çalıştığımızda alırız.

&nbsp;

## Sözlükler İle Döngü Kullanımı

Sözlükler ile `for` döngüsü kullanılabilir. Varsayılan olarak for döngüsünde anahtarlar kullanılır. Eğer değerleri kullanmak istiyorsak `values()` metodunu kullanabiliriz. Eğer hem anahtar hem de değerleri kullanmak istiyorsak `items()` metodunu kullanabiliriz.


```python
# Sözlüklerde döngüler ile anahtarları almak
sozluk = {"a": 1, "b": 2, "c": 3}
for anahtar in sozluk:
    print(anahtar)
```

    a
    b
    c



```python
# Sözlüklerde döngüler ile değerleri almak
sozluk = {"a": 1, "b": 2, "c": 3}
for deger in sozluk.values():
    print(deger)
```

    1
    2
    3



```python
# Sözlüklerde döngüler ile anahtar ve değerleri almak
sozluk = {"a": 1, "b": 2, "c": 3}
for anahtar, deger in sozluk.items():
    print(anahtar, deger)
```

    a 1
    b 2
    c 3


&nbsp;
## Sözlüklerle Çalışmak

### Sözlüklerde Anahtar Kontrolü

Sözlüklerde anahtarın olup olmadığını kontrol etmek için `in` operatörünü kullanabiliriz. Eğer anahtar sözlükte varsa `True` değilse `False` döner.


```python
# Sözlüklerde olmayan anahtarlar sorgulandığında hata almamak için in operatörü kullanılabilir
sozluk = {"a": 1, "b": 2, "c": 3}
if "d" in sozluk:
    print(sozluk["d"])
else:
    print("Sözlükte 'd' anahtarı bulunmamaktadır.")
```

    Sözlükte 'd' anahtarı bulunmamaktadır.


&nbsp;
### Sözlüklerde Kullanışlı Metodlar

- `sozluk.clear()` : Sözlüğü temizler.
- `sozluk.copy()` : Sözlüğü kopyalar. Yüzeysel kopyalama yapar (shallow copy). Yani içindeki objeler aynı referansı gösterir. Deep copy yapmak için `copy.deepcopy()` kullanabiliriz.
- `len(sozluk)` : Sözlükteki anahtar değer çiftlerinin sayısını döner.

&nbsp;

### Sözlük Oluşturmak ve Diğer Metodlar

Sözlükler `{}` ile oluşturulabilir. Ayrıca `dict()` fonksiyonu ile de oluşturulabilir. `dict()` fonksiyonu ile oluştururken iki şekilde oluşturabiliriz.


```python
# {} ve dict() fonksiyonu ile sözlük oluşturma
sozluk_1 = {"a": 1, "b": 2, "c": 3}
sozluk_2 = dict(a=1, b=2, c=3)                  # anahtar=değer şeklinde
sozluk_3 = dict([("a", 1), ("b", 2), ("c", 3)]) # liste içerisinde tuple şeklinde
```


```python
# Aynı değer ile birden fazla anahtar tanımlama
sozluk = dict.fromkeys(["a", "b", "c"], 1)
print(sozluk)
```

    {'a': 1, 'b': 1, 'c': 1}



```python
# fromkeys() fonksiyonu tekrarlanabilir bir veri tipi olmalıdır. String, List, Tuple gibi.
sozluk = dict.fromkeys("abc", 1)
print(sozluk)
```

    {'a': 1, 'b': 1, 'c': 1}


&nbsp;
### Boş Bir Sözlük Oluşturmak


```python
# Boş sözlük oluşturma
sozluk = {}
sozluk = dict()
```

&nbsp;
### Sözlüklerde get() Metodu

`get()` metodunda sözlükten ilgili anahtarı isteriz yoksa eğer hata almak yerine belirlenen varsayılan bir değer döndürülür.


```python
# Sözlüklerde get metodu kullanımı
sozluk = {"a": 1, "b": 2, "c": 3}
print(sozluk.get("d", 0))
```

    0


&nbsp;
### İki Sözlüğü Birleştirmek

`update()` metodunu kullanarak iki sözlüğü birleştirebiliriz. Eğer iki sözlükte aynı anahtar varsa ikinci sözlükteki değer geçerli olur.


```python
# Update metodu ile sözlüklerin birleştirilmesi
sozluk_1 = {"a": 1, "b": 2, "c": 3}
sozluk_2 = {"c": 4, "d": 5, "e": 6}
sozluk_1.update(sozluk_2)
print(sozluk_1)
```

    {'a': 1, 'b': 2, 'c': 4, 'd': 5, 'e': 6}

