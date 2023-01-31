+++
title = "Setler"
date = "2023-01-21T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


- Setler, matematikteki kümelere benzerdirler. 
- Sekans veri tipleri gibi veri koleksiyonları tutarlar.
- Setlerde sıralama yoktur.
- Setlerde tekrar eden elemanlar olmaz. Her eleman benzersizdir.
- Setler döngülerde kullanılabilir. Ancak sıralama olmadığı için sırasızdır.
- Setlerin tipi `set`'dir.
- Setlerin içindeki elemanlar hashlenebilir olmalıdır.
- Setler değiştirilebilirdir (mutable). Dolayısıyla setlerin kendisi hashlenemezler.


> Setlerin içinde set kullanılmak isteniyorsa `frozenset` kullanılmalıdır. Çünkü `frozenset` hashlenebilir bir veri tipidir.
Konumuz değil ancak isterseniz araştırabilirsiniz.

Setler, matematikteki kümelerin fonksiyonlarına sahiptirler. Bunlar:

- Birleşim (union)
- Kesişim (intersection)
- Fark (difference)
- Üyelik (membership) testi (in, not in)
- Alt küme (subset) testi (issubset)

Python imlementasyonu açısından `setleri` sözlükler gibi ama değeri olmayan sadece anahtarları olan bir veri yapısı olarak düşünebiliriz.
Dolayısıyla sözlüklerin anahtar verileri için geçerli olan kurallar `setler` için de geçerlidir.

&nbsp;

## Set Oluşturma

Setlerin oluşturulması için `set()` fonksiyonu veya `{}` sözdizimi kullanılabilir.


```python
# Set oluşturma
set1 = set([1,2,3])
set2 = {1,2,3}
print(set1, set2)
```

    {1, 2, 3} {1, 2, 3}


> boş set oluşturmak için `set()` fonksiyonu kullanılmalıdır. `{}` sözdizimi boş sözlük oluşturur.

Başka bir sekans veri tipinden set oluşturulabilir. Örneğin bir listeyi sete çevirebiliriz.


```python
# Listeyi set e çevirme
liste = [1,2,3,4,5,6,7,8,9,10]
set3 = set(liste)
print(set3)
```

    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}



```python
# Tekrarlı eleman olan bir listeyi sete çevirelim
liste = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
set4 = set(liste)
print(set4)
```

    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


> setlerde bir eleman birden fazla kez olmaz. Bu yüzden eğer bir listedeki birden fazla elemanı silmek ve sadece tekil kalmasını istiyorsanız o listeyi sete çevirip tekrar listeye çevirebilirsiniz.


```python
# Stringler sete çevrilebilir. Sekans veri tipiydi.
string = "Python"
set5 = set(string)
print(set5)
```

    {'P', 'n', 't', 'o', 'y', 'h'}


> Bir elemanın sette olup olmadığını aramak liste ve demetlere göre çok daha hızlıdır. Çünkü setlerde arama işlemi `hash` tablosu kullanılarak yapılır. Hız ihtiyacınız varsa arama yapmadan önce listenizi sete çevirin ve sonra sette arama yapın.

&nbsp;

## Set İle Kullanılan Fonksiyonlar

- Döngüler için `for` döngüsü kullanılabilir.
- Bir elemanın sette olup olmadığını `in` operatörü ile kontrol edilebilir.
- `len()` fonksiyonu ile setin eleman sayısını bulabiliriz.
- `set1.clear()` fonksiyonu ile setin içindeki tüm elemanları siler.
- `set1.copy()` fonksiyonu ile setin bir kopyasını oluşturur. Yüzeysel kopya (shallow copy) oluşturur.
- Derin kopya (deep copy) oluşturmak için `copy.deepcopy()` fonksiyonu kullanılabilir.

&nbsp;

## Sık Kullanılan Set Fonksiyonları

### Ayrık (disjointness) Fonksiyonu

Eğer iki setin kesişimi boş küme ise bu iki set ayrık kümedir. Bu durumda hiç ortak elemanları yok demektir.




```python
# Setlerde disjointness kontrolü. Ortak eleman yoksa True döner.
# Bir veya birden fazla ortak eleman varsa False döner.
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
print(set1.isdisjoint(set2))
```

    True


&nbsp;
### Setlerde Eleman Ekleme ve Çıkarma

Setlerde eleman ekleme ve çıkarma işlemleri yapılabilir. Bunun için `add()` ve `remove()` fonksiyonları kullanılır.


```python
# Bir sete eleman eklemek
set1 = {1,2,3,4,5}
set1.add(6)
print(set1)
```

    {1, 2, 3, 4, 5, 6}



```python
# Bir setten eleman silmek
set1 = {1,2,3,4,5}
set1.remove(5)
print(set1)
```

    {1, 2, 3, 4}


> Sette olmayan bir eleman silmeye çalışırsanız `KeyError` hatası alırsınız. Bu yüzden `discard()` fonksiyonunu kullanmalısınız. `discard()` fonksiyonu sette olmayan bir elemanı silmeye çalışırsa hata vermez.


```python
# Discard ile eleman silmek
set1 = {1,2,3,4,5}
set1.discard(5)
set1.discard(6)
print(set1)
```

    {1, 2, 3, 4}


&nbsp;
### Alt Küme (Subset) Testi

Karşılaştırma operatörleri ile setlerin alt küme olup olmadığı test edilebilir.

- `s1 < s2` eğer `s1` `s2`'nin alt kümesi ise `True` değerini döndürür.
- `s1 <= s2` eğer `s1` `s2`'nin alt kümesi veya `s1` ve `s2` eşit ise `True` değerini döndürür.
- `s1 > s2` eğer `s1` `s2`'nin üst kümesi ise `True` değerini döndürür.
- `s1 >= s2` eğer `s1` `s2`'nin üst kümesi veya `s1` ve `s2` eşit ise `True` değerini döndürür.


```python
# Setlerde alt küme karşılaştırması
{1, 2} < {1, 2, 3}
```




    True




```python
# Setlerde alt küme karşılaştırması 2
{1, 2} <= {1, 2, 3}
```




    True



&nbsp;
### Birleşim (Union) ve Kesişim (Intersection) Fonksiyonları

- Birleşim fonksiyonu `s1.union(s2)` veya `s1 | s2` şeklinde kullanılır.
- Kesişim fonksiyonu `s1.intersection(s2)` veya `s1 & s2` şeklinde kullanılır.

![Setlerde Birleşim ve Kesişim](set-union-intersection.png)

&nbsp;
### Fark (Difference) Fonksiyonu

- Fark fonksiyonu `s1.difference(s2)` veya `s1 - s2` şeklinde kullanılır.
- Fark fonksiyonu komütatif değildir değişim özelliği yoktur. `s1 - s2` ile `s2 - s1` farklı sonuçlar verebilir.

![Setlerde Fark](set-difference.png)


