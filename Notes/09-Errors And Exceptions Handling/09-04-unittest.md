# Pylint vs. Unittest Farkı

**Hayır, unittest aynı şeyi yapmaz.** Pylint ile Unittest tamamen farklı amaçlara hizmet eden iki ayrı kavramdır.

Aralarındaki temel fark şudur:

---

## 1. Pylint (Statik Kod Analiz Aracı)

* **Ne yapar?** Kodu **çalıştırmadan** (statik olarak) inceler.
* **Neye bakar?** Yazım kurallarına (PEP 8), değişken isimlerine, girintilere ve olası mantık hatalarına bakar.
* **Soru cümlesi:** *"Bu kod düzgün yazılmış mı, standartlara uygun mu?"*

---

## 2. Unittest (Birim Test Kütüphanesi)

* **Ne yapar?** Kodu **bizzat çalıştırır**.
* **Neye bakar?** Kodun fonksiyonlarının beklenen girdilere karşı **doğru çıktıları (sonuçları)** verip vermediğine bakar.
* **Soru cümlesi:** *"Bu kod doğru çalışıyor mu, hesaplamayı mantıksal olarak doğru yapıyor mu?"*

---

## Örnekle Açıklama

Aşağıdaki fonksiyonu düşün:

```python
def topla(a, b):
    return a - b  # HATA: Toplamak yerine yanlışlıkla çıkardık!
```
* **Pylint bu koda bakıp:** *"Kodun yazımı çok güzel, PEP 8'e uygun, değişken isimleri doğru. Puanın 10/10!"* der. Çünkü Pylint matematiksel mantığın doğru olup olmadığını bilemez.


* **Unittest ise:** `topla(2, 3)` fonksiyonunu çalıştırır. Beklenen cevap `5` iken fonksiyon `-1` döndürdüğü için **TEST BAŞARISIZ (FAIL)** hatası verir.

**Özet:** Pylint kodun **biçimine ve kalitesine** bakar, Unittest ise kodun **işlevine ve doğruluğuna** bakar.


---

## Unittest Test Kodu ve Hata Raporu Analizi


### 1) cap.py dosyası (Hedef Kod)

```python
def cap_text(text):
    return text.capitalize()
```


### 2) Test Kodu (`test_cap.py`)

```python
# test_cap.py dosyası (Test Kodu)
import unittest
import cap # cap.py dosyasını çağırıyoruz

class TestCap(unittest.TestCase): # Testi çalıştırabilmek için CLASS şart! ve içerisine parent olarak unittest'in özelliğini koyuyoruz, miras alıyor bu class (pythonda miras alma parantez içine yazarak yapılıyordu)
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text) # Düz fonksiyonu test ediyoruz
        self.assertEqual(result, 'Python')
        
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')
        
    def test_with_apostrophes(self):
        text = "monty python's flying circus"
        result = cap.cap_text(text)
        self.assertEqual(result, "Monty Python's Flying Circus")

if __name__ == '__main__':
    unittest.main()
```

## Terminalde 'python test_cap.py' Çalıştırıldıktan Sonra Rapor:

```text
F.F
======================================================================
FAIL: test_multiple_words (__main__.TestCap.test_multiple_words)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_cap.py", line 16, in test_multiple_words
    self.assertEqual(result, 'Monty Python')
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'Monty python' != 'Monty Python'
- Monty python
?       ^
+ Monty Python
?       ^


======================================================================
FAIL: test_with_apostrophes (__main__.TestCap.test_with_apostrophes)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_cap.py", line 21, in test_with_apostrophes
    self.assertEqual(result, "Monty Python's Flying Circus")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: "Monty python's flying circus" != "Monty Python's Flying Circus"
- Monty python's flying circus
?       ^        ^      ^
+ Monty Python's Flying Circus
?       ^        ^      ^


----------------------------------------------------------------------
Ran 3 tests in 0.003s

FAILED (failures=2)
```

### 3) Test Raporunun Detaylı Analizi

Bu raporda toplam **3 adet test** çalıştırılmış ve **2 tanesi başarısız (FAILED)** olmuştur. Hataların teknik detayları şöyledir:

**1. `F.F` İfadesinin Anlamı**
En üstte yer alan `F.F` ifadesi, testlerin sırasıyla başarı durumlarını gösterir. Unittest, metotları alfabetik sırayla çalıştırır:
* `F` (Fail): İlk test (`test_multiple_words`) başarısız.
* `.` (Nokta): İkinci test (`test_one_word`) başarılı.
* `F` (Fail): Üçüncü test (`test_with_apostrophes`) başarısız.

**2. Hata Çıktısındaki İşaretlerin (Diff) Anlamı**
AssertionError (İddia Hatası) kısmında gösterilen işaretler, iki metin arasındaki harf uyuşmazlıklarını gösterir:
* **`-` işareti:** `cap.py` dosyasındaki fonksiyonun ürettiği yanlış çıktı.
* **`+` işareti:** Senin `assertEqual` içine yazdığın, olması gereken doğru çıktı.
* **`?` ve `^` işaretleri:** Tam olarak hatanın hangi harflerde olduğunu (büyük/küçük harf uyuşmazlığı) işaret eder.

**3. Birinci Hata Neden Kaynaklandı? (`test_multiple_words`)**
* **Beklenen:** `Monty Python`
* **Gelen:** `Monty python`
* **Neden:** `cap.py` dosyasının içindeki fonksiyon, `text.capitalize()` fonksiyonunu kullanıyor. `capitalize()` fonksiyonu sadece string'in en başındaki ilk harfi büyütür, diğer kelimelere dokunmaz. Test tek kelimelik (`test_one_word`) olduğunda geçti; ancak iki kelimelik olduğunda ikinci kelimenin baş harfi küçük kaldığı için test patladı.

**4. İkinci Hata Neden Kaynaklandı? (`test_with_apostrophes`)**
* **Beklenen:** `Monty Python's Flying Circus`
* **Gelen:** `Monty python's flying circus`
* **Neden:** Yukarıdaki hatanın aynısıdır. String'in en başındaki "M" büyütülmüş, geri kalan kelimelerin ("python's", "flying", "circus") ilk harfleri küçük bırakılmıştır.

**Nasıl Düzeltilir?**
Bu testlerin üçünün de nokta (`. . .`) verip başarılı olması için, `cap.py` içerisindeki fonksiyonun tüm kelimelerin ilk harfini büyütecek şekilde düzeltilmesi gerekir. Hedef koddaki `.capitalize()` yerine, her kelimenin baş harfini büyüten `.title()` metodu kullanılmalıdır (Ör: `return text.title()`).

---

### 4) `text.title()` Değişikliği Sonrası Yeni Durum

`cap.py` dosyasındaki `cap_text` fonksiyonunda yer alan `text.capitalize()` ifadesini `text.title()` olarak değiştirdiğimizde aldığımız yeni test raporu:

```text
..F
======================================================================
FAIL: test_with_apostrophes (__main__.TestCap.test_with_apostrophes)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_cap.py", line 21, in test_with_apostrophes
    self.assertEqual(result, "Monty Python's Flying Circus")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: "Monty Python'S Flying Circus" != "Monty Python's Flying Circus"
- Monty Python'S Flying Circus
?              ^
+ Monty Python's Flying Circus
?              ^


----------------------------------------------------------------------
Ran 3 tests in 0.003s

FAILED (failures=1)
```

### Rapor Analizi: Ne Değişti, Ne Oldu?

* **İkinci Test Başarıyla Geçti:** En üstteki `..F` ifadesinden de anlaşılacağı üzere, artık ilk iki test (`test_one_word` ve `test_multiple_words`) başarılı (`.`) sonuçlandı. `text.title()` kullanımı sayesinde birden fazla kelimenin baş harflerini büyütme sorunu çözüldü ve hata sayımız 2'den 1'e düştü.


* **Üçüncü Test Neden Patladı?** (`test_with_apostrophes`)
  * **Beklenen:** `Monty Python's Flying Circus`
  * **Gelen:** `Monty Python'S Flying Circus`
  * **Neden:** `.title()` metodu, kelime sınırlarını belirlerken kesme işaretini (`'`) de bir boşluk veya noktalama gibi kelime ayracı olarak kabul eder. Bu yüzden `python's` kısmını tek bir kelime olarak değil, "python" ve "s" olarak iki ayrı parça şeklinde algıladı. Sonuç olarak kesme işaretinden sonraki "s" harfini de büyüterek `Python'S` çıktısını üretti ve testimiz bu yüzden başarısız oldu (FAIL).

--- 

### 5) 3.Testin Hata Vermesini Nasıl Engelleriz?

### 5) 3. Testin Hata Vermesini Nasıl Engelleriz?

Kesme işareti (`'`) içeren metinlerde `.title()` metodunun hatasını (`Python'S`) engellemek için, `string` modülü içerisindeki `capwords()` fonksiyonunu kullanmalıyız. Tabii ki bu modülü kullanabilmemiz için kodun en başına `import string` yazarak `string` kütüphanesini projeye dahil etmemiz gerekiyor.

#### `cap.py` Dosyasının Güncellenmiş Hali
```python
import string

def cap_text(text):
    return string.capwords(text)
```

#### Mekanizma Nasıl Çalışır?

**1. `text.title()` neden yetersiz kaldı?**
`title()` fonksiyonu harf olmayan **her türlü karakteri** (boşluk, nokta, tire, kesme işareti `'` vb.) ayraç kabul eder. Bu yüzden `python's` yapısındaki `'` işaretini görünce `s` harfini yeni bir kelimenin başı sanıp `S` yaptı.

**2. `string.capwords()` ne yapar?**
Varsayılan olarak metni **sadece boşluklardan (` `)** ayırır.

*   `text = 'python'` -> Tek kelime, baş harfini büyütür: `Python` **(1. Test Geçer)**
*   `text = 'monty python'` -> Boşluktan böler, her parçanın ilk harfini büyütür: `Monty Python` **(2. Test Geçer)**
*   `text = "monty python's flying circus"` -> Kesme işaretini (`'`) ayraç saymaz. Sadece boşluklardan böldüğü için `python's` yapısını bozmadan ilk harfini büyütür: `Monty Python's Flying Circus` **(3. Test Geçer)**

Yani `capwords()`, ilk iki testin mantığını korurken kesme işaretinin yarattığı yan etkiyi ortadan kaldırır.

### 6) Sonuç: Testlerin Başarıyla Tamamlanması

`cap.py` dosyasında yaptığımız `string.capwords()` güncellemesinden sonra terminalde aldığımız son çıktı şu şekildedir:

```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```