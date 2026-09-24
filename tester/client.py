import requests
import time

def fetch_api(url, expected_status=200):
    """
    Exécute une requête GET avec un timeout de 3s et 1 retry max.
    Retourne un tuple : (succès_booléen, temps_réponse_ms, données_json_ou_erreur)
    """
    timeout_sec = 3
    max_retries = 1
    
    for attempt in range(max_retries + 1):
        start_time = time.time()
        try:
            response = requests.get(url, timeout=timeout_sec)
            latency_ms = (time.time() - start_time) * 1000
            
            if response.status_code == expected_status:
                return True, latency_ms, response.json()
            else:
                return False, latency_ms, f"Statut inattendu : {response.status_code}"
                
        except requests.exceptions.RequestException as e:
            latency_ms = (time.time() - start_time) * 1000
            if attempt == max_retries:
                return False, latency_ms, f"Erreur réseau : {str(e)}"
            time.sleep(1) # Backoff simple avant le retry