def hargaMahal():
    List1=[]
    List2=[]
    for x,y in buah.items():
        print('-',x,', Harga: Rp.',y,)
        List1.append(y)
        List2.append(x)
    a=max(List1)
    b=List1.index(a)
    print('Buah yang harganya paling mahal adalah:',List2[b])
    

buah={'apel':5000,'jeruk':8500,'mangga':7800,'duku':6500}
print('*****DAFTAR HARGA BUAH*****')

hargaMahal()
