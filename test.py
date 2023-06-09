from cgitb import text
from bs4 import BeautifulSoup
import requests

link = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-DIYogyakarta.xml"
def info(link):
    page = requests.get(link)
    sop = BeautifulSoup(page.text, features="xml")
    #KODE KABUPATEN
    print('''=========================== Kode Kabupaten Sesuai Nomor Urutan ===========================
1.  Kabupaten Bantul
2.  Kabupaten Sleman
3.  Kabupaten Wates
4.  Kabupaten Gunung Kidul
5.  Kota Yogyakarta
    ''')

    
    x = ""
    #INPUT KODE KABUPATEN
    input_kota = str(input("Masukkan Kabupaten/Kota di D.I.Yogyakarta : "))
    if input_kota == "1":
        x = "501186"
        
    elif input_kota == "2":
        x = "501187"
    elif input_kota == "3":
        x = "501188"
    elif input_kota == "4":
        x = "501189"
    elif input_kota == "5":
        x = "501190"
    else:
        print("Kode yang anda input salah/tidak sesuai !!!")
    
            
    # Menggunakan BS4 utk scraping/parsing halaman web
    # Utk mencari elemen pada "id"
    infobanjir = sop.find_all(id = x) #sop.find_all = pemanggilan metode pada objek 'sop' & metode library bs4
    h = ""
    for i in infobanjir:
    # "infobanjir" akan berisi daftar elemen yang sesuai dengan pencarian
        print()
        print('''========================== input Waktu dalam waktu 3 hari kedepan ==========================

Kode Hari:
~~~Besok~~~
~~~Lusa~~~
~~~3 Hari kedepan~~~

Kode Jam:
1 - 24

example : Input_hari    = besok
          Input_jam     = 7    

''')
        # 7 - 12 = format 12 jam (7 AM hingga 12 PM)
        listwaktu1 = ["7","8","9","10","11","12"]
        # 13 - 18 =  format 24 jam (1 PM hingga 6 PM)
        listwaktu2 = ["13","14","15","16","17","18"]
        # 19 - 24 = format 24 jam (7 PM hingga 12 AM)
        listwaktu3 = ["19","20","21","22","23","24"]
        # 1 - 6 = format 24 jam (1 AM hingga 6 AM)
        listwaktu4 = ["1","2","3","4","5","6"]

        #Input Hari dan Waktu yang mau dimasukkan
        input_waktu = str(input("Masukkan Hari yang diinginkan  : ").lower())

        #Waktu Besok
        h = ""
        if input_waktu == "besok":
            input_jam = str(input("Masukkan waktu yang diinginkan : "))
            if input_jam in listwaktu1:
                h += "0"
            elif input_jam in listwaktu2:
                h += "6"
            elif input_jam in listwaktu3:
                h += "12"
            else:
                print("Salah input bro, coba lagi!")
                break

        #Waktu Lusa
        elif input_waktu == "lusa":
            input_jam = str(input("Masukkan waktu yang diinginkan : "))
            if input_jam in listwaktu1:
                h += "24"
            elif input_jam in listwaktu2:
                h += "30"
            elif input_jam in listwaktu3:
                h += "36"
            elif input_jam in listwaktu4:
                h += "18"
            else:
                print("Salah input bro, coba lagi!")

        #Waktu 3 Hari kedepan
        elif input_waktu == "3 hari kedepan":
            input_jam = str(input("Masukkan waktu yang diinginkan : "))
            if input_jam in listwaktu1:
                h += "48"
            elif input_jam in listwaktu2:
                h += "54"
            elif input_jam in listwaktu3:
                h += "60"
            elif input_jam in listwaktu4:
                h += "42"
            else:
                print("Salah input bro, coba lagi!")
        else:
            print("salah input bro, coba lagi!")
        
        #Input CurahHujan
        input_curahhujan = float(input("Masukkan Curah hujan dalam mm  : "))
        print("=============================================================")

        #Kelembapan Udara
        total_kelembapan_udara = 0
        kelembapan_udara = int(i.find(id="hu").find(h=h).find(unit="%").text)
        rumus_kUdara = 0
        if kelembapan_udara <= int(60):
            print(f"Kelembapan udara pada {input_waktu} sangat rendah sebesar", kelembapan_udara,"%  dan berada pada persentase sebesar 20%" )
            total_kelembapan_udara += 20
            rumus_kUdara = (total_kelembapan_udara/100 * 25/100)*100

        elif kelembapan_udara >= int(61) and kelembapan_udara <= int(70):
            print(f"Kelembapan udara pada {input_waktu} rendah sebesar", kelembapan_udara,"%  dan berada pada persentase sebesar 40%") 
            total_kelembapan_udara += 40
            rumus_kUdara = (total_kelembapan_udara/100 * 25/100)*100

        elif kelembapan_udara >= int(71) and kelembapan_udara <= int(80):
            print(f"Kelembapan udara pada {input_waktu} Sedang sebesar", kelembapan_udara,"%  dan berada pada persentase sebesar 60%") 
            total_kelembapan_udara += 60 
            rumus_kUdara = (total_kelembapan_udara/100 * 25/100)*100

        elif kelembapan_udara <= int(81) and kelembapan_udara <= int(90):
            print(f"Kelembapan udara pada {input_waktu} Tinggi sebesar", kelembapan_udara,"%  dan berada pada persentase sebesar 80%") 
            total_kelembapan_udara += 80
            rumus_kUdara = (total_kelembapan_udara/100 * 25/100)*100

        elif kelembapan_udara >= int(91):
            print(f"Kelembapan udara pada {input_waktu} Sangat Tinggi sebesar", kelembapan_udara,"%  dan berada pada persentase sebesar 100%") 
            total_kelembapan_udara += 100
            rumus_kUdara = (total_kelembapan_udara/100 * 25/100)*100

        #Suhu Udara
        total_suhuudara = 0
        suhu_udara = int(i.find(id="t").find(h=h).find(unit="C").text)
        rumusSuhu = 0
        if suhu_udara <= int(25):
            print(f"Suhu Udara diperkirakan pada {input_waktu} Dingin dengan suhu", suhu_udara, "C dan berada pada persentase sebesar 100%")
            total_suhuudara += 100
            rumusSuhu = (total_suhuudara/100 * 25/100)*100 

        elif suhu_udara >= int(26) and suhu_udara <= int(27):
            print(f"Suhu Udara diperkirakan pada {input_waktu} Normal dengan suhu", suhu_udara, "C dan berada pada persentase sebesar 75%")
            total_suhuudara += 75
            rumusSuhu = (total_suhuudara/100 * 25/100)*100 

        elif suhu_udara >= int(28) and  suhu_udara <= int(29):
            print(f"Suhu Udara diperkirakan pada {input_waktu} Panas dengan suhu", suhu_udara, "C dan berada pada persentase sebesar 40%")
            total_suhuudara += 40
            rumusSuhu = (total_suhuudara/100 * 25/100)*100 

        elif suhu_udara >= int(30):
            print(f"Suhu Udara diperkirakan pada {input_waktu} Sangat Panas dengan suhu", suhu_udara, "C dan berada pada persentase sebesar 5%")
            total_suhuudara += 5
            rumusSuhu = (total_suhuudara/100 * 25/100)*100 

        #Kecepatan Angin
        total_kecepatanangin = 0
        kecepatan_angin = int(i.find(id="ws").find(h=h).find(unit="Kt").text)
        rumus_kAngin = 0
        if kecepatan_angin >= int(23):
            print(f"Kecepatan Angin diperkirakan pada {input_waktu} Tinggi sebesar", kecepatan_angin, "Knot dan berada pada persentase sebesar 100%")
            total_kecepatanangin += 100
            rumus_kAngin = (total_kecepatanangin/100 * 25/100)*100

        elif kecepatan_angin >= int(11) and suhu_udara <= int(22):
            print(f"Kecepatan Angin diperkirakan pada {input_waktu} Sedang sebesar", kecepatan_angin, "Knot dan berada pada persentase sebesar 75%")
            total_kecepatanangin += 75
            rumus_kAngin = (total_kecepatanangin/100 * 25/100)*100

        elif kecepatan_angin >= int(1) and kecepatan_angin <= int(5):
            print(f"Kecepatan Angin diperkirakan pada {input_waktu} Pelan sebesar", kecepatan_angin, "Knot dan berada pada persentase sebesar 20%")
            total_kecepatanangin += 20
            rumus_kAngin = (total_kecepatanangin/100 * 25/100)*100

        elif kecepatan_angin >= int(6) and kecepatan_angin <= int(10):
            print(f"Kecepatan Angin diperkirakan pada {input_waktu} Normal sebesar", kecepatan_angin, "Knot dan berada pada persentase sebesar 50%")
            total_kecepatanangin += 50
            rumus_kAngin = (total_kecepatanangin/100 * 25/100)*100

      #Curah Hujan
        total_curahhujan = 0
        rumus_curahhujan = 0
        if input_curahhujan == 0:
            print(f"Curah hujan sebesar {input_curahhujan}mm diprediksi Berawan dengan persentase sebesar 0%")
            total_curahhujan += 0
            rumus_curahhujan = (total_curahhujan/100 * 25/100)*100

        elif input_curahhujan >= int(1) and input_curahhujan <= int(20):
            print(f"Curah Hujan sebesar {input_curahhujan}mm diprediksi Hujan Ringan dengan persentase sebesar 20%")
            total_curahhujan += 20
            rumus_curahhujan = (total_curahhujan/100 * 25/100)*100
        
        elif input_curahhujan >= int(21) and input_curahhujan <= int(50):
            print(f"Curah Hujan sebesar {input_curahhujan}mm diprediksi Hujan Sedang dengan persentase sebesar 40%")
            total_curahhujan += 40
            rumus_curahhujan = (total_curahhujan/100 * 25/100)*100
         
        elif input_curahhujan >= int(51) and input_curahhujan <= int(100):
            print(f"Curah Hujan sebesar {input_curahhujan}mm diprediksi Hujan Lebat dengan persentase sebesar 60%")
            total_curahhujan += 60
            rumus_curahhujan = (total_curahhujan/100 * 25/100)*100

        elif input_curahhujan >= int(101) and input_curahhujan <= int(150):
            print(f"Curah Hujan sebesar {input_curahhujan}mm diprediksi Hujan Sangat Lebat dengan persentase sebesar 80%")
            total_curahhujan += 80
            rumus_curahhujan = (total_curahhujan/100 * 25/100)*100
        
        elif input_curahhujan > 150:
            print(f"Curah Hujan sebesar {input_curahhujan}mm diprediksi Hujan Ekstrem dengan persentase sebesar 100%")
            total_curahhujan += 80
            rumus_curahhujan = (total_curahhujan/100 * 25/100)*100

    
        print("======================================================")
        print("Potensi Curah Hujan adalah       :",rumus_curahhujan,"%")
        print("Potensi Kecepatan Angin adalah   :",rumus_kAngin,"%")
        print("Potensi Kelembaban Udara adalah  :",rumusSuhu,"%")
        print("Potensi Suhu Udara adalah        :",rumus_kUdara,"%")
        print("Potensi terjadi banjir adalah    :",(rumus_curahhujan+rumus_kAngin+rumusSuhu+rumus_kUdara),"%")

        
info(link)