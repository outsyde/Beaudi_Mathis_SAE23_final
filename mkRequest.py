_requetes = {
    "drop" : "DROP DATABASE IF EXISTS astronomie",
    "createBase" : "CREATE DATABASE IF NOT EXISTS astronomie DEFAULT CHARACTER SET utf8",
    "use" : "USE astronomie",
    "createTableMateriel" : "CREATE TABLE materiel ( id_materiel INTEGER PRIMARY KEY AUTO_INCREMENT,\
        type VARCHAR(30) NOT NULL,\
        prix int NOT NULL)ENGINE=InnoDB;",
    "createTableObjet" : "CREATE TABLE objet ( id_objet INTEGER PRIMARY KEY AUTO_INCREMENT,\
        nom varchar(10) NOT NULL,\
        type enum('Téllurique','Gazeux') NOT NULL,\
        distanceTerre int(20) UNSIGNED DEFAULT NULL,\
        distanceSoleil int(20) UNSIGNED NOT NULL,\
        distanceGalaxie int(20) UNSIGNED DEFAULT NULL,\
        luminosite int(10) UNSIGNED DEFAULT NULL,\
        vitesse int(10) UNSIGNED DEFAULT NULL,\
        age int(20) UNSIGNED NOT NULL)ENGINE=InnoDB AUTO_INCREMENT=0;",
    "createTableObserve" : "CREATE TABLE observation ( id_observe INTEGER PRIMARY KEY AUTO_INCREMENT,\
        date date NOT NULL,\
        lieu varchar(10) NOT NULL,\
        observatoire varchar(20) DEFAULT NULL,\
        filmObjet varchar(10) DEFAULT NULL,\
        type enum('soirée','journée') NOT NULL,\
        materiel int DEFAULT NULL,\
        objetObserve int DEFAULT NULL,\
        FOREIGN KEY (materiel) REFERENCES materiel (id_materiel) ON DELETE NO ACTION ON UPDATE CASCADE,\
        FOREIGN KEY (objetObserve) REFERENCES objet (id_objet) ON DELETE NO ACTION ON UPDATE CASCADE )ENGINE=InnoDB AUTO_INCREMENT=0;",
    "createTableProposition" : "CREATE TABLE proposition ( id_proposition INTEGER PRIMARY KEY AUTO_INCREMENT,\
        prenom varchar(20) NOT NULL,\
        nom varchar(20) NOT NULL,\
        date date NOT NULL,\
        lieu varchar(20) NOT NULL,\
        heure varchar(10) NOT NULL,\
        materiel int DEFAULT NULL,\
        objetObservable int DEFAULT NULL,\
        FOREIGN KEY (materiel) REFERENCES materiel (id_materiel) ON DELETE NO ACTION ON UPDATE CASCADE,\
        FOREIGN KEY (objetObservable) REFERENCES objet (id_objet) ON DELETE NO ACTION ON UPDATE CASCADE )ENGINE=InnoDB AUTO_INCREMENT=0;",
    "clearMateriel" : "DELETE FROM materiel;",
    "clearObjet" : "DELETE FROM objet;",
    "clearObserve" : "DELETE FROM observation;",
    "clearProposition" : "DELETE FROM proposition;",
    "getAllMateriel" : "select * from materiel;",
    "getAllObjet" : "select * from objet;",
    "getAllObserve" : "select * from observation;",
    "getAllObserveWeb" : "SELECT obs.id_observe, obs.date, obs.lieu, obs.observatoire, obs.filmObjet, obs.type, mat.type, obj.nom FROM observation obs INNER JOIN materiel mat ON obs.materiel = mat.id_materiel INNER JOIN objet obj ON obs.objetObserve = obj.id_objet",
    "getAllProposition" : "select * from proposition;",
    "getAllTables" : "show tables from astronomie;",
    "getMaterialIdByName" : "SELECT id_materiel from materiel where type = '{}';",
    "getObjetIdByName" : "SELECT id_objet from objet where nom = '{}';",
    "insertMateriel" : "insert into materiel (id_materiel,type,prix) values ('{}','{}','{}');",
    "insertObjet" : "insert into objet (id_objet,nom,type,distanceTerre,distanceSoleil,distanceGalaxie,luminosite,vitesse,age) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}');",
    "insertObserve" : "insert into observation (id_observe,date,lieu,observatoire,filmObjet,type,materiel,objetObserve) values ('{}','{}','{}','{}','{}','{}','{}','{}');",
    "insertProposition" : "insert into proposition (id_proposition,prenom,nom,date,lieu,heure,materiel,objetObservable) values ('{}','{}','{}','{}','{}','{}','{}','{}');",
    "getMaterielById" : "select * from materiel where id_materiel = '{}';",
    "deleteMaterielById" : "delete from materiel where id_materiel = '{}';",
    "getObjetById" : "select * from objet where id_objet = '{}';",
    "deleteObjetById" : "delete from objet where id_objet = '{}';",
    "getObserveById" : "select * from observation where id_observe = '{}';",
    "deleteObserveById" : "delete from observation where id_observe = '{}';",
    "getPropositionById" : "select * from proposition where id_proposition = '{}';",
    "deletePropositionById" : "delete from proposition where id_proposition = '{}';",
    "dropDataBase" : "DROP DATABASE astronomie;"
    }


def mkInsertRequestMateriel(id_materiel,type,prix) :
    s= _requetes["insertMateriel"].format(id_materiel,type,prix)
    return s

def mkInsertRequestObjet(id_objet,nom,type,distanceTerre,distanceSoleil,distanceGalaxie,luminosite,vitesse,age) :
    s= _requetes["insertObjet"].format(id_objet,nom,type,distanceTerre,distanceSoleil,distanceGalaxie,luminosite,vitesse,age)
    return s

def mkInsertRequestObserve(id_observe,date,lieu,observatoire,filmObjet,type,materiel,objetObserve) :
    s= _requetes["insertObserve"].format(id_observe,date,lieu,observatoire,filmObjet,type,materiel,objetObserve)
    return s

def mkInsertRequestProposition(id_proposition,prenom,nom,date,lieu,heure,materiel,objetObservable) :
    s= _requetes["insertProposition"].format(id_proposition,prenom,nom,date,lieu,heure,materiel,objetObservable)
    return s

""" Clear table Materiel by ID """

def mkGetMaterielByIdRequest(id_materiel) :
    s= _requetes["getMaterielById"].format(id_materiel)
    return s

def mkDeleteMaterielRequest(id_materiel) :
    s= _requetes["deleteMaterielById"].format(id_materiel)
    return s

""" Clear table Objet by ID """

def mkGetObjetByIdRequest(id_objet) :
    s= _requetes["getObjetById"].format(id_objet)
    return s

def mkDeleteObjetRequest(id_objet) :
    s= _requetes["deleteObjetById"].format(id_objet)
    return s

""" Clear table Observe by ID """

def mkGetObserveByIdRequest(id_observe) :
    s= _requetes["getObserveById"].format(id_observe)
    return s

def mkDeleteObserveRequest(id_observe) :
    s= _requetes["deleteObserveById"].format(id_observe)
    return s

""" Clear table Proposition by ID """

def mkGetPropositionByIdRequest(id_proposition) :
    s= _requetes["getPropositionById"].format(id_proposition)
    return s

def mkDeletePropositionRequest(id_proposition) :
    s= _requetes["deletePropositionById"].format(id_proposition)
    return s

def mkgetMaterialIdByName(id_materiel) :
    s=_requetes["getMaterialIdByName"].format(id_materiel)
    return s

def mkgetObjetIdByName(id_objet) :
    s=_requetes["getObjetIdByName"].format(id_objet)
    return s
