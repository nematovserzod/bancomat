import sys
import time
from import_sys.py import *



hozir = time.asctime(time.localtime(time.time()))
print("\n📆 Bugungi vaqt:" ,hozir)



def languages():     #  ---------->>>>   demonstration
    print(
         "\n\t\t*****Languages*****\n\n" 
             "\t\t E =>  English Ⓔ\n"
             "\t\t U =>  Uzbek   Ⓤ\n"
             "\t\t R =>  Russian Ⓡ \n"
             "\t\t Q =>  Chiqish 🚪 \n"
             )


languages()   
javob = str.capitalize(input(">>>>>_"))


def hozirr():
    hozir = time.asctime(time.localtime(time.time()))
    
    print("\n📆 Bugungi vaqt:" ,hozir)
    
def english():
    print("\n\nHello dear SIR/MADAM!!!\t How can i help you ?")
    sys.exit()
    
def Uzbek():
    print("\n\nAssalomu alekum hurmatli mijoz, qanday yordam berishimiz mumkin")
    sys.exit()

def Russian():
    print("\nПРИВЕТ")
    sys.exit()
    
def Exxit():
        time.sleep(2) 
        languages()
        print("\nXizmatimizdan foydalanganingiz un rahmat\n")
        javob = str.capitalize(input(">>>>>_"))
    


while javob:
    if javob == 'E':
        hozirr()
        english()
    elif javob == 'U':
        hozirr()
        Uzbek()
    elif javob == 'R':
        hozirr()
        Russian() 
    elif javob == "Q":
        hozirr()
        Exxit()

        

   

        







