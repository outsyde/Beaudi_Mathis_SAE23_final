import os
import BDAstronomieUtils as BDU
from configDB import dbConnect

""" FONCTIONS POUR CLEAR COMPLET AVEC MENU """

def clearTableMateriel() -> None:
    BDU.clearMateriel()
    print("\n*** Done.\n")

def clearTableObjet() -> None:
    BDU.clearObjet()
    print("\n*** Done.\n")

def clearTableObserve() -> None:
    BDU.clearObserve()
    print("\n*** Done.\n")

def clearTableProposition() -> None:
    BDU.clearProposition()
    print("\n*** Done.\n")

def printMateriel() -> None:
    print(BDU.getMateriel())

def printObjet() -> None:
    print(BDU.getObjet())

def printObservation() -> None:
    print(BDU.getObserve())

def printProposition() -> None:
    print(BDU.getProposition())

""" FONCTION D'INSERTION DE DONNEES MANUELLEMENT """

def addMateriel() -> None:
    """ Ajout de materiel """
    id_materiel_req = int(input("Identifiant matériel (-1 pour AUTO INCREMENT): "))
    type_req = input("Type de matériel : ")
    prix_req = int(input("Prix du matériel : "))
    try:
        if id_materiel_req == -1:
            id_materiel_req = "default"
        BDU.insertMateriel(id_materiel_req, type_req, prix_req)
    except Exception as e:
        print(f"Error : {e}")

def addObjet() -> None:
    """ Ajout d'un objet """
    id_objet_req = int(input("Identifiant objet (-1 pour AUTO INCREMENT): "))
    nom_req = input("Nom de l'astre : ")
    type_req = input("Type de l'astre : ")
    distanceTerre_req  = input("Distance de l'astre à la Terre (ex : 140 000 km, peut être vide) : ")
    DistanceSoleil_req  = input("Distance de l'astre au Soleil (ex : 140 000 km) : ")
    DistanceGalaxie_req  = input("Distance de l'astre à notre Galaxie (ex : 140 000 km, peut être vide) : ")
    luminosite_req = input("Luminosité de l'astre (ex : 100, peut être vide) : ")
    vitesse_req  = input("Vitess de l'astre en m/s (ex: 430, peut être vide) : ")
    age_req = input("Âge de l'astre (ex : 140 millions d'années) : ")
    try:
        if id_objet_req == -1:
            id_objet_req = "default"
        distanceTerre_req = None if distanceTerre_req == '' else distanceTerre_req
        DistanceGalaxie_req = None if DistanceGalaxie_req == '' else DistanceGalaxie_req
        luminosite_req = None if luminosite_req == '' else luminosite_req
        vitesse_req = None if vitesse_req == '' else vitesse_req
        BDU.insertObjet(id_objet_req, nom_req, type_req, distanceTerre_req, DistanceSoleil_req, DistanceGalaxie_req, luminosite_req, vitesse_req, age_req)
    except Exception as e:
        print(f"Error : {e}")

def addObservation() -> None:
    """ Ajout d'une observation """
    id_observation_req = int(input("Identifiant d'observation (-1 pour AUTO INCREMENT): "))
    jour_req = input("Jour de l'observation : ")
    mois_req = input("Mois de l'observation : ")
    annee_req = input("Année de l'observation : ")
    date = f"{int(annee_req):04d}-{int(mois_req):02d}-{int(jour_req):02d}"
    lieu_req = input("Lieu de l'observation : ")
    observatoire_req  = input("Observatoire visité (peut être vide) : ")
    filmObjet_req  = input("Film en rapport avec l'observation (peut être vide) : ")
    type_req  = input("Type de l'observation (soirée/journée) : ")
    print("\nRappel : {}\n".format(BDU.getMateriel()))
    materiel_req = input("Materiel utilisé (Identifiant matériel, peut être vide) : ")
    print("\nRappel : {}\n".format(BDU.getObjet()))
    objetObserve_req  = input("Objet observé (Identifiant objet, peut être vide) : ")
    try:
        if id_observation_req == -1:
            id_observation_req = "default"
        observatoire_req = None if observatoire_req == '' else observatoire_req
        filmObjet_req = None if filmObjet_req == '' else filmObjet_req
        materiel_req = None if materiel_req == '' else materiel_req
        objetObserve_req = None if objetObserve_req == '' else objetObserve_req
        BDU.insertObserve(id_observation_req, date, lieu_req, observatoire_req, filmObjet_req, type_req, materiel_req, objetObserve_req)
    except Exception as e:
        print(f"Error : {e}")

def addProposition() -> None:
    """ Ajout d'une observation """
    id_proposition_req = int(input("Identifiant de la proposition (-1 pour AUTO INCREMENT): "))
    prenom_req = input("Prénom : ")
    nom_req = input("Nom : ")
    jour_req = input("Jour de l'observation : ")
    mois_req = input("Mois de l'observation : ")
    annee_req = input("Année de l'observation : ")
    date = f"{int(annee_req):04d}-{int(mois_req):02d}-{int(jour_req):02d}"
    lieu_req = input("Lieu de l'observation : ")
    heure_req  = input("Heure de l'événement (ex : 15h) : ")
    print("\nRappel : {}\n".format(BDU.getMateriel()))
    materiel_req = input("Materiel utilisé (Identifiant matériel, peut être vide) : ")
    print("\nRappel : {}\n".format(BDU.getObjet()))
    objetObserve_req  = input("Objet observé (Identifiant objet, peut être vide) : ")
    try:
        if id_proposition_req == -1:
            id_proposition_req = "default"
        materiel_req = None if materiel_req == '' else materiel_req
        objetObserve_req = None if objetObserve_req == '' else objetObserve_req
        BDU.insertProposition(id_proposition_req, prenom_req, nom_req, date, lieu_req, heure_req, materiel_req, objetObserve_req)
    except Exception as e:
        print(f"Error : {e}")

""" FONCTION SUPPRIMER UN ITEM PAR SON ID """

def removeMaterielById() -> None:
    """ supprime du materiel par son numéro de clé primaire """
    printMateriel()
    id = int(input("Entrez le numéro du matériel : "))
    try:
        BDU.deleteMateriel(id)
        print("\n*** Done.\n")
    except ValueError as e:
        print(f"\n*** ERREUR : {e}\n")
    printMateriel()

def removeObjetById() -> None:
    """ supprime des objets par leur numéro de clé primaire """
    printObjet()
    id = int(input("Entrez le numéro de l'objet : "))
    try:
        BDU.deleteObjet(id)
        print("\n*** Done.\n")
    except ValueError as e:
        print(f"\n*** ERREUR : {e}\n")
    printObjet()

def removeObservationById() -> None:
    """ supprime des observation par leur numéro de clé primaire """
    printObservation()
    id = int(input("Entrez le numéro de l'observation : "))
    try:
        BDU.deleteObserve(id)
        print("\n*** Done.\n")
    except ValueError as e:
        print(f"\n*** ERREUR : {e}\n")
    printObservation()

def removePropositionById() -> None:
    """ supprime des proposition par leur numéro de clé primaire """
    printProposition()
    id = int(input("Entrez le numéro de la proposition : "))
    try:
        BDU.deleteProposition(id)
        print("\n*** Done.\n")
    except ValueError as e:
        print(f"\n*** ERREUR : {e}\n")
    printProposition()

""" FONCTION D'AFFICHAGE DE MENU """

def afficheMenu(choixActions : list ) -> None :
    """ Affichage du menu """
    print ("Choix possibles :")
    for ch  in choixActions:
        print (f'{choixActions.index(ch)+1} : {ch[0]}')
    print (f'{len(choixActions)+1} : Quitter')

def afficheMenuCore(liste) -> None:

    while True :
        afficheMenu(liste)
        try :
            choix = int(input("\nVotre Choix ? : "))
            if ( choix == len(liste) + 1 ):
                break
            elif 1 <= choix and choix <= len(liste):
                label, fct = liste[choix-1]
                fct()
            else :
                print ("*** Choix non valide, recommencez")
        except IndexError as e:
            print(e)
            print ('*** Choix non valide, recommencez')
        except ValueError as e :
            print(e)
            print ('*** Erreur, entrez un entier.')

""" FONCTION DE CHARGEMENT DE DONNEES PAR CSV"""

def loadFromCSV() -> None:
    import glob
    """ Demande quel fichier charger pour une table puis importe les données """
    csvFile = r'*.csv'
    print(f"Les fichiers CSV disponibles sont :")
    
    listeCSV = glob.glob(csvFile)
    for i, csv in enumerate(listeCSV, start=1):
        print(f"{i} : Charger le fichier : {csv}")

    choix = int(input("\nVotre choix ? : "))

    if choix > 0 and choix <= len(listeCSV):
        fichierChoisi = listeCSV[choix - 1]
        print(f"Vous avez choisi le fichier : {fichierChoisi}")
        if fichierChoisi == "materiel.csv":
            BDU.loadMaterielFromCSVFile()
        elif fichierChoisi == "objet.csv":
            BDU.loadObjetFromCSVFile()
        elif fichierChoisi == "observation.csv":
            BDU.loadObserveFromCSVFile()
        elif fichierChoisi == "proposition.csv":
                BDU.loadPropositionFromCSVFile()
    else:
        print("Choix invalide.")

def dropBase() -> None:
    try:
        BDU.dropDataBase()
        print("\n*** Done.\n")
        BDU.initBase()
    except Exception as e:
        print(f"Error : {e}")

""" FONCTION PERMETTANT DE MODIFIER TOUTES LES TABLES"""

def getAllTables() -> None:
    """ Affiche les tables de la base de données """
    tables = BDU.getTables()
    for i, table in enumerate(tables, start=1):
        table_name = str(table).replace("(", "").replace(")", "").replace("'", "").replace(",", "")
        print(f"{i} : Table : {table_name}")

    choix = int(input("\nVotre choix ? : "))

    if choix > 0 and choix <= len(BDU.getTables()):
        tableChoisie = tables[choix - 1]
        table_name = str(tableChoisie).replace("(", "").replace(")", "").replace("'", "").replace(",", "")
        print(f"Vous avez choisi la table : {table_name}")
        if table_name == "materiel":
            listeMateriel = [("Afficher la table Materiel",printMateriel),
                             ("Vider la table Materiel", clearTableMateriel),
                             ("Supprimer du materiel (par son numéro)", removeMaterielById),
                             ("Charger la table avec un fichier (CSV)", BDU.loadMaterielFromCSVFile),
                             ("Insérer un élément matériel", addMateriel)
                                ]
            afficheMenuCore(listeMateriel)
        elif table_name == "objet":
            listeObjet = [("Afficher la table Objet", printObjet),
                          ("Vider la table Objet", clearTableObjet),
                          ("Supprimer des objets (par leur numéro)", removeObjetById),
                          ("Charger la table avec un fichier (CSV)", BDU.loadObjetFromCSVFile),
                          ("Insérer un objet céleste", addObjet)
                            ]
            afficheMenuCore(listeObjet)
        elif table_name == "observation":
            listeObservation = [("Afficher la table Observation", printObservation),
                                ("Vider la table Observation", clearTableObserve),
                                ("Supprimer des Observation (par leur numéro)", removeObservationById),
                                ("Charger la table avec un fichier (CSV)", BDU.loadObserveFromCSVFile),
                                ("Insérer une observation", addObservation)
                                ]
            afficheMenuCore(listeObservation)
        elif table_name == "proposition":
            listeProposition = [("Afficher la table Proposition", printProposition),
                                ("Vider la table Proposition", clearTableProposition),
                                ("Supprimer des Proposition (par leur numéro)", removePropositionById),
                                ("Charger la table avec un fichier (CSV)", BDU.loadPropositionFromCSVFile),
                                ("Insérer une proposition", addProposition)
                                ]
            afficheMenuCore(listeProposition)
    else:
        print("Choix invalide.")

if __name__ == '__main__':
    import glob
    csvFile = r'*.csv'
    BDU.initBase()
    listeChoix1 = [
             ("Charger un fichier (CSV)",loadFromCSV),
             ("Afficher la table Materiel",printMateriel),
             ("Afficher la table Objet", printObjet),
             ("Afficher la table Observation", printObservation),
             ("Afficher la table Proposition", printProposition),
             ("Modifier des tables", getAllTables),
             ("Supprimer la base de données", dropBase)
            ]
    
    while True :
        afficheMenu(listeChoix1)
        try :
            choix = int(input("\nVotre Choix ? : "))
            if ( choix == len(listeChoix1) + 1 ):
                    break
            elif 1 <= choix and choix <= len(listeChoix1):
                label, fct = listeChoix1[choix-1]
                fct()
            else :
                print ("*** Choix non valide, recommencez")
        except IndexError as e:
            print(e)
            print ('*** Choix non valide, recommencez')
        except ValueError as e :
            print(e)
            print ('*** Erreur, entrez un entier.')
    print ("A bientôt !")