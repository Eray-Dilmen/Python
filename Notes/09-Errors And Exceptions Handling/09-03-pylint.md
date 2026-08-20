# Pylint Nedir?

Pylint, Python kodlarını analiz eden bir **statik kod analizi (linter)** aracıdır.

Temel olarak iki şey yapar:
- **Hataları Bulur:** Kod çalıştırılmadan önce syntax hatalarını, tanımlanmamış değişkenleri veya kullanılmayan modülleri tespit eder.
- **Stil Denetimi Yapar:** Kodun **PEP 8** (Python standart yazım kuralları) standartlarına uygun olup olmadığını denetler (ör. girintileme hataları, fazla uzun satırlar, eksik docstring açıklamaları) ve koda 10 üzerinden bir kalite puanı verir.

---

## Nasıl Çalıştırılır?

Terminal veya komut satırı üzerinden `ilgili dosyanın bulunduğu dizine gidilerek` çalıştırılır.
yani terminalde iken kod dosyasının olduğu aynı path'de olmanız gerekir.

### 1. Standart Kullanım (Sadece Hatalar ve Puan)
Yeni Pylint sürümlerinde varsayılan olarak sadece bulunan hatalar, uyarılar ve genel kalite puanı listelenir:

```bash
pylint dosya_adi.py
```

### 2. Detaylı Kullanım (İstatistik Raporlu)
Tüm istatistik tablolarını, kod oranlarını ve detaylı analiz raporunu görmek için komutun sonuna -r y parametresi eklenir:

```bash
pylint dosya_adi.py -r y
```


---

---


### simple.py içerisindeki kod:
```python
a = 5
b=7
c = "Deneme"
print(a)
print(B)
print(C)
```

```pylint simple.py -r y``` komutuyla çalıştırdığımızda aldığımız çıktı:

```text
************* Module simple
simple.py:6:0: C0304: Final newline missing (missing-final-newline)
simple.py:1:0: C0114: Missing module docstring (missing-module-docstring)
simple.py:1:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
simple.py:2:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
simple.py:3:0: C0103: Constant name "c" doesn't conform to UPPER_CASE naming style (invalid-name)
simple.py:5:6: E0602: Undefined variable 'B' (undefined-variable)
simple.py:6:6: E0602: Undefined variable 'C' (undefined-variable)


Report
======
6 statements analysed.

Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |NC         |NC         |0.00        |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |0      |NC         |NC         |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|method   |0      |NC         |NC         |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|function |0      |NC         |NC         |0           |0        |
+---------+-------+-----------+-----------+------------+---------+



8 lines have been analyzed

Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |7      |87.50 |NC       |NC         |
+----------+-------+------+---------+-----------+
|docstring |0      |0.00  |NC       |NC         |
+----------+-------+------+---------+-----------+
|comment   |0      |0.00  |NC       |NC         |
+----------+-------+------+---------+-----------+
|empty     |1      |12.50 |NC       |NC         |
+----------+-------+------+---------+-----------+



Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |NC       |NC         |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |NC       |NC         |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |5      |NC       |NC         |
+-----------+-------+---------+-----------+
|refactor   |0      |NC       |NC         |
+-----------+-------+---------+-----------+
|warning    |0      |NC       |NC         |
+-----------+-------+---------+-----------+
|error      |2      |NC       |NC         |
+-----------+-------+---------+-----------+



% errors / warnings by module
-----------------------------

+-------+-------+--------+---------+-----------+
|module |error  |warning |refactor |convention |
+=======+=======+========+=========+===========+
|simple |100.00 |0.00    |0.00     |100.00     |
+-------+-------+--------+---------+-----------+



Messages
--------

+-------------------------+------------+
|message id               |occurrences |
+=========================+============+
|invalid-name             |3           |
+-------------------------+------------+
|undefined-variable       |2           |
+-------------------------+------------+
|missing-module-docstring |1           |
+-------------------------+------------+
|missing-final-newline    |1           |
+-------------------------+------------+


-----------------------------------
Your code has been rated at 0.00/10
```

## Hata Çıktılarının Açıklamaları

* **`C0304: Final newline missing`**: PEP 8 kurallarına göre Python dosyalarının sonunda boş bir satır olmalıdır.
* **`C0114: Missing module docstring`**: Pylint, dosyanın en üstünde modülün işlevini açıklayan bir docstring (`''' ... '''`) bekler.
* **`C0103: Constant name "..." doesn't conform to UPPER_CASE...`**: Fonksiyon dışında (modül seviyesinde) tanımlanan değişkenleri Pylint "sabit (constant)" olarak kabul eder ve isimlerinin büyük harfle (`A`, `B`, `C` vb.) yazılmasını talep eder.
* **`E0602: Undefined variable 'B' / 'C'`**: Python büyük/küçük harfe duyarlıdır. Kodda `b` ve `c` tanımlanmışken, `print(B)` ve `print(C)` yazıldığı için tanımsız değişken hatası oluşur.

## Detaylı Rapor (Tablolar) Bölümlerinin Anlamları

Raporun alt kısmında yer alan tabloların ifade ettiği istatistikler şunlardır:

* **Statistics by type (Tip İstatistikleri):** Dosyadaki modül, sınıf (class), metot ve fonksiyonların sayılarını ve ne kadarının docstring ile açıklandığını (`%documented`) gösterir.
* **Raw metrics (Ham Metrikler):** Dosyanın satır analizidir. Toplam satırların yüzde kaçının gerçek kod (`code`), boş satır (`empty`), yorum (`comment`) veya docstring olduğunu belirtir.
* **Duplication (Tekrar):** Kodda birbirini tekrar eden (kopyala-yapıştır yapılmış) blokların oranını gösterir. Temiz kodda sıfıra yakın olması beklenir.
* **Messages by category (Kategoriye Göre Mesajlar):** Bulunan sorunları türlerine göre gruplar:
  * **Convention (C):** PEP 8 stil ve isimlendirme kuralları ihlalleri.
  * **Refactor (R):** Hata olmayan ancak daha iyi/verimli yazılabilecek kod blokları.
  * **Warning (W):** Kodu anında bozmayan ancak potansiyel risk taşıyan durumlar.
  * **Error (E):** Kodun çalışmasını engelleyen kritik hatalar (ör. tanımsız değişken).
* **% errors / warnings by module (Modüle Göre Hata/Uyarı Yüzdesi):** Hangi dosyanın/modülün toplam hataların yüzde kaçına sebep olduğunu gösterir. Çok dosyalı projelerde sorunlu dosyayı tespit etmeye yarar.
* **Messages (Mesajlar Özeti):** Spesifik hata kodlarının (`invalid-name`, `undefined-variable` vb.) toplamda kaç kez tekrar ettiğini sayan özet tablodur.
* **Global evaluation (Genel Değerlendirme):** Kodun genel kalite puanıdır. Hata ve uyarılar giderildikçe puan 10.00/10 seviyesine yaklaşır.

---


## Kodu Değiştirdikten Sonraki Rapor

### Code

```python
'''
A Very Simple Script
'''

def myfunc():
    '''
    A simple function
    '''
    first = 1
    second = 2
    #Printing first variable 'first'
    print(first)
    #Printing second variable 'second'
    print(second)

# Running myfunc function
myfunc()
```


```text
************* Module myfirst
myfirst.py:17:0: C0304: Final newline missing (missing-final-newline)


Report
======
6 statements analysed.

Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |0      |NC         |NC         |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|method   |0      |NC         |NC         |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|function |1      |NC         |NC         |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+



19 lines have been analyzed

Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |7      |36.84 |7        |=          |
+----------+-------+------+---------+-----------+
|docstring |6      |31.58 |NC       |NC         |
+----------+-------+------+---------+-----------+
|comment   |3      |15.79 |NC       |NC         |
+----------+-------+------+---------+-----------+
|empty     |3      |15.79 |1        |+2.00      |
+----------+-------+------+---------+-----------+



Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |0          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |1      |5        |5          |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |0          |
+-----------+-------+---------+-----------+
|warning    |0      |0        |0          |
+-----------+-------+---------+-----------+
|error      |0      |2        |2          |
+-----------+-------+---------+-----------+



% errors / warnings by module
-----------------------------

+--------+------+--------+---------+-----------+
|module  |error |warning |refactor |convention |
+========+======+========+=========+===========+
|myfirst |0.00  |0.00    |0.00     |100.00     |
+--------+------+--------+---------+-----------+



Messages
--------

+----------------------+------------+
|message id            |occurrences |
+======================+============+
|missing-final-newline |1           |
+----------------------+------------+




------------------------------------------------------------------
Your code has been rated at 8.33/10 (previous run: 0.00/10, +8.33)
```
## Kodda Ne Değişti ve Puan Neden Arttı?

* **Modül ve Fonksiyon Açıklamaları (Docstrings):** Kodun en başına modülün genel amacını belirten `''' A Very Simple Script '''`, fonksiyonun içine de ne işe yaradığını belirten `''' A simple function '''` açıklamaları eklendi. Pylint bu blokları gördüğü için "eksik dokümantasyon" hatalarını kaldırdı ve koda PEP 8 standartlarına uygunluktan puan verdi.
* **Tanımsız Değişken Hataları Giderildi (Errors):** Önceki versiyonda var olmayan `B` ve `C` değişkenleri ekrana yazdırılmaya çalışılmıştı. Yeni kodda bunlar tamamen kaldırılarak sadece fonksiyon içinde düzgünce tanımlanan `first` ve `second` kullanıldı. Bu sayede en büyük puan kırıcı etken olan `E0602: Undefined variable` hatası yok edildi.
* **İsimlendirme Kuralları Düzeltildi (Convention):** Önceki kodda değişkenler global alanda oluşturulduğu için Pylint onları "Sabit (Constant)" olarak değerlendirip isimlerinin BÜYÜK HARF olmasını beklemişti. Yeni kodda değişkenler `myfunc()` fonksiyonunun içine alındı. Lokal değişken oldukları için küçük harfle (first, second) yazılmaları kabul gördü ve isimlendirme cezaları silindi.
* **Genel Standartlara Uyum:** Yapılan temizlikler sonucunda puan **0.00'dan 8.33'e** yükseldi. Mükemmel 10 puana ulaşılamamasının tek nedeni, dosyanın en sonunda boş bir satır bırakılmamış olmasıdır (`C0304: Final newline missing`).

## İstatistiksel Olarak Tablodan Analiz:

* **Statistics by type (Tip İstatistikleri):** `%documented` sütununda modül (module) ve fonksiyon (function) değerlerinin **%100.00** olduğu görülüyor. Önceki çalışmada bu tablo, docstring eksikliği yüzünden zayıf kalmıştı.
* **Raw metrics (Ham Metrikler):** Toplam analiz edilen 19 satırın nasıl dağıldığı net bir şekilde ortaya çıktı. Satırların **%36.84**'ü çalışan kod, **%31.58**'i docstring (geniş açıklama), **%15.79**'u ise normal yorumlardan (`#`) oluşuyor. Bu durum, önceki sade haline kıyasla kodun artık ciddi şekilde belgelendirildiğini istatistiksel olarak ispatlıyor.
* **Messages by category (Kategoriye Göre Mesajlar):** Kodun düzeltilmesiyle tabloda çok ciddi bir iyileşme görünüyor:
  * **Convention (C):** Stil ihlalleri `previous` (önceki) turda 5 iken, şu an 1'e düşmüş (sadece eksik son boşluk).
  * **Error (E):** Kritik çalışma hataları önceden 2 iken (tanımsız değişkenler), şu an tamamen 0'a indirilmiş.
* **Puan İyileşmesi (Global Evaluation):** En alt satırdaki `(previous run: 0.00/10, +8.33)` verisi, Pylint'in aynı dosyanın eski halini hatırladığını ve düzeltmeler sayesinde koda tam **+8.33** net puan kazandırıldığını gösteriyor.