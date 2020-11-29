# no.1
print('[NO.1 - Membuat List]')
a=[1,5,6,3,6,9,11,20,12]
b=[7,4,5,6,7,1,12,5,9]
print('List a =',a)
print('List b =',b)
print('-----------------------------')
# no.2
print('[NO.2 - Menyisipkan suatu nilai ke dalam indeks tertentu]')
a.insert(3, 10)
b.insert(2, 15)
print('List a =',a)
print('List b =',b)
print('-----------------------------')
# no.3
print('[NO.3 - Menyisipkan suatu nilai ke dalam indeks terakhir]')
a.append(4)
b.append(8)
print('List a =',a)
print('List b =',b)
print('-----------------------------')
# no.4
print('[NO.4 - Mengurutkan data secara ascending]')
a.sort()
b.sort()
print('List a =',a)
print('List b =',b)
print('-----------------------------')
# no.5
print('[NO.5 - Membaca Sub-List]')
c= (a[:8])
d= (b[2:10])
print('List c =',c)
print('List d =',d)
print('-----------------------------')
# no.6
print('[NO.6 - Menjumlahkan setiap elemen list c dan d yang bersesuaian indeksnya]')
e=[]
for i in range(len(c)):
    p= c[i]+d[i]
    e.append(p)
print('List e =',e)
print('-----------------------------')
# no.7
print('[NO.7 - Mengubah list e menjadi tupple]')
E=tuple(e)
print('Tupple e =',E)
print('-----------------------------')
# no.8
print('[NO.8 - Mencari nilai min, maks, dan jumlahan seluruh elemen e]')
print('Elemen terkecil dari e:',min(E))
print('Elemen terbesar dari e:',max(E))
print('Jumlahan seluruh elemen e:',sum(E))
print('-----------------------------')
# no.9
print('[NO.9 - Membuat data String]')
myString= 'python adalah bahasa pemrograman yang menyenangkan'
print('myString =',myString)
print('-----------------------------')
# no.10
print('[NO.10 - Mengubah String menjadi Set]')
f=set(myString)
print('Karakter penyusun myString =',f)
print('-----------------------------')
# no.11
print('[NO.11 - Mengurutkan data Set sesuai alfabet dengan mengubahnya menjadi data list dulu]')
p=list(set(myString))
p.sort()
print('Karakter penyusun myString =',p)
