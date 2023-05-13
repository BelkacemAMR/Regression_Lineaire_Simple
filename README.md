# Regression_Lineaire_Simple

Ce programme est conçu pour effectuer une régression linéaire simple à l'aide de la bibliothèque scikit-learn en Python. Il vous permet de modéliser et de prédire la relation linéaire entre une variable dépendante et une variable indépendante en utilisant la méthode des moindres carrés.

## La Regression Lineaire Simple:

La régression linéaire simple est une technique d'analyse statistique qui permet de modéliser la relation entre une variable dépendante (variable cible) et une variable indépendante (variable prédictive) en utilisant une droite. Elle suppose que la relation entre ces variables peut être approximée par une fonction linéaire.

L'équation générale d'une régression linéaire simple est donnée par :

```python
y = a * x + b

```
où 'y' est la variable dépendante, 'x' est la variable indépendante, 'a' est le coefficient de pente (qui représente le changement moyen dans y pour un changement unitaire dans 'x'), et 'b' est l'ordonnée à l'origine (la valeur de 'y' lorsque 'x' est égal à zéro).

L'objectif de la régression linéaire simple est de trouver la meilleure droite qui représente au mieux la relation entre les variables. Cela se fait en ajustant les coefficients 'a' et 'b' de manière à minimiser l'écart entre les valeurs observées de la variable dépendante et les valeurs prédites par le modèle.

## Instructions
1. Assurez-vous d'avoir Python 3 installé sur votre système.
2. Installez les bibliothèques requises en exécutant la commande suivante :
3. 
```python
pip install scikit-learn numpy matplotlib
```
Clonez ce référentiel GitHub ou téléchargez simplement le fichier du programme main.py.
Exécutez le programme à l'aide de la commande suivante :

```python
main.py
```
Vous verrez les coefficients de la droite de régression et la prédiction pour une nouvelle valeur de x affichés dans la console. De plus, un graphique sera généré montrant les données d'exemple, la droite de régression et la prédiction pour la nouvelle valeur de 'x'.
