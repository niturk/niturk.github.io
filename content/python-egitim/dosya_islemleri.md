+++
title = "Dosya İşlemleri"
date = "2023-01-26T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


Dosya okuma işlemlerini yapabilmek için `open()` fonksiyonunu kullanırız. Bu fonksiyonun iki parametresi vardır. İlk parametre dosya adı, ikinci parametre ise dosya açma modudur.  
Dosya açma modları şunlardır:  
- `r` : Dosyayı okuma modunda açar. Bu mod varsayılan moddur.
- `w` : Dosyayı yazma modunda açar. Eğer dosya mevcut ise içerik silinir.
- `a` : Dosyayı yazma modunda açar. Eğer dosya mevcut ise içerik silinmez ve dosyanın sonuna ekleme yapılır.


```python
dosya_adi = "deneme.txt"
dosya = open(dosya_adi, "r")

print(dosya.name, dosya.readable(), dosya.writable(), dosya.closed)

dosya.close()
print(dosya.closed)
```

    deneme.txt True False False
    True



```python
# Dosya Okuma
dosya_adi = "deneme.txt"
dosya = open(dosya_adi, "r")
icerik = dosya.readlines()
print(icerik)
dosya.close() # önemlidir.
```

    ['Python harikadır!\n', 'Python harikadır!\n', 'Python harikadır!Python harikadır!\n']



```python
# Dosya Okuma
dosya_adi = "deneme.txt"
dosya = open(dosya_adi, "r")
for satir in dosya:
    # print(satir)
    print(satir, end="")
dosya.close() # önemlidir.
```

    Python harikadır!
    Python harikadır!
    Python harikadır!Python harikadır!



```python
# Try Except Finally ile Dosya Okuma
dosya = open("deneme.txt", "r")
try:
    for satir in dosya:
        print(satir, end="")
        raise Exception("Hata")
except Exception as e:
    print(e)
finally:
    dosya.close()
```

    Python harikadır!
    Hata



```python
# With ile Dosya Okuma ("içerik yöneticisi")
with open("deneme.txt", "r") as dosya:
    for satir in dosya:
        print(satir, end="")
```

    Python harikadır!
    Python harikadır!
    Python harikadır!Python harikadır!


# Dosya Yazma


```python
# Normal yöntemlerle dosya yazma
dosya = open("deneme.txt", "w")
dosya.write("Python harikadır!\n")
dosya.write("Python harikadır!\n")
dosya.write("Python harikadır!\n")
dosya.close()
```


```python
# İçerik Yöneticisi ile dosya yazma
with open("deneme.txt", "w") as dosya:
    dosya.write("Python harikadır!\n")
    dosya.write("Python harikadır!\n")
    dosya.write("Python harikadır!\n")
```


```python
# İçerik Yöneticisi ile toplu dosya yazma 1
veri = ["Python harikadır!\n", "Python harikadır!\n", "Python harikadır!\n"]
with open("deneme.txt", "w") as dosya:
    dosya.writelines(veri)
```


```python
# İçerik Yöneticisi ile toplu dosya yazma 2
veri = ["Python harikadır!", "Python harikadır!", "Python harikadır!"]
with open("deneme.txt", "w") as dosya:
    dosya.write('\n'.join(veri))
```


```python
# İçerik Yöneticisi ile ekleme modunda dosya yazma
with open("deneme.txt", "a") as dosya:
    dosya.write("\nPython harikadır!")
```
