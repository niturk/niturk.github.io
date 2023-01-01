+++
title = "Python Geliştirme Ortamı: VsCode"
date = "2022-12-27T18:00:00+03:00"
categories = ["python", "temel-python-egitimi"]
tags = ["python", ""]
draft = "false"
+++


![VsCode](vscode.png)
## Python Geliştirme Ortamı: VsCode

VsCode, ücretsiz ve açık kaynak kodlu bir çoklu platform kod editörüdür. [Electron](https://www.electronjs.org/) ile geliştirildiği için hemen hemen her işletim sisteminde problemsiz kullanılabilmektedir(Windows, Linux, Mac, Arm). Bu kod editörü microsoft tarafından geliştirilmektedir. [Kaynak koduna](https://github.com/microsoft/vscode) buradan ulaşabilirsiniz.  

VsCode ilk kurulumda temel özellikler ile gelir. Kullandığınız teknolojilere göre eklentiler yükleyerek kişiselleştirmenize olanak tanır. Bu eklentileri, [eklentiler](https://marketplace.visualstudio.com/vscode) üzerinden indirebilirsiniz.  

Eğer birçok programlama dili veya aracı kullanıyorsanız VsCode sizin içinde en iyi tercihlerden birisi olacaktır. Örneğin, benim kullandığım eklentiler sayesinde sahip olduğum editörde Python, C/C++, Docker, Kubernetes, PlatformIO... gibi teknolojileri tek bir editörde kullanabiliyorum. Hatta biraz daha ileri gittiğinizde çeşitli uygulamalarda kurabiliyorsunuz, rest client, GitHub Copilot gibi yapay zeka ile çalışan size kod yazmakta yardımcı olan araçlara bile sahip. 


### VsCode Kurulumu

VsCode'yu [buradan](https://code.visualstudio.com/) indirebilirsiniz. Kullandığınız işletim sistemine göre kurulumunu yapın.
Code editörünü kurduktan sonra bir takım ayarlamalar ve yüklemeler yapmanız gerekiyor. Şimdi öncelikle code editörünü açın ve editörü tanıyalım.

![VsCode](vscode_ilk_calistirma.png)

Code editörünü ilk açtığımızda resimdeki ekran bizi karşılıyor. Eklentiler menüsüne tıklayarak code editörümüzü kişiselleştirmeye başlayabiliriz. Eklentiler menüsüne girdikten sonra arama kısmına python için aşağıdaki eklentilerin adlarını yazarak arayın ve kur butonuna tıklayarak eklentileri kurun.

Python için gerekli eklentiler:

- **Python** (Microsoft) # Microsoft tarafından geliştirilir. Python eklentisi ile birlikte başka eklentilerde kurulacaktır bunları kullanmak istemezseniz pasif hale getirebilirsiniz ancak silemiyorsunuz. Bu eklentiler;
    - **Isort** (Kodlarınızı okunabilirlik için sıralar)
    - **Pylance** (Kod yazarken yardımcı bir python aracı)
    - **Jupyter** (Web tabanlı python interaktif çalışma ortamı)
    - **Jupyter Slide Show**
    - **Jupyter Notebook Renderers**
    - **Jupyter Keymap**
    - **Jupyter Cell Tags**
- **indent-rainbow** (oderwat) (Kodunuzun içindeki parantezlerin içindeki kodları renklendirerek okunabilirliği arttırır)
- **Path Intellisense** (Christian Kohler) (Dosya yollarını otomatik tamamlar)
- **Project Manager** (Alexey Shvetsov) (Projelerinizi kolayca yönetebilirsiniz)

Python programlama dilini öğrendikten sonra yöneleneceğiniz alana göre bazı eklentilerde mevcut. Bunlar;
- **autoDocstring** (Nils Werner) (Python fonksiyonlarınızın açıklamalarını otomatik olarak oluşturur)
- **Better** Comments (Aaron Bond) (Kodunuzun içindeki yorumları renklendirerek okunabilirliği arttırır)
- **Django** (Baptiste Darthenay) (Django ile çalışırken size yardımcı olur)
- **Prettier - Code formatter** (Prettier) (Kodunuzu düzenler)
- **Docker** (Microsoft) (Docker ile çalışırken size yardımcı olur)
- **Github Copilot** (Github) (Yazdığınız kodları yapay zeka ile tamamlar)
- **GitLens** (GitKraken) (Git ile çalışırken size yardımcı olur)

Sık kullanmadığınız eklentileri pasif hale getirebilirsiniz. Pasif hale getirdiğiniz eklentileri tekrar aktif hale getirmek için eklentiler menüsünden pasif hale getirdiğiniz eklentileri bulup aktif hale getirebilirsiniz. Her bir eklentinin editörünüzü yavaşlatacağını unutmayın bu yüzden sadece gerekli olanları kurmakta fayda var.

Editörü biraz daha kişiselleştirmek isterseniz temalar ve ikonlar için eklentilerde mevcut. Benim kullandıklarım;
- One Dark Pro  (Temalar)
- vscode-icons (Dosya ve klasör ikonları)

Diğer temalara [buradan](https://marketplace.visualstudio.com/search?target=VSCode&category=Themes&sortBy=Installs) ulaşabilirsiniz.

&nbsp;

### VsCode Python Ayarları

Code editörümüzü ve eklentileri kurduk. Şimdi bu eklentileri ayarlayalım. Ayarlar menüsünü açıp ayarlara tıklayalım.
Bu ayarlar sayfasında hem editör ayarlarını hemde eklenti ayarlarını yapabiliyorsunuz. Bu ayarlar için iki seçenek mevcut.
- Görsel olarak ayarları seçmek veya yazmak
- İstediğiniz ayarları json formatında yazmak.

Görsel olarak ayarlamak için açılan sayfadaki ayarları kurcalayabilirsiniz. Biz python için gereken ayarları json olarak yapacağız. Şimdi açılan sayfada sağ üstte olan **json ayarlarını aç** butonuna tıklayın.

![VsCode Json Ayarları](vscode_ayarlar.png)

```json
{
    // PYTHON
    "python.formatting.provider": "black",
    "[python]": {
        "editor.defaultFormatter": "ms-python.python",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        },
    },
    "isort.args":["--profile", "black"],
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "python.linting.banditEnabled": true,
    "python.linting.flake8Enabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": [
        "tests",
        "--verbose",
        "--cov"
    ],
    "python.languageServer": "Pylance",
    // PYTHON
}
```

Ayarları satır satır açıklamak gerekirse, bu ayarlar ile;
- Kodunuzun formatını **black** ile otomatik formatlayacaksınız.
- Kodunuzun içindeki importlar otomatik olarak sıralanacak.
- Kodunuzun içindeki hataları **flake8** size gösterecek.
- Kodunuzun içindeki güvenlik açıklarını **bandit** size gösterecek.
- Kodunuzun içindeki testleri **pytest** ile çalışacak.
- Kodunuzunu yazarken **pylance** size otomatik tamamlama desteği verecek.

> Bu ayarlar temel python eğitimi için zorunlu değildir. Eğitim sonunda projelerinizi kodlamaya başladığınızda işinize çok yarayacak araçlardır bunlar. **black**, **flake8**, **bandit**, **pytest** gibi araçlar kodlama standartlarına uymanız için size yardımcı oluyor. Temel Eğitim sırasında bazı satırları kapatabilirsiniz, bu araçların kurulması gerekmektedir her yeni bir sanal ortam açtığınızda tekrar tekrar kurmanız gerekiyor. Bu kurulum uyarılarını almak istemiyorsanız ilgili satırları yorum satırı yapın.

&nbsp;


### VsCode İlk Python Projesi

Bir klasör oluşturun ve bu klasörü terminalde açarak `code .` komutunu girdiğinizde o klasör code editöründe açılacaktır. Diğer bir yöntem code editörünü açın ve dosya menüsünden klasör aç diyerek veya oluşturarak bu klasörü code editöründe açabilirsiniz.

Şimdi bir `.py` ile biten python kod dosyası oluşturalım. Örneğin `main.py` olabilir. `main.py` dosyası açılır açılmaz code editörü python kodu yazacağınızı anlar ve buna göre davranır. Code editörünün durum çubuğunun sağ tarafında python yazıyor olmalıdır. Hemen yanında ise çalışıyor olan python sürümünü göreceksiniz. Code editörü sanal ortamları desteklemektedir, eğer bir sanal ortamınız varsa otomatik olarak aktif etmesini sağlayabilirsiniz.  

Yeni bir sanal ortam oluşturmak için `Terminal` menüsünden `yeni terminal oluştur diyelim ve code editörünün terminalini açalım.  
Ardından `pipenv` yi kullanarak sanal ortami oluşturalım. `pipenv install` veya `pipenv shell` ardından code editöründe python sürümü yazan bölüme tıklayarak çıkan listeden sanal ortamınızı seçmelisiniz. Eğer listede yoksa yenileme butonuna basmayı unutmayın.  

Tüm adımları doğru takip ettiyseniz artık python kodu yazmaya hazırsınız.
Şimdi açtığımız `main.py` dosyasına birkaç satır kod yazalım.

```python
# main.py
print("Hello World")
```

Ardından code editöründe sağ üstteki oynatma butonuna basarak kodumuzu çalıştıralım. Eğer kodumuz çalıştıysa terminalde `Hello World` yazısını göreceksiniz.

Artık temel python kodlarını yazmak için hazırız. Code editörünün özellikleri bu kadarla sınırlı değil özellikle `debug` özelliği gibi gelişmiş özelliklerde mevcut kodunuzu satır satır çalıştırarak hatalarınızı bulabilirsiniz. Ortak geliştirilen projeler içinde çok kullanışlıdır `git` desteği mevcuttur. Bu sayede terminale ile uğraşmadan görsel olarak kodlarınızı github gibi online repolara gönderebilirsiniz. Yazdığınız kodları test edebilirsiniz.

> Code editörü ile ilgili daha fazla bilgi için resmi sitesindeki dökümantasyonunu incelemek için [buraya](https://code.visualstudio.com/docs) tıklayabilirsiniz.  

> İyi bir yazılımcı olmak istiyorsanız kullandığınız araçları iyi şekilde öğrenmelisiniz. Code editörü ile devam edecekseniz daha fazla araştırma yaparak ileri özelliklerini öğrenerek etkili şekilde kod yazma kabiliyeti kazanabilirsiniz.

