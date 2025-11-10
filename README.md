Système de Réservation de Cinéma 🎟️
Contexte
Vous travaillez pour un cinéma qui souhaite automatiser son système de réservation. Le cinéma applique des tarifs différents selon l'âge des spectateurs.

Objectif
Créez un programme Python qui permet de réserver des places de cinéma pour un groupe de personnes.

Spécifications du programme
Votre programme doit obligatoirement :

Demander à l'utilisateur le nombre de personnes qui souhaitent réserver (un nombre entier positif)

Pour chaque personne, demander son âge (un nombre entier positif)

Calculer le prix du billet selon l'âge de la personne :

Enfant (moins de 12 ans) : 6 euros
Adulte (de 12 à 65 ans inclus) : 10 euros
Senior (plus de 65 ans) : 7 euros
Compter le nombre de billets de chaque catégorie (enfants, adultes, seniors)

Calculer le prix total de la réservation

Afficher un récapitulatif contenant :

Le nombre de billets enfant et leur prix total
Le nombre de billets adulte et leur prix total
Le nombre de billets senior et leur prix total
Le prix total à payer
Sauvegarder l'historique des réservations dans un fichier externe au format CSV ou JSON (vous choisissez). Le programme n'a pas besoin d'afficher cet historique à l'écran, mais le fichier doit contenir toutes les informations et être consultable manuellement (nombre d'enfants, d'adultes, de séniors, prix total payé, date à laquelle l'opération a été faite - basez vous sur la date de la machine)

Contraintes techniques
Votre code doit contenir :

✅ Une boucle (for ou while) pour traiter chaque personne
✅ Des conditions (if/elif/else) pour déterminer le tarif selon l'âge
✅ Des variables pour stocker :
Le nombre de personnes
Le prix total
Le nombre de billets par catégorie (enfants, adultes, seniors)
✅ Des affichages clairs avec print()
Vous pouvez vous aider des différents supports de cours que nous avons vu jusqu'ici, ainsi que de la documentation officielle de Python.

Exemple d'exécution attendu
=== RÉSERVATION CINÉMA ===

Nombre de personnes : 4

Âge de la personne 1 : 8
Billet Enfant : 6€

Âge de la personne 2 : 35
Billet Adulte : 10€

Âge de la personne 3 : 42
Billet Adulte : 10€

Âge de la personne 4 : 70
Billet Senior : 7€

=== RÉCAPITULATIF ===
Billets Enfant : 1 x 6€ = 6€
Billets Adulte : 2 x 10€ = 20€
Billets Senior : 1 x 7€ = 7€

TOTAL À PAYER : 33€
