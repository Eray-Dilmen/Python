# Bu dosya projeyi çalıştıracağımız ana dosyadır.
# 'calculator.py' dosyasındaki fonksiyonları kullanmak için import ederiz.

import calculator
# 'import calculator' satırı çalıştığı an Python calculator.py dosyasını okudu:
#  1. 'add' ve 'multiply' fonksiyonlarını belleğe yükledi (kullanıma hazır).
#  2. 'if __name__ == "__main__":' satırına geldi.
#  3. Dosya import edildiği için __name__ değeri "__main__" DEĞİL "calculator" oldu.
#  4. Bu yüzden calculator.py içindeki test kodlarını VE print'leri ATLADI.
#  5. Ekrana kirlilik yaratacak hiçbir test çıktısı basılmadı.

if __name__ == "__main__":
    print(" main.py ÇALIŞTIRILDI ")

    # Artık calculator.py içindeki fonksiyonları kendi kontrolümüzle çağırıyoruz:
    result1 = calculator.add(20, 30)
    result2 = calculator.multiply(5, 5)

    print(f"Main içinden Toplama Sonucu: {result1}")
    print(f"Main içinden Çarpma Sonucu: {result2}")