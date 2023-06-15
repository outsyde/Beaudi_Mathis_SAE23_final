import os,pymysql
from configDB import dbConnect,serveurConnect
import mkRequest

def createBaseMySQL() -> None :
     _dbEtudiant, _cursorEtudiant = serveurConnect()
     _cursorEtudiant.execute(mkRequest._requetes["drop"])
     _cursorEtudiant.execute(mkRequest._requetes["createBase"])
     _cursorEtudiant.execute(mkRequest._requetes["use"])
     _cursorEtudiant.execute(mkRequest._requetes["createTableMateriel"])
     _cursorEtudiant.execute(mkRequest._requetes["createTableObjet"])  
     _cursorEtudiant.execute(mkRequest._requetes["createTableObserve"])  
     _cursorEtudiant.execute(mkRequest._requetes["createTableProposition"])
     #_cursorEtudiant.execute(_requetes["insertEtudiants"])

def initBase() -> None :
    """ Vérifie que la base existe, sinon propose de la créer en mode CLI.
            Jette une exception si paramètres de connexion incorrects """
    try :
        execute(mkRequest._requetes["getAllMateriel"])
    except pymysql.err.OperationalError as e:
        print(e)
        if '1044' in str(e) :
            print ("Vérifiez les paramètres de connexion")
            raise e
        elif '1049' in str(e) :
            choix = input("base inexistante, voulez-vouz créer une base 'astronomie' standard? (y/n) :")
            if choix not in 'yYOo' :
                raise e
            createBaseMySQL()

def execute(req : str) :    # type de valeur rendu variable :-(
    _db, _cursor = dbConnect()
    res = _cursor.execute(req)
    try:
        if "select" in req :
            res = _cursor.fetchall()
        else :
            _db.commit()
    except pymysql.err.OperationalError as e:
        if '1451' in str(e):
            raise e
    return res

def createBase()-> None :
    """ Crée la base étudiants (uniquement MySQL actuellement) """
    execute("")
    pass

""" INSERTION D'ITEM DANS LES DIFFERENTES TABLES """

def insertMateriel(id_materiel, type : str, prix : int) -> None :
    """ Insertion de materiel dans la collection"""
    req = mkRequest.mkInsertRequestMateriel(id_materiel,type,prix)
    execute(req)

def insertObjet(id_objet, nom : str, type : str, distanceTerre : int, distanceSoleil : int, distanceGalaxie : int, luminosite : int, vitesse: int, age : int) -> None :
    """ Insertion d'un objet dans la collection"""
    req = mkRequest.mkInsertRequestObjet(id_objet,nom,type,distanceTerre,distanceSoleil,distanceGalaxie,luminosite,vitesse,age)
    execute(req)

def insertObserve(id_observe, date : str, lieu : str, observatoire : str, filmObjet : str, type : str, materiel : int, objetObserve: int) -> None :
    """ Insertion d'une observation dans la collection"""
    req = mkRequest.mkInsertRequestObserve(id_observe,date,lieu,observatoire,filmObjet,type,materiel,objetObserve)
    execute(req)

def insertProposition(id_proposition, prenom : str, nom : str, date : str, lieu : str, heure : int, materiel : int, objetObservable: int) -> None :
    """ Insertion d'une proposition dans la collection"""
    req = mkRequest.mkInsertRequestProposition(id_proposition,prenom,nom,date,lieu,heure,materiel,objetObservable)
    execute(req)

""" CLEAR COMPLET DES DIFFERENTES TABLES """

def clearMateriel() -> None:
    """ Reset de la table materiel """
    req = mkRequest._requetes['clearMateriel']
    return execute(req)

def clearObjet() -> None:
    """ Reset de la table objet """
    req = mkRequest._requetes['clearObjet']
    return execute(req)

def clearObserve() -> None:
    """ Reset de la table observe """
    req = mkRequest._requetes['clearObserve']
    return execute(req)

def clearProposition() -> None:
    """ Reset de la table proposition """
    req = mkRequest._requetes['clearProposition']
    return execute(req)

""" AFFICHAGE DES DIFFERENTES TABLES """

def getMateriel() -> list :
    """ getMateriel() -> liste de tuples "Materiel"
    Rend le contenu de la base sous forme d'une liste de tuples """
    req = mkRequest._requetes["getAllMateriel"]
    materiel = []
    for t in execute(req) :
        materiel.append(t)
    return materiel

def getObjet() -> list :
    """ getObjet() -> liste de tuples "Objet"
    Rend le contenu de la base sous forme d'une liste de tuples """
    req = mkRequest._requetes["getAllObjet"]
    objet = []
    for t in execute(req) :
        objet.append(t)
    return objet

def getObserve() -> list :
    """ getObserve() -> liste de tuples "Observation"
    Rend le contenu de la base sous forme d'une liste de tuples """
    req = mkRequest._requetes["getAllObserve"]
    observe = []
    for t in execute(req) :
        observe.append(t)
    return observe

def getProposition() -> list :
    """ getProposition() -> liste de tuples "Proposition"
    Rend le contenu de la base sous forme d'une liste de tuples """
    req = mkRequest._requetes["getAllProposition"]
    proposition = []
    for t in execute(req) :
        proposition.append(t)
    return proposition

def getTables() -> tuple:
    _db, _cursor = dbConnect()
    _cursor.execute(mkRequest._requetes["getAllTables"])
    tables = _cursor.fetchall()
    return tables
    

""" SUPPRESSION D'ITEMS PAR SON ID """

def deleteMateriel(id_materiel : int) -> None :  
    """ Suppression de materiel dans la collection par ID """
    reqVerif = mkRequest.mkGetMaterielByIdRequest(id_materiel)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = mkRequest.mkDeleteMaterielRequest(id_materiel)
    execute(req)

def deleteObjet(id_objet : int) -> None :  
    """ Suppression de objet dans la collection par ID """
    reqVerif = mkRequest.mkGetObjetByIdRequest(id_objet)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = mkRequest.mkDeleteObjetRequest(id_objet)
    execute(req)

def deleteObserve(id_observe : int) -> None :  
    """ Suppression d'une observation dans la collection par ID """
    reqVerif = mkRequest.mkGetObserveByIdRequest(id_observe)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = mkRequest.mkDeleteObserveRequest(id_observe)
    execute(req)

def deleteProposition(id_proposition : int) -> None :  
    """ Suppression d'une observation dans la collection par ID """
    reqVerif = mkRequest.mkGetPropositionByIdRequest(id_proposition)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = mkRequest.mkDeletePropositionRequest(id_proposition)
    execute(req)

""" INSERTION D'ITEMS DEPUIS UN FICHIER CSV """

def loadMaterielFromCSVFile(path : str = "materiel.csv") -> None:
    """ Permet de charger une liste de materiel(s) à partir d'un fichier texte "CSV" """
    import csv
    try:
        with open(path, newline='\n',encoding='utf-8') as csvFile :
            lignesMateriel = csv.reader(csvFile,delimiter=';')
            for champs in lignesMateriel :
                id_materiel = champs[0]
                prix = champs[1]
                type = champs[2].upper()
                if id_materiel == '':
                    insertMateriel('default',type,prix)
                else:
                    insertMateriel(id_materiel,type,prix)
        print("\n*** Done.\n")
    except FileNotFoundError as e:
        print('\n*** ERROR : Fichier non trouvé !\n')
    except PermissionError:
        print('\n*** ERROR : Permission déclinée ! \n')


def loadObjetFromCSVFile(path : str = "objet.csv") -> None:
    """ Permet de charger une liste des objets à partir d'un fichier texte "CSV" """
    import csv
    try:
        with open(path, newline='\n',encoding='utf-8') as csvFile :
            lignesObjet = csv.reader(csvFile,delimiter=';')
            for champs in lignesObjet :
                id_objet = champs[0]
                nom = champs[1].capitalize()
                type = champs[2].upper()
                distanceTerre = champs[3]
                distanceSoleil = champs[4]
                distanceGalaxie = champs[5]
                luminosite = champs[6]
                vitesse = champs[7]
                age = champs [8]
                if id_objet == '':
                    insertObjet('default',nom,type,distanceTerre,distanceSoleil,distanceGalaxie,luminosite,vitesse,age)
                else:
                    insertObjet(id_objet,nom,type,distanceTerre,distanceSoleil,distanceGalaxie,luminosite,vitesse,age)

        print("\n*** Done.\n")
    except FileNotFoundError as e:
        print('\n*** ERROR : Fichier non trouvé !\n')
    except PermissionError:
        print('\n*** ERROR : Permission déclinée\n')

def loadObserveFromCSVFile(path : str = "observation.csv") -> None:
    """ Permet de charger une liste d'observation(s) à partir d'un fichier texte "CSV" """
    import csv
    try:
        with open(path, newline='\n',encoding='utf-8') as csvFile :
            lignesObserve = csv.reader(csvFile,delimiter=';')
            for champs in lignesObserve :
                id_observe = champs[0]
                date = champs[1].capitalize()
                lieu = champs[2].upper()
                observatoire = champs[3]
                filmObjet = champs[4]
                type = champs[5]
                materiel = champs[6]
                objetObserve = champs[7]
                if id_observe == '':
                    insertObserve('default',date,lieu,observatoire,filmObjet,type,materiel,objetObserve)
                else:
                    insertObserve(id_observe,date,lieu,observatoire,filmObjet,type,materiel,objetObserve)
        print("\n*** Done.\n")
    except FileNotFoundError as e:
        print('\n*** ERROR : Fichier non trouvé !\n')
    except PermissionError:
        print('\n*** ERROR : Permission déclinée\n')

def loadPropositionFromCSVFile(path : str = "proposition.csv") -> None:
    """ Permet de charger une liste de proposition à partir d'un fichier texte "CSV" """
    import csv
    try:
        with open(path, newline='\n',encoding='utf-8') as csvFile :
            lignesProposition = csv.reader(csvFile,delimiter=';')
            for champs in lignesProposition :
                id_proposition = champs[0]
                prenom = champs[1].capitalize()
                nom = champs[2].upper()
                date = champs[3]
                lieu = champs[4]
                heure = champs[5]
                materiel = champs[6]
                objetObservable = champs[7]
                if id_proposition == '':
                    insertProposition('default',prenom,nom,date,lieu,heure,materiel,objetObservable)
                else:
                    insertProposition(id_proposition,prenom,nom,date,lieu,heure,materiel,objetObservable)
        print("\n*** Done.\n")
    except FileNotFoundError as e:
        print('\n*** ERROR : Fichier non trouvé !\n')
    except PermissionError:
        print('\n*** ERROR : Permission déclinée\n')

""" AFFICHER """

def ObjetToString(objet: tuple) -> str:
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"""
        <div class="nom">{objet[1]}</div>
        <div class="line"></div><br>
        Type: {objet[2]}<br>
        Distance Terre: {objet[3]} km<br>
        Distance Soleil: {objet[4]} km<br>
        Distance Galaxie: {objet[5]} km<br>
        Luminosité: {objet[6]}<br>
        Vitesse: {objet[7]} m/s<br>
        Âge: {objet[8]} ans"""

def SupprObjetToString(objet: tuple) -> str:
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"""
        <div class="nom">{objet[1]}</div>
        <div class="line"></div><br>
        <span class="id">ID : {objet[0]}</span>"""

def SupprObjetToStringId(objet: tuple) -> str:
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"{objet[0]}"

def ObjetToStringId(objet: tuple) -> str:
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"{objet[0]}"

def ObservToString(observ : tuple) -> str :
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"""<div class="nom">{observ[7]}</div><br>
               <div class="line"></div><br>
               Date observation : {observ[1]}<br>
               Lieu : {observ[2]}<br>
               Observatoire : {observ[3]}<br>
               Film : {observ[4]}<br>
               Type : {observ[5]}<br>
               Materiel : {observ[6]}<br>
               Objet observé : {observ[7]}"""

def getObjetStr()-> list :
    req = mkRequest._requetes["getAllObjet"]
    objet = []
    for t in execute(req) :
        objet.append(ObjetToString(t))
    return objet

def getSupprObjetStr() -> list:
    req = mkRequest._requetes["getAllObjet"]
    objet = []
    for t in execute(req) :
        objet.append(SupprObjetToString(t))
    return objet

def getSupprObjetStrId() -> list:
    req = mkRequest._requetes["getAllObjet"]
    objet = []
    for t in execute(req) :
        objet.append(SupprObjetToStringId(t))
    return objet

def getObjetStrId() -> list:
    req = mkRequest._requetes["getAllObjet"]
    objet = []
    for t in execute(req) :
        objet.append(ObjetToStringId(t))
    return objet

def getObservStr() -> list :
    _db, _cursor = dbConnect()
    req = mkRequest._requetes["getAllObserveWeb"]
    res = _cursor.execute(req)
    res = _cursor.fetchall()
    observ = []
    for t in res :
        observ.append(ObservToString(t))
    return observ

def getSupprObservStr() -> list:
    req = mkRequest._requetes["getAllObserve"]
    observ = []
    for t in execute(req) :
        observ.append(SupprObservToString(t))
    return observ

def getSupprObservStrId() -> list:
    req = mkRequest._requetes["getAllObserve"]
    observ = []
    for t in execute(req) :
        observ.append(SupprObservToStringId(t))
    return observ

def SupprObservToStringId(observ: tuple) -> str:
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"{observ[0]}"

def SupprObservToString(observ: tuple) -> str:
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"""
        <div class="lieu">{observ[2]}</div>
        <div class="line"></div><br>
        <span class="id">ID : {observ[0]}</span>"""



def getMaterielStr() -> list :
    _db, _cursor = dbConnect()
    req = mkRequest._requetes["getAllMateriel"]
    res = _cursor.execute(req)
    res = _cursor.fetchall()
    materiel = []
    for t in res :
        materiel.append(MaterielToString(t))
    return materiel

def MaterielToString(materiel : tuple) -> str :
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"""<div class="nom">{materiel[1]}</div><br>
               <div class="line"></div><br>
               Prix : {materiel[2]} €"""

def getSupprMaterielStr() -> list:
    req = mkRequest._requetes["getAllMateriel"]
    materiel = []
    for t in execute(req) :
        materiel.append(SupprMaterielToString(t))
    return materiel

def SupprMaterielToString(materiel: tuple) -> str:
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"""
        <div class="modele">{materiel[1]}</div>
        <div class="line"></div><br>
        <span class="id">ID : {materiel[0]}</span>"""

def getSupprMaterielStrId() -> list:
    req = mkRequest._requetes["getAllMateriel"]
    materiel = []
    for t in execute(req) :
        materiel.append(SupprMaterielToStringId(t))
    return materiel

def getMaterielStrId() -> list:
    req = mkRequest._requetes["getAllMateriel"]
    materiel = []
    for t in execute(req) :
        materiel.append(MaterielToStringId(t))
    return materiel

def getMaterielStrByName() -> list:
    req = mkRequest._requetes["getAllMateriel"]
    materiel = []
    for t in execute(req) :
        materiel.append(MaterielToStringByName(t))
    return materiel

def SupprMaterielToStringId(materiel: tuple) -> str:
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"{materiel[0]}"

def MaterielToStringId(materiel: tuple) -> str:
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"{materiel[0]}"

def MaterielToStringByName(materiel: tuple) -> str:
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"{materiel[1]}"

def getObjetStrByName() -> list:
    req = mkRequest._requetes["getAllObjet"]
    objet = []
    for t in execute(req) :
        objet.append(ObjetToStringByName(t))
    return objet

def ObjetToStringByName(objet: tuple) -> str:
    """ Rend le tuple sous forme d'une chaîne de caractères """
    return f"{objet[1]}"

def getMaterielIdByName(type) -> list:
    _db, _cursor = dbConnect()
    req = mkRequest.mkgetMaterialIdByName(type)
    res = _cursor.execute(req)
    res = _cursor.fetchall()
    return res

def getObjetIdByIdByName(nom) -> list:
    _db, _cursor = dbConnect()
    req = mkRequest.mkgetObjetIdByName(nom)
    res = _cursor.execute(req)
    res = _cursor.fetchall()
    return res

def dropDataBase() -> None:
    req = mkRequest._requetes["dropDataBase"]
    execute(req)