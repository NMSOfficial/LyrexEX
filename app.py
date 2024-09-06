import tkinter as tk
from tkinter import messagebox
import random
from tkinter import ttk
import time

liderler = [
    ("Mete Han", "Hun İmparatorluğu'nun kurucusu ve ilk hükümdarı. Türk Silahlı Kuvvetlerinin kurucusudur.",
     "Yiğit LyrexEX, ömrün uzun, kılıcın keskin olsun! Doğduğun gün kutlu olsun!"),
    ("Atilla", "Avrupa Hun İmparatorluğu'nun lideri, Batı Roma İmparatorluğu'na karşı büyük seferler düzenledi.",
     "Ey LyrexEX, Hun soyundan gelen cesur yoldaşım! Bu mübarek günde güç ve kudretin daim olsun."),
    ("Bilge Kağan", "Göktürk Kağanlığı'nın önemli hükümdarlarından biri, devlet yönetiminde bilge kişiliğiyle tanındı.",
     "Kutlu LyrexEX, göklerden aldığın ilhamla bilge ol, devletin ve milletin için hayırlı hizmetlerde bulun. Doğum günün kutlu olsun!"),
    ("Kürşad", "Göktürklerin efsanevi liderlerinden, Çin'e karşı ayaklanma başlatan kahraman.",
     "Kahraman LyrexEX, yüreğindeki ateş sönmesin, milletin için dimdik ayakta durasın! Doğum günün kutlu olsun."),
    ("Tonyukuk", "Göktürk Kağanlığı'nda önemli bir devlet adamı ve danışman.",
     "Ey LyrexEX, aklını doğru kullan, milletine faydalı ol. Doğduğun gün kutlu, yolun açık olsun."),
    ("Alparslan", "Büyük Selçuklu Devleti'nin ikinci sultanı, 1071 Malazgirt Zaferi ile Anadolu'nun kapılarını Türklere açtı.",
     "Yiğit LyrexEX, Malazgirt’in zafer ruhu seninle olsun, doğum günün kutlu, ömrün fetihle dolu olsun."),
    ("Melikşah", "Büyük Selçuklu Devleti'nin en parlak dönemini yaşatan hükümdar.",
     "Ey LyrexEX, adaletle hükmet, daima doğruyu savun. Doğum günün kutlu olsun, devletin payidar olsun."),
    ("Nizamülmülk", "Büyük Selçuklu Devleti'nin ünlü veziri, devlet yönetimi üzerine yazdığı 'Siyasetname' ile tanınır.",
     "LyrexEX, bil ki adalet mülkün temelidir. Doğum gününde sana adil ve hikmet dolu bir ömür dilerim."),
    ("Osman Gazi", "Osmanlı İmparatorluğu'nun kurucusu ve ilk padişahı.",
     "Dost LyrexEX, bu mübarek günde Allah yolunu açık etsin, soyun daim, ömrün bereketli olsun."),
    ("Orhan Gazi", "Osmanlı Devleti'nin ikinci padişahı, fetihlerle Osmanlı topraklarını genişletti.",
     "Ey LyrexEX, fetih yolunda nice başarılarla dolu bir ömür dilerim. Doğum günün mübarek olsun."),
    ("Yıldırım Bayezid", "Osmanlı padişahı, Niğbolu Savaşı'nda Haçlı ordusunu mağlup etti.",
     "LyrexEX, doğum gününde sana yıldırım gibi bir kuvvet, zaferlerle dolu bir ömür dilerim."),
    ("Fatih Sultan Mehmet", "İstanbul'un fatihi. Dünyanın ve Türk tarihinin en büyük liderlerinden.",
     "Cihanı titreten LyrexEX, doğum gününde fetih ruhu seninle olsun. Nice zafer dolu yıllara!"),
    ("Kanuni Sultan Süleyman", "Osmanlı İmparatorluğu'nun en uzun süre tahtta kalan padişahı, 'Muhteşem Süleyman' olarak tanınır.",
     "Ey LyrexEX, cihanın dört bir yanına hükmeden bir irade ile dolu bir ömür dilerim. Doğum günün kutlu olsun."),
    ("Yavuz Sultan Selim", "Osmanlı İmparatorluğu'nu genişleten padişah, Mısır Seferi ile halifeliği Osmanlı'ya taşıdı.",
     "Yiğit LyrexEX, doğum gününde Allah’tan sana güç, kuvvet ve sarsılmaz bir irade diliyorum."),
    ("Mustafa Kemal Atatürk", "Türkiye Cumhuriyeti'nin kurucusu ve ilk Cumhurbaşkanı, modern Türkiye'nin temellerini attı.",
     "Ey LyrexEX, doğum günün kutlu olsun. Bağımsızlık ve özgürlük ateşi her daim içinde yanmaya devam etsin."),
    ("İsmet İnönü", "Türkiye Cumhuriyeti'nin ikinci Cumhurbaşkanı, Kurtuluş Savaşı'nın önemli komutanlarından biri.",
     "LyrexEX, bu mübarek günde sana kararlı ve azimli bir ömür dilerim. Cumhuriyet uğruna verdiğin mücadele daim olsun."),
    ("Alparslan Türkeş", "Türk siyasetçi, modern cumhuriyet dönemlerinde Türkçülüğün baştemsilcilerinden.",
     "Ey LyrexEX, doğum günün kutlu olsun. Mücadele gücün artarak devam etsin."),
    ("Kazım Karabekir", "İstiklal Savaşında Doğu Cephesinin komutanı. İstiklal Kahramanı.",
     "Yiğit LyrexEX, doğum günün kutlu olsun. Milletimiz için verdiğin mücadele daim olsun, yolun açık olsun."),
    ("Enver Paşa", "Osmanlı Harbiye Bakanı, Bolşeviklere karşı Türkistan savunmasının komutanı.",
     "Ey LyrexEX, doğum gününde sana cesur bir yürek, fedakâr bir ruh diliyorum. Ömrün zaferlerle dolu olsun!"),
    ("Talat Paşa", "Üç Paşalardan birisi. 1. Dünya Savaşında görev almıştır.",
     "Sevgili LyrexEX, doğum günün kutlu olsun. İttihat ve Terakki ruhuyla daima ileriye bakman dileğiyle."),
    ("Cemal Paşa", "Güneyde Arap ihanetine karşı mücadele eden komutan, Arap kasabı olarak da bilinir.",
     "LyrexEX, bu özel günde sana vatanperver bir ruh ve kuvvetli bir irade diliyorum. Doğum günün kutlu olsun."),
    ("Kara Murat", "Bizansın başbelası.",
     "Ey LyrexEX, doğum gününde sana denizler kadar engin, kılıcın kadar keskin bir ömür dilerim."),
    ("Çaka Bey", "Türk Deniz Hakimiyetinin kurucusu.",
     "Yiğit denizci LyrexEX, dalgalar gibi coşkulu, fırtınalar gibi güçlü bir ömür dilerim. Doğum günün kutlu olsun.")
]

def gradyan_arka_plan(renk1, renk2):
    # Gradyan buton arka planı
    buton.config(bg=renk1)
    buton.update_idletasks()
    for i in range(100):
        r = int(renk1[1:3], 16) + (int(renk2[1:3], 16) - int(renk1[1:3], 16)) * i // 100
        g = int(renk1[3:5], 16) + (int(renk2[3:5], 16) - int(renk1[3:5], 16)) * i // 100
        b = int(renk1[5:7], 16) + (int(renk2[5:7], 16) - int(renk1[5:7], 16)) * i // 100
        buton.config(bg=f'#{r:02x}{g:02x}{b:02x}')
        buton.update_idletasks()
        time.sleep(0.01)

def mesaji_goster():
    rastgele_lider = random.choice(liderler)
    ad, aciklama, mesaj = rastgele_lider
    messagebox.showinfo(f"{ad}", f"{aciklama}\n\n{mesaj}")
    gradyan_arka_plan("#00FF00", "#0000FF")

root = tk.Tk()
root.title("Doğum Günün Kutlu Olsun LyrexEX")

ekran_genisligi = root.winfo_screenwidth()
ekran_yuksekligi = root.winfo_screenheight()
pencere_genisligi = 600
pencere_yuksekligi = 600
x_koordinati = (ekran_genisligi / 2) - (pencere_genisligi / 2)
y_koordinati = (ekran_yuksekligi / 2) - (pencere_yuksekligi / 2)
root.geometry(f'{pencere_genisligi}x{pencere_yuksekligi}+{int(x_koordinati)}+{int(y_koordinati)}')

buton = tk.Button(root, text="Doğum günün kutlu olsun LyrexEX", command=mesaji_goster, width=300, height=300)
gradyan_arka_plan("#FF7F50", "#8A2BE2")
buton.pack(pady=150)

root.mainloop()
