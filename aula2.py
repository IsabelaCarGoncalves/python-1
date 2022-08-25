print ("Para qual cidade voce vai?")
cid=(input ())
print ("e qual a distancia entre o lugar que vc está até ",cid,"?")
dist=int(input())
if dist<=200: 
    print ("hmm, até que é perto! E qual a velocidade média do seu carro?")
else: print ("hmm, longe né? E qual a velocidade média do seu carro?")  
vel=int(input())
med= dist/vel
import math
frac, whole = math.modf (med)
frac = 6/frac
print("Você chegará em aproximadamente:",int (whole),"horas e",int (frac),"minutos")