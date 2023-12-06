#Plots of 6 sessions

import datos
import matplotlib.pyplot as plt
import numpy as np
import statistics

fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
fig_2, ((ax1_2, ax2_2), (ax3_2, ax4_2), (ax5_2, ax6_2)) = plt.subplots(3, 2)




auxDatos = datos.sesionGloria
ax1_2.plot(auxDatos.xCliente, auxDatos.yClienteBlob, auxDatos.xTerapeuta, auxDatos.yTerapeutaBlob)
ax1.plot(auxDatos.yClienteBlob)

auxDatos = datos.sesionSylvia
ax2.plot(auxDatos.yClienteBlob)
ax2_2.plot(auxDatos.xCliente, auxDatos.yClienteBlob, auxDatos.xTerapeuta, auxDatos.yTerapeutaBlob)

auxDatos = datos.sesionSylvia2
ax3.plot(auxDatos.yClienteBlob)
ax3_2.plot(auxDatos.xCliente, auxDatos.yClienteBlob, auxDatos.xTerapeuta, auxDatos.yTerapeutaBlob)

auxDatos = datos.sesionKathy
ax4.plot(auxDatos.yClienteBlob)
ax4_2.plot(auxDatos.xCliente, auxDatos.yClienteBlob, auxDatos.xTerapeuta, auxDatos.yTerapeutaBlob)

auxDatos = datos.sesionDione
ax5.plot(auxDatos.yClienteBlob)
ax5_2.plot(auxDatos.xCliente, auxDatos.yClienteBlob, auxDatos.xTerapeuta, auxDatos.yTerapeutaBlob)

auxDatos = datos.sesionDione2
ax6.plot(auxDatos.yClienteBlob)
ax6_2.plot(auxDatos.xCliente, auxDatos.yClienteBlob, auxDatos.xTerapeuta, auxDatos.yTerapeutaBlob)

for i in [ax1, ax2, ax3, ax4, ax5, ax6]:
    i.legend(["Cliente", "Terapeuta"])
    i.set_xlabel("Num. diálogo")
    i.set_ylabel("Emocionalidad")
ax1.set_title("Sesión 1")
ax2.set_title("Sesión 2")
ax3.set_title("Sesión 3")
ax4.set_title("Sesión 4")
ax5.set_title("Sesión 5")
ax6.set_title("Sesión 6")


plt.show()
