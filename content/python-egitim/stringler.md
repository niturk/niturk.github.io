+++
title = "Stringler"
date = "2023-01-04T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


Stringlerin sekans veri yapısı olduğunu görmüştük. Öncelikle stringler homojenik veri yapısına sahip yani stringlerin her bir elemanı bir karakterdir. Özel bir veri yapısı olduğu için özel metodları mevcuttur. Başlangıçta sadece ASCII karakterleri desteklenmekteydi. ASCII karakterleri 128 karakterden oluşmaktadır, bu karakterlerden 95 tanesi print edilebilir, 33 tanesi ise print edilemez. ASCII karakterlerinin hepsi 8 bitlik bir sayısal değere sahiptir. Bu sayısal değerlerin hepsi 0 ile 255 arasındadır. ASCII karakterlerinin sayısal değerlerini görmek için aşağıdaki tabloyu kullanabilirsiniz.

![Ascii Table](ascii-table.jpg)

## Unicode

ASCII karakterleri sadece amerikan karakterlerini destekler. Bu yüzden Unicode karakterleri geliştirilmiştir. Python 3.0 sürümünden itibaren Unicode karakterleri desteklenmektedir.

Unicode için birkaç standart bulunmaktadır, python varsayılan olarak `UTF-8` kullanmaktadır.

`A` karakterini unicode için inceleyelim. Ascii kod karşılığı 65 olan karakterin unicode karşılığıda 65 tir.

![Unicode A](unicode-a.png)

String içerisinde unicode kullanımının iki yöntemi vardır.
- `\u` ile unicode karakterlerini kullanabiliriz.
- `\N{Karakter Adı}` ile unicode karakterlerini kullanabiliriz.


```python
# unicode kullanarak Greek Small Letter Alpha karakterini yazdıralım.
s = '\u03b1'
print(s)
```

    α



```python
# unicode kullanarak Snake karakterini yazdıralım.
s = '\N{snake}'
print(s)
```

    🐍


> https://www.compart.com/en/unicode/U+1F40D snake için bu sayfayı inceleyebilirsiniz. Dikkat edilmesi gereken snake 5 karakterden oluşmaktadır. `\u` ile kullanırken 4 karakter yazılmalıdır. Daha büyük karakterli bir sembol yazdırmak için 8'e tamamlamalısınız. Snake için `\U0001F40D` kullanmalısınız.

> Ayrıca `ord` fonksiyonunu kullanarak tüm karakterleri temsil eden sayısal değerlerini de görebilirsiniz.


```python
snake = ord('🐍')
print(snake)
```

    128013


&nbsp;
## String Metodları

Stringler için tonlarca metod vardır. [Tüm metodları burada görebilirsiniz](https://docs.python.org/3/library/stdtypes.html#string-methods). Bu metodları kullanmak için stringlerin sonuna nokta koyup metodun adını yazmalısınız.

En çok kullanılan ve üzerinde duracağımız metodlar;
- Büyük küçük harf dönüşümleri
- String içerisinden istenilen karakterleri çıkarma
- Stringlerin birleştirilmesi
- Stringlerin bölünmesi (split) veya birleştirme (join) işlemleri
- String içerisinde arama işlemleri

> Stringlerin değiştirilemez(immutable) olduğu unutulmamalıdır. Method çağrıları sonucunda oluşan çıktılar yeni stringler oluşturacaktır.

### Büyük Küçük Harf Dönüşüm Metodları

|  **Method**  |    **Method Kullanımı**    |   **Çıktı**   |
|:------------:|:--------------------------:|:-------------:|
|    lower()   |    'Hello World'.lower()   | 'hello world' |
|    upper()   |    'Hello World'.upper()   | 'HELLO WORLD' |
|    title()   |    'Hello World'.title()   | 'Hello World' |
| capitalize() | 'hello world'.capitalize() | 'Hello world' |


```python
# Stringleri büyük/küçük harf önemi olmadan karşılaştırma
s1 = 'Python'
s2 = 'PyThOn'
# s1 ve s2 stringlerini karşılaştırıyoruz. 
# İşlemi direk yaparsak s1 ve s2 için python eşit olmadığını söyleyecektir.
# bu durumlar için casefold methodunu kullanmamız gerekiyor.
print(s1.casefold() == s2.casefold())
```

    True


### Karakter Temizleme Metodları

`strip` metodu Stringlerde başta ve sonda bulunan boşlukları temizler. `lstrip` ve `rstrip` ise sadece soldaki ve sağdaki boşlukları temizler.
Eğer bir karakteri temizlemek istiyorsak `strip` metoduna parametre olarak temizlemek istediğimiz karakteri vermemiz yeterlidir. Varsayılan olarak üç metod sadece boşluk temizliği yapar.


```python
# Strip yaparak boşluk temizleyelim.
s = '   Python   '
print(s.strip())
```

    Python


> Kullanışsız görünüyorsa çok kullanılan ve önemli bir methodtur. String verileri çoğu zaman kullanıcıdan ve internetten alıyoruz gereksiz boşluklar can sıkıcı olabiliyor. Bu methodlar sayesinde bu boşlukları temizleyebiliriz.

### Stringlerin Birleştirilmesi

`+` operatörü ile stringler birleştirilebilir. Bu işlemde iki string birleştirilir ve yeni bir string oluşturulur.



```python
# Stringleri birleştirme
s1 = 'Python'
s2 = ' '
s3 = 'rocks!'

s = s1 + s2 + s3
print(s)
```

    Python rocks!


### Stringlerin Bölünmesi

`split` metodu stringleri bölmenize yarar. Bu metodu kullanmak için parametre olarak bölme işlemini yapacağımız karakteri vermemiz gerekmektedir. Varsayılan olarak boşluk karakteri kullanılır.


```python
# Stringi split metodu ile bölelim. Sonucunda bir liste elde edeceğiz.
s = 'Python rocks!'
print(s.split())
```

    ['Python', 'rocks!']



```python
# Parametre ile split yapalım.
s = '100, 200, 300, 400'
print(s.split(', '))
```

    ['100', '200', '300', '400']


### Stringlerin Join İle Birleştirilmesi

`join` metodu stringlerin birleştirilmesine yarar. Bu metodu kullanmak için parametre olarak birleştirme işlemini yapacağımız karakteri vermemiz gerekmektedir. Varsayılan olarak boşluk karakteri kullanılır.


```python
# join metodu ile stringleri birleştirelim.
liste = ['100', '200', '300', '400']
print(','.join(liste))
```

    100,200,300,400



```python
# Stringde bir sekans veri tipiydi şimdide join metodu ile string birleştirelim.
s = 'Python'
print('-'.join(s))
```

    P-y-t-h-o-n


### String İçerisinde Arama

String içerisinde arama yapmak için `in` operatörü kullanılır. Bu operatör string içerisinde aranan karakteri bulursa `True` bulamazsa `False` döndürür.


```python
# String içerisinde in operatörüyle arama yapalım.
s = 'Python rocks!'
print('Python' in s)
```

    True


#### String Başında ve Sonunda Arama

`startswith` ve `endswith` metodları stringlerin başında ve sonunda arama yapmanıza yarar. Bu metodlara parametre olarak arama yapacağımız karakteri vermemiz gerekmektedir. Varsayılan olarak boşluk karakteri kullanılır.


```python
# Örneğin öğrenci mail adresi doğrulaması yapalım.
# Öğrenci mailleri .edu ile bitiyor. Böylece basit bir şekilde doğrulama yapabiliriz.
email = 'info@nikitaturkmen.edu'
print(email.endswith('.edu'))
```

    True


#### String İçerisinde Aranan Kelimenin İndexini Bulma

`index` metodu string içerisinde aranan karakterin indexini bulmanıza yarar. Bu metodlara parametre olarak arama yapacağımız karakteri vermemiz gerekmektedir. Varsayılan olarak boşluk karakteri kullanılır.


```python
# index metodu ile index bulma.
s = 'Python rocks!'
print(s.index('rocks'))
```

    7


> `index` methodu aranan karakteri bulamazsa hata verir. Bu yüzden `in` operatörünü kullanarak aranan karakterin string içerisinde olup olmadığını kontrol etmeniz önerilir veya `find` methodunu kullanabilirsiniz.  
`find` methodu aranan karakteri bulamazsa `-1` döndürür.

&nbsp;

## Stringlerin Formatlanarak Düzenlenmesi

Şimdiye kadar iki string ile işlemler yaptık. Fakat daha fazla string ile işlem yapmak zorundayız. String birleştirmesini ele alırsak iki string için `+` operatörünü kullanıyoruz. Bazı durumlarda `+` operatörünü kullanamayacaksınız, örneğin bir string ile bir int veri tipinde kullanırsanız hata alırsınız. Bu durumlar için `format` metodu kullanılmaktadır.


```python
# Format kullanmadan stringleri birleştirelim.
name = 'John'
surname = 'Doe'
age = 25
print('My name is ' + name + ' ' + surname + ' and I am ' + str(age) + ' years old.')
```

    My name is John Doe and I am 25 years old.


Örnek biraz karışık gözüküyor çok fazla `+` operatörü kullanıyoruz. Bu durumda `format` metodunu kullanarak daha düzenli bir hale getirebiliriz.


```python
# Format kullanarak aynı stringleri birleştirelim.
name = 'John'
surname = 'Doe'
age = 25
print('My name is {} {} and I am {} years old.'.format(name, surname, age))
```

    My name is John Doe and I am 25 years old.



```python
# Formatlama sırasında sayılar için virgülden sonrası kaç basamak olacağını belirtebiliriz.
pi = 3.141592653589793
print('Pi sayısı: {:.2f}'.format(pi))
```

    Pi sayısı: 3.14


### F String Kullanımı

Python 3.6 versiyonu ile birlikte hayatımıza `f-string` girdi `format` metodunun yerini aldı diyebiliriz. `format` methodunda string içerisinde boş `{}`ler kullanıp format içerisinde parametreler verirken, `f-string`  bu `{}`lerin içerisine direkt olarak değişken ismini veya kod parçamızı. Evet `f-string` ile direkt olarak kod parçalarınızı yazabilirsiniz.

Hemen az önceki örneği `f-string` ile yapalım.


```python
# f string ile az önceki örneğin aynısını yapalım. 
# Ama bu sefer ad ve soyad stringlerini büyük harfe çevirelim.
name = 'John'
surname = 'Doe'
age = 25
print(f'My name is {name.upper()} {surname.upper()} and I am {age} years old.')
```

    My name is JOHN DOE and I am 25 years old.



```python
# f-string bununla sınırlı değil. {} içerisinde matematiksel işlemler yapabiliriz.
a = 5
b = 10
print(f'{a} + {b} = {a + b}')
```

    5 + 10 = 15

