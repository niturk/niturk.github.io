+++
title = "pip İle Paket Kurulumu ve Pipenv Kullanımı"
date = "2022-12-25T11:00:00+03:00"
categories = ["python", ""]
tags = ["python", "pipenv"]
+++


## Pip ile Paket Kurulumu

Python standart kütüphaneleri en temel paketlerdir. Bu paketlerin dışındaki paketleri kurmak için `pip` paket yöneticisini kullanırız.
Python kurulumu ile birlikte `pip` de kurulur. `pip` ile paket kurulumu için `pip install` komutunu kullanırız. 

Örneğin web sitelerine giriş yaparak bir sayfanın içeriğini almak istiyorsunuz. Bunun için bir kütüphane kurmanız gerekiyor. `requests` paketini kullanalım, terminal açarak aşağıdaki komutu girin.


```bash
pip install requests
```
> Bu paketi sanal ortamda kurmak için önce sanal ortamı aktif etmeniz gerekmektedir. Aksi taktirde bu paket sisteminizde yüklü olan pythona yüklenecektir!

&nbsp;

`pip` uygulaması bu paketleri internet üzerinden indirir ve kurar. Python geliştiricileri üçüncü parti paketleri için `PyPI` adlı bir depo oluşturmuşlardır. Tüm python paketlerine [Python Package Index](https://pypi.org/) bu linkten ulaşarak inceleyebilirsiniz. `pip` uygulamasına kurulacak paketin adını verdiğinizde aslında bu depoda paketi bulur ve kurulumunu gerçekleştirir. Bu depo resmi bir python paket deposudur. Bu depoda yüzbinlerce paket bulunmaktadır. Python programlama dilinin gücü birazda bu depodaki paketlerden gelmektedir.
Python kullanırken tekerleği sıfırdan icat etmezsiniz, onu alır ve kullanırsınız!

Bazen bazı paketlerin spesifik sürümlerini kullanmanız gerekmektedir. Bu durumlarda pip ile kurulum yaparken sürüm belirtebilirsiniz. Yukarıdaki örnekte sürüm belirtmedik ve bizim için pip paketin en güncel sürümünü kurdu.

Sürüm belirterek kurulum için terminale dönelim ve aşağıdaki komutu çalıştıralım.

```bash
pip install requests==2.25.1 # 2.25.1 sürümü kurulur.
```

&nbsp;

`pip` oldukça gelişmiştir, mantık ifadeleri kullanarak ona istediğinizi söyleyebilirsiniz. Örneğin `requests` paketinin 2.25 sürümüne eşit veya küçük olan sürümleri kurmak için aşağıdaki komutu çalıştırın.
```bash
pip install requests<=2.26.0 # 2.25 sürümüne eşit veya küçük olan sürümler kurulur.
```

## requirements.txt Kullanımı

Projelerimizde genelde birden fazla paket kullanırız. Sanal ortamımızı silmemiz veya projeyi başka birisiyle paylaşmanız gerekirse bu paketlerin adını ve sürümünü aklımızda tutmamız gerekirdi. Bu durum için `requirements.txt` dosyası kullanılmaktadır. Bu dosyayı oluşturarak `pip` programına paketlerinizi teker teker söylemek yerine ben paketlerimi bu dosyanın içerisine yazdım. Bu dosyayı oku ve sırasıyla istediğim paketleri istediğim sürümde kur diyebilirsiniz.

Örnek bir `requirements.txt` dosyası aşağıdaki gibidir.

```bash
requests==2.25.1
numpy==1.19.5
pandas==1.2.4
```

&nbsp;

Bu dosyayı oluşturduktan sonra `pip` programına bu dosyayı okutarak istediğim paketleri kurmasını sağlayabilirsiniz. Terminali `requirements.txt` dosyasının bulunduğu dizinde açın ve aşağıdaki komutu çalıştırın.

```bash
pip install -r requirements.txt
```
Bu komut ile 3 paketin birden kurulduğunu göreceksiniz.

&nbsp;

**Tüm geliştirme sürecini özetlemek gerekirse;**

1. `python -m venv env` Projeye başladığınızda sanal ortamınızı oluşturun.
2. `source env/bin/activate` Sanal ortamınızı aktif edin.
3. `pip install requests` Paket kurulumunu gerçekleştirin. 

> Paket kurulumundan önce sanal ortamı aktif etmeyin unutmayın! Aksi halde paketler sanal ortamınıza değil sistemdeki pythona kurulacaktır.

Biraz karmaşık görünüyor ancak yıllarca python geliştiricileri süreci bu şekilde kullandılar. Bu noktada imdadımıza `pipenv` paketi yetişiyor. Sanal ortam ve paketleri yönetebileceğimiz yine bir python paketi `pip` ile kurmanız mumkun. Harika değil mi ? Paketleri düzenleyen paket işte python bu kadar güçlü kendi eksiklerini kendisi kapatıyor.

## `pipenv` Kurulumu ve Kullanımı

### `pipenv` Kurulumu

`pipenv` paketini kurmak için aşağıdaki komutu terminalde çalıştırın.

```bash
pip install pipenv
```

&nbsp;

Artık bilgisayarınızda pipenv paketi kuruldu. Sanal ortam çalıştırmak için `virtualenv` ve `pip` e ihtiyacınız kalmayacak. Paket adındanda anlaşılacağı gibi `pipenv` pip ve env kelimelerinden oluşuyor yani tek bir paket ile her iki modülüde kullanabilirsiniz.

&nbsp;
### `pipenv` Kullanımı

`pipenv` kurulumundan sonra terminalden `pipenv` komutunu yazdığınızda karşınıza kullanılabilir komutlar ve örnek kullanımlar gelecektir.
Listedeki komutların en önemli aşağıda anlatılmıştır.

&nbsp;
#### Sanal Ortam Oluşturma

Bir proje klasörü oluşturun ve içerisinde terminal açarak `pipenv` ile sanal ortam oluşturmak için aşağıdaki komutu girin.

```bash
pipenv --python 3.11
```
> Bu komutu çalıştırır çalıştırmaz pipenv sizin python 3.11 sürümünü kullanarak özel bir lokasyonda sanal ortam oluşturacaktır. Ardından python sürümü ve paketleri takip etmek için klasör içerisinde `Pipfile` dosyasını oluşturacaktır.

&nbsp;

`Pipfile` dosyası aşağıdaki gibi görünecektir.
- [packages] - kurulu olan paketleri ve sürümlerini gösterir.
- [dev-packages] - geliştirme aşamasında kullanılan paketleri ve sürümlerini gösterir.
- [requires] - python sürümünü gösterir.

```bash
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]

[dev-packages]

[requires]
python_version = "3.11"
```


&nbsp;
#### Sanal Ortamı Aktif Etme


Şimdi isterseniz önce sanal ortamı nasıl aktif edeceğimizi görelim. Aşağıdaki komutu çalıştırın.

**Not:** `pipenv` komutlarını kullanmak için sanal ortamı aktif etmeye ihtiyacınız yoktur.

```bash
pipenv shell
```
> Bu komutu girdiğinizde sanal ortamınız aktif olacaktır. Bu komutu `Pipfile` dosyasının bulunduğu dizinde çalıştırmanız gerekmektedir. Başka bir dizinde çalıştırırsanız `pipenv` sanal ortamınızı bulamayacağı için hemen yeni bir tane oluşturacaktır. Dikkat etmeniz gerekiyor.

&nbsp;
#### Paket Kurulumu

Şimdide bir paket kurulumu yapalım. Aşağıdaki komut ile `requests` paketini kurabilirsiniz.

```bash
pipenv install requests
```
> Bu komutu çalıştırdığınızda `Pipfile` dosyasının içerisine `requests` paketinin adı ve sürümü yazılacaktır. Ayrıca `Pipfile.lock` dosyası oluşturulacaktır. Bu dosya `requests` paketinin hangi sürümünü kullandığınızı tutar. Bu dosya `Pipfile` dosyası ile birlikte paylaşılmalıdır. Bu dosya ile birlikte paylaşılan `Pipfile` dosyası ile `pipenv` sizin için paketleri kuracaktır.

&nbsp;
#### Spesifik Versiyon Seçilerek Paket Kurulumu
Belirli bir sürümü kullanmak isterseniz `==` operatörünü kullanabilirsiniz.

```bash
pipenv install requests==2.25.1
```

&nbsp;
#### Geliştirme Paketi Kurulumu

Bazen projelerimizde sadece geliştiricilerin kullanması gereken paketleri kullanırız. Bu paketler genelde geliştiriciye yardımcı olan paketlerdir. Örneğin `pytest` paketi böyle bir pakettir. Yazdığınız kodu test etmenize yardımcı olur. Bu paketin geliştirici paketi olarak kurmak isterseniz kurulum komutuna `--dev` parametresini ekleyin.

```bash
pipenv install pytest --dev
```
> `pytest` paketi `Pipfile` içerisinde [dev-packages] bölümüne eklenecektir.

&nbsp;
#### Kurulu Paketleri Güncelleme

Sanal ortamınızda kurulu olan paketler için yeni güncellemeler yayınlanmış olabilir. Kontrol etmek ve kullanmak için terminalde aşağıdaki komutu çalıştırın.

```bash
pipenv update
```

&nbsp;
#### Kurulu Paketleri Listeleme

Kurulu olan paketleri ve sürümlerini görmek için aşağıdaki komutu çalıştırın.

```bash
pipenv graph
```
> Unutmayın ki python paketlerini yüklerken mantık ifadeleri kullanabiliyorsunuz dolayısıyla `Pipfile` içerisinde yazan paketler sadece kurmak istediklerinizi belirtir ancak yeni güncellemeler için `pipenv update` komutunu kullanmanız gerekmektedir. Aktif halde kurulu paketleri görmek için graph komutu kullanmalısınız.

&nbsp;
#### Sanal Ortamı Aktif Etmeden Python Kodu Çalıştırma

`pipenv` ile sanal ortamı aktif etmeden python kodu çalıştırabilirsiniz. Aşağıdaki komutu çalıştırın.

```bash
pipenv run python dosya_adi.py
```
> `pipenv` size sanal ortamı aktif etmedende bir python dosyasını çalıştırmaya olanak tanır `run` komutu sonrası sanal ortam aktifmiş gibi düşünebilirsiniz.

&nbsp;
#### Sanal Ortamı Silme

Sanal ortamı silmek için aşağıdaki komutu çalıştırın. Bu komutu çalıştırdığınızda sadece sanal ortam silinecektir. `Pipfile` dosyası ve proje dosyalarınız kalacaktır.

```bash
pipenv --rm
```

