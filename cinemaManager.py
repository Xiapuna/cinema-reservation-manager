from fonctions import get_id, people_number, age_ask, ticket_price, ticket_number, print_informations
from jsonManager import write_json
from datetime import datetime
import os

os.system('cls')

print("""Bonjour, bienvenue sur notre plateforme de réservation de places de cinéma.
""")

reservationId = get_id()

peopleNumber = people_number()

initialPeopleInformations = age_ask(peopleNumber)

finalPeopleInformations = ticket_price(initialPeopleInformations)

final = ticket_number(finalPeopleInformations)

print_informations(finalPeopleInformations, final)

jsonInformations = {
    "nbEnfants" : final["nbChildTicket"],
    "nbAdultes" : final["nbAdultTicket"],
    "nbSenior" : final["nbSeniorTicket"],
    "prixTotal" : final["totalPrice"],
    "date" : str(datetime.now())
}

write_json("reservationInformations.json", reservationId, jsonInformations)
