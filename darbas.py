#                                     ## #darbas su gitu###
#
#                                         #git init
#                                         #git add darbas.py
#                                         #git commit -m "zinute"
#                                         #git push -u origin master
#
# #funkcijos kurimas/kvietimas
# def labas():
#     print("printinu funkcijos vidu")
#
# labas()
#
# #duodam parametrus funkcijai
# def duodam_parametra(x,y):
#      return x+y
# print(duodam_parametra(5,5))
#
#
# #tuple kurimas,kvietimas
# musu_tuple=("kazkas","kazkas2")  # ju pakeisti nebegalesim. jie "amzini"
# print(musu_tuple[0])
#
# # dictonary kurimas / sarasas/raktazodziai
#
# musu_dict={
#     "raktas_i":"atsakymas",
#     "raktas_i2":"atsakymas2"
# }
# print(musu_dict["raktas_i"]) #printas atsakymas
#
# #listo kurimas,panaudojimas
# musu_listas=["vienas","du","trys","keturi"]
# print(musu_listas[0])
# # listai turi funkcijas. append(prideda elementa i gala),clear(),copy(),extend(),pop(),remove()...arrays method
#
# # for ciklas kurimas / range funkcija
# for i in range(1,10,2): # pirmas skaicius nuo, antras iki (ne imtinai "9" , tarpas tarp skaicius(jei reikia)
#     print(i)
# # for ciklas printinu viska is listo. listo panaudojimas for cikle
# listas=["musu",'listas',"printinamas","lauk"]
# for i in listas:
#     print(i)
# # while ciklas kurimas,pridejimas int skaiciaus/skaicius
# a=0
# b=10
# while a<b: #galima nauodoti funkcija ir " while True"
#     a+=1
#     print(a)
# # if salyga ar stringai vienodi
# zodis="labas"
# kitas_zodis="rytas"
#
# if zodis in kitas_zodis:
#     print("yra")
# else:
#     print("nera")
# #failo atidarymas/skaitymas
# with open("teksto_failas", "r") as input_file:
#     skaityti_eilutes = input_file.readlines()
#     print(skaityti_eilutes)
#
# #stringo formatavimas
# suma=15.4
# produktas="sokoladas"
# print(f"mokama suma {suma} produktas {produktas}")
#
# #bool tiesa melas. true or false
# print(True or False) #true
# print(False or True)#true
# ##and
# print(True and False)# false
# print(False and False)#false
# print(True and True)#true
#
# ## gaunam inputa is zmogaus/input kurimas
# a=input("jusu string inputas: ")#inputuoju stringa
# b=int(input("inputuoju int"))# int inputuoju sveika skaiciu
# c= float(input("inputuoju float skaicius")) #flot skaiciai galimi skaiciai po kablelio
#
# # skaiciu suapvalinimas
# a=10.15412
# print(f"{a:.2f}") #2skaiciai po kabelio
# # klases kurimas,naudojimas,kvietimas,priskirimas
# class person:
#     def __init__(self,name,age): # argumentai kuriuos naudosim
#         self.name=name
#         self.age=age
# a=person("laimonas",23) ## prisikirimas
# print(a.name,a.age) #kvietimas
# # stringas didziosimis
# tekstas="kazkas ZEMO"
# print(tekstas.upper())
# ## stringas maziosiomis
# print(tekstas.lower())
# ## skaiciuojam kiek zodziu vienodu
# print(tekstas.count("kazkas")) #print 1
## lyginiai skaiciai,pridedam naudojam lista.  darbas su laiku
# import time
# pradzia=time.time()
# sveikieji=[]
# for i in range(1,10_000):
#     if  i %2 != 0:
#         skaicius=i
#         sveikieji.append(skaicius)
# print(sveikieji)
# suma=sum(sveikieji)
# print(suma)
# pabaiga=time.time()
# print(f"laiko uztruo {pabaiga - pradzia}2f")
## loggingas klaidu rasymas. loginimas
# import logging
# l=logging.getLogger("mano logeris")
# h= logging.StreamHandler()
# f=logging.Formatter("%(asctime)s: %(message)%s")
# h.setFormatter(f)
# l.addHandler(h)
# l.setLevel(logging.INFO)
## break / continue funkcija
# a=0
# while True:
#     a += 1
#     if a==5:
#         break  #condinue nesustabdo o kartoja
#     else:
#         print("elee")
## lamdai paduodamas skaicius ar skaiciai ir su jeis dirbama. visai kaip per def (pravercia jeigu funkcijoje galima nurodyti tik viena sk)
# x=lambda  a,b: a*b
# print(x(2,2))














