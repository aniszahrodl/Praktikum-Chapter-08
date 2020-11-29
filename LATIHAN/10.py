def InputBuah():
    try:
        print('Buah yang ingin dibeli:',end='')
        A=input()
        print('Berapa Kg:',end='')
        B=int(input())
        p=buah[A]
        Total= p*B
        List.append(Total)
        print('')
        global lagi
        lagi=input('Beli lagi? (y/n):')
        print('')
    except KeyError:
        print('Buah tidak tersedia')
        print('')
        lagi=input('Beli lagi? (y/n):')
        print('')

List=[]
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
InputBuah()
while lagi=='y':
    InputBuah()
    
if lagi=='n':
    sum=0
    for i in range(len(List)):
        sum+=List[i]
    print('--------------------------')
    print('TOTAL HARGA: Rp.',sum)

