import json
import datetime
import random
import sys
sys.path.append(r'.\models')
from Review import Review 

#Serializar y guardar
lista_dicc = []
for i in range(15):
    #Creamos Review i
    v1 = Review(
        i, 
        random.randint(1, 5), 
        i, 
        random.randint(1, 5), 
        "Comentario"+str(i), 
        random.randint(0,1))
    
    v1_dic = v1.a_json()
    lista_dicc.append(v1_dic)
    #Cargamos el review
with open(r"data\review.json","w") as Review:
    json.dump(lista_dicc,Review, indent=4)
    Review.write("\n")
