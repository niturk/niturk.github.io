+++
title = "Sekans Veri Tipleri - 2"
date = "2023-01-02T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


## Slicing (Dilimleme)

Slicing, sekans veri tiplerinden belli bir aralıktaki verileri almaya arar. Daha önce list, tuple ve stringlerden ve bu sekans veri tiplerinin elemanlarına index numarası ile erişebildiğimizden bahsetmiştik. Bu erişim tek bir eleman için geçerliydi. Slicing ile ise bir aralıkta bulunan elemanlara erişebiliriz. Slicing işleminde kullanılan ifadeyi dilimleme ifadesi olarak da adlandırabiliriz.

- Slicing **başlangıç indexi dahil**, **bitiş indexi hariçtir**.
- [başlangıç:bitiş] şeklinde kullanılır.


```python
# Bir liste üzerinden örneklerle açıklayalım
# Bir liste oluşturalım
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Listedeki bir elemana index ile erişebiliyorduk liste[0] gibi 
# slice işlemi ile de bir alt liste oluşturabiliriz

# liste[0:3] 0. indexten başla 3. indexe kadar slice et demek
print(liste[0:3])
# liste[3:6] 3. indexten başla 6. indexe kadar slice et demek
print(liste[3:6])
```

    [1, 2, 3]
    [4, 5, 6]



```python
# Aynı örnek tuple veri tipi için birebir geçerlidir.
# tuple[0:3] 0. indexten başla 3. indexe kadar slice et demek
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(t[0:3])
# tuple[3:6] 3. indexten başla 6. indexe kadar slice et demek
print(t[3:6])
```

    (1, 2, 3)
    (4, 5, 6)



```python
# Pekiştirmek için string veri tipi üzerinden de örnekler yapalım
# string[0:3] 0. indexten başla 3. indexe kadar slice et demek
s = "Python"
print(s[0:3])
```

    Pyt


> Slicing işlemlerinde başlangıç ve bitiş sınırlarını yazmazsanız veya var olandan çok büyük yazarsanız python sadece başlangıçtan veya bitişe kadar olan elemanları alır.

Bu durumda bir önceki string örneğinde slicingi s[0:100] yaparsanız hata vermeden çalışıp son indexe kadar olan elemanları alacaktır.


Dolayısıyla bitiş indexini aslında yazmak bile zorunda değiliz. Başlangıç indexini yazarak bitiş indexini boş bırakabiliriz. Python bu durumda bitiş indexini son elemana kadar otomatik alacaktır. Hemen bir örnek yapalım.


```python
# Bitiş indexi olmadan slicing
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# liste[3:] 3. indexten başla sonuna kadar slice et demek
print(liste[3:])
```

    [4, 5, 6, 7, 8, 9, 10]



```python
# Başlangıç indexi olmadan slicing aslında 0. indexten başlayarak slice et demektir.
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# liste[:3] 0. indexten başla 3. indexe kadar slice et demek
print(liste[:3])
```

    [1, 2, 3]



```python
# Her iki indexide yazmazsak aslında tüm listeyi slice etmiş oluruz.
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# liste[:] 0. indexten başla sonuna kadar slice et demek
print(liste[:])
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


> Az önceki örnekte bir nevi yüzeysel kopyalama (shallow copy) yaptık yani mevcut listenin bir kopyasını oluşturduk. İlerleyen konularda daha detaylı inceleyeceğiz bu durumu. 


```python
# Negatif indexlerle slicing
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# liste[-3:] sondan 3. indexten başla sonuna kadar slice et demek
print(liste[-3:])
```

    [8, 9, 10]


&nbsp;
## Adımlayarak Dilimleme (Step Slicing)

Adımlayarak dilimleme, slicing işleminde dilimleme ifadesinin sonuna bir adım değeri eklenerek kullanılır. Adım değeri, dilimleme işleminde kaçar kaçar eleman alınacağını belirtir. Adım değeri belirtilmezse varsayılan olarak 1 alınır. Adım değeri negatif olursa dilimleme işlemi sondan başa doğru gerçekleşir.

`liste[başlangıç:bitiş:adım]` şeklinde kullanılır.

`[2:10:2]` bu şekilde bir kullanımda 2. indexten başla 10. indexe kadar 2 adım atlayarak elemanları al demiş oluyorsunuz.


```python
# Adımlayarak slice işlemi yapalım
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# liste[0:10:2] 0. indexten başla 10. indexe kadar 2şer 2şer slice et demek
print(liste[0:10:2])
```

    [1, 3, 5, 7, 9]


> Yukarıdaki örnekte adımlama kullanarak sadece tek sayıları alıp bir listesini oluşturduk.

### Negatif Adım Değeri

Negatif adım değeri ile sondan başa doğru dilimleme işlemi gerçekleştirilebilir. Bu durumda başlangıç ve bitiş indexleri değiştirilerek kullanılır.



```python
# Negatif index ile slice işlemi
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# liste[9:6:-1] adım değeri negatif olduğu için sondan başa doğru slice eder
print(liste[9:6:-1])
```

    [10, 9, 8]



```python
# Başlangıç değeri olmadan negatif index ile slice işlemi
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# liste[:6:-1] sondan başa doğru slice eder
print(liste[:6:-1])
```

    [10, 9, 8]



```python
# Bir listenin tam tersini almak için slice işlemi çok kullanışlıdır.
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# liste[::-1] sondan başa doğru slice eder
print(liste[::-1])
```

    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


> Slicing işlemi öğrendiğimiz tüm sekans veri tipleri için geçerlidir ve çok kullanışlıdır. İyice oturtmak için epey bir örnek yapılması ve kodlama sırasında kullanılarak pratik yapılması gerekmektedir.
