import json
import os

def write_json(nomjson: str, reservationId: str, jsonInformations: dict) :
    '''Cette fonction créé un fichier json s'il n'existe pas encore et s'il existe ajoute des informations sans effacer les précédentes informations'''
    if os.path.exists(nomjson) and os.path.getsize(nomjson) > 0 :
        with open (nomjson, 'r', encoding="utf-8") as f :
            contenu = f.read()
            if contenu :
                data = json.loads(contenu)
            else :
                data = {}
    else : 
        data = {}
    
    data[reservationId] = jsonInformations
    with open (nomjson, 'w', encoding="utf-8") as f :
        json.dump(data, f, indent=2)
    
    return(nomjson)
