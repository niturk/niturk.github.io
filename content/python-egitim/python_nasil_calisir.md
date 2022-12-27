+++
title = "Python Kodları Nasıl Çalışır?"
date = "2022-12-26T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "true"
+++


## Python Kodları Nasıl Çalışır?
![Python Interpreter](interpreter.png)

Python kaynak kodu sadece bir text dosyasıdır. Python kodları hem derlenmekte hemde yorumlanmaktadır.

Python kodları iki şekilde çalışmaktadır.
1. **İnteraktif mod**
2. **Script modu**

&nbsp;

### İnteraktif Mod
Python kodlarını çalıştırmak için bir terminal açıp python yazıp enter tuşuna basmanız yeterlidir. Bu şekilde açılan terminal python interpreter (REPL) olarak adlandırılır. Bu terminalde python kodlarını satır satır yazarak çalıştırabilirsiniz.

```bash
$ python3.11
Python 3.11.1 (main, Dec  7 2022, 01:11:34) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print('hello world')
hello world
```

- Bu mod grafik arayüzü içermez. Grafik arayüzsüz işletim sistemleri için idealdir.(serverlar, embedded sistemler)
- Biraz can sıkıcı olabilir çünkü interaktif mod sadece bir komut arayüzü. `Ctrl + D` tuşlarına basarak çıkabilirsiniz.
Ancak unutmayın yazdığınız tüm kodlar silinecek dolayısıyla pek verimli bir yöntem değil.
- Bu blog yazılarınıda severek yazdığım web sürümü mevcut, `Jupyter Notebooks` bu modda çalışır. Kullanabilmek için daha önce bahsettiğim `pip` aracı ile kurmanız gerekiyor. Jupyter notebook ile yazdığınız kodlara bir dosyaya kayıt edebilirsiniz. Dosya uzantısı `.ipynb` olan dosyalar Jupyter notebook dosyalarıdır.

&nbsp;

### Script Modu
Bu yöntemde python komutları bir dosyaya yazılır ve o dosya python ile çalıştırılır. Şimdi `hello.py` adında bir dosya oluşturalım ve içine `print("Hello World")` kodunu yazalım. Ardından bu dosyayı `python3 hello.py` komutu ile çalıştıralım.

```bash
# hello.py
print("Hello World")
```

```bash
$ python3 hello.py
Hello World
```

- Tekrar tekrar kodlarınızı çalıştırmak için bu yöntem daha verimlidir.
- Karmaşık uygulamalar geliştirebilirsiniz. (web servisleri, grafik arayüzleri, kütüphaneler vb.)
- Python kodlarının dosya uzantısı `.py` dir.
- Kodlarınızı herhangi bir metin editörünüde yazabilirsiniz. (vim, emacs, nano, vscode, atom, pycharm, spyder, jupyter notebook vb.)
Ancak yazılım geliştirme ortamı kullanmanız daha iyi olacaktır. Python için geliştirilmiş bir çok editör mevcuttur.  
Bu editörlerin başında;
    - `vscode`
    - `pycharm`
    - `atom` 
    - `spyder`  
gelmektedir. 
    
Bu editörlerin, diğer editörlerden en önemli özellikleri size python kodu yazarken veya test ederken sahip oldukları çeşitli araçlarla yardımcı olarak konfor sağlamalarıdır.
- Yeni başlayanlara `pycharm` önerilmektedir. Topluluk ve Profesyonel sürümleri bulunmaktadır. Topluluk sürümü ücretsizdir. Profesyonel sürümü ise ücretlidir. Sadece Pythona özel geliştirilmiş bir ide(Yazılım geliştirme ortamı) dir.
- Eğitime [vscode](https://code.visualstudio.com/) kod editörü ile devam edeceğiz. VsCode sahip olduğu eklentiler sayesinde istenildiği gibi bir ide haline getirilebiliyor. Birden fazla yazılım dili ile uğraşıyorsanız muhtemelen en iyi seçenek bu olacaktır. VsCode editörünü kurmak için [buraya](https://code.visualstudio.com/download) tıklayabilirsiniz. Bir sonraki yazımızda bu editörü `python editörü` yapacağız ve kodlarımızı yazmaya başlayacağız.

&nbsp;

> Daha önceki yazımızda sanal ortamdan bahsetmiştik, Bu iki mod içinde sanal ortam kullanımı aynı şekildedir. Sanal ortamınızı ister `venv` ister `pipenv` ile oluşturup aktif ettikten sonra interaktif veya script modunda python kodlarınızı çalıştırabilirsiniz.

