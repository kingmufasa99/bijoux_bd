import os
import bcrypt
import jwt
# from flask_cors import CORS
import pymysql
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, request, render_template

load_dotenv()
app = Flask(__name__)
mydb = pymysql.connect(
	host="localhost",
	user=os.getenv('DBPUSER'),
	password=os.getenv('DBPASSWORD'),
	database="bijoux"
)
mycursor = mydb.cursor()


@app.route("/")
def Accueil():
	pass


@app.route("/api/Connexion", methods=['POST'])
def Connexion():
	pass


@app.route("/api/Inscription", methods=['POST'])
def Inscription():
	pass


@app.route("/api/Deconnexion", methods=['POST'])
def Deconnexion():
	pass


@app.route("/api/rechercheProduit", methods=['POST'])
def rechercheProduit():
	try:
		reponse = make_response(jsonify({"redirect": "/Recherche", "message": request.form}))
		return reponse
	except:
		return ("", 404)


@app.route("/Recherche")
def Recherche():
	# params = []
	# mycursor.callproc("selection_produits")
	pass

@app.route("/api/ajouterPanier", methods=['POST'])
def ajouterPanier():
    try:
        produit_id = int(request.form['produit_id'])
        user_id = int(request.form['user_id'])
        mycursor.execute("INSERT INTO Commandes (ID_Produit, ID_Client) VALUES (%s, %s)", (produit_id, user_id))
        mydb.commit()
        return make_response(jsonify({'message': 'Produit ajouté au panier'}), 200)
    except:
        return make_response(jsonify({'error': 'Failed to add product to cart'}), 500)


@app.route("/api/supprimerPanier", methods=['POST'])
def supprimerPanier():
    try:
        produit_id = int(request.form['produit_id'])
        user_id = int(request.form['user_id'])
        mycursor.execute("DELETE FROM Commandes WHERE ID_Produit = %s AND ID_Client, (produit_id, user_id))
        mydb.commit()
        return make_response(jsonify({'message': 'Produit supprimé du panier'}), 200)
    except:
        return make_response(jsonify({'error': 'Failed to remove product from cart'}), 500)


@app.route("/api/commanderPanier", methods=['POST'])
def commanderPanier():
	try:
		resp = make_response(jsonify({"redirect": "/Commande", "message": request.form}))
		return resp
	except:
		return ("", 404)


@app.route("/Commande")
def Commande():
	pass


@app.route("/api/Noter", methods=['POST'])
def Noter():
	pass


if __name__ == "__main__":
	app.run(port=3500)