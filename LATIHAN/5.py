def kuadrat(bil):
    Kuadrat=[]
    for i in range(len(bil)):
        p=bil[i]**2
        Kuadrat.append(p)
    print(Kuadrat)

bil=[]
print('Banyaknya bilangan yang diinginkan:',end='')
n=int(input())

for i in range(n):
    print('Masukkan bilangan ke-',str(i+1),':',end='')
    a=int(input())
    bil.append(a)
print('Bilangan=',bil)
print('Hasil Kuadrat=', end='')
kuadrat(bil)
