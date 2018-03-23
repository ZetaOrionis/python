from bottle import route, run, template, error, get, request, static_file, view, url
import mysql.connector

""" Selection d'une installation précise dans une ville donnée """
def rechercheInstallation(ville) :

    """ Connection à la base de données """

    conn = mysql.connector.connect(host="infoweb",user="E165106N",password="E165106N",database="E165106N")
    cursor = conn.cursor()

    query = ("SELECT * FROM test where commune LIKE \""+ ville +"\" ")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row

    cursor.close()
    conn.close()

""" Selection d'une activitée précise dans une ville donnée """
def recherche(activite,ville) :

    """ Connection à la base de données """

    conn = mysql.connector.connect(host="infoweb",user="E165106N",password="E165106N",database="E165106N")
    cursor = conn.cursor()

    query = ("SELECT * FROM PaysdelaLoire where activite LIKE \""+ activite +"\" and ville LIKE \""+ ville +"\" ")

    cursor.execute(query)

    """ Afficher sous forme de tableau """
    row = cursor.fetchall()
    return row


    cursor.close()
    conn.close()

@error(404)
def error404(error):
    return {"Excusez nous, une erreur 404 vient d'apparaître" : 404}

@error(500)
def error500(error):
    return {"Excusez nous, une erreur 500 vient d'apparaître" : 500}

@route('/')
@view('home')
def home():
    return { 'url': url }

@route('/views/:path#.+#', name='views')
def static(path):
    return static_file(path, root='views')

@route('/traitement')
def home() :
    activite = request.query.activite
    ville = request.query.ville1

    reponse = recherche(activite,ville)
    if len(reponse) == 0:
        return {"Excusez nous, nous n'avons pas trouvé de réponse à votre requète."}

    return template('reponse', reponse=reponse)

@route('/test')
def home() :
    ville = request.query.ville2
    reponseInstallation = rechercheInstallation(ville)
    if len(reponseInstallation) == 0:
        return {"Excusez nous, nous n'avons pas trouvé de réponse à votre requète."}

    return template('reponseInstallation', reponseInstallation=reponseInstallation)

run(host='localhost', port=8000,debug=False, reloader=True)
