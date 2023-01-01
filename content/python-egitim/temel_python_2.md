+++
title = "Temel Python'a Giriş - 2"
date = "2022-12-29T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


## Değişkenler

Oluşturduğumuz nesneleri ne için kullandığımızı anlamak için değişkenlere ihtiyacımız vardır.
Örneğin `bir_sayi` değişkenine bir sayı atamak için `=` operatörünü kullanırız.
```python
bir_sayi = 5
hesap_bakiyem = 1000.50
```
Artık `bir_sayi` etiketine sahip bir `int` nesnesine sahip olduk ve 5 değerini verdik. Bu nesneyi kullanmak için `bir_sayi` etiketini kullanabiliriz. Ekrana yazdıralım.
```python
print(bir_sayi)

5
```
Atadığımız bu etiketleri aslında nesnenin kendisi değildir, nesneyi bulmamızı sağlayan referans numarasıdır. Nesnenin kendisi bellekteki bir yerde saklanır.

    # Değişkenler tüm veri tiplerini tutabilir
    bir_sayi = 5
    bir_ondalikli_sayi = 5.5
    bir_metin = "Merhaba"
    bir_boolean = True
    bir_sayi = 10  # değişkeni yeniden tanımladık. Artık 5 e ulaşılamaz.

Peki nasıl bir değişken yaratıyoruz. Python her zaman önce eşitliğin sağ kısmını hesaplar ve sol kısmına atar.

&nbsp;

### Değişkenlerin Kullanımı

Değişkenleri tanımladıktan sonra istediğimiz gibi işlemlere dahil edebiliriz. Örneğin,


```python
yaricap = 5
pi = 3.14
alan = pi * yaricap * yaricap
print(alan)
```

    78.5



```python
# Değişkenleri işlemler sırasında kullanabiliriz.
sayi1 = 5
sayi2 = 3
sayi3 = sayi1 + sayi2
print(sayi3)
```

    8


&nbsp;
### Değişkenlerin İsimlendirilmesi

Değişkenlerin isimlendirilmesinde bazı kurallar vardır. Bunlar:
- Büyük küçük harf duyarlıdır `sayi` ve `Sayi` farklı değişkenlerdir.
- Değişken isimleri `_` veya `harf` ile başlamalıdır. Ardından istenildiği kadar `harf`, `sayı` veya `_` kullanılabilir.
    Bu kuralaya uyan birkaç değişken adı;
    `var`, `var_`, `var1`, `var_1`, `_var`, `_var_1`, `_1_var`, `__add__`
- Bazı özel rezerve kelimeler kullanılamaz. Bunlar `and`, `True`, `return` vb. Merak etmeyin vscode sizi bu kelimeler için uyaracaktır.



```python
True = 5
# Gördüğünüz gibi özel anahtar kelimeleri değişken olarak kullanamayız.
```


      Cell In[59], line 1
        True = 5
        ^
    SyntaxError: cannot assign to True



Bu kurallar zorunlu kurallardı. Bazı kurallar da tavsiye niteliğindedir. Her zaman yalnız çalışmayacağız. Çoğu zaman başkalarının kodlarını okuyacağız, başkalarıda bizim kodlarımızı okuyacak. O zaman bir standart olması gerekmektedir, aksi halde birbirimizin kodunu anlamak için çok fazla zaman harcamak zorunda kalırız. Bu problemin ortadan kaldırılması için bazı standartlar belirlenmiştir. `PEP8` standartları bunları kapsamaktadır.

[PEP8](https://peps.python.org/pep-0008/) standartları tam olarak bu tarz kuralları kapsamaktadır.

> İyi bir yazılımcı olmak istiyorsanız PEP8 standartlarını mutlaka uyarak kod yazmalısınız. Daha önceki yazılarımızda vscode editörüne eklediğimiz
> `flake8`, `black`, `isort` gibi eklentiler bu standartları uygulamamızı sağlar.

Birden çok kelime içeren değişkenler isimlendirilirken iki metod kullanılır. Birincisi `camelCase` diğeri ise `snake_case`. Bu iki metodun farkı ise `camelCase` değişkenlerde ilk kelimenin baş harfi küçük, diğer kelimelerin baş harfleri büyük olurken `snake_case` değişkenlerde tüm kelimelerin baş harfleri küçük ve her kelime arasında `_` vardır.  
Bazı diller `camelCase` kullanırken, python `snake_case` kullanmaktadır.

Yani; pythonda bir değişken tanımlarken `bir_sayi`, `banka_hesabi` şeklinde tanımlamalısınız.  

Bazen bu kuralları bozmak zorunda kalabilirsiniz. Bunun için iyi bir sebebinizin olması yeterlidir. Örneğin `PySide2` paketi ile çalışarak bir gui yapmak istiyorsanız `camelCase` kullanmak zorundasınız. Çünkü `PySide2` paketi c++ ile yazıldığı için `camelCase` kullanmaktadır. Bu durumda `snake_case` kullanmak yerine `camelCase` kullanmak zorundasınız. `PySide6` paketinde ise `snake_case` kullanılabilmektedir. Eğer bir gün `PySide6` kullanmak isterseniz `snake_case` kullanmanız daha mantıklı olacaktır.

> Değişkenleri isimlendirirken amacına uygun şekilde isimlendirmeniz, uzun zaman sonra kodunuza tekrar baktığınızda ne yaptığınızı anlamaya yardımcı olacaktır. `x`, `y`, `z` gibi değişken isimleri yerine `x_konum`, `y_konum`, `z_konum` gibi değişken isimleri kullanmanız daha mantıklı olacaktır.

&nbsp;

## Aritmetik İşlemler


#### Tekil(Unary İşlemler)
- `-` (Negatif) sayıyı negatif yapar. `-10` gibi.
- `+` (Pozitif) sayıyı pozitif yapar. `+10` gibi.


#### İkili(Binary İşlemler)
- `+` (Toplama) iki sayıyı toplar. `10 + 20` gibi.
- `-` (Çıkarma) birinci sayıdan ikinci sayıyı çıkarır. `10 - 20` gibi.
- `*` (Çarpma) iki sayıyı çarpar. `10 * 20` gibi.
- `/` (Bölme) birinci sayıyı ikinci sayıya böler. `10 / 20` gibi.
- `**` (Üs Alma) birinci sayının ikinci sayıda ki üssü alınır. `10 ** 20` gibi.

> İşlem önceliği matematikte olduğu gibi geçerlidir. Öncelik tanımak için matematikteki gibi parantez kullanabilirsiniz. 


Bu aritmetik işlemleri sayılar veri tiplerinin hepsinde geçerlidir : `int`, `float` tüm bu işlemleri destekler.
Sayısal veri tipleriyle karışık işlemler yapabilirsiniz.
- `2 + 2` sonucu tam sayı yani `int` veri tipinde olacaktır.
- `2 + 2.0` sonucu ondalıklı sayı yani `float` veri tipinde olacaktır.
- `5.5 * 2` sonucu ondalıklı sayı yani `float` veri tipinde olacaktır.
- `4 / 2` sonucu her zaman `float` olacaktır.

> Python'da bölme işlemi sonucu tam sayı bile olsa `float` veri tipinde olacaktır.
> `1 / (2 * 5)` gibi. 

&nbsp;

### Python Aritmetik İşlemleri Nasıl Yapar?

Sayılar objedir. Objelerinde durum ve metodları vardı. Pythonda sayı objeleri için `dunder` metod adı verilen metodlar vardır. `__add__` bu
metodlara örnektir. İki sayı toplamak istediğimizde python bu metodun kullanılması gerektiğini anlar ve sayıları bu metoda gönderir. Aşağıda bu işlemin nasıl gerçekleştiğini görebilirsiniz ancak pek okunabilir ve anlaşlabilir değil. Bu yüzden `+` operatörünü kullanıyoruz.



```python
a = 5
b = 3
c = a.__add__(b)
print(c)
```

    8


Peki burada şu soru aklımıza gelebilir. Biz kendi nesnelerimizi oluşturabiliyorduk. Örneğin `bina` nesnesi. Peki iki binayı toplarsak ne olur.
İşte python yine `+` operatörünü kullanırsanız. Nesnenin `__add__` metodunu çağırır. Eğer bu metod yoksa hata verir. Metodu iki binayı toplayarak bir site yapmak istediğinizi kodlarsanız toplamanın sonucu olarak bir bina sitesi elde edersiniz. Nesneler konusunda bunu nasıl yapacağımızı göreceğiz.

&nbsp;
### Operatörlerin İşlem Öncelikleri

Matematikte olduğu gibi pythonda da işlem önceliği vardır. Önceliği düşükten yükseğe doğru sıralarsak;
- `+`, `-` (Toplama, Çıkarma)
- `*`, `/`, `//`, `%` (Çarpma, Bölme, Tam Bölme, Mod Alma)
- `-` (Tekil Unary Negatif)
- `**` (Üs Alma)
- `()` (Parantez) Önceliği değiştirir. Parantezler her zaman önce işlenir.

> Bir öneri operatör incelikleri bazen hatalara sebep olabiliyor. Bu yüzden karmaşık işlemlerde kesinlikle önceliği kendimiz ayarlamak için `()` kullanıyoruz. Basit işlemlerde buna gerek olmayabilir.
> `2 * 10 + 5` bu şekilde yazmak yerine `(2 * 10) + 5` şeklinde yazmak daha mantıklı olacaktır.


```python
# Bankamizda 10_000 TL mevcut bakiye var. Yillik %20 faiz oraniyla 10 yil vadeli bir hesap aciyoruz.
# Hesap sonunda ne kadar para olacagini parantezlerle doğru öncelikleri vererek hesaplayalım.
mevcut_bakiye = 10_000
faiz = 0.2
yil = 10

gelecekteki_bakiye = mevcut_bakiye * ((1 + faiz/12) ** (yil * 12))
print(gelecekteki_bakiye)
```

    72682.54992160187


&nbsp;
### Tam Sayı Bölmesi ve Mod Alma

- `//` işareti ile bölümün tam kısmı alınır. `10 // 3` sonucu `3` olur.
- `%` işareti ile mod alınır. `10 % 3` sonucu `1` olur.
