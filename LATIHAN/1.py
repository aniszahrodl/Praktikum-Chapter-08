while True:
    try:
        n=int(input('Banyaknya bilangan bulat yang diinginkan:'))
        List=[]
        for i in range(n):
            Bil=print('Masukkan bilangan bulat ke-',str(i+1),':', end='')
            p=int(input())
            List.append(p)
        print('------------------------------------------------------')
        print('- Bilangan bulat:',List)
        List.sort(reverse=True)
        print('- Urutan bilangan dari yang terbesar:', List)
        break
    except ValueError:
        print('***Input tidak valid***')
        print('> ULANGI <')
