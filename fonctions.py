import os

def get_id() -> str:
    """Cette fonction demande le nom et le prenom à l'utilisateur pour l'utiliser en tant qu'id"""
    
    name = input("Quel est votre nom de famille ? ").strip().upper()
    firstname = input("Quel est votre prénom ? ").strip().capitalize()
    reservationId = name + "_" + firstname
    
    return(reservationId)

def people_number() -> int:
    """Demande à l'utilisateur le nombre de places qu'il souhaite réserver. Un entier positif est attendu"""
    os.system('cls')
    
    peopleNumber = input("Pour combien de personnes souhaitez-vous réserver de places de cinéma ? ")
    while (not peopleNumber) or (not peopleNumber.isdigit()) :
        peopleNumber = input("Veuillez entrer un nombre entier positif : ")
    return(int(peopleNumber))

def age_ask(peopleNumber: int) -> dict :
    """Demande à l'utilisateur l'âge de chaque personne. Un entier positif est attendu. Un statut est ajouté en fonction de l'âge : "enfant" si age < 12ans, "adulte" si 12ans >= age <= 65ans et "senior" si age > 65ans. Toutes les variables seront stockées dans un dictionnaire"""
    os.system('cls')
    
    peopleInformations = {}
    for i in range(peopleNumber) :
        peopleAge = input(f"Quel est lâge de la personne {i+1} ? ")
        while (not peopleAge) or (not peopleAge.isdigit()) :
            peopleAge = input("Veuillez entrer un âge entier positif : ")
        if int(peopleAge) < 12 :
            peopleStatus = "enfant"
        elif int(peopleAge) <= 65 :
            peopleStatus = "adulte"
        else :
            peopleStatus = "senior"
        
        peopleInformations[i+1] = {
            "age" : int(peopleAge),
            "statut" : peopleStatus
        }
    return(peopleInformations)

def ticket_price(peopleInformations: dict) -> dict:
    """Cette fonction associe le prix du billet en fonction du statut du statut de la personne"""
    
    PRICES = {
        "enfant" : 6,
        "adulte" : 10,
        "senior" : 7
    }
    
    for key in peopleInformations :
        status = peopleInformations[key]["statut"]
                
        if status == "enfant" : 
            peopleInformations[key]["prix"] = PRICES["enfant"]
        elif status == "adulte" :
            peopleInformations[key]["prix"] = PRICES["adulte"]
        else :
            peopleInformations[key]["prix"] = PRICES["senior"]
    return(peopleInformations)

def ticket_number(peopleInformations: dict) -> dict:
    """Cette fonction calcule le prix de la réservation de places de cinéma en fonction du statut de chaque personne ainsi que le prix total. Elle récapitule ces informations dans un dictionnaire"""
    
    nbChildTicket = 0
    nbAdultTicket = 0
    nbSeniorTicket = 0
    PRICES = {
        "enfant" : 6,
        "adulte" : 10,
        "senior" : 7
    }
    
    for key in peopleInformations :
        if peopleInformations[key]["statut"] == "enfant" :
            nbChildTicket += 1
        elif peopleInformations[key]["statut"] == "adulte" :
            nbAdultTicket += 1
        else :
            nbSeniorTicket += 1

    pricesDict = {
        "nbChildTicket" : nbChildTicket,
        "totalChildPrice" : nbChildTicket*PRICES["enfant"],
        "nbAdultTicket" : nbAdultTicket,
        "totalAdultPrice" : nbAdultTicket*PRICES["adulte"],
        "nbSeniorTicket" : nbSeniorTicket,
        "totalSeniorPrice" : nbSeniorTicket*PRICES["senior"],
        "totalPrice" : nbChildTicket*PRICES["enfant"] + nbAdultTicket*PRICES["adulte"] + nbSeniorTicket*PRICES["senior"]
    }
    
    return(pricesDict)

def print_informations(peopleInformations: dict, pricesDict: dict) -> str :
    """Cette fonction permet l'affichage des informations """
    
    os.system('cls')
    
    PRICES = {
        "enfant" : 6,
        "adulte" : 10,
        "senior" : 7
    }
    
    print(f"""=== RÉSERVATION CINÉMA ===

Nombre de personnes : {len(peopleInformations)}
""")
    for key in peopleInformations :
        print(f"""Âge de la personne {key} : {peopleInformations[key]["age"]}
Billet {peopleInformations[key]["statut"]} : {peopleInformations[key]["prix"]}€
""")

    print(f"""=== RÉCAPITULATIF ===

Billets Enfant : {pricesDict["nbChildTicket"]} x {PRICES["enfant"]}€ = {pricesDict["totalChildPrice"]}€
Billets Adulte : {pricesDict["nbAdultTicket"]} x {PRICES["adulte"]}€ = {pricesDict["totalAdultPrice"]}€
Billets Senior : {pricesDict["nbSeniorTicket"]} x {PRICES["senior"]}€ = {pricesDict["totalSeniorPrice"]}€

TOTAL À PAYER : {pricesDict["totalPrice"]}€""")