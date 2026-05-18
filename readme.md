# 📦 TEMPLATE PYTHON MODULAIRE

## Documentation Utilisateur Complète

---

# 📖 Introduction

Bienvenue dans la documentation du Template Python Modulaire.

Ce système a été conçu pour permettre :

* le chargement automatique de modules Python,
* l’exploitation de fichiers DBF,
* la génération de fichiers,
* l’envoi automatique d’emails,
* l’automatisation de tâches métier,
* la création de scripts de reporting professionnels.

Ce template permet de standardiser tous les scripts internes de l’entreprise afin d’avoir :

✅ une structure propre
✅ des logs uniformes
✅ une maintenance simplifiée
✅ une architecture évolutive
✅ des scripts facilement réutilisables

---

# 🎯 Objectif du Template

Le but principal du template est de permettre aux développeurs et analystes :

* d’ajouter rapidement de nouveaux scripts,
* de réutiliser des modules communs,
* d’éviter la duplication de code,
* de centraliser les traitements métiers.

---

# 🏗️ Architecture Générale

Le projet est organisé sous forme modulaire.

Chaque fonctionnalité importante est placée dans un module indépendant.

---

# 📂 Structure du projet

```bash
dev/
│
├── modules/
│   │
│   ├── file-manager/
│   │   └── file_manager.py
│   │
│   ├── dbf-loader/
│   │   └── dbf_loader.py
│   │
│   └── quincaillerie-mailer/
│       └── mailer.py
│
└── scripts/
    │
    └── template/
        └── main.py
```

---

# 🧠 Comprendre le fonctionnement

Le script principal :

1. détecte automatiquement le dossier racine du projet,
2. charge les modules nécessaires,
3. vérifie les fonctions disponibles,
4. exécute les traitements,
5. affiche les logs,
6. gère les erreurs.

---

# 🔧 Les modules

---

# 1️⃣ Module FILE MANAGER

## 📌 Rôle

Le module `file-manager` permet :

* de générer des noms de fichiers,
* d’organiser les exports,
* de créer automatiquement des chemins,
* d’éviter les conflits de fichiers.

---

## 📁 Exemple d’utilisation

```python
file_name = "rapport_mai_2026.xlsx"

file_path = generer_chemin_fichier(file_name)
```

---

## 📌 Cas d’usage

Le module peut être utilisé pour :

* les exports Excel,
* les rapports PDF,
* les sauvegardes automatiques,
* les fichiers temporaires,
* les archives.

---

# 2️⃣ Module DBF LOADER

## 📌 Rôle

Le module `dbf-loader` sert à charger les anciens fichiers `.DBF`.

Ces fichiers sont souvent utilisés dans :

* les anciens ERP,
* les logiciels de caisse,
* les logiciels de stock,
* les systèmes historiques.

---

## 📂 Exemple

```python
df = get_dbf("qc/article.dbf")
```

---

## 📊 Résultat

Le module retourne généralement :

```python
pandas.DataFrame
```

Ce DataFrame peut ensuite être :

* filtré,
* analysé,
* exporté,
* envoyé vers SQL,
* utilisé dans Power BI.

---

## 📌 Exemple concret

```python
df_filtered = df[df["NART"] == "710092"]
```

---

# 3️⃣ Module MAILER

## 📌 Rôle

Le module `mailer` permet :

* d’envoyer des emails automatiques,
* d’envoyer des rapports,
* d’ajouter des pièces jointes,
* d’automatiser les notifications.

---

## 📧 Exemple

```python
envoyer_email(
    destinataire="support@entreprise.nc",
    sujet="Rapport automatique",
    corps="<p>Bonjour</p>",
    chemin_piece_jointe="rapport.xlsx"
)
```

---

# ⚙️ Configuration des modules

Tous les modules sont déclarés dans :

```python
MODULES_CONFIG
```

---

# 📌 Exemple

```python
MODULES_CONFIG = {
    "file_manager": {
        "folder": "file-manager",
        "file": "file_manager.py",
        "functions": [
            "generer_chemin_fichier",
            "generer_nom_fichier"
        ]
    }
}
```

---

# 🧠 Comprendre cette configuration

| Clé       | Description              |
| --------- | ------------------------ |
| folder    | dossier du module        |
| file      | fichier Python principal |
| functions | fonctions à récupérer    |

---

# 🔄 Chargement Dynamique

---

# 📌 Pourquoi utiliser un chargement dynamique ?

Le chargement dynamique permet :

✅ d’ajouter facilement des modules
✅ de ne pas modifier les imports
✅ d’avoir une architecture flexible
✅ de séparer les responsabilités

---

# ⚡ Fonction `load_module()`

Cette fonction :

* construit le chemin du module,
* vérifie son existence,
* charge le fichier Python,
* retourne le module prêt à être utilisé.

---

# 📌 Exemple

```python
module = load_module(
    "file_manager",
    "file-manager",
    "file_manager.py"
)
```

---

# 🚀 Fonction `init_modules()`

Cette fonction initialise automatiquement tous les modules.

Elle :

* charge les modules,
* récupère les fonctions,
* vérifie leur présence,
* prépare le dictionnaire global.

---

# 📦 Résultat obtenu

```python
modules = {
    "file_manager": {
        "module": module,
        "functions": {
            "generer_chemin_fichier": function
        }
    }
}
```

---

# 📝 Le système de logs

Le système de logs permet :

* de suivre le traitement,
* de détecter les erreurs,
* d’avoir un historique clair.

---

# 📌 Types de logs

| Niveau  | Description             |
| ------- | ----------------------- |
| DEBUG   | informations techniques |
| INFO    | informations générales  |
| WARNING | avertissements          |
| ERROR   | erreurs critiques       |

---

# 📌 Exemple réel

```bash
[14:32:10] ℹ️ [INFO] Chargement du module: file_manager...
```

---

# ❌ Gestion des erreurs

Le template possède une gestion avancée des erreurs.

---

# 📌 Exemple

```python
except Exception as e:
    log(f"❌ ERREUR CRITIQUE: {e}", "ERROR")
```

---

# 📌 Types d’erreurs gérées

✅ module manquant
✅ fonction absente
✅ erreur DBF
✅ erreur email
✅ erreur critique globale

---

# 🏁 Fonction principale

---

# 📌 Point d’entrée

```python
if __name__ == "__main__":
    main()
```

---

# 📌 Rôle de `main()`

La fonction principale :

1. initialise les modules,
2. lance les traitements,
3. affiche les logs,
4. gère les erreurs.

---

# 📊 Cas d’utilisation métier

---

# 🏪 Quincaillerie

Le template peut servir à :

* lire les articles,
* générer les rapports de ventes,
* exporter vers Excel,
* envoyer les rapports aux responsables.

---

# 📦 Gestion de stock

Le template peut :

* lire les DBF,
* détecter les ruptures,
* générer des alertes,
* envoyer des notifications.

---

# 📈 Reporting Power BI

Le template peut :

* préparer les données,
* nettoyer les DBF,
* générer des tables SQL,
* alimenter Power BI.

---

# 🧪 Exemple de workflow complet

---

# Étape 1

Lecture du DBF :

```python
df = get_dbf("qc/article.dbf")
```

---

# Étape 2

Filtrage :

```python
df_filtered = df[df["FAM"] == "OUTILLAGE"]
```

---

# Étape 3

Export :

```python
file_path = generer_chemin_fichier("rapport.xlsx")
```

---

# Étape 4

Envoi automatique :

```python
envoyer_email(...)
```

---

# 🔐 Bonnes pratiques

---

# ✅ Toujours faire

* utiliser les logs,
* commenter le code,
* tester les modules séparément,
* utiliser Git,
* vérifier les erreurs.

---

# ❌ Ne jamais faire

* stocker des mots de passe en dur,
* modifier les modules en production,
* envoyer des emails de test à de vrais utilisateurs,
* exécuter des scripts sans logs.

---

# 📦 Dépendances recommandées

---

# Installation

```bash
pip install pandas
pip install openpyxl
pip install sqlalchemy
pip install dbfread
```

---

# 🛠️ Évolutions possibles

---

# Fonctionnalités futures

Le template peut évoluer avec :

✅ configuration `.env`
✅ exports PDF
✅ exports Excel avancés
✅ logs dans fichiers
✅ scheduler automatique
✅ interface web
✅ API REST
✅ synchronisation SQL
✅ monitoring serveur

---

# 🌍 Cas d’usage réels

Ce template est adapté pour :

* ERP,
* reporting,
* migration DBF,
* automatisation métier,
* ETL,
* gestion de stock,
* synchronisation SQL,
* reporting Power BI,
* automatisation emails.

---

# 👨‍💻 Public cible

Ce template est destiné :

* aux développeurs Python,
* aux data analysts,
* aux administrateurs systèmes,
* aux services informatiques,
* aux entreprises utilisant encore des DBF.

---

# 📜 Conclusion

Ce template constitue une base professionnelle robuste permettant de construire rapidement :

* des outils métiers,
* des scripts d’automatisation,
* des pipelines ETL,
* des systèmes de reporting.

Grâce à son architecture modulaire, il peut évoluer facilement selon les besoins de l’entreprise.

---
