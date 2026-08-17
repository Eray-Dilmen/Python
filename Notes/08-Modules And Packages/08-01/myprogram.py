# Bu dosya paketin içindeki kodları "çağırıp kullanan" patrondur.

from MyMainPackage import mymainprogram #paket içerisine girip ilgili modülü (.py scripti) çağırıyoruz
mymainprogram.mainreport() # çağırdığımız modüldeki fonksiyonu çağırıyoruz

from MyMainPackage.MySubPackage import mysubprogram
mysubprogram.subreport()
