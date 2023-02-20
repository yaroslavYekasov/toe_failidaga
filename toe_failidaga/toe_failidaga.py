from OmaModul import *
laused=["Tere tulemast"]

while True:
    v=int(input("1-loeme failist\n2-salvestame failiste\n3-Tekst helisse"))
    if v==1:
        laused=Loe_failist("Laused.txt")
        for line in laused:
            print(line)
    elif v==2:
        line=input("Lisa lause: ")
        laused.append(line)
        Kirjuta_failisse("Laused.txt",laused)
    elif v==3:
        text=""
        for line in laused:
            text=text+" "+line
        ind=int(input("Number: "))
        Heli(laused[ind],'et')

