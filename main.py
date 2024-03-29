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

def getUidName(conn, UID):
    cur = conn.cursor()
    cur.execute("SELECT prenomclient, nomclient, datenaissance FROM camping.client WHERE idclient == %s", (UID))
    result = cur.fetchall()
    return result

def getRespUid(conn, resaUID):
    cur = conn.cursor()
    cur.execute("SELECT numResp FROM camping.reservation WHERE idresa = %s", (resaUID))
    result = cur.fetchall()
    return result[-1][0]

def getMaxId(conn, table):
    cur = conn.cursor()
    if table == "client":
        cur.execute("SELECT idclient FROM camping.client ORDER BY idclient")
    elif table == "reservation":
        cur.execute("SELECT idresa FROM camping.reservation ORDER BY idresa")

    result = cur.fetchall()
    return result[-1][0]

def createResaSQL(conn, numEmplacement, numResp, dateResa, typeResa, tempResa, nbrVel, nbrVoit):
    maxId = getMaxId(conn, "reservation")
    newId = maxId + 1
    cur = conn.cursor()
    cur.execute('INSERT INTO camping.reservation VALUES(%d, %s, %s, %s, %s, %s, %s, %s)', (newId, numEmplacement, numResp, dateResa, typeResa, tempResa, nbrVel, nbrVoit))
    conn.commit()
    cur.close()
    print("Réservation ajouté avec l'UID :", newId)
    return

def delResaSQL(conn, idResa):
    cur = conn.cursor()
    cur.execute('DELETE FROM camping.reservation WHERE idResa = %s', (idResa))
    conn.commit()
    cur.close()
    return

def createClientSQL(conn, nomClient, prenomClient, dateClient, rueClient, villeClient, cpClient, telClient, mailClient):
    maxId = getMaxId(conn, "client")
    newId = maxId + 1
    cur = conn.cursor()
    cur.execute('INSERT INTO camping.client VALUES(%d, %s, %s, %s, %s, %s, %s, %s, %s)', (newId, nomClient, prenomClient, dateClient, rueClient, villeClient, cpClient, telClient, mailClient))
    conn.commit()
    cur.close()
    print("Client ajouté avec l'UID :", newId)
    return

def delClientSQL(conn, UID):
    cur = conn.cursor()
    cur.execute('DELETE FROM camping.client WHERE idClient = %s', (UID))
    conn.commit()
    cur.close()
    return

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
        print("|  3. Créer client           4. Supprimer client       |")
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
        print("|  5. Durée séjour           6. --------------------   |")
        print("|  7. Nombre voiture(s)      8. Nombre vélo(s)         |")
        print("|                                                      |")
        print("x======================================================x")
        print("\nSelectionnez le champs à renseigner")
        print("\nVous devez renseigner tout les champs marqués d'un (*)")
        print("\nEntrez Y pour créer la réservation ou Q pour abandonner")
    elif screen == "addClientMenu":
        print("x======================================================x")
        print("|                                                      |")
        print("|                   Création de Client                 |")
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
        return "leave"
    elif action == "1" and menu == "mainMenu":
        display("addResaMenu")
        menu = "addResaMenu"
        createResaMenu()
        return "mainMenu"
    elif action == "2" and menu == "mainMenu":
        delResaMenu()
        return "mainMenu"
    elif action == "3" and menu == "mainMenu":
        display("addClientMenu")
        menu = "addClientMenu"
        createClientMenu()
        return "mainMenu"
    elif action == "4" and menu == "mainMenu":
        delClientMenu()
        return "mainMenu"

def createResaMenu():
    run = True
    arg1 = False
    arg2 = False
    arg3 = False
    arg4 = False
    arg5 = False
    arg7 = False
    arg8 = False
    while run:
        action = str(input("\nSaisir l'action à effectuer : "))
        if action == "q" or action == "Q":
            run = False
        elif action == "1":
            numEmplacement = str(input("Entrez le numéro d'emplacement à assigner à la réservation : "))
            arg1 = True
        elif action == "2":
            action = n
            while action == n or action == N and action != y and action != Y and action != q and action != Q:
                numResp = str(input("Entrez l'UID du Client responsable de la réservation : "))
                online, myConnection = dbConnect()
                action = str(input("\nLe client responsable est-il bien ", getUidName(myConnection, numResp), "? (Y/N) : "))
                dbClose(myConnection)
            if action == y or action == Y:
                arg2 = True
        elif action == "3":
            dateResa = str(input("Entrez la date de début de la réservation (sous la forme AAAA-MM-JJ) : "))
            arg3 = True
        elif action == "4":
            typeResa = str(input("Entrez le type de la réservation (jour/sem/mois) : "))
            arg4 = True
        elif action == "5":
            tempResa = str(input("Entrez la durée du séjour : "))
            arg5 = True
        elif action == "7":
            nbrVel = str(input("Entrez le nombre de vélo(s) : "))
            arg7 = True
        elif action == "8":
            nbrVoit = str(input("Entrez le nombre de voiture(s) : "))
            arg8 = True
        elif action == "y" or action == "Y":
            if not arg1:
                print("Il manque le numéro d'emplacement")
            elif not arg2:
                print("Il manque l'UID du Client responsable de la réservation")
            elif not arg3:
                print("Il manque la date de début de la réservation")
            elif not arg4:
                print("Il manque le type de la réservation")
            elif not arg5:
                print("Il manque la durée du séjour")
            elif not arg7:
                print("Il manque le nombre de vélo(s)")
            elif not arg8:
                print("Il manque le nombre de voiture(s)")
            else:
                online, myConnection = dbConnect()
                createResaSQL(myConnection, numEmplacement, numResp, dateResa, typeResa, tempResa, nbrVel, nbrVoit)
                dbClose(myConnection)
                run = False
    return

def delResaMenu():
    action = n
    online, myConnection = dbConnect()
    while action == n or action == N and action != y and action != Y and action != q and action != Q:
        resaUID = str(input("Entrez l'UID de la réservation à supprimer: "))
        respUID = getRespUid(resaUID)
        action = str(input("\nVoulez-vous supprimer la réservation", resaUID, " dont le client responsable est ", getUidName(myConnection, respUID), "? (Y/N) : "))
    if action == y or action == Y:
        delResaSQL(myConnection, resaUID)
    dbClose(myConnection)
    return

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

def delClientMenu():
    action = n
    online, myConnection = dbConnect()
    while action == n or action == N and action != y and action != Y and action != q and action != Q:
        UID = str(input("Entrez l'UID du client à supprimer: "))
        action = str(input("\nLe client", UID, "est-il bien", getUidName(myConnection, UID), "? (Y/N) : "))
    if action == y or action == Y:
        delClientSQL(myConnection, UID)
    dbClose(myConnection)
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
    menu = actionHandler(actionListener, menu)
    display(answer)
    if menu == "leave":
        run = False
        dbClose(myConnection)
