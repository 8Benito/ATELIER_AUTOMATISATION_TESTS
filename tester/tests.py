from .client import fetch_api

BASE_URL = "https://api.frankfurter.app"

def executer_tests():
    resultats = []
    
    # 1. Test "Contrat" : HTTP 200 attendu
    succes, lat, data = fetch_api(f"{BASE_URL}/latest", expected_status=200)
    resultats.append({"name": "HTTP 200", "status": "PASS" if succes else "FAIL", "latency_ms": lat, "details": data})

    # 2. Test "Contrat" : Champs obligatoires présents
    if succes:
        champs_presents = all(cle in data for cle in ["amount", "base", "date", "rates"])
        resultats.append({"name": "Champs obligatoires", "status": "PASS" if champs_presents else "FAIL", "latency_ms": 0, "details": ""})
    else:
        resultats.append({"name": "Champs obligatoires", "status": "FAIL", "latency_ms": 0, "details": "Requête échouée"})

    # 3. Test "Contrat" : Types des données (string, float, dict)
    if succes and isinstance(data.get("amount"), (int, float)) and isinstance(data.get("rates"), dict) and isinstance(data.get("base"), str):
        resultats.append({"name": "Types de données (string/float)", "status": "PASS", "latency_ms": 0, "details": ""})
    else:
         resultats.append({"name": "Types de données (string/float)", "status": "FAIL", "latency_ms": 0, "details": "Type invalide"})

    # 4. Test Métier : Conversion de devise spécifique (USD vers EUR)
    succes, lat, data = fetch_api(f"{BASE_URL}/latest?from=USD&to=EUR", expected_status=200)
    if succes and "EUR" in data.get("rates", {}):
        resultats.append({"name": "Conversion USD/EUR", "status": "PASS", "latency_ms": lat, "details": ""})
    else:
        resultats.append({"name": "Conversion USD/EUR", "status": "FAIL", "latency_ms": lat, "details": data})

    # 5. Test Robustesse : Entrée invalide (Code 404 attendu)
    succes, lat, data = fetch_api(f"{BASE_URL}/endpoint_inexistant", expected_status=404)
    resultats.append({"name": "Bad Path (404 Not Found)", "status": "PASS" if succes else "FAIL", "latency_ms": lat, "details": data})
    
    # 6. Test Robustesse : Paramètre invalide (ex: Devise inconnue)
    succes, lat, data = fetch_api(f"{BASE_URL}/latest?from=FAKECURRENCY", expected_status=404)
    resultats.append({"name": "Bad Path (Devise Invalide)", "status": "PASS" if succes else "FAIL", "latency_ms": lat, "details": data})

    return resultats