Sayur=['Bayam','Kangkung','Wortel','Selada']

def dataSayur():
    print('*****DATA SAYUR*****')
    for i in range (len(Sayur)):     
        print('-',Sayur[i])

def tambah():
    print('Masukkan nama sayur yang ingin ditambahkan:',end='')
    tambahSayur=input()
    if tambahSayur in Sayur:
        print('Sayur',tambahSayur,'sudah ada di dalam daftar')
    else:
        Sayur.append(tambahSayur)
    print('')
    global TambahLagi
    TambahLagi=input('Tambah data lagi? (y/n):')
    print('')

def hapus():
    try:
        print('Nama sayur yang ingin dihapus:',end='')
        nama=input()
        p=Sayur.index(nama)
        del Sayur[(p)]
        global hapusLagi
        hapusLagi=input('Ada yang ingin dihapus lagi?(y/n):')
        print('')
    except ValueError:
        print(nama,'tidak ada di dalam daftar sayur')
        hapusLagi=input('Ada yang ingin dihapus lagi?(y/n):')

def menu():
    print('-----------------------------')
    menu=print('Menu:')
    print('-----------------------------')
    print('A. Tampilkan Data Sayur')
    print('B. Tambah Data Sayur')
    print('C. Hapus Data Sayur')

    print('')
    pilih=str(input('Pilihan Anda:'))
    print('')

    if pilih=='A':
        dataSayur()
    elif pilih=='B':
        tambah()
        while TambahLagi=='y':
            tambah()
        if  TambahLagi=='n':
            dataSayur()
    elif pilih=='C':
        hapus()
        while hapusLagi=='y':
            hapus()
        if hapusLagi=='n':
            dataSayur()
    else:
        print('input tidak valid')
    print('')
    global lagi
    lagi= str(input('Kembali ke Menu? (y/n):'))

       

menu()
while lagi=='y':
    menu()
    if lagi=='n':
        break
    
