# neolegal-test

Utiliser le framework Python fastApi pour l’API ( le tout doit fonctionner avec Postman, pas de frontEnd nécessaire ) et doit utiliser le JWT pour l’authentification :
 
- Créer 2 API endpoints ( (POST) /authenticate et (GET) /users ) 
- Dans une db de type mongodb tu as les users ( username, password, firstname, lastname )
- Authenticate, doit valider un post json (username, password)
- Si l’authentification est réussie, generer le JWT et le retourner dans un json. ( gerer aussi le failures )
- Le endpoint /users retourne la liste des users en json si on lui envoie un JWT valide.
- Le endpoint /users?filter={‘username’ :’sid’} peut être filtrer par username et retourne les usernames qui reflètent le filtre
- Le endpoint /users?download=pdf retourne un fichier pdf de la liste des users ( username, firstname, lastname )

