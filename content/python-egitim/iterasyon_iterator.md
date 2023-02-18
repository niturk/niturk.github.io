+++
title = "İterasyon ve İteratörler"
date = "2023-01-24T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


İterasyon yapisini bir veri yapısından her seferinde bir eleman alarak işlem yapmak için kullanırız.

- Sequence veri tipleri itere edilebilir. (list, tuple, string) index sırasına göre.
- Sözlük veri tipi itere edilebilir. (ekleme sırasına göre.)
- Set veri tipi itere edilebilir. (sırasız)

İterasyonda genel yapı tüm elemanlar bitene kadar bir eleman istenir.

Bu durumda iki konsepten bahsedebiliriz. `itere edilebilir` ve `iteratör`.

-`itere edilebilir` veri koleksiyonu olan nesnelerdir. (list, tuple, string, sözlük, set)
-`iteratör` ise bir nesnenin içindeki elemanları tek tek dolaşmak için kullanılan nesnedir.

İtere edilebilir nesneler özel bir metot olan `__iter__` metodu ile iteratör nesnesi oluşturur. Aynı zamanda iter() fonksiyonu ile de iteratör nesnesi oluşturulabilir.

İteratörler ise özel bir metot olan `__next__` metodu ile bir sonraki elemanı döndürür. Aynı zamanda next() fonksiyonu ile de bir sonraki elemanı döndürebilir.

> `next()` fonksiyonu eğer bir sonraki eleman yoksa `StopIteration` hatası fırlatır.

&nbsp;


```python
# İterasyon Örneği
liste = [1,2,3,4,5]
iterator = iter(liste)
ilk_eleman = next(iterator)
print(ilk_eleman)
```

    1


&nbsp;
## For Döngüsü Bir İterasyon Yapısıdır

For döngüsü aslında bir iterasyon yapısıdır. Python for döngüsünü aşağıdaki şekilde gerçekleştirir.


```python
# For döngüsünün nasıl çalıştığını gösteren örnek
l = [1,2,3]
iterator = iter(l)
try:    
    while True:
        print(next(iterator))
except StopIteration:
    pass
```

    1
    2
    3



```python
# Range fonksiyonu itere edilebilir bir nesnedir.
r = range(3)
iterator = iter(r)
try:
    while True:
        print(next(iterator))
except StopIteration:
    pass
```

    0
    1
    2


> İterasyon verileri hazır tutmaz. Her istekte bir eleman üretir bu yüzden bellek kullanımı azdır. Range fonksiyonu `100_000_000` sayısını bellekte tutmaz. Her istekte bir sayı üretir.

&nbsp;

## Generatörler

Daha önce compherension yapısını görmüştük. Liste, Sözlük ve set veri tipinde kullanarak veri yapısı oluşturmuştuk.
Bu yapıyı demetler(tuple) üzerinde görmemiştik çünkü demetler değiştirilemez(immutable) veri tipleriydi.  

Ayni yapıyı demetler üzerinde kullanırsanız `generatör` nesnesi oluşturmuş olursunuz.
`generatör`ler iteratörlerdir. Yani `next()` fonksiyonu ile bir sonraki elemanı döndürürler.


```python
# Generatör Oluşturma

generator = (i for i in range(5))
print(type(generator))
print(next(generator))
print(next(generator))
```

    <class 'generator'>
    0
    1


> Generatörler bellekte veri tutmazlar. Her istekte bir eleman üretirler. Bu yapıya `lazy evaluation` denir.
Veri hazır bulunmaz, sadece ihtiyaç oldukça üretilir.

### Neden Generatörler Kullanılır?

- Bellek Verimliliği
    - Örneğin büyük bir dosya okunup içindeki veriler işlenecekse dosyayı belleğe alırsak hem işlem uzun sürecektir, hemde bellek dolacaktır. Bunun yerine `generatör` kullanarak dosyayı satır satır okuyup işlem yaparak dosyanın sonuna kadar devam edebiliriz. Böylece bellek dolmamış olur.

> Dosya Okumada Performans Kıyaslaması
    Eğer size gereken birkaç satır dosyanın başında ise `generatörler` sayesinde tüm dosyanın okunması beklenmeden işlem tamamlanmış olacaktır.

> `Generatörler` tek kullanımlıktır, tekrar tekrar aynı verilere ulaşmanız gerekecekse kullanılmamalıdır.


```python
# Generatör ve Compherension Hız Karşılaştırması
from timeit import timeit

compherension = timeit('[i for i in range(10_000_000)]', number=1)
generator = timeit('(i for i in range(10_000_000))', number=1)
print(f'Comphere: {(compherension * 1000):.3f}ms', f'Generator: {(generator * 1000):.3f}ms')
```

    Comphere: 269.205ms Generator: 0.003ms

