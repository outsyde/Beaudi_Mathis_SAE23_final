import cherrypy, os, os.path

from mako.template import Template
from mako.lookup import TemplateLookup
import BDAstronomieUtils
from configDB import dbConnect

lookup = TemplateLookup(directories=['res/templates'], input_encoding='utf-8', module_directory='res/tmp/mako_modules')

class InterfaceWebAstronomie(object):    
    @cherrypy.expose
    def index(self):
        mytemplate = lookup.get_template("index.html")
        return mytemplate.render()
    
    @cherrypy.expose
    def objetsceleste(self):
        mytemplate = lookup.get_template("objetsceleste.html")
        return mytemplate.render(mesObjets=BDAstronomieUtils.getObjetStr())
    
    @cherrypy.expose
    def observation(self):
        mytemplate = lookup.get_template("observation.html")
        return mytemplate.render(mesObserv=BDAstronomieUtils.getObservStr())
    
    @cherrypy.expose
    def materiel(self):
        mytemplate = lookup.get_template("materiel.html")
        return mytemplate.render(mesMateriel=BDAstronomieUtils.getMaterielStr())
    
    @cherrypy.expose
    def insertionobjetsceleste(self):        
        mytemplate = lookup.get_template("insertionobjetsceleste.html")        
        return mytemplate.render(message="Veuillez remplir tous les champs", type="info")
    
    @cherrypy.expose
    def insertionobjetscelesteDone(self, nom,type,distanceTerre,distanceSoleil,distanceGalaxie,luminosite,vitesse,age):
        # le test suivant est rendu inutile par l'utilisation de javascript dans formulaire bootstrap
        if nom and type or distanceTerre and distanceSoleil or distanceGalaxie or luminosite or vitesse and age:
            try:
                BDAstronomieUtils.insertObjet('default',nom,type,distanceTerre,distanceSoleil,distanceGalaxie,luminosite,vitesse,age)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = lookup.get_template("insertionobjetsceleste.html")        
        return mytemplate.render(message=message, type=typ)
    
    @cherrypy.expose
    def insertionobservation(self):
        mytemplate = lookup.get_template("insertionobservation.html")        
        return mytemplate.render(mesMateriel=BDAstronomieUtils.getMaterielStrByName(), mesObjet=BDAstronomieUtils.getObjetStrByName(), message="Veuillez remplir tous les champs", type="info")
    
    @cherrypy.expose
    def insertionobservationDone(self, date,lieu,observatoire,filmObjet,type,materiel,objetObserve):
        # le test suivant est rendu inutile par l'utilisation de javascript dans formulaire bootstrap
        materielId = BDAstronomieUtils.getMaterielIdByName(materiel)
        objetObserveId = BDAstronomieUtils.getObjetIdByIdByName(objetObserve)

        if date and lieu or observatoire or filmObjet and type and materiel and objetObserve:
            try:
                BDAstronomieUtils.insertObserve('default',date,lieu,observatoire,filmObjet,type,materielId[0][0],objetObserveId[0][0])
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = lookup.get_template("insertionobservation.html")        
        return mytemplate.render(mesMateriel=BDAstronomieUtils.getMaterielStrByName(), mesObjet=BDAstronomieUtils.getObjetStrByName(), message=message, type=typ)

    @cherrypy.expose
    def insertionmateriel(self):        
        mytemplate = lookup.get_template("insertionmateriel.html")        
        return mytemplate.render(message="Veuillez remplir tous les champs", type="info")

    @cherrypy.expose
    def insertionmaterielDone(self, type,prix):
        # le test suivant est rendu inutile par l'utilisation de javascript dans formulaire bootstrap
        if type and prix:
            try:
                BDAstronomieUtils.insertMateriel('default',type,prix)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = lookup.get_template("insertionmateriel.html")        
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def supprimerobjetsceleste(self, numObjet=None):
        if numObjet :
            try:
                BDAstronomieUtils.deleteObjet(int(numObjet))
                message = "Suppression réussie !"
                typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Veuillez remplir tous les champs."
            typ = "warning"
        mytemplate = lookup.get_template("supprimerobjetsceleste.html")        
        return mytemplate.render(mesObjets=BDAstronomieUtils.getSupprObjetStr(), mesObjetsId=BDAstronomieUtils.getSupprObjetStrId(), message=message,type=typ)

    @cherrypy.expose
    def supprimerobservation(self, numObserv=None):
        if numObserv :
            try:
                BDAstronomieUtils.deleteObserve(int(numObserv))
                message = "Suppression réussie !"
                typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Veuillez remplir tous les champs."
            typ = "warning"
        mytemplate = lookup.get_template("supprimerobservation.html")        
        return mytemplate.render(mesObservs=BDAstronomieUtils.getSupprObservStr(), mesObservsId=BDAstronomieUtils.getSupprObservStrId(), message=message,type=typ)
    
    @cherrypy.expose
    def supprimermateriel(self, numMateriel=None):
        if numMateriel :
            try:
                BDAstronomieUtils.deleteMateriel(int(numMateriel))
                message = "Suppression réussie !"
                typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Veuillez remplir tous les champs."
            typ = "warning"
        mytemplate = lookup.get_template("supprimermateriel.html")        
        return mytemplate.render(mesMateriels=BDAstronomieUtils.getSupprMaterielStr(), mesMaterielsId=BDAstronomieUtils.getSupprMaterielStrId(), message=message,type=typ)

    @cherrypy.expose
    def loadCSVMateriel(self):
        BDAstronomieUtils.loadMaterielFromCSVFile(path="materiel.csv")
        mytemplate = lookup.get_template("index.html")
        return mytemplate.render()
    
    @cherrypy.expose
    def loadCSVObjet(self):
        BDAstronomieUtils.loadObjetFromCSVFile(path="objet.csv")
        mytemplate = lookup.get_template("index.html")
        return mytemplate.render()
    
    @cherrypy.expose
    def loadCSVObservation(self):
        BDAstronomieUtils.loadObserveFromCSVFile(path="observation.csv")
        mytemplate = lookup.get_template("index.html")
        return mytemplate.render()


rootPath = os.path.abspath(os.getcwd())
print(f"la racine du site est :\n\t{rootPath}\n\tcontient : {os.listdir()}")
BDAstronomieUtils.initBase()
cherrypy.quickstart(InterfaceWebAstronomie(), '/', 'config.txt')
