import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users/1"

def test_api_disponibilite():
    reponse = requests.get(BASE_URL)
    
    assert reponse.status_code == 200, f"Erreur, code HTTP reçu : {reponse.status_code}"
    
    temps_reponse = reponse.elapsed.total_seconds()
    assert temps_reponse < 1.0, f"API trop lente : {temps_reponse} secondes"

def test_api_structure_json():
    reponse = requests.get(BASE_URL)
    
    assert reponse.headers["Content-Type"].startswith("application/json"), "Le format n'est pas du JSON"
    
    donnees = reponse.json()
    
    assert "id" in donnees, "La clé 'id' est manquante"
    assert "name" in donnees, "La clé 'name' est manquante"
    assert "email" in donnees, "La clé 'email' est manquante"
    
    assert isinstance(donnees["id"], int), "L'ID doit être un entier"
    assert isinstance(donnees["name"], str), "Le nom doit être une chaîne de caractères"

def test_api_erreur_404():
    url_invalide = "https://jsonplaceholder.typicode.com/users/999999"
    reponse = requests.get(url_invalide)
    
    assert reponse.status_code == 404, f"Attendu 404, mais reçu : {reponse.status_code}"
    
    donnees = reponse.json()
    assert isinstance(donnees, dict), "Le retour d'erreur doit être un objet JSON valide"