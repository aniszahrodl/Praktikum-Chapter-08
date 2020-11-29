print('--------------------------')
print('DAFTAR HARGA BUAH')
print('--------------------------')
buah={'apel':5000,
      'jeruk':8500,
      'mangga':7800,
      'duku':6500}

for x,y in buah.items():
    print(x,'-> Harga: Rp',y)
print('')
try:
    print('Buah yang dibeli:',end='')
    A=input()
    print('Berapa Kg:',end='')
    B=int(input())
    p=buah[A]
    Total= p*B
    print('--------------------------')
    print('TOTAL HARGA: Rp.',Total)
except KeyError:
    print(A,'tidak ada di dalam daftar')
except ValueError:
    print('Input tidak valid')
