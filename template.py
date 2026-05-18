# -*- coding: utf-8 -*-
"""
================================================================================
TEMPLATE - Script utilisant les 4 modules
================================================================================
Description: Template de base pour tous les scripts
Auteur: Stoyann - support QC
Date: 2026-05-18
================================================================================
"""

import sys
from pathlib import Path
import importlib.util
from datetime import datetime
import pandas as pd


ROOT = Path(__file__).parent.parent.parent
logger = None

MODULES_CONFIG = {
    "file_manager": {
        "folder": "file-manager",
        "file": "file_manager.py",
    },
    "dbf_loader": {
        "folder": "dbf-loader",
        "file": "dbf_loader.py",
    },
    "mailer": {
        "folder": "quincaillerie-mailer",
        "file": "mailer.py",
    }
}

# =====================================================
# CHARGEMENT DYNAMIQUE DES MODULES
# =====================================================

def load_module(module_name, folder_name, file_name):
    """Charge un module Python depuis un chemin absolu"""
    module_path = ROOT / "modules" / folder_name / file_name

    if not module_path.exists():
        raise FileNotFoundError(f"Module not found: {module_path}")

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module

def init_logger_module():
    """Initialise le logger"""
    try:
        logger_module = load_module("logger_manager", "logger-manager", "logger.py")
        return logger_module.init_logger()
    except Exception as e:
        print(f"Erreur logger: {e}")
        sys.exit(1)

def init_modules():
    """Initialise tous les modules"""
    modules = {}

    for module_name, config in MODULES_CONFIG.items():
        try:
            logger.info(f"Chargement de {module_name}...")
            module = load_module(module_name, config["folder"], config["file"])
            modules[module_name] = module
            logger.info(f"  OK {module_name} charge")

        except FileNotFoundError as e:
            logger.error(f"  ERREUR {module_name}: {e}")
            raise

    return modules

# =====================================================
# EXEMPLES D'UTILISATION
# =====================================================
def example_file_manager(modules):
    """Exemple: utilisation du file_manager"""
    logger.info("--- EXEMPLE: file_manager ---")
    try:
        file_manager = modules["file_manager"]
        
        # Generer un nom de fichier
        nom = file_manager.generer_nom_fichier("rapport_test", "xlsx")
        logger.info(f"Nom genere: {nom}")
        
        # Generer un chemin - CORRECTION ICI
        chemin = file_manager.generer_chemin_fichier(nom)
        logger.info(f"Chemin genere: {chemin}")
        
        # Creer le fichier Excel
        logger.info("Creation du fichier Excel...")
        wb = file_manager.openpyxl.Workbook()
        ws = wb.active
        ws.title = "Donnees"
        
        # Ajouter des donnees
        ws.append(["ID", "Nom", "Prix", "Quantite"])
        ws.append([1, "Produit A", 10.50, 5])
        ws.append([2, "Produit B", 25.99, 3])
        ws.append([3, "Produit C", 15.00, 10])
        
        # Sauvegarder
        wb.save(chemin)
        logger.info(f"OK Fichier cree: {chemin}")
        
    except Exception as e:
        logger.error(f"Erreur dans example_file_manager: {e}")
        import traceback
        logger.error(traceback.format_exc())

def example_dbf_loader(modules):
    """Exemple: utilisation du dbf_loader"""
    logger.info("--- EXEMPLE: dbf_loader ---")
    try:
        dbf_loader = modules["dbf_loader"]
        
        logger.info("Recherche de fichiers DBF...")
        logger.info("Note: Installez un fichier DBF pour tester cette fonction")
        logger.info("Chemin attendu: ROOT/data/fichiers.dbf")
        
    except Exception as e:
        logger.error(f"Erreur dans example_dbf_loader: {e}")
        import traceback
        logger.error(traceback.format_exc())

def example_mailer(modules):
    """Exemple: utilisation du mailer avec documentation HTML"""
    logger.info("--- EXEMPLE: mailer ---")
    try:
        mailer = modules["mailer"]

        html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f9f9f9;
        }
        .container { 
            max-width: 900px; 
            margin: 0 auto; 
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 8px 8px 0 0;
            margin: -20px -20px 20px -20px;
        }
        .header h1 { font-size: 28px; margin-bottom: 5px; }
        .header p { font-size: 14px; opacity: 0.9; }
        h2 { 
            color: #667eea;
            font-size: 20px;
            margin-top: 25px;
            margin-bottom: 15px;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }
        h3 { 
            color: #555;
            font-size: 16px;
            margin-top: 15px;
            margin-bottom: 10px;
        }
        .section { 
            margin: 20px 0; 
            padding: 20px; 
            background: #f5f7fa; 
            border-left: 4px solid #667eea;
            border-radius: 4px;
        }
        .code-block { 
            background: #2d2d2d; 
            color: #f8f8f2; 
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            line-height: 1.4;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        .note {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
        }
        .success {
            background: #d4edda;
            border-left: 4px solid #28a745;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
            color: #155724;
        }
        .error {
            background: #f8d7da;
            border-left: 4px solid #dc3545;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
            color: #721c24;
        }
        ul, ol { margin-left: 20px; margin-top: 10px; }
        li { margin: 8px 0; }
        .footer {
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            text-align: center;
            color: #666;
            font-size: 12px;
        }
        .status {
            background: #e7f3ff;
            border-left: 4px solid #2196F3;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
            color: #0c5aa0;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }
        th {
            background: #667eea;
            color: white;
            padding: 12px;
            text-align: left;
        }
        td {
            padding: 10px 12px;
            border-bottom: 1px solid #ddd;
        }
        tr:hover {
            background: #f5f7fa;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>DOCUMENTATION TEMPLATE SCRIPT</h1>
            <p>Guide complet d'utilisation des 4 modules Python</p>
        </div>

        <h2>1. INTRODUCTION</h2>
        <div class="section">
            <p>Ce template script demontre l'utilisation de 4 modules essentiels pour vos projets Python:</p>
            <ul>
                <li><strong>file_manager</strong> - Gestion des fichiers et repertoires</li>
                <li><strong>dbf_loader</strong> - Chargement et traitement des fichiers DBF</li>
                <li><strong>mailer</strong> - Envoi d'emails avec attachements</li>
                <li><strong>logger_manager</strong> - Journalisation des operations</li>
            </ul>
        </div>

        <h2>2. ARCHITECTURE DU PROJET</h2>
        <div class="section">
            <p>Structure recommandee:</p>
            <div class="code-block">
ROOT/
├── modules/
│   ├── file-manager/
│   │   └── file_manager.py
│   ├── dbf-loader/
│   │   └── dbf_loader.py
│   ├── quincaillerie-mailer/
│   │   └── mailer.py
│   └── logger-manager/
│       └── logger.py
├── scripts/
│   ├── template-script/
│   │   └── template.py
│   └── autres_scripts/
├── data/
│   └── fichiers.dbf
└── dochistory/
            </div>
        </div>

        <h2>3. MODULE FILE_MANAGER</h2>
        <div class="section">
            <h3>Description</h3>
            <p>Utilitaire pour generer des noms et chemins de fichiers avec timestamps</p>
            
            <h3>Fonctions principales</h3>
            <table>
                <tr>
                    <th>Fonction</th>
                    <th>Description</th>
                    <th>Exemple</th>
                </tr>
                <tr>
                    <td>generer_nom_fichier(base, ext)</td>
                    <td>Genere un nom avec timestamp</td>
                    <td>rapport_test_20260518_143022.xlsx</td>
                </tr>
                <tr>
                    <td>generer_chemin_fichier(dossier, nom)</td>
                    <td>Genere un chemin complet</td>
                    <td>ROOT/dochistory/test_combined/...</td>
                </tr>
            </table>

            <h3>Exemple d'utilisation</h3>
            <div class="code-block">
from modules.file_manager import generer_nom_fichier, generer_chemin_fichier

# Generer un nom
nom = generer_nom_fichier("rapport", "xlsx")
print(nom)  # rapport_20260518_143022.xlsx

# Generer un chemin
chemin = generer_chemin_fichier("mes_rapports", nom)
print(chemin)  # /path/to/ROOT/dochistory/mes_rapports/rapport_20260518_143022.xlsx
            </div>
        </div>

        <h2>4. MODULE DBF_LOADER</h2>
        <div class="section">
            <h3>Description</h3>
            <p>Charge et traite les fichiers DBF (base de donnees Delphi/FoxPro)</p>
            
            <h3>Fonctions principales</h3>
            <table>
                <tr>
                    <th>Fonction</th>
                    <th>Description</th>
                </tr>
                <tr>
                    <td>load_dbf(chemin)</td>
                    <td>Charge un fichier DBF</td>
                </tr>
                <tr>
                    <td>get_records()</td>
                    <td>Recupere tous les enregistrements</td>
                </tr>
                <tr>
                    <td>filter_records(colonne, valeur)</td>
                    <td>Filtre les donnees</td>
                </tr>
            </table>

            <h3>Exemple d'utilisation</h3>
            <div class="code-block">
from modules.dbf_loader import DBFLoader

# Charger le fichier
loader = DBFLoader("data/produits.dbf")

# Recuperer tous les records
records = loader.get_records()

# Filtrer par prix
produits_chers = loader.filter_records("prix", lambda x: x > 50)

# Convertir en DataFrame
df = loader.to_dataframe()
            </div>
        </div>

        <h2>5. MODULE MAILER</h2>
        <div class="section">
            <h3>Description</h3>
            <p>Envoie des emails avec support HTML et attachements</p>
            
            <h3>Parametres de configuration</h3>
            <table>
                <tr>
                    <th>Parametre</th>
                    <th>Description</th>
                    <th>Exemple</th>
                </tr>
                <tr>
                    <td>SMTP_SERVER</td>
                    <td>Serveur SMTP</td>
                    <td>smtp.gmail.com</td>
                </tr>
                <tr>
                    <td>SMTP_PORT</td>
                    <td>Port SMTP</td>
                    <td>587</td>
                </tr>
                <tr>
                    <td>EMAIL_ADDRESS</td>
                    <td>Adresse email</td>
                    <td>votre@email.com</td>
                </tr>
                <tr>
                    <td>EMAIL_PASSWORD</td>
                    <td>Mot de passe</td>
                    <td>votre_mot_de_passe</td>
                </tr>
            </table>

            <h3>Exemple d'utilisation</h3>
            <div class="code-block">
from modules.quincaillerie_mailer import envoyer_email

# Email simple
envoyer_email(
    destinataire="client@example.com",
    sujet="Test Email",
    corps="Ceci est un test"
)

# Email HTML avec attachement
envoyer_email(
    destinataire="client@example.com",
    sujet="Rapport Monthly",
    corps=html_content,
    html=True,
    attachements=["rapport.pdf"]
)
            </div>
        </div>

        <h2>6. MODULE LOGGER_MANAGER</h2>
        <div class="section">
            <h3>Description</h3>
            <p>Journalisation des operations avec fichier et console</p>
            
            <h3>Niveaux de log</h3>
            <table>
                <tr>
                    <th>Niveau</th>
                    <th>Description</th>
                    <th>Methode</th>
                </tr>
                <tr>
                    <td>DEBUG</td>
                    <td>Informations de debogage</td>
                    <td>logger.debug()</td>
                </tr>
                <tr>
                    <td>INFO</td>
                    <td>Informations generales</td>
                    <td>logger.info()</td>
                </tr>
                <tr>
                    <td>WARNING</td>
                    <td>Avertissements</td>
                    <td>logger.warning()</td>
                </tr>
                <tr>
                    <td>ERROR</td>
                    <td>Erreurs</td>
                    <td>logger.error()</td>
                </tr>
                <tr>
                    <td>CRITICAL</td>
                    <td>Erreurs critiques</td>
                    <td>logger.critical()</td>
                </tr>
            </table>

            <h3>Exemple d'utilisation</h3>
            <div class="code-block">
from modules.logger_manager import init_logger

# Initialiser
logger = init_logger()

# Utiliser
logger.debug("Message de debogage")
logger.info("Operation complete")
logger.warning("Attention!")
logger.error("Une erreur s'est produite")
logger.critical("Erreur critique!")
            </div>
        </div>

        <h2>7. CONFIGURATION ET INSTALLATION</h2>
        <div class="section">
            <h3>Prerequis</h3>
            <ul>
                <li>Python 3.8+</li>
                <li>pip (gestionnaire de paquets)</li>
            </ul>

            <h3>Installation des dependances</h3>
            <div class="code-block">
pip install openpyxl
pip install pandas
pip install dbfread
pip install python-dotenv
            </div>

            <h3>Variables d'environnement</h3>
            <p>Creer un fichier <strong>.env</strong> a la racine:</p>
            <div class="code-block">
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_ADDRESS=votre_email@gmail.com
EMAIL_PASSWORD=votre_mot_de_passe_app
            </div>

            <div class="note">
                <strong>Note:</strong> Pour Gmail, utilisez une "App Password" et non votre mot de passe principal. Activez la verification en deux etapes.
            </div>
        </div>

        <h2>8. GUIDE D'UTILISATION COMPLET</h2>
        <div class="section">
            <h3>Etape 1: Initialiser le logger</h3>
            <div class="code-block">
from modules.logger_manager import init_logger

logger = init_logger()
logger.info("Script demarre")
            </div>

            <h3>Etape 2: Charger les modules</h3>
            <div class="code-block">
import importlib.util
from pathlib import Path

def load_module(module_name, folder, file):
    path = Path(__file__).parent / folder / file
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

file_manager = load_module("file_manager", "modules/file-manager", "file_manager.py")
            </div>

            <h3>Etape 3: Traiter les donnees</h3>
            <div class="code-block">
# Generer un nom de fichier
nom = file_manager.generer_nom_fichier("resultat", "xlsx")

# Generer un chemin
chemin = file_manager.generer_chemin_fichier("resultats", nom)

# Creer un fichier Excel
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Colonne1", "Colonne2"])
wb.save(chemin)

logger.info(f"Fichier cree: {chemin}")
            </div>

            <h3>Etape 4: Envoyer un email</h3>
            <div class="code-block">
from modules.quincaillerie_mailer import envoyer_email

envoyer_email(
    destinataire="client@example.com",
    sujet="Rapport Complet",
    corps="Votre rapport est pret!",
    attachements=[chemin]
)

logger.info("Email envoye avec succes")
            </div>
        </div>

        <h2>9. GESTION DES ERREURS</h2>
        <div class="section">
            <h3>Exemple de gestion d'erreur</h3>
            <div class="code-block">
try:
    # Votre code ici
    resultat = diviser(10, 0)
except ZeroDivisionError as e:
    logger.error(f"Erreur mathematique: {e}")
except Exception as e:
    logger.error(f"Erreur inattendue: {e}")
    import traceback
    logger.error(traceback.format_exc())
finally:
    logger.info("Nettoyage des ressources")
            </div>

            <div class="error">
                <strong>Important:</strong> Toujours logger les erreurs avec la stacktrace complete pour le debogage.
            </div>
        </div>

        <h2>10. BONNES PRATIQUES</h2>
        <div class="section">
            <div class="success">
                <strong>✓ A FAIRE:</strong>
                <ul>
                    <li>Utiliser des chemins absolus avec pathlib.Path</li>
                    <li>Logger chaque etape importante</li>
                    <li>Valider les donnees avant de les traiter</li>
                    <li>Utiliser des variables d'environnement pour les secrets</li>
                    <li>Gerer les exceptions explicitement</li>
                </ul>
            </div>

            <div class="error">
                <strong>✗ A EVITER:</strong>
                <ul>
                    <li>Chemins en dur (hardcoded)</li>
                    <li>Mots de passe en clair dans le code</li>
                    <li>Ignorer les erreurs</li>
                    <li>Ne pas fermer les fichiers</li>
                    <li>Fichiers volumineux non pagines</li>
                </ul>
            </div>
        </div>

        <h2>11. REFERENCES ET LIENS UTILES</h2>
        <div class="section">
            <ul>
                <li><a href="https://docs.python.org/3/">Documentation Python officielle</a></li>
                <li><a href="https://openpyxl.readthedocs.io/">OpenpyXL - Excel</a></li>
                <li><a href="https://pandas.pydata.org/">Pandas - Data Science</a></li>
                <li><a href="https://docs.python.org/3/library/logging.html">Logging - Journalisation</a></li>
                <li><a href="https://docs.python.org/3/library/email.html">Email - Envoi emails</a></li>
            </ul>
        </div>

        <div class="status">
            <strong>✅ Status:</strong> Documentation generee avec succes<br/>
            <strong>📁 Fichiers:</strong> Verifiez le dossier 'dochistory'<br/>
            <strong>📧 Email:</strong> Consultez votre boite mail<br/>
        </div>

        <div class="footer">
            <p><strong>Template Script v1.0</strong> - Support QC - 2026-05-18</p>
            <p>Pour toute question: support@quincaillerie.nc</p>
        </div>
    </div>
</body>
</html>
"""

        logger.info("Preparation et envoi de l'email de documentation...")

        mailer.envoyer_email(
            destinataire="support@quincaillerie.nc",
            sujet="Documentation - Template Script Complet",
            corps=html_content,
            html=True
        )

        logger.info("OK Email envoye avec succes!")
        logger.info("   Destinataire: support@quincaillerie.nc")
        logger.info("   Format: HTML complet et stylise")

    except Exception as e:
        logger.error(f"Erreur dans example_mailer: {e}")
        import traceback
        logger.error(traceback.format_exc())

# =====================================================
# FONCTION PRINCIPALE
# =====================================================

def main():
    """Fonction principale"""
    global logger

    try:
        logger = init_logger_module()

        logger.info("")
        logger.info("="*80)
        logger.info("DEMARRAGE DU SCRIPT TEMPLATE")
        logger.info("="*80)
        logger.info("")

        logger.info("INITIALISATION DES MODULES...")
        logger.info("")
        modules = init_modules()

        logger.info("")
        logger.info("OK Tous les modules sont charges avec succes !")
        logger.info("")

        logger.info("EXECUTION DES EXEMPLES...")
        logger.info("")

        example_file_manager(modules)
        logger.info("")

        example_dbf_loader(modules)
        logger.info("")

        example_mailer(modules)
        logger.info("")

        logger.info("="*80)
        logger.info("OK SCRIPT TEMPLATE TERMINE AVEC SUCCES")
        logger.info("="*80)
        logger.info("")
        logger.info("Verifiez :")
        logger.info("   - Le dossier 'dochistory' pour voir le fichier cree")
        logger.info("   - Votre boite mail pour voir l'email de documentation")
        logger.info("")

    except Exception as e:
        if logger:
            logger.error("")
            logger.error("="*80)
            logger.error("ERREUR CRITIQUE")
            logger.error("="*80)
            logger.error(f"{e}")
            import traceback
            logger.error(traceback.format_exc())
        else:
            print(f"ERREUR CRITIQUE: {e}")
            import traceback
            traceback.print_exc()
        sys.exit(1)

# =====================================================
# POINT D'ENTREE
# =====================================================

if __name__ == "__main__":
    main()
