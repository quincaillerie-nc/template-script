# -*- coding: utf-8 -*-
"""
================================================================================
TEMPLATE - Script utilisant les 4 modules (file-manager, dbf-loader, mailer, logger-manager)
================================================================================
Description: Template de base pour tous les scripts utilisant ces modules
Auteur: [Ton nom]
Date: 2026-05-18
================================================================================
"""

import sys
from pathlib import Path
import importlib.util
from datetime import datetime

# =====================================================
# CONFIGURATION GLOBALE
# =====================================================

# Récupère le répertoire racine (dev/)
ROOT = Path(__file__).parent.parent.parent

# Config des modules à charger
MODULES_CONFIG = {
    "file_manager": {
        "folder": "file-manager",
        "file": "file_manager.py",
        "functions": ["generer_chemin_fichier", "generer_nom_fichier"]
    },
    "dbf_loader": {
        "folder": "dbf-loader",
        "file": "dbf_loader.py",
        "functions": ["get_dbf"]  # À adapter selon tes vraies fonctions
    },
    "mailer": {
        "folder": "quincaillerie-mailer",
        "file": "mailer.py",
        "functions": ["envoyer_email"]  # À adapter selon tes vraies fonctions
    }
}

# Variable globale pour le logger
logger = None

# =====================================================
# CHARGEMENT DYNAMIQUE DES MODULES
# =====================================================

def load_module(module_name, folder_name, file_name):
    """
    Charge un module Python depuis un chemin absolu
    
    Args:
        module_name (str): Nom du module
        folder_name (str): Nom du dossier (peut contenir des tirets)
        file_name (str): Nom du fichier .py
        
    Returns:
        module: Le module chargé
        
    Raises:
        FileNotFoundError: Si le fichier n'existe pas
    """
    module_path = ROOT / "modules" / folder_name / file_name
    
    if not module_path.exists():
        raise FileNotFoundError(
            f"❌ Module not found: {module_path}\n"
            f"   Chemin attendu: {module_path}"
        )
    
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    return module


def init_logger_module():
    """
    Initialise le logger depuis le module logger-manager
    
    Returns:
        logging.Logger: L'instance du logger configurée
    """
    try:
        logger_module = load_module(
            "logger_manager",
            "logger-manager",
            "logger.py"
        )
        
        # Récupère la fonction init_logger et l'appelle
        init_logger_func = logger_module.init_logger
        return init_logger_func()
        
    except FileNotFoundError as e:
        print(f"❌ Erreur de chargement du logger: {e}")
        sys.exit(1)


def init_modules():
    """
    Initialise tous les modules configurés
    
    Returns:
        dict: Dictionnaire contenant tous les modules et leurs fonctions
    """
    modules = {}
    
    for module_name, config in MODULES_CONFIG.items():
        try:
            logger.info(f"Chargement du module: {module_name}...")
            
            module = load_module(
                module_name,
                config["folder"],
                config["file"]
            )
            
            modules[module_name] = {
                "module": module,
                "functions": {}
            }
            
            # Récupère les fonctions du module
            for func_name in config["functions"]:
                if hasattr(module, func_name):
                    modules[module_name]["functions"][func_name] = getattr(module, func_name)
                    logger.debug(f"  ✓ Fonction trouvée: {func_name}")
                else:
                    logger.warning(f"  ⚠ Fonction manquante: {func_name}")
            
            logger.info(f"✅ Module chargé: {module_name}")
            
        except FileNotFoundError as e:
            logger.error(f"❌ Erreur de chargement: {e}")
            sys.exit(1)
    
    return modules

# =====================================================
# EXEMPLES D'UTILISATION DES MODULES
# =====================================================

def example_file_manager(modules):
    """Exemple d'utilisation du module file-manager"""
    logger.info("--- EXEMPLE: file-manager ---")
    
    try:
        generer_chemin_fichier = modules["file_manager"]["functions"]["generer_chemin_fichier"]
        
        # Exemple: générer un chemin pour un fichier
        file_name = "mon_rapport_mai-2026.xlsx"
        file_path = generer_chemin_fichier(file_name)
        
        logger.info(f"Fichier généré à: {file_path}")
        
    except Exception as e:
        logger.error(f"Erreur dans example_file_manager: {e}")


def example_dbf_loader(modules):
    """Exemple d'utilisation du module dbf-loader"""
    logger.info("--- EXEMPLE: dbf-loader ---")
    
    try:
        get_dbf = modules["dbf_loader"]["functions"]["get_dbf"]
        
        # Exemple: charger un fichier DBF
        df = get_dbf("qc/article.dbf")
        
        logger.info(f"DBF chargé avec {len(df)} lignes")
        logger.debug(f"Colonnes: {list(df.columns)}")
        
        # Exemple: filtrer les données
        # df_filtered = df[df["NART"].astype(str).isin(["710092", "760043"])]
        # logger.info(f"Données filtrées: {len(df_filtered)} lignes")
        
    except Exception as e:
        logger.error(f"Erreur dans example_dbf_loader: {e}")


def example_mailer(modules):
    """Exemple d'utilisation du module mailer"""
    logger.info("--- EXEMPLE: mailer ---")
    
    try:
        envoyer_email = modules["mailer"]["functions"]["envoyer_email"]
        
        # Exemple: envoyer un email
        # NOTE: Décommente si tu veux vraiment envoyer un email
        
        # envoyer_email(
        #     destinataire="support@quincaillerie.nc",
        #     sujet="[TEST] Template Script",
        #     corps="<p>Ceci est un email de test du template</p>",
        #     chemin_piece_jointe=None
        # )
        # logger.info("Email envoyé avec succès")
        
        logger.info("Fonction mailer disponible (exemple commenté)")
        
    except Exception as e:
        logger.error(f"Erreur dans example_mailer: {e}")

# =====================================================
# FONCTION PRINCIPALE
# =====================================================

def main():
    """Fonction principale du script"""
    global logger
    
    try:
        # ÉTAPE 1: Initialiser le logger en premier
        logger = init_logger_module()
        
        logger.info("="*80)
        logger.info("DÉMARRAGE DU SCRIPT")
        logger.info("="*80)
        logger.info("")
        
        # ÉTAPE 2: Initialiser tous les autres modules
        modules = init_modules()
        
        logger.info("")
        logger.info("✅ Tous les modules sont chargés avec succès !")
        logger.info("")
        
        # ÉTAPE 3: Exemples d'utilisation
        example_file_manager(modules)
        logger.info("")
        
        example_dbf_loader(modules)
        logger.info("")
        
        example_mailer(modules)
        logger.info("")
        
        logger.info("="*80)
        logger.info("✅ SCRIPT TERMINÉ AVEC SUCCÈS")
        logger.info("="*80)
        
    except Exception as e:
        if logger:
            logger.error(f"❌ ERREUR CRITIQUE: {e}")
            import traceback
            logger.error(traceback.format_exc())
        else:
            print(f"[ERROR] ❌ ERREUR CRITIQUE: {e}")
            import traceback
            traceback.print_exc()
        sys.exit(1)

# =====================================================
# POINT D'ENTRÉE
# =====================================================

if __name__ == "__main__":
    main()
