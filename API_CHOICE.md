# API Choice

- Étudiant : Béni Mahoungou
- API choisie : Frankfurter (Taux de change de la BCE)
- URL base : https://api.frankfurter.app
- Documentation officielle / README : https://www.frankfurter.app/docs/
- Auth : None
- Endpoints testés :
  - GET /latest
  - GET /latest?from=USD&to=EUR
- Hypothèses de contrat (champs attendus, types, codes) :
  - Code HTTP : 200 attendu pour un succès, 404 pour une ressource introuvable.
  - Format : Content-Type `application/json`.
  - Champs obligatoires : `amount` (nombre / float), `base` (chaîne de caractères / string), `date` (chaîne de caractères / string), `rates` (dictionnaire / objet).
- Limites / rate limiting connu : Pas de quota strict documenté, mais nécessite un usage raisonnable ("fair use") pour éviter le spam.
- Risques (instabilité, downtime, CORS, etc.) : Très stable, mais risque inhérent de downtime (indisponibilité temporaire) lié à la dépendance d'un serveur tiers externe.
