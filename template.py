# -*- coding: utf-8 -*-
"""
================================================================================
SCRIPT : scripts/template-script/template.py
================================================================================
Template de base pour tous les nouveaux scripts du projet Quincaillerie NC.

Pour créer un nouveau script :
  1. Copier ce fichier dans scripts/<nom_script>/
  2. Renommer le fichier
  3. Adapter la section CONFIGURATION
  4. Écrire la logique dans main()

Auteur  : Stoyann - support QC
Date    : 2026-05-18
================================================================================
"""

import sys
from pathlib import Path

# =====================================================
# CHEMINS & IMPORT DES MODULES
# =====================================================
ROOT        = Path(__file__).resolve().parent.parent.parent
MODULES_DIR = ROOT / "modules"

sys.path.insert(0, str(MODULES_DIR))
from _loader import load_module

# Chargement des modules
_fm     = load_module("file-manager",         "file_manager.py")
_dbf    = load_module("dbf-loader",           "dbf_loader.py")
_mailer = load_module("quincaillerie-mailer",  "mailer.py")
_log    = load_module("logger-manager",       "logger.py")

# Fonctions exposées
generer_nom_fichier    = _fm.generer_nom_fichier
generer_chemin_fichier = _fm.generer_chemin_fichier
get_dbf                = _dbf.get_dbf
envoyer_email          = _mailer.envoyer_email
envoyer_debug          = _mailer.envoyer_debug
init_logger            = _log.init_logger

# =====================================================
# INITIALISATION LOGGER
# =====================================================
logger = init_logger("template")

# =====================================================
# CONFIGURATION  ← À ADAPTER
# =====================================================
MAIL_SUPPORT = ["support@quincaillerie.nc"]


# =====================================================
# FONCTIONS MÉTIER  ← À COMPLÉTER
# =====================================================
def exemple_file_manager():
    """Démo : génération d'un fichier Excel."""
    logger.info("--- Exemple file_manager ---")
    import openpyxl

    nom    = generer_nom_fichier("template_test", "xlsx")
    chemin = generer_chemin_fichier(nom)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Données"
    ws.append(["ID", "Produit", "Prix"])
    ws.append([1, "Vis M6", 0.15])
    ws.append([2, "Boulon M8", 0.30])
    wb.save(chemin)

    logger.info(f"✅ Fichier créé : {chemin}")
    return chemin


def exemple_dbf_loader():
    """Démo : chargement du DBF article via le réseau."""
    logger.info("--- Exemple dbf_loader ---")
    try:
        df = get_dbf("qc/article.dbf")
        logger.info(f"✅ {len(df)} lignes chargées depuis article.dbf")
        logger.info(f"   Colonnes : {list(df.columns[:5])}")
    except Exception as e:
        logger.error(f"❌ Erreur DBF : {e}")


def exemple_mailer(chemin_fichier=None):
    """Démo : envoi d'un email HTML avec pièce jointe."""
    logger.info("--- Exemple mailer ---")

    corps = """
    <html><body>
    <h2 style="color:#4472C4;">Template Script — Test email</h2>
    <p>Cet email confirme que le module <strong>mailer</strong> fonctionne.</p>
    <ul>
        <li>✅ file-manager</li>
        <li>✅ dbf-loader</li>
        <li>✅ quincaillerie-mailer</li>
        <li>✅ logger-manager</li>
    </ul>
    <p style="color:#777;font-size:12px;">— Quincaillerie NC | Script automatique</p>
    </body></html>
    """

    ok = envoyer_email(
        destinataire=MAIL_SUPPORT,
        sujet="[TEMPLATE] Test email automatique",
        corps=corps,
        html=True,
        chemin_piece_jointe=str(chemin_fichier) if chemin_fichier else None
    )

    if ok:
        logger.info("✅ Email envoyé avec succès")
    else:
        logger.error("❌ Échec envoi email")


# =====================================================
# MAIN
# =====================================================
def main():
    logger.info("=" * 60)
    logger.info("DÉMARRAGE — template")
    logger.info("=" * 60)

    try:
        # Étape 1 : file manager
        chemin = exemple_file_manager()

        # Étape 2 : dbf loader
        exemple_dbf_loader()

        # Étape 3 : mailer
        exemple_mailer(chemin_fichier=chemin)

        logger.info("=" * 60)
        logger.info("✅ Template terminé avec succès")
        logger.info("=" * 60)

    except Exception as e:
        logger.error(f"❌ ERREUR CRITIQUE : {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()