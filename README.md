# neolegal-test

Utiliser le framework Python fastApi pour l’API ( le tout doit fonctionner avec Postman, pas de frontEnd nécessaire ) et doit utiliser le JWT pour l’authentification :
 
- Créer 2 API endpoints ( (POST) /authenticate et (GET) /users ) 
- Dans une db de type mongodb tu as les users ( username, password, firstname, lastname )
- Authenticate, doit valider un post json (username, password)
- Si l’authentification est réussie, generer le JWT et le retourner dans un json. ( gerer aussi le failures )
- Le endpoint /users retourne la liste des users en json si on lui envoie un JWT valide.
- Le endpoint /users?filter={‘username’ :’sid’} peut être filtrer par username et retourne les usernames qui reflètent le filtre
- Le endpoint /users?download=pdf retourne un fichier pdf de la liste des users ( username, firstname, lastname )

# Github link

https://github.com/MassiouenB/neolegal-test.git

# Installation

run `pip install -r dependency.txt`

# Start the server
run `uvicorn index:app --reload`

# Postman collection for test
https://www.postman.com/restless-flare-429526/workspace/neolegal/collection/20410822-ce82a678-0271-4e33-bac1-9f2df29f0873?action=share&creator=20410822

# swagger docs

http://35.203.174.71/docs

# endpoints 

-POST : http://35.203.174.71/authenticate

-GET : http://35.203.174.71/users?filter={"username": "massi_bek"}&download=pdf

# Test users data

- username1: "massi_bek"
- password1 = 'test1'

- username2: "dave_khal"
- password2 = 'test2'

- username3: "karima_khal"
- password3 = 'test3'

- username4: "sarah_khal"
- password4 = 'test4'