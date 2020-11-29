def dataStat(x):
    sum=0
    for i in range(len(x)):
        sum+=x[i]
    rataRata=sum/len(x)   
    List.append(rataRata)
    List.append(max(x))
    List.append(min(x))
    print(List)

x=[]
List=[]

try:
    print('Banyak nya bilangan yang diinginkan:',end='')
    n=int(input())

    for i in range(n):
        i+=1
        print('Masukkan bilangan ke-',str(i),':',end='')
        a=int(input())
        x.append(a)
    dataStat(x)
except ValueError:
    print('***Input Tidak Valid***')
    

