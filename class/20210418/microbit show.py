from microbit import*
import time
lalala = Image("00900:""09590:""95959:""09590:""00900")
lalala1 = Image("00500:""05950:""59595:""05950:""00500")
lalali = Image("99999:""95559:""95959:""95559:""99999")
lalili = Image("00000:""09990:""09590:""09990:""00000")
lilili = Image("00000:""00000:""00900:""00000:""00000")
l=[lalala,lalala1,lalali,lalili,lilili,lalili,lalali,lalala1]

s=0.2

while True:
 for i in l:
     display.show(i)
     time.sleep(s)
