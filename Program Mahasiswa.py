i=a=b=c=0
nama=[ ]
npm=[ ]
kls=[ ]
jur=[ ]
ang=[ ]
while True:
  print ('Masukkan data ke - ',i+1)
  nama.append(input('Nama Anda : '))
  npm.append(input('NPM Anda : '))
  if len(npm[i])!=8:
    print ('NPM Salah')        
    print
    nama.pop(i)
    npm.pop(i)
    continue
  kls.append(input('Kelas Anda : '))
  if len(kls[i])!=5:
    print ('Kelas Salah')
    print
    nama.pop(i)
    npm.pop(i)
    kls.pop(i)
    continue
  jur.append(kls[i][1:3])
  ang.append(npm[i][3:5])
  if jur[i]=='IA':
    jur[i]='Teknik Informatika'
    a+=1
  elif jur[i]=='IB':
    jur[i]='Teknik Industri'
    b+=1
  elif jur[i]=='IC':
    jur[i]='Teknik Mesin'
    c+=1
  else:
    print ('Kelas Salah')
    print
    continue
  lagi=''
  while lagi!='y' and lagi!='t':
    lagi=input('INPUT LAGI [Y/T] : ')
    i+=1
  if lagi=='t':
    break
print ('                        Daftar Mahasiswa')
print ('===============================================')
print ('    No    Nama    NPM        Kelas        Angkatan    Jurusan    ')
print ('================================================')
for n in range(i):
  print (n+1,'    ',nama[n],'   ',npm[n],' ',kls[n],'  ',ang[n],'        ',jur[n],'')
print ('TOTAL JURUSAN TEKNIK INFORMATIKA = ',a,'orang\n')
print ('TOTAL JURUSAN TEKNIK INDUSTRI = ',b,'orang\n')
print ('TOTAL JURUSAN TEKNIK MESIN = ',c,'orang\n')
ing=''
while ing!='y' and ing!='t':
  ing=input('Ingin melihat hasil [Y/T]? ')
  if ing=='y':
    cari=input('Cari berdasarkan NPM : ')
    for n in range(i):
      if cari==npm[n]:
        print
        print ('Nama :',nama[n])
        print ('Kelas :',kls[n])
        print ('Angkatan :',ang[n])
        print ('Jurusan :',jur[n])
        break
    else:
      print ('NPM TIDAK ADA')
      break
