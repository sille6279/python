# 19.11.26 Sille Loo

#Ülesanne 3.7: Python Turtle kolmnurk
import turtle
kylg = 100
nurk = 120
varv = "red"

turtle.pencolor(varv)
for i in range(3):
    turtle.fd(kylg)
    turtle.lt(nurk)


turtle.done()


#Ülesanne 3.3: Reisiplaan
sk = "eesti"
pa = 10
hind = 50
print(sk,"reis kestab",pa,"päeva ja üks öö maksab" ,hind, "eurot.")

#Ülesanne 3.2 Ostunimekiri
toode = "sussid"
kogus = "10"
hind = "1.10"
print("Soovin " + toode + " " + str(kogus) + ", mille tüki hind on " + str(hind) + " eurot.")

#Ülesanne 3.1 Tervitus
nimi = "Sille"
vanus = 18
keskmine_hinne = 5.0
print(nimi,vanus,keskmine_hinne)
