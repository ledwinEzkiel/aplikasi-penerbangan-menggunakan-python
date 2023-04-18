while True:
    import os
    so = os.name
    match so:
        case 'nt': os.system('cls')

    # Aplikasi Penerbangan
    # jp = jenis penerbangan
    # kkp = kode kelas penerbangan
    # jmp = jumlah penumpang
    # jtb = jumlah total bagasi
    # hpp = harga per penumpang
    # bbgs = bagasi total per penumpang
    # kb = kelebihan bagasi
    # ckb = cas kelebihan bagasi
    # tb = total bayar

    print("Aplikasi Penerbangan")
    print('=====================================================================================')
    jp = input('Masukan Jenis Penerbangan (Nasional/ Internasional)\t = ')
    kkp = input('Masukan Kode Kelas Penerbangan (B/E)\t\t\t = ')
    jmp = int(input('Masukan Jumlah Total Penumpang\t\t\t\t = ')) 
    jtb = int(input('Masukan Jumlah Total Bagasi\t\t\t\t = '))
    print('=====================================================================================')
    # if statement
    if(jp == 'Nasional' or jp == 'nasional'):
        jp = 'Nasional'
        if(kkp == 'B' or kkp == 'b'):
            kp = 'Bisnis'
            bagasi = 20
            if(jmp >= 1 and jmp <=10):
                hpp = 900000
                diskon = 0.1
                bbgs = bagasi * jmp
                if(jtb > bbgs):
                    kb = jtb - bbgs
                else:
                    kb = 0
            elif(jmp >= 11 and jmp <= 20):
                hpp = 895000
                diskon = 0.2
                bbgs = bagasi * jmp
                if(jtb > bbgs):
                    kb = jtb - bbgs
                else:
                    kb = 0
            else:
                hpp = 700000
                diskon = 0.3
                bbgs = bagasi * jmp
                if(jtb > bbgs):
                    kb = jtb - bbgs
                else:
                    kb = 0
        else:
            kp = 'Ekonomi'
            bagasi = 10
            if(jmp >= 1 and jmp <=10):
                hpp = 600000
                diskon = 0.1
                bbgs = bagasi * jmp
                if(jtb > bbgs):
                    kb = jtb - bbgs
                else:
                    kb = 0
            elif(jmp >= 11 and jmp <= 20):
                hpp = 585000
                diskon = 0.2
                bbgs = bagasi * jmp
                if(jtb > bbgs):
                    kb = jtb - bbgs
                else:
                    kb = 0
            else:
                hpp = 500000
                diskon = 0.3
                bbgs = bagasi * jmp
                if(jtb > bbgs):
                    kb = jtb - bbgs
                else:
                    kb = 0

    else:
        jp = 'Internasional'
        if(kkp == 'B' or kkp == 'b'):
            kp = 'Bisnis'
            bagasi = 30
            if(jmp >= 1 and jmp <=10):
                hpp = 2500000
                diskon = 0.1
                bbgs = bagasi * jmp
                if(jtb > bbgs):
                    kb = jtb - bbgs
                else:
                    kb = 0
            elif(jmp >= 11 and jmp <= 20):
                hpp = 2200000
                diskon = 0.2
                bbgs = bagasi * jmp
                if(jtb > bbgs):
                    kb = jtb - bbgs
                else:
                    kb = 0
            else:
                hpp = 2000000
                diskon = 0.3
                bbgs = bagasi * jmp
                if(jtb > bbgs):
                    kb = jtb - bbgs
                else:
                    kb = 0
            
        else:
            kp = 'Ekonomi'
            bagasi = 20
            if(jmp >= 1 and jmp <=10):
                hpp = 2000000
                diskon = 0.1
                bbgs = bagasi * jmp
                if(jtb > bbgs):
                    kb = jtb - bbgs
                else:
                    kb = 0
            elif(jmp >= 11 and jmp <= 20):
                hpp = 1850000
                diskon = 0.2
                bbgs = bagasi * jmp
                if(jtb > bbgs):
                    kb = jtb - bbgs
                else:
                    kb = 0
            else:
                hpp = 1700000
                diskon = 0.3
                bbgs = bagasi * jmp
                if(jtb > bbgs):
                    kb = jtb - bbgs
                else:
                    kb = 0

    sub_total = jmp * hpp
    potongan = sub_total * diskon
    ckb = kb * 50000
    tb = sub_total - potongan + ckb

    # output program
    print(f'Jenis Penerbangan\t\t= {jp}')
    print(f'Kelas Penerbangan\t\t= {kp}')
    print(f'bagasi per penumpang\t\t= {bagasi}Kg')
    print(f'Harga per Penumpang\t\t= Rp.{hpp}')
    print(f'diskon\t\t\t\t= {diskon}')
    print(f'sub harga\t\t\t= Rp.{sub_total}')
    print(f'Potongan\t\t\t= Rp.{potongan}')
    print(f'Kelebihan Bagasi\t\t= {kb}Kg')
    print(f'Cas Kelebihan Bagasi\t\t= Rp.{ckb}')
    print(f'Total Bayar\t\t\t= Rp.{tb}')
    print('=====================================================================================')

    loop = str(input("Apakah Anda ingin mengulang Program? [Y/T] = "))
    print('=====================================================================================')
    if (loop == 'Y' or loop == 'y'):
        so = os.name
        match so:
            case 'nt': os.system('cls')
    else:
        break
