from bottle import route, run, template, error, get, request, static_file, view, url
import ast
import mysql.connector

""" Selection d'une activitée précise dans une ville donnée """
def recherche(activite,ville) :


    """ Connection à la base de données """

    conn = mysql.connector.connect(host="infoweb",user="E165106N",password="E165106N",database="E165106N")
    cursor = conn.cursor()

    query = ("SELECT * FROM PaysdelaLoire where activite LIKE \""+ activite +"\" and codePostal LIKE \""+ ville +"\" ")

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

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/traitement')
def home() :
    activite = request.query.activite
    ville = request.query.ville

    reponse = recherche(activite,ville)
    if len(reponse) == 0:
        return {"Excusez nous, nous n'avons pas trouvé de réponse à votre requète."}

    response = list(reponse)
    print ("response[0]: ", response[0])

    return template('reponse', reponse=reponse)

run(host='localhost', port=8000,debug=False, reloader=True)
