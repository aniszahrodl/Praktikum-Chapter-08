def RataHarga():
    List=[]
    for x in buah.values():
        List.append(x)
    
    Sum = 0
    for x in range(len(List)):
        a=List[x]
        Sum += a
    Average= Sum//len(List)
    print('Rata-rata harga satuan buah adalah',Average)
    

buah={'apel':5000,'jeruk':8500,'mangga':7800,'duku':6500}
RataHarga()
