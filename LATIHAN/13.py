print('             DAFTAR NILAI MAHASISWA')
print('----------------------------------------------------')

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

MID=[]
UAS=[]
nilai=[]
for i in range(len(nilaiMhs)):
    a=nilaiMhs[i]
    print(a)
    b=a['mid']
    MID.append(b)
    d=a['uas']
    UAS.append(d)
    
for x in range(len(MID)):
    nilaiAkhir=(MID[x]+(2*UAS[x]))/3
    nilai.append(nilaiAkhir)

Max=nilai.index(max(nilai))
p=nilaiMhs[Max]
nim=p['nim']
nama=p['nama']
print('')
print('Mahasiswa yang mendapat nilai akhir paling tinggi adalah:')
print('- NIM:',nim)
print('- Nama:',nama)
