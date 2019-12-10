def display(screen):
    if screen == "startScreen":
        print("\nx======================================================x")
        print("|                                                      |")
        print("|              Gestionnaire de camping v0.1            |")
        print("|                                                      |")
        print("x======================================================x")
        print("\nConnexion à la BDD...")
    elif screen == "successConnect":
        print("\nConnexion à la BDD établie.\n")
    elif screen == "failConnect":
        print("\nEchec de la connexion à la BDD.\n")
    elif screen == "mainMenu":
        print("x======================================================x")
        print("|                                                      |")
        print("|                     Menu Principal                   |")
        print("|                                                      |")
        print("+======================================================+")
        print("|                                                      |")
        print("|                 Selectionnez une action              |")
        print("|                                                      |")
        print("|  1. Créer réservation      2. Supprimer réservation  |")
        print("|  3. Ajouter client         4. Supprimer client       |")
        print("|  5. Modifier réservation   6. Modifier info client   |")
        print("|  7. Lister réservation     8. Lister clients         |")
        print("|                                                      |")
        print("x======================================================x")
    elif screen == "addResaMenu":
        print("x======================================================x")
        print("|                                                      |")
        print("|                 Création de Réservation              |")
        print("|                                                      |")
        print("+======================================================+")
        print("|                                                      |")
        print("|                 Selectionnez une action              |")
        print("|                                                      |")
        print("|  1. Emplacement            2. Responsable            |")
        print("|  3. Date arrivée           4. Type (jour/sem/mois)   |")
        print("|  5. Durée séjour           6. Modifier info client   |")
        print("|  7. Nombre voiture(s)      8. Nombre vélo(s)         |")
        print("|                                                      |")
        print("x======================================================x")
        print("\nSelectionnez le champs à renseigner")
        print("\nVous devez renseigner tout les champs marqués d'un (*)")
        print("\nEntrez Y pour créer la reservation ou Q pour abandonner")
    elif screen == "leave":
        print("\nFermeture du gestionnnaire de camping...")

def actionHandler(action, menu):
    if action == "q" or action == "Q" and menu == "mainMenu":
        return "leave"
    elif action == "1" and menu == "mainMenu":
        display("addResaMenu")
        menu = "addResaMenu"
        createResaMenu()

def createResaMenu():
    return

display("startScreen")
#online = dbConnect()
#Si online alors run = True et display successConnect
#Sinon run = False et display failConnect

run = True
menu = "mainMenu"
display("successConnect")

while run:
    display("mainMenu")
    actionListener = str(input("\nSaisir l'action à effectuer : "))
    answer = actionHandler(actionListener, menu)
    display(answer)
    if answer == "leave":
        run = False
