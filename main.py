import psycopg2

def dbConnect():
    hostname = 'sinfo1'
    username = 'areboul424'
    password = ''
    database = 'areboul424'

    try:
        myConnection = psycopg2.connect(host=hostname, user=username, password=password, database=database)
        print(myConnection)
        return True, myConnection
    except:
        return False, None

def dbClose(myConnection):
    myConnection.close()

def doQuery(conn):
    cur = conn.cursor()
    cur.execute("SELECT prenomclient, nomclient, datenaissance FROM camping.client")

    result = cur.fetchall()
    line1 = result[0]
    line2 = result[1]
    print(line1, line2)

def getMaxId(table, conn):
    cur = conn.cursor()
    if table == "client":
        cur.execute("SELECT idclient FROM camping.client ORDER BY idclient")
    elif table == "reservation":
        cur.execute("SELECT idresa FROM camping.reservation ORDER BY idresa")

    result = cur.fetchall()
    return result[-1][0]

def createClientSQL(conn, nomClient, prenomClient, dateClient, rueClient, villeClient, cpClient, telClient, mailClient):
    maxId = getMaxId("client", conn)
    newId = maxId + 1
    cur = conn.cursor()
    cur.execute('INSERT INTO camping.client VALUES(%d, %s, %s, %s, %s, %s, %s, %s, %s)', (newId, nomClient, prenomClient, dateClient, rueClient, villeClient, cpClient, telClient, mailClient))
    conn.commit()
    cur.close()
    print("Client ajouté avec l'UID :", newId)

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
    elif screen == "addClientMenu":
        print("x======================================================x")
        print("|                                                      |")
        print("|                     Ajout de Client                  |")
        print("|                                                      |")
        print("+======================================================+")
        print("|                                                      |")
        print("|           Selectionnez un champs à renseigner        |")
        print("|                                                      |")
        print("|  1. Nom                    2. Prénom                 |")
        print("|  3. Date de naissance      4. Rue                    |")
        print("|  5. Ville                  6. Code Postal            |")
        print("|  7. Numéro de telephone    8. Mail                   |")
        print("|                                                      |")
        print("x======================================================x")
        print("\nSelectionnez le champs à renseigner")
        print("\nVous devez renseigner tout les champs avant de valider")
        print("\nEntrez Y pour ajouter le client ou Q pour abandonner")
    elif screen == "leave":
        print("\nFermeture du gestionnnaire de camping...")

def actionHandler(action, menu):
    if action == "q" or action == "Q" and menu == "mainMenu":
        return "leave", "mainMenu"
    elif action == "1" and menu == "mainMenu":
        display("addResaMenu")
        menu = "addResaMenu"
        createResaMenu()
    elif action == "3" and menu == "mainMenu":
        display("addClientMenu")
        menu = "addClientMenu"
        createClientMenu()
        return "mainMenu", "mainMenu"

def createClientMenu():
    run = True
    arg1 = False
    arg2 = False
    arg3 = False
    arg4 = False
    arg5 = False
    arg6 = False
    arg7 = False
    arg8 = False
    while run:
        action = str(input("\nSaisir l'action à effectuer : "))
        if action == "q" or action == "Q":
            run = False
        elif action == "1":
            nomClient = str(input("Entrez le nom du Client : "))
            arg1 = True
        elif action == "2":
            prenomClient = str(input("Entrez le prénom du Client : "))
            arg2 = True
        elif action == "3":
            dateClient = str(input("Entrez la date de naissance du Client (sous la forme AAAA-MM-JJ) : "))
            arg3 = True
        elif action == "4":
            rueClient = str(input("Entrez la rue du Client : "))
            arg4 = True
        elif action == "5":
            villeClient = str(input("Entrez la ville du Client : "))
            arg5 = True
        elif action == "6":
            cpClient = str(input("Entrez le code postal du Client : "))
            arg6 = True
        elif action == "7":
            telClient = str(input("Entrez le numéro de telephone du Client : "))
            arg7 = True
        elif action == "8":
            mailClient = str(input("Entrez le mail du Client : "))
            arg8 = True
        elif action == "y" or action == "Y":
            if not arg1:
                print("Il manque le nom du client")
            elif not arg2:
                print("Il manque le prénom du client")
            elif not arg3:
                print("Il manque la date de naissance du client")
            elif not arg4:
                print("Il manque la rue du client")
            elif not arg5:
                print("Il manque la ville du client")
            elif not arg6:
                print("Il manque le code postal du client")
            elif not arg7:
                print("Il manque le numéro de telephone du client")
            elif not arg8:
                print("Il manque le mail du client")
            else:
                online, myConnection = dbConnect()
                createClientSQL(myConnection, nomClient, prenomClient, dateClient, rueClient, villeClient, cpClient, telClient, mailClient)
                dbClose(myConnection)
                run = False
    return

display("startScreen")
online, myConnection = dbConnect()
if online:
    run = True
    display("successConnect")
else:
    run = False
    display("failConnect")

doQuery(myConnection)
dbClose(myConnection)

menu = "mainMenu"
display("mainMenu")

while run:
    actionListener = str(input("\nSaisir l'action à effectuer : "))
    answer, menu = actionHandler(actionListener, menu)
    display(answer)
    if answer == "leave":
        run = False
        dbClose(myConnection)
