# 19.11.26 Sille Lo

#Ring
import turtle
try:
    r = int(input("Sisesta raadius: "))
    s = 3.14*r**2
    p = 2*3.14*r
    turtle.circle(r)
    print(s,p)
    turtle.done()
except ValueError:
    print("ksjhdfkshf")

#Faili allalaadimine
#Kirjuta programm, mis aitab arvutada, kui kaua kulub aega faili allalaadimiseks.
try:
    kiirus = int(input("Sisesta kiirus MB/s: "))
    suurus = int(input("Sisesta suurus MB: "))
    if kiirus == 0:
        print("Loll")
    else:
        vastus = suurus / kiirus
        print(int(vastus))
except ValueError: 
    print(akjshdkajshd)

#1. Aia pikkus
# Kirjuta programm, mis aitab aiapidajala arvutada
x = int(input("Sisesta külg 1: "))
y= int(input("Sisesta külg 2: "))
pikkus = (x+y)*2

print(f"Aia kogupikkus on {pikkus} meetrit.")
