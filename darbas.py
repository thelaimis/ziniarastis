#darbas su gitu
#git init
#git add darbas.py
#git commit -m "zinute"
#git push -u origin master

#funkcijos kurimas/kvietimas
def labas():
    print("printinu funkcijos vidu")

labas()

#duodam parametrus funkcijai
def duodam_parametra(x,y):
     return x+y
print(duodam_parametra(5,5))


#tuple kurimas,kvietimas
musu_tuple=("kazkas","kazkas2")  # ju pakeisti nebegalesim. jie "amzini"
print(musu_tuple[0])

# dictonary kurimas

musu_dict={
    "raktas_i":"atsakymas",
    "raktas_i2":"atsakymas2"
}
print(musu_dict["raktas_i"]) #printas atsakymas

#listo kurimas,panaudojimas
musu_listas=["vienas","du","trys","keturi"]
print(musu_listas[0])

# for ciklas kurimas / range funkcija
for i in range(1,10,2): # pirmas skaicius nuo, antras iki (ne imtinai "9" , tarpas tarp skaicius(jei reikia)
    print(i)
# while ciklas kurimas,pridejimas int skaiciaus/skaicius
a=0
b=10
while a<b: #galima nauodoti funkcija ir " while True"
    a+=1
    print(a)
# if salyga ar stringai vienodi
zodis="labas"
kitas_zodis="rytas"

if zodis in kitas_zodis:
    print("yra")
else:
    print("nera")
#failo atidarymas/skaitymas
with open("teksto_failas", "r") as input_file:
    skaityti_eilutes = input_file.readlines()
    print(skaityti_eilutes)

#stringo formatavimas
suma=15.4
produktas="sokoladas"
print(f"mokama suma {suma} produktas {produktas}")

#bool tiesa melas. true or false
print(True or False) #true
print(False or True)#true
##and
print(True and False)# false
print(False and False)#false
print(True and True)#true

