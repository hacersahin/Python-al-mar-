"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""
boy = float( input("Boy:"))
kilo = int( input("Kilo:"))

print( "Beden Kitle İndeksi:", kilo/ (boy ** 2))