n=int(input('Jumlah Mahasiswa:'))
nama=[]
for i in range(n):
      i+=1
      a=print('Nama Mahasiswa ke-',str(i),':',end='')
      x=str(input())
      nama.append(x)

nama.sort()
print('--------------------------------------')
for i in range (n):
    p=set(nama[i])
    q=(len(p))
    print(nama[i]+' (' + str(q) + ' Karakter)')
