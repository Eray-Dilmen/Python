# CALCULATOR.PY - YARDIMCI MODÜL
# Bu dosya bir "kütüphane/modül" olarak tasarlanmıştır.
# Amacı fonksiyonları barındırmaktır.


def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


# __name__ VE "__main__" KONTROL BLOĞU
# Python bu dosyayı çalıştırırken __name__ adında gizli bir değişken oluşturur.
# 1. Eğer bu dosya DOĞRUDAN çalıştırılırsa (Terminal: python calculator.py):
#    -> __name__ değişkeninin değeri "__main__" olur.
#    -> Aşağıdaki 'if' koşulu TRUE çıkar ve bloğun içindeki kodlar çalışır.

# 2. Eğer bu dosya BAŞKA BİR DOSYADAN 'import calculator' edilirse:
#    -> __name__ değişkeninin değeri "calculator" (dosya adı) olur.
#    -> "calculator" == "__main__" koşulu FALSE çıkacağı için Python bu bloğu ATLAR.
#    -> İçindeki test kodları, print'ler ve fonksiyon çağrıları ÇALIŞMAZ.

if __name__ == "__main__": # Dosya çalıştırıldığında çalışacak kısım buranın aşağısı
    print(" calculator.py DOĞRUDAN ÇALIŞTIRILDI ")
    print("Bu blok sadece dosyayı tek başına test ederken görünür.")

    # Test çağrıları (Import edildiğinde ortalığı karıştırmasın diye buradalar):
    test1 = add(5, 10)
    test2 = multiply(4, 3)

    print(f"Toplama Testi (5+10): {test1}")
    print(f"Çarpma Testi (4x3): {test2}")