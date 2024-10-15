# 🏠 **Odoo Technical Training - Estate Module**

![odoo-logo](https://img.shields.io/badge/Odoo-16.0-purple?style=for-the-badge&logo=odoo&logoColor=white)  
![license](https://img.shields.io/badge/License-MIT-blue?style=flat-square)  
![status](https://img.shields.io/badge/Status-In_Development-orange?style=flat-square)  
![python](https://img.shields.io/badge/Python-3.10+-yellow?style=flat-square&logo=python)  

---

## 📖 **Introduction**

Bienvenue dans le projet **"Odoo Technical Training"** ! 🎓  
Ce dépôt contient un **module personnalisé** appelé **"Estate"**, inspiré du **use case Real Estate** d’Odoo. Ce module est conçu pour gérer la **vente et la location de biens immobiliers**, en ajoutant des fonctionnalités supplémentaires adaptées à tes besoins.

---

## 🛠️ **Fonctionnalités du Module Estate**

✅ **Gestion des biens immobiliers** :  
Ajoute, modifie, et supprime des propriétés (maisons, appartements, terrains).  
✅ **Suivi des offres** :  
Gère les offres d'achat et négocie avec les clients.  
✅ **Statut des propriétés** :  
Met à jour le statut des biens : *nouveau, vendu, ou annulé*.  
✅ **Gestion des agents** :  
Suivi des agents immobiliers associés à chaque propriété.  
✅ **Filtrage avancé** :  
Recherchez des biens par prix, localisation, et statut.  

---

## 🧰 **Pré-requis**

- Odoo **16.0+** installé  
- Python **3.10+**  
- Module **base** activé

---

## 🚀 **Installation**

1. Clone ce dépôt dans le répertoire des modules Odoo :  
   ```bash
   git clone https://github.com/Walter28/odoo-technical-training.git
    ```

2. Redémarrez votre instance Odoo :  
   ```bash
   ./odoo-bin -d my_database -u estate
    ```

3. Activez le mode développeur dans Odoo et installez le module Estate depuis l'interface.

---

## 📂 **Structure du Module**

```bash
    odoo-technical-training/
    │
    ├── estate/
    │   ├── __init__.py
    │   ├── __manifest__.py
    │   ├── models/
    │   │   ├── estate_property.py
    │   │   └── estate_offer.py
    │   ├── views/
    │   │   ├── estate_property_views.xml
    │   │   └── estate_offer_views.xml
    │   └── security/
    │       └── ir.model.access.csv
    └── README.md

```

---

## 👷 **Développement Futur**

- Intégration avec le module CRM pour relier les prospects avec les offres immobilières.
- Ajout d’une fonctionnalité de rapports pour visualiser les ventes par agent.
- Automatisation des e-mails pour les notifications de suivi des offres.

---

## 🤝 **Contribuer**

1. Fork le dépôt.
2. Crée une nouvelle branche :
```bash
    git checkout -b feature/your-feature-name
```
3. Soumets une pull request une fois prêt.

---


## 📄 **Licence**

Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus d'informations.

---

## 👨‍💻 **Auteur**

Ce module a été créé dans le cadre de l'entraînement technique Odoo par Walter28.
N'hésitez pas à poser vos questions ou suggérer des améliorations ! 😊

---

