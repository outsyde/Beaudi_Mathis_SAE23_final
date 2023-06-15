Projet : SAE 2.3 -> Astronomie

Fonctionnement entièrement sur Windows.

RENDU FINAL :

Lancer interfaceWeb.py

Configurtion phpmyadmin voir juste en dessous.


Instruction :

Ouvrir "configDB.txt" y changer host,user,pass,port si nécessaire.

Ensuite éxecuter le script AstronomieCLI.py

Précaution : 

En raison du moteur InnoDB utilisé, charger les CSV dans l'ordre présenté, soit au minimum : matériel.csv puis objet.csv


Structure des fichiers CSV :

materiel.csv : id_materiel;type;prix
id_materiel étant la clé primaire
Pour activer AUTO INCREMENT supprimer la première valeur, tout en laissant le ";" (ex :  ;1000;Téléscope de Newton)
           Pour désactiver AUTO INCREMENET mettre une valeur avant le premier ";" (ex : 1;1000;Téléscope de Newton)

objet.csv : id_objet;nom;type;distanceTerre;distanceSoleil;distanceGalaxie;luminosite;vitesse;age
id_objet étant la clé primaire
Pour activer AUTO INCREMENT supprimer la première valeur, tout en laissant le ";" (ex :  ;terre;tellurique;...)
           Pour désactiver AUTO INCREMENET mettre une valeur avant le premier ";" (ex : 1;terre;tellurique;...)
Pour mettre une valeur null mettre un ";" et passer à la donnée suivante.

observation.csv : id_observe;date;lieu;observatoire;filmObjet;type;materiel;objetObserve
id_observe étant la clé primaire
materiel une clé étrangère
objetObserve une clé étrangère
Pour activer AUTO INCREMENT supprimer la première valeur, tout en laissant le ";" (ex :  ;2023-05-10;Valence;;;soirée;2;1)
           Pour désactiver AUTO INCREMENET mettre une valeur avant le premier ";" (ex : 1;2023-05-10;Valence;;;soirée;2;1)
Pour mettre une valeur null mettre un ";" et passer à la donnée suivante.

proposition.csv : id_proposition;prenom;nom;date;lieu;heure;materiel;objetObservable
id_proposition étant la clé primaire
materiel une clé étrangère
objetObservable une clé étrangère
Pour activer AUTO INCREMENT supprimer la première valeur, tout en laissant le ";" (ex :  ;mathis;beaudi;2023-06-01;Valence;15h;3;1)
           Pour désactiver AUTO INCREMENET mettre une valeur avant le premier ";" (ex : 1;mathis;beaudi;2023-06-01;Valence;15h;3;1)
Pour mettre une valeur null mettre un ";" et passer à la donnée suivante.