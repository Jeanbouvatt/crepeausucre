# crepeausucre

## Routage des microservices

* Microservice I :
 * Route : /login/id
 * Port : 8091
 * Retour : 200 => id connue, 401 => sinon
 
* Microservice S
 * Route : /get_status/id
 * Port : 8092
 * Retour : 200 => id a joué, 401 => sinon
 * Autre route : /set_status/id indique au serveur que id a joué
 
* Microservice B
 * Route : /get_button/id
 * Port : 8090
 * Retour : un lien pour jouer

* Microservice W
 * Route : /play/id
 * Port : 8090
 * Retour : lance le jeu pour id
 


