+++
title = "Sekans Veri Tipleri - 3"
date = "2023-01-03T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


## Manipülasyon

Değiştirilebilir(mutable) olan veri tipleri manipüle edilebilir. Listeler bu tipe oldukça güzel bir örnektir.
Listelerde bir elemanı değiştirebilir, silebilir veya ekleyebilirsiniz. Genelde en çok eleman ekleme (append) işlemi yapılır. 


### Bir Elemanı İndex Numarasına Göre Değiştirme

En çok kullanılan yöntemdir. `[index]` ile elemanı seçebildiğimiz gibi değiştirebiliyoruzda aynı şekilde.


```python
# Tek bir elemanı index numarası ile değiştirebiliriz
# Örneğin, 3. elemanı değiştirelim
liste = [1, 2, 3, 4, 5]
liste[2] = 10
print(liste)
```

    [1, 2, 10, 4, 5]


### Slice İle Birden Fazla Elamanı Değiştirme

Çok kullanılan bir yöntem olmasada bazen ihtiyaç duyulabilir eğer belli bir aralıkta elemanları değiştirmek istiyorsanız bunu yapabilirsiniz.


```python
# Slice ile değiştirebiliriz
# Örneğin, 2. ve 3. elemanları değiştirelim
liste = [1, 2, 3, 4, 5]
liste[1:3] = [10, 20]
print(liste)
```

    [1, 10, 20, 4, 5]


### Bir Elemanı İndex Numarasına Göre Silme


```python
# Bir elemanı listeden silelim
# Örneğin, 3. elemanı silelim
liste = [1, 2, 3, 4, 5]
del liste[2]
print(liste)
```

    [1, 2, 4, 5]


### Slice İle Birden Fazla Elemanı Silmek


```python
# Slice ile bir aralığı silelim
# Örneğin, 2. ve 3. elemanları silelim
liste = [1, 2, 3, 4, 5]
del liste[1:3]
print(liste)
```

    [1, 4, 5]


### Listeye Yeni Bir Eleman Eklemek

En çok kullanılan yöntemdir. `append` metodu ile listenin sonuna yeni bir eleman ekleyebilirsiniz.


```python
# Listeye yeni bir eleman ekleyelim
liste = [1, 2, 3, 4, 5]
liste.append(6)
print(liste)
```

    [1, 2, 3, 4, 5, 6]


### Listeye Birden Fazla Eleman Ekleme

Eklememiz gereken birden fazla eleman varsa `append` metodunu kullanmak mantıklı değil, bu durumda `extend` methodu ile bunları tek seferde ekleyebiliriz. `extend` methodu bir liste alır ve bu listeyi listenin sonuna ekler.


```python
# Listeye birden fazla eleman ekleyelim
liste = [1, 2, 3, 4, 5]
liste.extend([6, 7, 8])
print(liste)
```

    [1, 2, 3, 4, 5, 6, 7, 8]


### Listenin İstenilen Bir Yerine Eleman Eklemek

`insert` methodu ile listenin istenilen bir yerine eleman ekleyebilirsiniz. Bu methodun ilk parametresi index numarası, ikinci parametresi ise eklemek istediğiniz elemandır.


```python
# Insert ile bir eleman ekleyelim
# Örneğin, 3. elemanın önüne 10 ekleyelim
liste = [1, 2, 3, 4, 5]
liste.insert(2, 10)
print(liste)
```

    [1, 2, 10, 3, 4, 5]


> `insert` metodunu kullandığınızda listedeki elemanların index numaraları değişir.  
`insert` metodunu kullanırken dikkatli olunmalıdır. `append` veya `extend` metodlarına göre çok daha yavaştır. Çünkü tüm elemanları etkilemektedir.

&nbsp;

## Sekans Veri Tiplerinde Kopyalama

İki çeşit kopyalama tipi vardır.
- `yüzeysel (shallow)` kopyalama
- `derin (deep)` kopyala

### Yüzeysel Kopyalama (Shallow Copy)

Yeni bir sekans yaratılır ve bu sekansın elemanları eski sekansın elemanlarına referans verir. Bu durumda yeni sekansın elemanları eski sekansın elemanları ile aynıdır. Yani yeni sekansın elemanları değişirse eski sekansın elemanları da değişir. Dikkatli olunmalıdır çok fazla hataya sebep olmaktadır.

Yüzeysel kopyalama için kullanılabilecek yöntemler
- slice ile kopyalanabilir `[:]`
- `copy` methodu ile kopyalanabilir


```python
# Bir listenin yüzeysel kopyasını yaratalım ve içerisindeki bir elemanı güncelleyip orjinal listeyi kontrol edelim.
liste = [1, 2, 3, 4, 5]
liste2 = liste[:]
liste2[2] = 10
print(liste)
```

    [1, 2, 3, 4, 5]


> 2. indexte bulunan eleman bir `int` ve değiştirilemez bir veri tipi dolayısıyla yeni bir obje yaratıldığı için orjinal liste etkilenmedi. Şimdi ise değiştirilebilir `mutable` bir veri tipi olan `list` kullanalım.


```python
# Bir listenin yüzeysel kopyasını yaratalım ve içerisindeki bir elemanı güncelleyip orjinal listeyi kontrol edelim.
liste = [[1, 2, 3], 4, 5, 6, 7]
liste2 = liste[:]
liste2[0].append(4)
print(liste)
```

    [[1, 2, 3, 4], 4, 5, 6, 7]


> Bakın liste2 ye eleman eklendi ancak orjinal listedede o eleman eklenmiş oldu. Çok hata yapılan bir durumdur ve fark edilmeside oldukça zordur. Listelerle çalışırken dikkat edin!


```python
# Aynı örneği copy metodu ile yapalım. Sonuç değişmeyecek.
liste = [[1, 2, 3], 4, 5, 6, 7]
liste2 = liste.copy()
liste2[0].append(4)
print(liste)
```

    [[1, 2, 3, 4], 4, 5, 6, 7]


> Gördüğünüz gibi slice veya copy ile yüzeysel kopyalama yapıyoruz. Elemanımız bir mutable veri tipi olduğu için orjinal listeye de etki etti.

### Derin Kopyalama (Deep Copy)

Derin kopyalama için `copy` modülünün `deepcopy` fonksiyonunu kullanabiliriz. Bu fonksiyon ile yeni bir sekans yaratılır ve bu sekansın elemanları eski sekansın elemanlarına değil, eski sekansın elemanlarının kopyalarına referans verir. Bu durumda yeni sekansın elemanları değişirse eski sekansın elemanları değişmez. Hemen bir örnek yapalım.


```python
# deep copy ile kopyalama yapalım.
import copy
liste = [[1, 2, 3], 4, 5, 6, 7]
liste2 = copy.deepcopy(liste)
liste2[0].append(4)
print(liste)
```

    [[1, 2, 3], 4, 5, 6, 7]


> Gördüğünüz gibi derin kopyalama ile yeni bir liste oluşturduk ve bu listeye eleman ekledik. Ancak orjinal listeye etki etmedi.

&nbsp;

## Sekans Dizilerinin Açılması (Unpacking)

Sekans veri tiplerinde birden fazla veri vardı. Bu verilere index numarasıyla erişebiliyorduk. Ancak bu verileri tek tek değişkenlere atayabiliriz. Bunun için `unpacking` yapmamız gerekiyor. Bunun için `=` operatörünü kullanıyoruz. Bu operatörün sol tarafında değişkenler, sağ tarafında ise sekans veri tipi olmalıdır. Bu durumda değişkenlerin sayısı ile sekans veri tipindeki elemanların sayısı aynı olmalıdır. Aksi takdirde hata alırız.


```python
# Unpacking yaparak birden fazla değer ataması yapalım
veri = [1, 2, 3, 4, 5]
a, b, c, d, e = veri
print(a, b, c, d, e)
```

    1 2 3 4 5



```python
# Sekans olmak zorunda değil (tuple, set, dictionary).
x, y, z = 1, 2, 3
print(x, y, z)
```

    1 2 3



```python
# String bir sekans olduğu için unpacking yapabiliriz.
a, b, c, d, e, f = "Python"
print(a, b, c, d, e, f)
```

    P y t h o n


> Dikkat edilmesi gereken nokta eşitliğin her iki tarafındaki eleman sayısının eşit olması gerekmektedir. 5 elemanlı bir listeyi 3 değişkene atamak mümkün değildir.

&nbsp;

## İki Değişkenin Değerlerinin Değiştirilmesi

İki değişkenin değerlerinin bazen değiştirilmesi gerekmektedir. Python'da bunun için çok güzel bir yöntem var. Bazı yazılım dillerindeyse bunu zor yoldan yapmanız gerekiyor çünkü eğer bir değişkenin değerini değiştirirseniz önceki değerini kaybedersiniz dolayısıyla değiştirmeden önce onu bir yerde saklamanız gerekiyor.
`a = 5 ve b = 3` iki değişkeniniz olsun değerlerini nasıl değiştirirsiniz ?

Diğer tüm dillerde kullanabileceğiniz yöntem

```python
a = 5
b = 3

# a = 3 ve b = 5 olacak

gecici = a
a = b
b = gecici
```

&nbsp;

Python'da neler yapabileceğimize bakalım şimdi;


```python
# Pythonda ise kolayca swap yapabilirsiniz.
a = 5
b = 3
a, b = b, a
print(a, b)
```

    3 5

