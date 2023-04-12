evaluar = """ título: Experiences in Developing a Distributed Agent-based
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures.
"""
import sys

print(sys.platform)
parrafos = evaluar.split(":")
titulo = parrafos[1].split()
if ((len(titulo)) <=(11)):
    print("TITULO  : OK")
else:
    print("TITULO MAL")

oraciones = parrafos[2].replace("\n", " ").split(".")
palabras_faciles = 0
palabras_aceptables = 0
palabras_dificiles = 0
palabras_muy_dificiles = 0

print(f"LA CANTIDAD DE PALABRAS FACILES : {palabras_faciles} CANTIDAD DE PALABRAS ACEPTABLES : {palabras_aceptables} CANTIDAD DE PARABRAS DIFICILES : {palabras_dificiles} CANTIDAD DE PALABRAS MUY DIFICILES : {palabras_dificiles}")
print(oraciones)
oraciones.remove(" ")

for oracion in oraciones:
    palabras = oracion.split()
    cantidad = len(palabras)
    match cantidad:
        case cantidad if  cantidad < 12 :
            palabras_faciles += 1
        case cantidad if  12  <= cantidad <= 17:
            palabras_aceptables += 1
        case cantidad if   18 <= cantidad <= 25:
            palabras_dificiles += 1
        case cantidad if cantidad > 25:
            palabras_muy_dificiles += 1
print(f"LA CANTIDAD DE PALABRAS FACILES : {palabras_faciles} CANTIDAD DE PALABRAS ACEPTABLES : {palabras_aceptables} CANTIDAD DE PARABRAS DIFICILES : {palabras_dificiles} CANTIDAD DE PALABRAS MUY DIFICILES : {palabras_muy_dificiles}")
