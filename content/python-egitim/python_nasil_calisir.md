+++
title = "Python Kodları Nasıl Çalışır?"
date = "2022-12-26T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


## Python Kodları Nasıl Çalışır?
![Python Interpreter](interpreter.png)

Python kaynak kodu sadece bir metin dosyasıdır. Python kodları hem derlenmekte hemde yorumlanmaktadır.

Python kodları iki şekilde çalışmaktadır.
1. **İnteraktif mod**
2. **Script modu**
&nbsp;

> Daha önceki yazımızda sanal ortamdan bahsetmiştik, Bu iki mod içinde sanal ortam kullanımı aynı şekildedir. Sanal ortamınızı ister `venv` ister `pipenv` ile oluşturup aktif ettikten sonra interaktif veya script modunda python kodlarınızı çalıştırabilirsiniz.

&nbsp;

### İnteraktif Mod
Python kodlarını çalıştırmak için bir terminal açıp python yazıp enter tuşuna basmanız yeterlidir. Bu şekilde açılan terminal python interpreter (REPL) olarak adlandırılır. Bu terminalde python kodlarını satır satır yazarak çalıştırabilirsiniz.

```bash
$ python3.11
Python 3.11.1 (main, Dec  7 2022, 01:11:34) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print('hello world')
hello world
>>> 1 + 1
2
>>> exit()
```

- Interaktif mod grafik arayüzü içermez. Grafik arayüzü olmayan işletim sistemleri için idealdir.(serverlar, embedded sistemler)
- Biraz can sıkıcı olabilir çünkü interaktif mod sadece bir komut arayüzü. `Ctrl + D` tuşlarına basarak veya komut satirina `exit()` yazarak çıkabilirsiniz.
Ancak unutmayın yazdığınız tüm kodlar silinecek dolayısıyla pek verimli bir yöntem değil.
- Interaktif modun birde web sürümü mevcut. [Jupyter Notebook](https://jupyter.org/) popüler bir web tabanlı interaktif modtur. Bu blog yazılarını şu anda Jupyter Notebook üzerinden yazıyorum. Jupyter notebook dosyaları `.ipynb` uzantılıdır.

&nbsp;

### Script Modu
Bu yöntemde python komutları bir dosyaya yazılır ve o dosya python ile çalıştırılır. Şimdi `hello.py` adında bir dosya oluşturalım ve içine `print("Hello World")` kodunu yazalım. Ardından bu dosyayı `python3 hello.py` komutu ile çalıştıralım. `print` fonksiyonu en temel fonksiyonlardan birisidir. Neredeyse her programlama dilinde aynıdır. Bu fonksiyon ekrana bir şey yazdırmak için veya kodlama sırasında birşeylerin doğru gidip gitmediğini ekrana yazdırarak kontrol etmemize olanak tanır.

```bash
# hello.py
print("Hello World")
```

```bash
$ python3 hello.py
Hello World
```

- Tekrar tekrar kodlarınızı çalıştırmak için bu yöntem daha verimlidir.
- Karmaşık uygulamalar script modu ile geliştirilebilir. (web servisleri, grafik arayüzleri, kütüphaneler vb.)
- Python kodlarının dosya uzantısı `.py` dir.
- Kodlarınızı herhangi bir metin editörünüde yazabilirsiniz. (vim, emacs, nano, vscode, atom, pycharm, spyder, jupyter notebook vb.)
Ancak yazılım geliştirme ortamı kullanmanız daha iyi olacaktır. Python için geliştirilmiş bir çok editör mevcuttur.  
Bu editörlerin başında;
    - `vscode`
    - `pycharm`
    - `atom` 
    - `spyder`  
gelmektedir. 
    
Bu editörlerin, diğer editörlerden ayrılan en önemli özellikleri size python kodu yazarken veya test ederken sahip oldukları çeşitli araçlarla yardımcı olarak konfor sağlamalarıdır.
- Yeni başlayanlara `pycharm` önerilmektedir. Topluluk ve Profesyonel sürümleri bulunmaktadır. Topluluk sürümü ücretsizdir. Profesyonel sürümü ise ücretlidir. Sadece Pythona özel geliştirilmiş bir ide(Yazılım geliştirme ortamı) dir.
- Eğitime [vscode](https://code.visualstudio.com/) kod editörü ile devam edeceğiz. VsCode sahip olduğu eklentiler sayesinde istenildiği gibi bir ide haline getirilebiliyor. Birden fazla yazılım dili ile uğraşıyorsanız muhtemelen en iyi seçenek bu olacaktır. VsCode editörünü kurmak için [buraya](https://code.visualstudio.com/download) tıklayabilirsiniz. Bir sonraki yazımızda bu editörü `python editörü` yapacağız ve kodlarımızı yazmaya başlayacağız.

&nbsp;
