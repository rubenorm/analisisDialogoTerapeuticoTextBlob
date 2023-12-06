#Plots of 6 sessions

import datos
import matplotlib.pyplot as plt
import numpy as np
import statistics

fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)

def listaCompara(listaAComparar):
    listaX = []
    listaY = []
    aux = []
    for dialogo in listaAComparar:
        if (len(aux) == 0):
            #aux = [dialogo["numero"], dialogo["persona"], dialogo["valornltk"]]
            aux = [dialogo["numero"], dialogo["persona"], dialogo["valorblob"]]
        elif (aux[0] == dialogo["numero"]):
            if (aux[1] == dialogo["persona"]):
                #aux[2] = (aux[2] + dialogo["valornltk"])/2
                aux[2] = (aux[2] + dialogo["valorblob"])/2
            else:
                listaX.append(aux[2])
                #listaY.append(dialogo["valornltk"])
                listaY.append(dialogo["valorblob"])
                aux = []
        else:
            #aux = [dialogo["numero"], dialogo["persona"], dialogo["valornltk"]]
            aux = [dialogo["numero"], dialogo["persona"], dialogo["valorblob"]]
            
    return {"x" : listaX, "y" : listaY}

gloriaCT = listaCompara(datos.gloria)
sylviaCT = listaCompara(datos.sylvia)
sylvia2CT = listaCompara(datos.sylvia2)
kathyCT = listaCompara(datos.kathy)
dioneCT = listaCompara(datos.dione)
dione2CT = listaCompara(datos.dione2)


ax1.plot(gloriaCT["x"], gloriaCT["y"], 'o')
ax2.plot(sylviaCT["x"], sylviaCT["y"], 'o')
ax3.plot(sylvia2CT["x"], sylvia2CT["y"], 'o')
ax4.plot(kathyCT["x"], kathyCT["y"], 'o')
ax5.plot(dioneCT["x"], dioneCT["y"], 'o')
ax6.plot(dione2CT["x"], dione2CT["y"], 'o')


for i in [ax1, ax2, ax3, ax4, ax5, ax6]:
    #i.legend(["Cliente", "Terapeuta"])
    i.set_xlabel("Emocionalidad Cliente")
    i.set_ylabel("Emocionalidad Terapeuta")
ax1.set_title("Sesión 1")
ax2.set_title("Sesión 2")
ax3.set_title("Sesión 3")
ax4.set_title("Sesión 4")
ax5.set_title("Sesión 5")
ax6.set_title("Sesión 6")


plt.show()
