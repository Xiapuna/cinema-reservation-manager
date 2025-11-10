import json
import os

def write_json(nomjson, reservationId, peopleInformations: dict) :
    '''Création et/ou écriture d'un fichier Json'''
    if os.path.exists(nomjson) and os.path.getsize(nomjson) > 0 :
        with open (nomjson, 'r', encoding="utf-8") as f :
            contenu = f.read()
            if contenu :
                data = json.loads(contenu)
            else :
                data = {}
    else : 
        data = {}
    
    data[reservationId] = peopleInformations
    with open (nomjson, 'w', encoding="utf-8") as f :
        json.dump(data, f, indent=2)
    
    return(nomjson)
