# Raspberry

Voici les différents codes utilisés lors de ce projet. 

Dans le main.py se trouve le code qui va permettre l'arrosage automatique des plantes.
Cependant, pour réaliser ce code, il est nécessaire d'utiliser les codes suivants: 
-LED.py pour l'utilisation de la LED
-chumidite.py pour le capteur d'humidité
-ctemperature.py pour le capteur de température
-driverI2C.py pour le fonctionnement du programme pour l'écran
-ecran.py pour l'affichage sur l'écran 
-relai.py pour faire fonctionner le relai 
-tluminosite.py pour le capteur de luminosité

Tous ces codes sont importés dans le main. 

# Main
Plusieurs conditions sont dans le main. 

Tout d'abord, rentre en jeu le capteur d'humidité. En fonction de ce que le capteur d'humidité renvoie comme information soit l'arrosage n'a pas lieu, soit il a lieu directement soit les autres capteurs rentrent en jeu.
Si les autres capteurs sont utilisés, c'est le capteur de température qui est pris en compte. En prenant en compte les informations reçues auparavant, si la température est trop élevé, l'arrosage est déclenché, si la température est trop faible, l'arrosage ne s'effectue pas et si la température est ambiante alors c'est le capteur de luminosité qui est exploité. 
Même chose, en prenant en compte les informations précédantes, s'il y a de la luminosité, alors l'arrosage se produit, s'il n'y a pas de luminosité alors il n'y a pas d'arrosage et si la luminosité est ambiante, l'arrosage se fait aussi. 

Enfin, lorsque le programme est lancé mais que le capteur d'humidité n'est pas dans la terre, alors l'écran affichera "il n'y a pas de plante" 
Si l'arrosage a été fait, "Plante arrosée" et l'écran sera vert.
Si l'arrosage n'a pas été fait, "Plante non arrosée" et l'écran sera rouge.

Lors de l'arrosage la LED clignotera.  


