modal = 100000000
laba = 0
untung = 0
for i in range(1,7,1):
    if(i<3):
        laba = 0
        untung = untung + laba
    elif(i<5):
     laba = modal*1/100
     untung = untung + laba
    elif(i<8):
     laba = modal*5/100
     untung = untung + laba
    else:
        laba = modal*2/100
        untung = untung + laba
    print("Laba Bulan ke-",i," Sebesar = Rp.",laba)
print("Total Laba Adalah : ",untung)