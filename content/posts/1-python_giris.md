+++
title = "Python'a Giriş"
date = "2022-12-25T10:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", "python-giris"]
+++


## Python Nedir ?

![Python](python-logo.png)

Python, Guido van Rossum tarafından 1989 yılında geliştirilmeye başlanmış bir yazılım dilidir.
Günümüzde "Core Developer" olarak adlandırılan geliştiriciler tarafından geliştirilmeye devam etmektedir.
Bu eğitimde Python 3.11 sürümü kullanılmıştır.

&nbsp;
&nbsp;

**Günümüzde Popüler Kullanım Alanları**
- Web Geliştirme (Django, Flask, FastAPI)
- Oyun Geliştirme (Pygame, Pyglet)
- Grafiksel Kullanıcı Arayüzü (PyQt, PySide, Kivy)
- Bilgisayarlı Görü (OpenCV, Scikit-Image)
- Elektronik (MicroPython)
- Veri Bilimi ve Makine Öğrenmesi

Başlıca popüler kullanım alanlarını bu şekilde sıralayabiliriz.

&nbsp;
## Python Implementasyonları

Python temelde c programlama dili ile geliştirilmektedir ve birçok implementasyonu vardır. 

- [CPython](https://www.python.org/) (Eğitimde kullanılan implementasyon) 
- [PyPy](https://www.pypy.org/) (En hızlı python implementasyonu. CPython implementasyonunun değiştirilmiş ve JIT derleyicisi eklenmiş halidir. Üçüncü parti kütüphanelerle sorunlar yaşaması sebebiyle her zaman kullanılabilir değildir.)

Bazı implementasyonlar python kodunu diğer yazılım dillerine çevirerek kullanmaya imkan verir. Bunlar;
- [IronPython](https://ironpython.net/) .NET implementasyonudur. .NET kütüphaneleriyle ortak projeler geliştirmeye olanak tanır.
- [Jython](https://www.jython.org/) Java programlama dili implementasyonudur.
- [Cython](https://cython.org/) C/C++ implementasyonudur.

Tüm bu implementasyonlar içerisinde *CPython* resmi python implementasyonu olarak kabul edilir. Diğer implementasyonlar cpython implementasyonunu kök almış ve geliştirilmişlerdir. Diğer implementasyonların Cpython kadar stabil olduğu söylenemez ve kullanım alanları kısıtlıdır.

### CPython İmplementasyonu

- Python yazılım dili dendiğinde akla gelen implementasyondur. 
- Açık kaynaklıdır. [cpython kaynak kodu](https://github.com/python/cpython)
- C programlama dili kullanılarak geliştirilmektedir.
- "Standart Kütüphane" kavramına sahiptir. Sıkça kullanılan ve ihtiyaç duyulan fonksiyonları içermektedir.
    - Bu kütüphaneler c ve python kullanılarak geliştirilmiştir.
- Geniş bir platform desteği sunmaktadır. (Linux, Windows, Mac OS, iOS, Android, PlayStation, Xbox,...)


CPython basitçe bilgisayarınıza indirebileceğiniz birçok klasör ve dosyalardan oluşuyor. Bu dosyalardan bazıları çalıştırılabilir dosyalar örneğin pythonu çalıştırmak için kullanılıyor. Diğer dosyalar ise daha öncede bahsettiğimiz standart kütüphanelerden oluşuyor. Bilgisayarınızda birden fazla python sürümünü aynı anda bulundurabilirsiniz. İlerleyen zamanlarda buna ihtiyacınız olacaktır, sebebi büyük projelerin eski python sürümüyle geliştirilmeye başlandığı için hızlıca python sürümü güncellemesi yapılamıyor veya bazı üçüncü parti kütüphaneler güncel python sürümleriyle çalışmıyor. Python sürümünün güncellenebilmesi için herşeyi kontrol ederek çalıştığından emin olmanız gerekiyor.

&nbsp;

## Python Kurulumu

Resmi web sitesi üzerinden pythonun herhangi bir sürümünü indirip kurabilirsiniz. [python.org](https://www.python.org/downloads/).
Python kurulumunun standart kütüphaneler ve çalıştırılabilir dosyalardan oluştuğunu söylemiştik. Tüm platformlar için standart kütüphaneler ortak olmakla birlikte çalıştırılabilir dosyalar kurulacak platforma özeldir. Bu sebeple python kurulumu yaparken platformunuzu seçmeniz gerekiyor.

Python, linux platformunda çok fazla kullanılmaktadır bu sebeple çoğu linux dağıtımında güncel sürüm kurulu olarak gelir. Mac Os ve Windows için kurulum yapmanız gerekmektedir.


- Mac Os için kurulum sayfasına girdiğinizde "python_stabil_sürümü.pkg" dosyasını indirip çalıştırmanız yeterli olacaktır. Görsel bir arayüz ile kurulumu yapılabilmektedir.
- Windows için kurulum sayfasına girdiğinizde "python_stabil_sürümü.exe" dosyasını indirip çalıştırmanız yeterli olacaktır. Görsel bir arayüz ile kurulumu yapılabilmektedir.
- Linux işletim sistemi için ise işler biraz karmaşık olabilmektedir. Genelde python kurulumu terminalden `sudo apt install python3` komutu ile kurulum yapılabilmektedir ancak kullandığınız linux dağıtımı eski ise kurulacak python sürümüde eski olabilmektedir. Bu durumda kurulum için iki yol seçilmesi gerekmektedir.
    - Kolay yol, Ubuntu gibi çok kullanılan bir dağıtım kullanıyorsanız, [Deadsnakes](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa) gibi bir repoyu kendi repolarınıza ekleyerek hazırlanmış güncel python sürümünü kurabilirsiniz.
    - Zor yol, [python.org](https://www.python.org/downloads/) sitesinden istediğiniz python sürümünü derleyerek kurulum yapabilirsiniz. Bu yolun zorluğu, pythonun derlenmesi için gereken kütüphanelerin kurulumu ve derleme işleminin yapılmasıdır. Bu işlemleri yaparken birçok hata ile karşılaşabilirsiniz. Yeni başlayanlar için bu yolun kullanılması tavsiye edilmez.

Kurulumun başarılı olup olmadığını test etmek için;

- Windows için cmd veya powershell açıp `python --version` komutunu çalıştırmanız yeterli olacaktır.
- Mac Os için terminal açıp `python --version` komutunu çalıştırmanız yeterli olacaktır.
- Linux için terminal açıp `python3 --version` komutunu çalıştırmanız yeterli olacaktır.

&nbsp;

## Sanal Ortam (Virtual Environment)

Python sanal ortamları, bir Python uygulamasının çalıştırılması için bir çalışma alanı sağlar. Bu çalışma alanı, bir Python uygulamasının gerektirdiği tüm kütüphaneler ve bağımlılıkları içerebilir. Bu sayede, birden fazla Python uygulamasının aynı bilgisayarda çalışmasını sağlar ve bu uygulamaların birbirlerine olan bağımlılıklarını önler.

Sanal ortamlar, ayrıca bir Python uygulamasının bir sistemde yüklü olan Python sürümünden farklı bir Python sürümünü kullanmasını da sağlar. Örneğin, bir sanal ortamda Python 3.8 kullanırken, sistemde yüklü olan Python sürümü 3.9 olabilir. Bu, uygulamanın çalıştığı Python sürümünü kontrol etmeyi ve uygulamanın çalıştığı Python sürümüne göre gerekli kütüphaneleri yüklemeyi sağlar.

Peki buna neden ihtiyaç duyuyoruz diye düşünebilirsiniz. Hep en son çıkan güncel python sürümlerini kullansak problem yaşamayız diyebilirsiniz. Ama unutmayın python programlama dili açık kaynaklı bir dildir ve kullanacağınız birçok kütüphane sizin gibi yazılımcılar tarafından geliştiriliyor. Dolayısıyla uyum problemleri oluşma olasılığı çok yüksek. Bu yüzden birden fazla python sürümü ile çalışmak zorunda kalabiliyoruz. Kullandığımız önemli kütüphanelerin yeni python sürümleri ile uyumlu olmasını beklemek zorunda kalacaksınız. Her zaman en güncel sürümü kullanamayacaksınız. Bu yüzden sanal ortamların kullanımı gereklidir.

&nbsp;

### Sanal Ortam Çalışma Şekli

Python kurulumu bölümünde, kurulum için birkaç dosya ve pythonun çalıştırılabilir dosyalarının kurulmasıl gerektiğinden bahsetmiştik. Aslında sanal ortam dediğimiz yapı sizin için bu kurulumu yeniden yapar ve farklı bir ad verir. Şöyle düşünebilirsiniz Python3.11 sürümünü iki defa kurulum yapabilirsiniz Python3.10-BlogSitem Python3.10-OkulProjem sadece dosyaları kopyalamanız aslında iki python için bağımlılığı yok eder ancak pek kullanışlı gözükmüyor bu şekilde tüm dosyaları kendiniz taşımalısınız. İşte bunu fark eden python geliştiricileri sanal ortam (virtual environment) kavramını ortaya atmıştır.

- Linux/Mac için bu işlem oldukça verimlidir çünkü sadece kısayol oluşturularak birden fazla python sürümü oluşturulabiliyor.
- Windows için biraz az verimli çünkü sanal ortam için dosyalar kopyalanıyor diskteki kullanılan alan artıyor.


Bir sanal ortam oluşturmak için öncelikle sanal ortamı oluşturacağımız proje dizine gidip terminali açıyoruz. Terminali açtıktan sonra aşağıdaki komutu çalıştırıyoruz.

```shell
python3 -m venv sanal_ortam_adi # (Python 3 sürümü için sistem varsayılan python sürümü)
python3.9 -m venv sanal_ortam_adi # (Python 3.9 sürümü için)
python3.10 -m venv sanal_ortam_adi # (Python 3.10 sürümü için)
```

Bu komut ile `sanal_ortam_adi` adıyla sanal ortam oluşturuldu, proje klasörünüzde bu dosyayı göreceksiniz. Bu dosyaları incelerseniz kullandığınız python sürümünün bir kopyası olduğunu fark edeceksiniz. Şimdi sanal ortamı aktif edelim. Terminale aşağıdaki kodu girelim.

```shell
source sanal_ortam_adi/bin/activate
```


Bu komut ile sanal ortam aktif edildi. Şimdi sanal ortam içerisinde python sürümünü kontrol edelim.

```shell
python --version
```

&nbsp;
&nbsp;

Uzun uzun komutlar yazdık, her zaman hatırlamalıyız, biraz karmaşa yaratıyor sanki. Ayrıca bu proje klasörünü bir arkadaşınızla paylaşırsanız hala ona hangi python sürümünü kullandığınızı söylemeniz gerekiyor.
Python sürümlerini ve sanal ortamları proje bazlı olarak takip edebileceğiniz çok daha gelişmiş bir yöntem mevcut. [Pipenv](https://pipenv.pypa.io/en/latest/) tüm bu işlemleri otomatik olarak yapar. İlerleyen yazılarda bu yöntemi de ele alacağız.

Bir sonraki yazıda daha önce bahsettiğim üçüncü parti kütüphanelerin kurulumunu gerçekleştireceğiz.
