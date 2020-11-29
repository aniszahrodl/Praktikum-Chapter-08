def dataBuah():
    print('>>>>DAFTAR HARGA BUAH<<<<')
    for x,y in buah.items():
        print('-',x,'(Harga: Rp.', y,')')
    print('')

def tambah():
    print('Masukkan nama buah yang ingin ditambahkan:',end='')
    nama=input()
    if nama in buah:
        print('Buah',nama,'sudah ada di dalam daftar')
    else:
        print('Masukkan harga satuan:',end='')
        harga=int(input())
        buah[nama]=harga
    print('')
    global TambahLagi
    TambahLagi=input('Tambah data lagi? (y/n):')
    print('')

def beli():
    try:
        print('Buah yang ingin dibeli:',end='')
        A=input()
        print('Berapa Kg:',end='')
        B=int(input())
        p=buah[A]
        Total= p*B
        List.append(Total)
        print('')
        global BeliLagi
        BeliLagi=input('Beli lagi? (y/n):')
        print('')
    except KeyError:
        print('Buah tidak tersedia')
        print('')
        lagi=input('Beli lagi? (y/n):')
        print('')

def hapus():
    try:
        print('Nama buah yang ingin dihapus:',end='')
        hapus=input()
        del buah[hapus]
        global hapusLagi
        hapusLagi=input('Ada yang ingin dihapus lagi?(y/n):')
        print('')
    except KeyError:
        print(hapus,'tidak ada di daftar buah')
        hapusLagi=input('Ada yang ingin dihapus lagi?(y/n):')
        print('')
    
def menu():
    print('*****MENU*****')
    print('A. Tambah data buah')
    print('B. Beli buah')
    print('C. Hapus data buah')
    pilih=input('Pilihan Menu:')
    print('')
    if pilih=='A':
        tambah()
        while TambahLagi=='y':
            tambah()
        if  TambahLagi=='n':
            dataBuah()
        
    elif pilih=='B':
        dataBuah()
        beli()
        while BeliLagi=='y':
            beli()
        if BeliLagi=='n':
            sum=0
            for i in range(len(List)):
                sum+=List[i]
        print('--------------------------')
        print('TOTAL HARGA: Rp.',sum)

    elif pilih=='C':
        dataBuah()
        hapus()
        while hapusLagi=='y':
            hapus()
        if hapusLagi=='n':
            dataBuah()
        
    print('')
    global kembali
    kembali= str(input('Kembali ke Menu? (y/n):'))

    
List=[]        
buah={'apel':5000,
      'jeruk':8500,
      'mangga':7800,
      'duku':6500}

menu()
while kembali=='y':
    menu()
    if kembali=='n':
        break


    
