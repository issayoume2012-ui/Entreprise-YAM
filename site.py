import streamlit as st
import time
import urllib.parse
import base64
from datetime import datetime, timedelta  #=====================================================
# CONFIG (Exécuté une seule fois, au tout début)
# =====================================================
st.set_page_config(
    page_title="YouAgronoMe",
    page_icon="🌾",
    layout="wide"
)

# =====================================================
# SESSION STATES
# =====================================================
if "panier" not in st.session_state:
    st.session_state.panier = []

if "historique" not in st.session_state:
    st.session_state.historique = []


# =====================================================
# INJECTION CSS GLOBAL (Toutes les règles CSS regroupées)
# =====================================================
st.markdown("""
<style>
/* Importation de la police globale */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');

.stApp, .main .block-container {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* 1. Suppression des espaces blancs natifs de Streamlit tout en haut */
.stAppHeader {
    display: none !important;
}
.main .block-container {
    padding-top: 20px !important; /* Espace minimal en haut */
    max-width: 95% !important;
}

/* 2. Transformation XXL du st.radio en barre de navigation horizontale premium */
div[data-testid="stRadio"] {
    background-color: rgba(255, 255, 255, 0.95);
    padding: 12px !important;
    border-radius: 24px !important;
    box-shadow: 0 15px 35px rgba(0,0,0,0.06) !important;
    border: 1px solid rgba(0,0,0,0.03) !important;
    margin-bottom: 30px !important;
}

/* Cacher le label obligatoire de Streamlit pour le menu */
div[data-testid="stRadio"] > label {
    display: none !important;
}

/* Aligner les options horizontalement de manière équitable */
div[data-testid="stRadio"] > div[role="radiogroup"] {
    display: flex !important;
    flex-direction: row !important;
    justify-content: space-around !important;
    flex-wrap: wrap !important;
    gap: 10px !important;
}

/* Style XXL pour chaque option du menu (Label de la radio) */
div[data-testid="stRadio"] > div[role="radiogroup"] > label {
    flex: 1 !important;
    min-width: 140px !important;
    font-size: 20px !important; /* Texte XXL */
    font-weight: 700 !important;
    padding: 20px 15px !important; /* Boutons hauts et larges */
    margin: 0px 5px !important;
    border-radius: 16px !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    text-align: center !important;
    background-color: transparent !important;
    color: #444444 !important;
    cursor: pointer !important;
    border: none !important;
    display: block !important;
}

/* Cacher le petit cercle radio d'origine de Streamlit */
div[data-testid="stRadio"] > div[role="radiogroup"] > label > div:first-child {
    display: none !important;
}

/* Effet au survol (Hover) */
div[data-testid="stRadio"] > div[role="radiogroup"] > label:hover {
    background-color: rgba(67, 160, 71, 0.1) !important;
    color: #1B5E20 !important;
    transform: translateY(-3px) !important;
}

/* Style de l'onglet actif / sélectionné (Dégradé Eau & Plante XXL) */
div[data-testid="stRadio"] > div[role="radiogroup"] > label[data-checked="true"] {
    background: linear-gradient(135deg, #1B5E20, #0288D1) !important;
    color: white !important;
    font-weight: 800 !important;
    box-shadow: 0 10px 25px rgba(27, 94, 32, 0.25) !important;
}

/* FORÇAGE DE LA HAUTEUR IDENTIQUE POUR TOUTES LES COLONNES STREAMLIT */
div[data-testid="stColumn"] > div {
    height: 100%;
    display: flex;
    flex-direction: column;
}

/* Section HERO VERSION XXL */
.hero {
    background: linear-gradient(135deg, rgba(27, 94, 32, 0.9), rgba(2, 136, 209, 0.7)),
                url("https://images.unsplash.com/photo-1500937386664-56d1dfef3854");
    background-size: cover;
    background-position: center;
    border-radius: 32px;
    padding: 130px 60px;
    text-align: center;
    color: white;
    margin-bottom: 60px;
    box-shadow: 0 30px 60px rgba(27, 94, 32, 0.25);
    transition: transform 0.5s ease, box-shadow 0.5s ease;
}

.hero:hover {
    transform: scale(1.01);
    box-shadow: 0 35px 70px rgba(27, 94, 32, 0.35);
}

.hero h1 {
    font-size: 72px;
    font-weight: 800;
    margin-bottom: 20px;
    letter-spacing: -2px;
    text-shadow: 0 4px 15px rgba(0,0,0,0.3);
}

.hero h2 {
    font-size: 32px;
    font-weight: 600;
    margin-bottom: 40px;
    opacity: 0.95;
    letter-spacing: 1px;
}

.hero p {
    max-width: 950px;
    margin: 0 auto;
    font-size: 22px;
    line-height: 1.8;
    opacity: 0.95;
}

/* Titres des Sections */
.section-title {
    text-align: center;
    font-size: 36px;
    font-weight: 800;
    color: #1B5E20;
    margin: 70px 0 40px 0;
    position: relative;
}

.section-title::after {
    content: '';
    display: block;
    width: 80px;
    height: 5px;
    background: linear-gradient(90deg, #43A047, #0288D1);
    margin: 15px auto 0 auto;
    border-radius: 3px;
}

/* Base universelle des cartes */
.glass-base {
    border-radius: 22px;
    padding: 35px 25px;
    height: 100%;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.03);
    box-sizing: border-box;
}

.glass-base:hover {
    transform: translateY(-6px);
}

/* 📊 STYLE DYNAMIQUE DES CHIFFRES CLÉS */
.stat-card {
    background: white;
    border-radius: 20px;
    padding: 25px 20px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    border: 1px solid rgba(0,0,0,0.03);
    transition: all 0.4s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.stat-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.12);
}
.stat-number {
    font-size: 46px;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 8px;
}
.stat-label {
    font-size: 15px;
    font-weight: 600;
    color: #666;
}
.stat-plante .stat-number { color: #2E7D32; }
.stat-plante { border-bottom: 4px solid #2E7D32; }
.stat-sol .stat-number { color: #6D4C41; }
.stat-sol { border-bottom: 4px solid #6D4C41; }
.stat-eau .stat-number { color: #0288D1; }
.stat-eau { border-bottom: 4px solid #0288D1; }
.stat-innovation .stat-number { color: #673AB7; }
.stat-innovation { border-bottom: 4px solid #673AB7; }

/* 🌾 STYLE DYNAMIQUE DES DOMAINES D'INTERVENTION */
.domaine-card {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 18px;
    padding: 25px;
    text-align: center;
    font-weight: 700;
    font-size: 18px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.04);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    height: 100%;
    box-sizing: border-box;
}
.domaine-plante { border: 2px solid rgba(46, 125, 50, 0.2); color: #2E7D32; }
.domaine-plante:hover { background: #2E7D32; color: white; transform: scale(1.05); }

.domaine-eau { border: 2px solid rgba(2, 136, 209, 0.2); color: #0288D1; }
.domaine-eau:hover { background: #0288D1; color: white; transform: scale(1.05); }

.domaine-innovation { border: 2px solid rgba(103, 58, 183, 0.2); color: #673AB7; }
.domaine-innovation:hover { background: #673AB7; color: white; transform: scale(1.05); }

.domaine-sol { border: 2px solid rgba(109, 76, 65, 0.2); color: #6D4C41; }
.domaine-sol:hover { background: #6D4C41; color: white; transform: scale(1.05); }

/* VARIATIONS THÉMATIQUES DES SERVICES */
.card-eau { background: rgba(225, 245, 254, 0.85); border: 1px solid rgba(2, 136, 209, 0.25); backdrop-filter: blur(10px); }
.card-eau:hover { box-shadow: 0 20px 40px rgba(2, 136, 209, 0.2); border-color: rgba(2, 136, 209, 0.5); }
.card-eau h3 { color: #0288D1; font-weight: 700; margin-bottom: 12px; font-size: 22px; }
.card-eau p { color: #01579B; font-size: 15px; line-height: 1.6; margin: 0; }

.card-innovation { background: rgba(243, 229, 245, 0.85); border: 1px solid rgba(124, 77, 255, 0.25); backdrop-filter: blur(10px); }
.card-innovation:hover { box-shadow: 0 20px 40px rgba(124, 77, 255, 0.2); border-color: rgba(124, 77, 255, 0.5); }
.card-innovation h3 { color: #673AB7; font-weight: 700; margin-bottom: 12px; font-size: 22px; }
.card-innovation p { color: #4A148C; font-size: 15px; line-height: 1.6; margin: 0; }

.card-sol { background: rgba(245, 240, 235, 0.9); border: 1px solid rgba(141, 110, 99, 0.25); backdrop-filter: blur(10px); }
.card-sol:hover { box-shadow: 0 20px 40px rgba(141, 110, 99, 0.2); border-color: rgba(141, 110, 99, 0.5); }
.card-sol h3 { color: #5D4037; font-weight: 700; margin-bottom: 12px; font-size: 22px; }
.card-sol p { color: #3E2723; font-size: 15px; line-height: 1.6; margin: 0; }

.card-plante { background: rgba(232, 245, 233, 0.85); border: 1px solid rgba(67, 160, 71, 0.25); backdrop-filter: blur(10px); }
.card-plante:hover { box-shadow: 0 20px 40px rgba(67, 160, 71, 0.2); border-color: rgba(67, 160, 71, 0.5); }
.card-plante h3 { color: #1B5E20; font-weight: 700; margin-bottom: 12px; font-size: 22px; }
.card-plante p { color: #1B5E20; font-size: 15px; line-height: 1.6; margin: 0; }

.vision-nature {
    background: linear-gradient(135deg, #1B5E20, #0288D1, #8D6E63);
    color: white; border-radius: 22px; padding: 35px 25px; height: 100%; flex-grow: 1;
    display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;
    box-shadow: 0 12px 30px rgba(27, 94, 32, 0.25); transition: all 0.3s ease; box-sizing: border-box;
}
.vision-nature:hover { transform: translateY(-6px); box-shadow: 0 25px 50px rgba(27, 94, 32, 0.4); }
.vision-nature h3 { color: white; font-weight: 700; margin-bottom: 12px; font-size: 22px; }
.vision-nature p { color: rgba(255, 255, 255, 0.95); font-size: 15px; line-height: 1.6; margin: 0; }

/* Ajustement pour les écrans tactiles et mobiles */
@media (max-width: 992px) {
    div[data-testid="stRadio"] > div[role="radiogroup"] > label {
        font-size: 15px !important;
        padding: 12px 5px !important;
    }
    .hero { padding: 90px 30px; }
    .hero h1 { font-size: 52px; }
    .hero h2 { font-size: 24px; }
}
@media (max-width: 768px) {
    .hero { padding: 60px 20px; margin-bottom: 40px; }
    .hero h1 { font-size: 38px; }
    .hero h2 { font-size: 20px; }
    .hero p { font-size: 16px; }
    .section-title { font-size: 28px; }
    .glass-base, .vision-nature { padding: 25px 15px; }
    .stat-number { font-size: 36px; }
}
@media (max-width: 480px) {
    .hero h1 { font-size: 30px; }
    .hero h2 { font-size: 16px; }
    .section-title { font-size: 24px; }
}
</style>
""", unsafe_allow_html=True)


# =====================================================
# ADMINISTRATION — PARAMÈTRES EN SIDEBAR
# =====================================================
ADMIN_LOGIN = "iy@2012"
ADMIN_PASSWORD = "issayoume2026"

DEFAULT_PRODUCTS = [
    {"image":"to.jpg","nom":"Tomates fraîches","prix":3500,"conditionnement":"Sac de 5Kg","cat":"Fruits & Légumes","tag":"🔥 Prix Producteur","origine":"Niayes","dispo":True,"vedette":True},
    {"image":"fr.jpg","nom":"Fraises locales","prix":5000,"conditionnement":"Sachet de 2Kg","cat":"Fruits & Légumes","tag":"✨ Spécialité","origine":"Thiès (Mboro)","dispo":True,"vedette":True},
    {"image":"og.jpg","nom":"Oignons rouges","prix":2500,"conditionnement":"Sac de 5Kg","cat":"Fruits & Légumes","tag":"","origine":"Vallée du Fleuve","dispo":True,"vedette":False},
    {"image":"cr.jpg","nom":"Carottes lavées","prix":3000,"conditionnement":"Sac de 5Kg","cat":"Fruits & Légumes","tag":"","origine":"Zone des Niayes","dispo":True,"vedette":False},
    {"image":"pm.jpg","nom":"Piments Verts / Rouges","prix":2000,"conditionnement":"Sac de 3Kg","cat":"Fruits & Légumes","tag":"⚡ Récolte fraîche","origine":"Louga","dispo":True,"vedette":False},
    {"image":"cc.jpg","nom":"Concombres","prix":2800,"conditionnement":"Sac de 3Kg","cat":"Fruits & Légumes","tag":"","origine":"Zone des Niayes","dispo":True,"vedette":False},
    {"image":"pt.jpg","nom":"Pommes de terre local","prix":4500,"conditionnement":"Sachet de 5Kg","cat":"Fruits & Légumes","tag":"","origine":"Vallée du Fleuve","dispo":True,"vedette":False},
    {"image":"or.jpg","nom":"Oranges douces","prix":4000,"conditionnement":"Sac de 3Kg","cat":"Fruits & Légumes","tag":"","origine":"Casamance","dispo":True,"vedette":False},
    {"image":"mangue.jpg","nom":"Mangues Kent","prix":3500,"conditionnement":"Panier de 5Kg","cat":"Fruits & Légumes","tag":"🥭 Saison","origine":"Pout / Niayes","dispo":True,"vedette":True},
    {"image":"banane.jpg","nom":"Bananes douces","prix":2500,"conditionnement":"Régime (~4-5kg)","cat":"Fruits & Légumes","tag":"","origine":"Tambacounda","dispo":True,"vedette":False},
    {"image":"mais.jpg","nom":"Maïs grain jaune","prix":7000,"conditionnement":"Sac de 25Kg","cat":"Céréales & Graines","tag":"","origine":"Bassin Arachidier","dispo":True,"vedette":False},
    {"image":"arachide.jpg","nom":"Arachides décortiquées","prix":8500,"conditionnement":"Sac de 10Kg","cat":"Céréales & Graines","tag":"","origine":"Kaolack","dispo":True,"vedette":False},
    {"image":"riz.jpg","nom":"Riz local brisé","prix":12000,"conditionnement":"Sac de 25Kg","cat":"Céréales & Graines","tag":"⭐ Souveraineté","origine":"Vallée du Fleuve (Podor)","dispo":True,"vedette":True},
    {"image":"mil.jpg","nom":"Mil Souna","prix":9000,"conditionnement":"Sac de 20Kg","cat":"Céréales & Graines","tag":"","origine":"Région de Fatick","dispo":True,"vedette":False},
    {"image":"pasteque.jpg","nom":"Pastèques","prix":6000,"conditionnement":"Gros calibre (L'unité)","cat":"Fruits & Légumes","tag":"","origine":"Kaffrine","dispo":True,"vedette":False},
    {"image":"citron.jpg","nom":"Citrons verts","prix":2000,"conditionnement":"Filet de 2.5kg","cat":"Fruits & Légumes","tag":"","origine":"Thiès","dispo":True,"vedette":False},
    {"image":"niebe.jpg","nom":"Niébé (Haricot)","prix":6500,"conditionnement":"Sac de 10Kg","cat":"Céréales & Graines","tag":"","origine":"Louga (Kébémer)","dispo":True,"vedette":False},
    {"image":"gombo.jpg","nom":"Gombos frais","prix":2200,"conditionnement":"Panier de 3Kg","cat":"Fruits & Légumes","tag":"","origine":"Faye (Saint-Louis)","dispo":True,"vedette":False},
    {"image":"bissap.jpg","nom":"Bissap Rouge (Fleurs)","prix":3000,"conditionnement":"Sachet de 2Kg","cat":"Céréales & Graines","tag":"🌺 Qualité Supérieure","origine":"Kaolack","dispo":True,"vedette":False},
    {"image":"sesame.jpg","nom":"Graines de sésame","prix":7500,"conditionnement":"Sac de 10Kg","cat":"Céréales & Graines","tag":"","origine":"Sédhiou","dispo":True,"vedette":False},
]

if "admin_connecte" not in st.session_state:
    st.session_state.admin_connecte = False
if "admin_page" not in st.session_state:
    st.session_state.admin_page = None
if "produits_admin" not in st.session_state:
    st.session_state.produits_admin = DEFAULT_PRODUCTS.copy()

def image_source(produit):
    """Retourne la source image d'un produit : upload en mémoire ou fichier existant."""
    if produit.get("photo_bytes"):
        return produit["photo_bytes"]
    return produit.get("image", "")

with st.sidebar:
    st.markdown("## ⚙️ Paramètres")
    st.caption("Espace réservé à l'administration du catalogue et des commandes.")

    if not st.session_state.admin_connecte:
        with st.form("admin_login_form"):
            login_admin = st.text_input("Identifiant", placeholder="Identifiant administrateur")
            mdp_admin = st.text_input("Mot de passe", type="password", placeholder="Mot de passe")
            connexion = st.form_submit_button("🔐 Se connecter", use_container_width=True)
            if connexion:
                if login_admin == ADMIN_LOGIN and mdp_admin == ADMIN_PASSWORD:
                    st.session_state.admin_connecte = True
                    st.session_state.admin_page = "Produits"
                    st.rerun()
                else:
                    st.error("Identifiant ou mot de passe incorrect.")
    else:
        st.success("🟢 Administrateur connecté")
        st.caption("Vous pouvez modifier le catalogue sans rendre ces commandes visibles aux clients.")

        admin_page = st.radio(
            "Gestion",
            ["Produits", "Commandes"],
            index=0 if st.session_state.admin_page != "Commandes" else 1,
            key="admin_navigation"
        )
        st.session_state.admin_page = admin_page

        if st.button("🚪 Déconnexion", use_container_width=True):
            st.session_state.admin_connecte = False
            st.session_state.admin_page = None
            st.rerun()

    st.divider()
    st.markdown("### 🛒 Comment commander ?")
    st.markdown("""
    **1. Produits** → choisissez un article disponible.  
    **2. Quantité** → indiquez le nombre souhaité.  
    **3. Panier** → vérifiez les articles et le total.  
    **4. Livraison** → choisissez votre région et votre zone.  
    **5. Coordonnées** → renseignez nom, téléphone et adresse.  
    **6. Paiement** → choisissez le mode de règlement.  
    **7. Confirmation** → envoyez la commande par WhatsApp ou e-mail.
    """)

# =====================================================
# PANNEAU ADMINISTRATEUR
# =====================================================
if st.session_state.admin_connecte and st.session_state.admin_page == "Produits":
    st.markdown("# ⚙️ Administration du catalogue")
    st.info("Ici, vous pouvez **mettre un produit en vedette, modifier son prix, activer/désactiver sa disponibilité, modifier ses informations, supprimer un produit et ajouter de nouveaux produits avec photo**.")

    produits = st.session_state.produits_admin

    tab1, tab2 = st.tabs(["🧾 Gérer les produits", "➕ Ajouter un produit"])

    with tab1:
        if not produits:
            st.warning("Aucun produit dans le catalogue.")
        else:
            for idx, prod in enumerate(produits):
                with st.container(border=True):
                    cimg, cmain, cact = st.columns([1, 4, 1])
                    with cimg:
                        src = image_source(prod)
                        if src:
                            try:
                                st.image(src, width=100)
                            except Exception:
                                st.write("📦")
                        else:
                            st.write("📦")
                    with cmain:
                        st.markdown(f"### {prod['nom']}")
                        a,b,c,d = st.columns(4)
                        with a:
                            prod["prix"] = st.number_input(
                                "Prix (FCFA)", min_value=0, value=int(prod.get("prix",0)),
                                step=100, key=f"adm_prix_{idx}"
                            )
                        with b:
                            prod["dispo"] = st.toggle(
                                "Disponible", value=bool(prod.get("dispo",True)),
                                key=f"adm_dispo_{idx}"
                            )
                        with c:
                            prod["vedette"] = st.toggle(
                                "⭐ Vedette", value=bool(prod.get("vedette",False)),
                                key=f"adm_vedette_{idx}"
                            )
                        with d:
                            prod["tag"] = st.text_input(
                                "Badge", value=prod.get("tag",""),
                                key=f"adm_tag_{idx}"
                            )
                        d1,d2,d3 = st.columns(3)
                        with d1:
                            prod["nom"] = st.text_input("Nom du produit", value=prod["nom"], key=f"adm_nom_{idx}")
                        with d2:
                            prod["conditionnement"] = st.text_input("Conditionnement", value=prod["conditionnement"], key=f"adm_cond_{idx}")
                        with d3:
                            prod["origine"] = st.text_input("Origine", value=prod["origine"], key=f"adm_orig_{idx}")
                    with cact:
                        st.write("")
                        if st.button("🗑️ Retirer", key=f"adm_delete_{idx}", use_container_width=True):
                            st.session_state.produits_admin.pop(idx)
                            st.rerun()

    with tab2:
        with st.form("ajout_produit_admin", clear_on_submit=True):
            st.markdown("### ➕ Nouveau produit")
            n1,n2 = st.columns(2)
            with n1:
                nouveau_nom = st.text_input("Nom du produit *")
                nouveau_prix = st.number_input("Prix en FCFA *", min_value=0, value=1000, step=100)
                nouveau_cond = st.text_input("Conditionnement", value="Unité")
                nouvelle_cat = st.selectbox("Catégorie", ["Fruits & Légumes", "Céréales & Graines", "Irrigation & Équipements", "Autres"])
            with n2:
                nouvelle_origine = st.text_input("Origine", value="Sénégal")
                nouveau_tag = st.text_input("Badge / étiquette", placeholder="⭐ Nouveau, 🔥 Promo...")
                nouvelle_dispo = st.checkbox("Produit disponible", value=True)
                nouvelle_vedette = st.checkbox("⭐ Mettre en vedette", value=False)
                nouvelle_photo = st.file_uploader("📷 Photo du produit", type=["png","jpg","jpeg","webp"])

            ajouter = st.form_submit_button("➕ Ajouter au catalogue", use_container_width=True, type="primary")
            if ajouter:
                if not nouveau_nom.strip():
                    st.error("Le nom du produit est obligatoire.")
                else:
                    nouveau = {
                        "image": "",
                        "nom": nouveau_nom.strip(),
                        "prix": int(nouveau_prix),
                        "conditionnement": nouveau_cond.strip() or "Unité",
                        "cat": nouvelle_cat,
                        "tag": nouveau_tag.strip(),
                        "origine": nouvelle_origine.strip() or "Sénégal",
                        "dispo": nouvelle_dispo,
                        "vedette": nouvelle_vedette,
                    }
                    if nouvelle_photo is not None:
                        nouveau["photo_bytes"] = nouvelle_photo.getvalue()
                    st.session_state.produits_admin.append(nouveau)
                    st.success(f"✅ {nouveau['nom']} a été ajouté au catalogue.")
                    st.rerun()

    st.warning("ℹ️ Les modifications de cet espace sont conservées dans la session Streamlit actuelle. Pour une conservation permanente après redémarrage/déploiement, il faudra relier le catalogue à une base de données (par exemple Supabase).")
    st.stop()

if st.session_state.admin_connecte and st.session_state.admin_page == "Commandes":
    st.markdown("# 📋 Administration des commandes")
    st.info("Cette page permet de consulter les commandes créées pendant la session et de retrouver rapidement les informations utiles au traitement.")

    historique = st.session_state.historique
    if not historique:
        st.warning("Aucune commande enregistrée dans cette session.")
    else:
        st.metric("Commandes enregistrées", len(historique))
        for idx, cmd in enumerate(reversed(historique), start=1):
            with st.expander(f"📦 Commande #{idx} — {cmd.get('client','Client')} — {cmd.get('total','')}", expanded=False):
                st.write(f"**Mode de paiement :** {cmd.get('paiement','')}")
                st.code(cmd.get("brut_texte",""), language=None)
    st.stop()

# =====================================================
# SELECTION DU MENU VIA ST.RADIO
# =====================================================

options_menu = [
    "🏠 Accueil", 
    "🛒 Produits", 
    "📦 Commande", 
    "📊 Réalisations", 
    "📞 Contact"
]

selected_raw = st.radio(
    "Navigation Menu",
    options=options_menu,
    horizontal=True
)

# Extraction propre de la section sélectionnée
selected = selected_raw.split(" ")[1]

# =====================================================
# =====================================================
# ACCUEIL (VERSION STARTUP ÉMERGENTE - CONCRÈTE & DE CONFIANCE)
# =====================================================
if selected == "Accueil":

    # HERO SECTION - Identité forte, ancrage local et accessibilité numérique
    st.markdown("""
    <div class="hero" style="text-align: center; padding: 45px 25px; background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%); color: white; border-radius: 16px; margin-bottom: 30px; box-shadow: 0 10px 15px -3px rgba(27, 94, 32, 0.2);">
        <span style="background: rgba(255, 255, 255, 0.2); padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">🇸🇳 Agritech & Chaîne d'Approvisionnement</span>
        <h1 style="margin: 10px 0 5px 0; font-size: 2.8rem; font-weight: 800; letter-spacing: -0.5px;">YouAgronoMe</h1>
        <h2 style="margin: 0 0 20px 0; font-size: 1.3rem; font-weight: 300; opacity: 0.95; font-style: italic;">La technologie et l'accès au marché au service des producteurs sénégalais</h2>
        <p style="max-width: 750px; margin: 0 auto 25px auto; font-size: 1.05rem; line-height: 1.6; opacity: 0.9;">
            YouAgronoMe est une jeune infrastructure logistique et technologique basée à <b>Saint-Louis, Sénégal</b>. 
            Nous facilitons l'accès aux équipements d'irrigation de précision et connectons directement les récoltes locales aux circuits de distribution urbains, en parfait alignement avec les priorités de souveraineté alimentaire.
        </p>
        <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
            <span style="background: white; color: #1b5e20; padding: 8px 16px; border-radius: 8px; font-size: 0.9rem; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">📍 Hub National : Saint-Louis</span>
            <span style="background: rgba(255,255,255,0.15); color: white; padding: 8px 16px; border-radius: 8px; font-size: 0.9rem; font-weight: 500; border: 1px solid rgba(255,255,255,0.2);">🕒 Commandes en ligne 24h/7d</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # RECONNAISSANCE ET ENGAGEMENT DE CONFIANCE
    st.markdown("<div class='section-title' style='font-size: 1.4rem; color: #1b5e20; font-weight: 700; margin-bottom: 15px;'>🎯 Nos Engagements Opérationnels</div>", unsafe_allow_html=True)
    
    stat_cols = st.columns(4)
    
    with stat_cols[0]:
        st.markdown("""
        <div class="stat-card" style="background-color: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #1b5e20; padding: 18px; border-radius: 12px; text-align: center; height: 100%;">
            <div style="font-size: 1.8rem; font-weight: bold; color: #1b5e20;">100%</div>
            <div style="font-size: 0.85rem; color: #4a5568; margin-top: 5px; font-weight: 600;">Sourcing Local</div>
            <p style="font-size: 0.75rem; color: #718096; margin: 5px 0 0 0;">Intrants et semences adaptés à la typologie de nos sols.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with stat_cols[1]:
        st.markdown("""
        <div class="stat-card" style="background-color: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #0d47a1; padding: 18px; border-radius: 12px; text-align: center; height: 100%;">
            <div style="font-size: 1.8rem; font-weight: bold; color: #0d47a1;">-30%</div>
            <div style="font-size: 0.85rem; color: #4a5568; margin-top: 5px; font-weight: 600;">Consommation d'Eau</div>
            <p style="font-size: 0.75rem; color: #718096; margin: 5px 0 0 0;">Préservation de la ressource via nos kits d'irrigation économes.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with stat_cols[2]:
        st.markdown("""
        <div class="stat-card" style="background-color: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #e65100; padding: 18px; border-radius: 12px; text-align: center; height: 100%;">
            <div style="font-size: 1.8rem; font-weight: bold; color: #e65100;">PRAS</div>
            <div style="font-size: 0.85rem; color: #4a5568; margin-top: 5px; font-weight: 600;">Alignement National</div>
            <p style="font-size: 0.75rem; color: #718096; margin: 5px 0 0 0;">Partenaire direct de l'autonomie alimentaire du pays.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with stat_cols[3]:
        st.markdown("""
        <div class="stat-card" style="background-color: #ffffff; border: 1px solid #e2e8f0; border-top: 4px solid #2e7d32; padding: 18px; border-radius: 12px; text-align: center; height: 100%;">
            <div style="font-size: 1.8rem; font-weight: bold; color: #2e7d32;">0 Perte</div>
            <div style="font-size: 0.85rem; color: #4a5568; margin-top: 5px; font-weight: 600;">Distribution Directe</div>
            <p style="font-size: 0.75rem; color: #718096; margin: 5px 0 0 0;">Zéro intermédiaire entre la récolte et les marchés urbains.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # SOLUTIONS DE TERRAIN & DE CONFIANCE (SANS IA)
    st.markdown("<div class='section-title' style='font-size: 1.4rem; color: #1b5e20; font-weight: 700; margin-top: 15px;'>🚀 Nos Services & Catalogue de Terrain</div>", unsafe_allow_html=True)

    services = [
        ("💧 Kits de Micro-Irrigation Clé-en-main", "Systèmes de goutte-à-goutte basse pression optimisés pour le maraîchage. Installation rapide par nos techniciens sur toute l'étendue de la vallée.", "card-eau"),
        ("🧪 Diagnostic Physique des Sols", "Prélèvements et analyses directes d'humidité et d'azote/phosphore sur vos parcelles pour cibler exactement l'engrais requis.", "card-sol"),
        ("🛒 Plateforme Appro-Directe", "Notre catalogue numérique transparent connectant les producteurs de légumes et de riz du Fleuve aux grandes tables de consommation.", "card-plante"),
        ("📱 Service Alertes InfoClimatiques", "Envoi périodique par SMS des fenêtres de semis optimales et alertes de ravageurs locales, sans besoin d'accès Internet permanent.", "card-innovation"),
        ("🎓 Formations & Encadrement GIE", "Renforcement des capacités des coopératives agricoles et des groupements féminins sur les pratiques agroécologiques.", "card-plante"),
        ("📊 Rapports de Rendement & Data", "Mise à disposition de rapports de productivité locale pour éclairer la planification des communes et des agences de développement.", "card-sol")
    ]

    cols = st.columns(3)
    for i, (titre, texte, theme_class) in enumerate(services):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="glass-base {theme_class}" style="background-color: #ffffff; border: 1px solid #edf2f7; padding: 20px; border-radius: 12px; height: 100%; min-height: 200px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <h4 style="color: #1b5e20; font-size: 1.1rem; margin-top: 0; font-weight: 700;">{titre}</h4>
                    <p style="color: #4a5568; font-size: 0.88rem; line-height: 1.5; margin-bottom: 10px;">{texte}</p>
                </div>
                <span style="font-size: 0.75rem; color: #718096; font-weight: bold; text-transform: uppercase;">✔ Service Opérationnel</span>
            </div>
            """, unsafe_allow_html=True)

    st.write("")

    # POSITIONNEMENT STRATÉGIQUE & SÛRETÉ DES OPÉRATIONS
    st.markdown("<div class='section-title' style='font-size: 1.4rem; color: #1b5e20; font-weight: 700; margin-top: 15px;'>🛡️ Charte de Confiance & Cadre Juridique</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="glass-base" style="background-color: #ffffff; border: 1px solid #e2e8f0; padding: 22px; border-radius: 12px; border-left: 5px solid #2e7d32; height: 100%;">
            <h4 style="color: #2e7d32; font-size: 1.15rem; margin-top:0; font-weight: 700;">🤝 Proximité et Fiabilité Contractuelle</h4>
            <p style="color: #4a5568; font-size: 0.9rem; line-height: 1.6; margin-bottom: 15px;">
                Chaque commande passée sur notre site fait l'objet d'un suivi par SMS et d'un bon de commande formel imprimable. 
                Nous travaillons main dans la main avec les transporteurs agréés interurbains pour sécuriser la chaîne du froid et du sec.
            </p>
            <span style="font-size: 0.8rem; background-color: #f7fafc; padding: 4px 8px; border-radius: 4px; color: #4a5568; font-weight: bold;">🔒 Transactions Claires & Paiement Mobile Sécurisé (Wave / OM)</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color: #f1f8e9; border: 1px solid #c8e6c9; padding: 22px; border-radius: 12px; height: 100%;">
            <h4 style="color: #1b5e20; font-size: 1.15rem; margin-top:0; font-weight: 700;">🏢 Traçabilité Légale & Administrative</h4>
            <p style="color: #2e7d32; font-size: 0.9rem; line-height: 1.6; margin-bottom: 15px; font-weight: 500;">
                YouAgronoMe est une initiative enregistrée, garantissant à nos partenaires (ONG, Communes, GIE locaux) une facturation en bonne et due forme et des contrats d'approvisionnement encadrés par le droit sénégalais.
            </p>
            <div style="font-size: 0.8rem; color: #1b5e20; font-weight: bold; background: rgba(255,255,255,0.6); padding: 8px; border-radius: 6px;">
                📌 Siège d'opérations : Quartier Sor, Saint-Louis, Sénégal<br>
                📞 Ligne Directe : +221 77 747 31 70 | ✉️ Contact : issayoume2012@gmail.com
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("") 
    
    # Message rassurant de pied de page
    st.info("🇸🇳 **YouAgronoMe** : Une entreprise de technologie agropastorale de confiance, conçue pour durer et sécuriser la chaîne d'approvisionnement de nos terroirs.")
# =====================================================
# =====================================================
# PRODUITS — CATALOGUE DYNAMIQUE
# =====================================================
elif selected == "Produits":

    produits = st.session_state.produits_admin

    st.markdown("<h1 style='text-align: center; color: #1B5E20; font-weight: 800;'>🌾 Notre Marché Agricole en Direct</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; color: #4a5568; max-width: 800px; margin: 0 auto 20px auto;'>
        Choisissez un produit, consultez son prix et sa disponibilité, puis ajoutez-le au panier.
        Les produits marqués <b>⭐ Vedette</b> sont mis en avant par l'administration.
    </p>
    """, unsafe_allow_html=True)

    vedettes = [p for p in produits if p.get("vedette") and p.get("dispo")]
    if vedettes:
        st.markdown("### ⭐ Produits en vedette")
        cols_v = st.columns(min(4, len(vedettes)))
        for i, p in enumerate(vedettes[:4]):
            with cols_v[i % len(cols_v)]:
                with st.container(border=True):
                    src = image_source(p)
                    if src:
                        try: st.image(src, use_container_width=True)
                        except Exception: st.write("📦")
                    else:
                        st.markdown("<div style='text-align:center;font-size:45px;'>📦</div>", unsafe_allow_html=True)
                    st.markdown(f"**{p['nom']}**")
                    st.markdown(f"### {p['prix']:,} FCFA")
                    st.caption(p["conditionnement"])

    col_search, col_cat = st.columns([2, 1])
    with col_search:
        recherche = st.text_input("🔍 Rechercher un produit", "")
    with col_cat:
        categories = ["Toutes"] + sorted(set(p.get("cat","Autres") for p in produits))
        categorie_choisie = st.selectbox("📁 Filtrer par catégorie", categories)

    produits_filtres = [
        p for p in produits
        if recherche.lower() in p.get("nom","").lower()
        and (categorie_choisie == "Toutes" or p.get("cat") == categorie_choisie)
    ]

    st.markdown("### 🛍️ Catalogue")
    if not produits_filtres:
        st.warning("🔍 Aucun produit ne correspond à votre recherche.")
    else:
        cols = st.columns(4)
        for i, p in enumerate(produits_filtres):
            with cols[i % 4]:
                with st.container(border=True):
                    if p.get("vedette"):
                        st.markdown("<span style='background:#fff3cd;color:#856404;padding:4px 8px;border-radius:10px;font-size:11px;font-weight:bold;'>⭐ VEDETTE</span>", unsafe_allow_html=True)

                    src = image_source(p)
                    if src:
                        try: st.image(src, use_container_width=True)
                        except Exception: st.markdown("<div style='font-size:45px;text-align:center;'>📦</div>", unsafe_allow_html=True)
                    else:
                        st.markdown("<div style='font-size:45px;text-align:center;'>📦</div>", unsafe_allow_html=True)

                    st.markdown(f"### {p['nom']}")
                    if p.get("tag"):
                        st.caption(p["tag"])
                    st.write(f"📍 **Origine :** {p.get('origine','Sénégal')}")
                    st.write(f"📦 **Format :** {p.get('conditionnement','Unité')}")
                    st.markdown(f"### {p.get('prix',0):,} FCFA")

                    if p.get("dispo"):
                        st.success("🟢 Disponible")
                        qte = st.number_input(
                            "Quantité",
                            min_value=1, max_value=100, value=1,
                            key=f"qte_dyn_{i}_{p['nom']}"
                        )
                        if st.button("🛒 Ajouter au panier", key=f"add_dyn_{i}_{p['nom']}", use_container_width=True, type="primary"):
                            found = False
                            for item in st.session_state.panier:
                                if item["produit"] == p["nom"]:
                                    item["quantite"] += qte
                                    item["prix_unitaire"] = int(p["prix"])
                                    item["prix"] = f"{p['prix']} FCFA par {p['conditionnement']}"
                                    found = True
                                    break
                            if not found:
                                st.session_state.panier.append({
                                    "produit": p["nom"],
                                    "prix": f"{p['prix']} FCFA par {p['conditionnement']}",
                                    "prix_unitaire": int(p["prix"]),
                                    "quantite": qte
                                })
                            st.toast(f"✅ {qte} × {p['nom']} ajouté au panier", icon="🛒")
                    else:
                        st.error("🔴 Indisponible")
                        st.button("Indisponible", key=f"disabled_{i}_{p['nom']}", disabled=True, use_container_width=True)

# =====================================================
# COMMANDE — PARCOURS SIMPLIFIÉ
# =====================================================
elif selected == "Commande":

    st.markdown("<h1 style='text-align: center; color: #1B5E20; font-weight: 800;'>📦 Passer une commande</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#f0fdf4;border:1px solid #bbf7d0;padding:18px;border-radius:14px;margin-bottom:20px;">
    <b>Comment ça marche ?</b><br>
    ① Choisissez vos produits → ② vérifiez votre panier → ③ indiquez le lieu de livraison →
    ④ renseignez vos coordonnées → ⑤ choisissez le paiement → ⑥ confirmez.
    </div>
    """, unsafe_allow_html=True)

    NUMERO_WHATSAPP = "221777473170"
    EMAIL_DEST = "issayoume2012@gmail.com"
    panier = st.session_state.panier

    if not panier:
        st.warning("🛒 Votre panier est vide. Allez dans **Produits** pour ajouter un article.")
        st.stop()

    st.markdown("## 1️⃣ Vérifier votre panier")
    total_articles = 0
    total_financier = 0

    for i, item in enumerate(list(panier)):
        prix_unitaire = int(item.get("prix_unitaire", 0))
        if prix_unitaire == 0:
            try:
                prix_unitaire = int(''.join(filter(str.isdigit, item["prix"].split("FCFA")[0])))
            except:
                prix_unitaire = 0

        c1,c2,c3,c4 = st.columns([4,2,2,1])
        with c1:
            st.markdown(f"**🛒 {item['produit']}**")
            st.caption(item["prix"])
        with c2:
            nouvelle_qte = st.number_input("Quantité", min_value=1, max_value=100, value=int(item["quantite"]), key=f"cmd_qte_{i}")
            item["quantite"] = nouvelle_qte
        sous_total = prix_unitaire * nouvelle_qte
        total_financier += sous_total
        total_articles += nouvelle_qte
        with c3:
            st.markdown(f"**{sous_total:,} FCFA**")
        with c4:
            if st.button("🗑️", key=f"cmd_sup_{i}"):
                st.session_state.panier.pop(i)
                st.rerun()

    st.divider()
    st.markdown("## 2️⃣ Livraison")
    st.caption("La région et la zone servent à calculer automatiquement les frais et à donner une estimation du délai.")

    @st.cache_data
    def get_geo_senegal_detail():
        return {
            "Dakar": ["Dakar Plateau","Médina","Fann / Point E / Amitié","Mermoz / Sacré-Cœur","Ouakam","Ngor","Almadies","Yoff","Grand Yoff","Parcelles Assainies","Guédiawaye","Pikine","Thiaroye","Keur Massar","Rufisque","Diamniadio"],
            "Saint-Louis": ["SND (Saint-Louis île)","Sor","Ndiolofène","Balacos","Guet Ndar","Goxu Mbacc","Bango","Hydrobase","Rao","Richard-Toll","Dagana","Podor","Ndioum","Ross Béthio"],
            "Thiès": ["Thiès Ville (Mbourène / Grand Thiès)","Dixième","Saly Portudal","Mbour Ville","Somone","Ngaparou","Joal-Fadiouth","Tivaouane","Mboro","Pout","Khombole","Popenguine"],
            "Diourbel": ["Diourbel Ville","Touba Mosquée","Mbacké","Bambey"],
            "Louga": ["Louga Ville","Linguère","Dahra","Kébémer"],
            "Fatick": ["Fatick Ville","Foundiougne","Gossas","Sokone","Diofior"],
            "Kaolack": ["Kaolack Ville","Nioro du Rip","Guinguinéo","Kahone"],
            "Kaffrine": ["Kaffrine Ville","Koungheul","Birkelane","Malem Hodar"],
            "Tambacounda": ["Tambacounda Ville","Bakel","Goudiry","Koumpentoum"],
            "Kolda": ["Kolda Ville","Vélingara","Médina Yoro Foulah"],
            "Ziguinchor": ["Ziguinchor Ville","Bignona","Oussouye","Cap Skirring"],
            "Sédhiou": ["Sédhiou Ville","Goudomp","Bounkiling"],
            "Matam": ["Matam Ville","Ourossogui","Kanel","Ranérou"],
            "Kédougou": ["Kédougou Ville","Saraya","Salémata"]
        }

    geo_senegal = get_geo_senegal_detail()
    col_reg, col_com = st.columns(2)
    with col_reg:
        region_selectionnee = st.selectbox("📍 Région du Sénégal *", list(geo_senegal.keys()))
    with col_com:
        commune_selectionnee = st.selectbox("🏙️ Quartier / Commune / Zone *", geo_senegal[region_selectionnee])

    if region_selectionnee == "Saint-Louis":
        frais_livraison = 1500 if commune_selectionnee in ["SND (Saint-Louis île)","Sor","Ndiolofène","Balacos","Guet Ndar","Goxu Mbacc","Bango","Hydrobase"] else 3000
        delai_estime = "dans la journée" if frais_livraison == 1500 else "24h à 48h"
    elif region_selectionnee == "Dakar":
        frais_livraison, delai_estime = 2500, "sous 24h"
    elif region_selectionnee == "Thiès":
        frais_livraison, delai_estime = 3500, "24h à 48h"
    elif region_selectionnee in ["Diourbel","Fatick","Kaolack","Louga"]:
        frais_livraison, delai_estime = 4500, "48h à 72h"
    else:
        frais_livraison, delai_estime = 5500, "72h à 96h"

    st.info(f"🚚 Frais de livraison estimés : **{frais_livraison:,} FCFA** — Délai indicatif : **{delai_estime}**.")

    st.markdown("## 3️⃣ Coordonnées du destinataire")
    col1,col2 = st.columns(2)
    with col1:
        nom = st.text_input("Nom complet *", placeholder="Ex. Issa Youme")
        telephone = st.text_input("Téléphone / WhatsApp *", placeholder="Ex. 77 000 00 00")
        adresse = st.text_input("Adresse précise *", placeholder="Maison, rue, point de repère...")
    with col2:
        paiement = st.selectbox("💳 Mode de paiement", ["Présentiel (À la livraison)","Wave","Orange Money"])
        date_min = datetime.now() + timedelta(days=1 if region_selectionnee in ["Saint-Louis","Dakar"] else 2)
        date_livraison = st.date_input("📅 Date souhaitée", value=date_min, min_value=datetime.now().date())
        creneau_horaire = st.selectbox("🕐 Créneau", ["Matin (08h00 - 12h00)","Après-midi (13h00 - 17h00)","Fin de journée (17h00 - 20h00)"])

    commentaire = st.text_area("📝 Instruction pour le livreur (facultatif)", placeholder="Ex. Appeler 10 minutes avant d'arriver.")

    code_promo = st.text_input("🎟️ Code promo (facultatif)").strip()
    remise = int(total_financier * 0.10) if code_promo.upper() == "YOU2026" else 0
    if code_promo.upper() == "YOU2026":
        st.success("🎉 Code valide : 10 % de remise.")

    total_final_net = total_financier + frais_livraison - remise
    st.markdown("## 4️⃣ Récapitulatif")
    r1,r2,r3 = st.columns(3)
    r1.metric("Articles", total_articles)
    r2.metric("Sous-total", f"{total_financier:,} FCFA")
    r3.metric("Total à payer", f"{total_final_net:,} FCFA")
    st.caption(f"Livraison : {frais_livraison:,} FCFA · Remise : {remise:,} FCFA")

    st.markdown("## 5️⃣ Confirmer")
    if paiement in ["Wave","Orange Money"]:
        st.info("💳 Après confirmation, effectuez le transfert au **+221 77 747 31 70**.")

    if st.button("🚀 Confirmer et envoyer la commande", use_container_width=True, type="primary"):
        if not nom or not telephone or not adresse:
            st.error("⚠️ Remplissez les champs obligatoires : nom, téléphone et adresse.")
        else:
            texte_produits = "\n".join(
                f"• {p['produit']} x {p['quantite']} — {p.get('prix','')}" for p in panier
            )
            message = f"""🌾 COMMANDE YOUAGRONOME SÉNÉGAL

👤 DESTINATAIRE
Nom : {nom}
Téléphone : {telephone}
Région : {region_selectionnee}
Zone : {commune_selectionnee}
Adresse : {adresse}

📅 LIVRAISON
Date : {date_livraison.strftime('%d/%m/%Y')}
Créneau : {creneau_horaire}

📦 PANIER
{texte_produits}

💰 SOUS-TOTAL : {total_financier:,} FCFA
🚚 LIVRAISON : {frais_livraison:,} FCFA
📉 REMISE : {remise:,} FCFA
💵 TOTAL : {total_final_net:,} FCFA
💳 PAIEMENT : {paiement}
📝 INSTRUCTIONS : {commentaire or 'Aucune'}"""

            html_facture = f"""
            <div style="font-family:Arial;padding:25px;border:1px solid #c8e6c9;border-radius:12px;">
            <h2 style="color:#1B5E20;text-align:center;">YOUAGRONOME SÉNÉGAL</h2>
            <p><b>Client :</b> {nom}<br><b>Téléphone :</b> {telephone}<br>
            <b>Zone :</b> {region_selectionnee} — {commune_selectionnee}<br>
            <b>Adresse :</b> {adresse}<br><b>Date :</b> {date_livraison.strftime('%d/%m/%Y')} — {creneau_horaire}</p>
            <hr><p>{texte_produits.replace(chr(10), '<br>')}</p><hr>
            <p><b>Sous-total :</b> {total_financier:,} FCFA<br>
            <b>Livraison :</b> {frais_livraison:,} FCFA<br>
            <b>Remise :</b> -{remise:,} FCFA<br>
            <b>Total :</b> {total_final_net:,} FCFA</p>
            </div>"""

            whatsapp_link = "https://wa.me/" + NUMERO_WHATSAPP + "?text=" + urllib.parse.quote(message)
            email_link = f"mailto:{EMAIL_DEST}?subject=Commande YouAgronoMe - {nom}&body=" + urllib.parse.quote(message)

            st.session_state.historique.append({
                "client": nom,
                "telephone": telephone,
                "region": region_selectionnee,
                "zone": commune_selectionnee,
                "paiement": paiement,
                "total": f"{total_final_net:,} FCFA",
                "commande": panier.copy(),
                "brut_texte": message,
                "html_facture": html_facture
            })

            st.success("🎉 Commande préparée avec succès. Choisissez maintenant le canal d'envoi.")
            a,b = st.columns(2)
            with a:
                st.link_button("📱 Envoyer sur WhatsApp", whatsapp_link, use_container_width=True)
            with b:
                st.link_button("📧 Envoyer par e-mail", email_link, use_container_width=True)

    if st.button("🧹 Vider le panier", use_container_width=True):
        st.session_state.panier = []
        st.rerun()

    st.markdown("### 💡 Besoin d'aide ?")
    with st.expander("Comment savoir si ma commande est bien passée ?"):
        st.write("Après avoir cliqué sur « Confirmer et envoyer la commande », un message prérempli est créé. Envoyez-le par WhatsApp ou e-mail. La commande est alors transmise avec les coordonnées, les produits, les quantités et le montant.")
    with st.expander("Puis-je modifier ma commande ?"):
        st.write("Oui. Modifiez les quantités ou supprimez un article dans la section Panier avant de confirmer.")
    with st.expander("Quand vais-je être livré ?"):
        st.write("Le délai affiché est une estimation selon la zone sélectionnée. L'équipe confirme ensuite les modalités de livraison.")
    with st.expander("Comment payer ?"):
        st.write("Vous pouvez choisir le paiement à la livraison, Wave ou Orange Money. Pour un paiement mobile, le numéro indiqué après confirmation est +221 77 747 31 70.")

# =====================================================
elif selected == "Réalisations":
    import urllib.parse

    # Style CSS épuré, professionnel et moderne
    st.markdown("""
    <style>
    .concept-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02);
        margin-bottom: 20px;
        transition: transform 0.2s ease;
    }
    .concept-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.04);
    }
    .concept-title {
        color: #1b5e20;
        font-weight: 700;
        font-size: 1.25rem;
        margin-bottom: 8px;
    }
    .gov-badge {
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 12px;
        border: 1px solid #c8e6c9;
    }
    .study-box {
        background-color: #f7fafc;
        border-left: 5px solid #2b6cb0;
        padding: 25px;
        border-radius: 4px 16px 16px 4px;
        font-size: 0.95rem;
        margin-top: 15px;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
    }
    .metric-title {
        font-size: 0.85rem;
        color: #4a5568;
        text-transform: uppercase;
        font-weight: bold;
    }
    .metric-value {
        font-size: 1.5rem;
        color: #2b6cb0;
        font-weight: 800;
    }
    </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # 1. EN-TÊTE ET POSITIONNEMENT
    # =====================================================
    st.title("🏛️ Hub d'Innovation & Études de Conception")
    st.markdown(
        "**YouAgronoMe** n'est pas un simple fournisseur, c'est un **bureau d'études et d'exécution technologique** "
        "dédié à la souveraineté alimentaire du Sénégal. Nous concevons des architectures d'irrigation intelligente, "
        "de suivi parcellaire par capteurs et de logistique intégrée adaptées aux réalités de nos terroirs."
    )
    st.write("---")

    # Organisation de la section en deux onglets : Projets phares et Bureau d'études interactif
    tab1, tab2 = st.tabs(["📋 Références & Projets Phares", "⚙️ Bureau d'Études & Conception Interactive"])

    # =====================================================
    # ONGLET 1 : RÉFÉRENCES ET PROJETS
    # =====================================================
    with tab1:
        st.subheader("💡 Nos Projets d'Intégration Territoriale")
        st.markdown("Découvrez le déploiement opérationnel de nos solutions face aux défis structurels du pays :")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="concept-card">
                <span class="gov-badge">🇸🇳 VALLÉE DU FLEUVE (SAED)</span>
                <div class="concept-title">Pilotage de la Filière Rizicole</div>
                <p style="font-size: 0.9rem; color: #4a5568; line-height: 1.5;">
                    Déploiement de sondes tensiométriques connectées dans les aménagements hydro-agricoles de Podor et Dagana. 
                    Optimisation des cycles d'irrigation pour faire face aux variations de débit du Fleuve Sénégal.
                </p>
                <hr style="margin: 10px 0; border: 0; border-top: 1px solid #eee;">
                <small style="color: #2e7d32; font-weight: bold;">🎯 Impact : Réduction de 30% des frais énergétiques de pompage</small>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="concept-card">
                <span class="gov-badge">🇸🇳 DOMAINES AGRICOLES (ANIDA)</span>
                <div class="concept-title">Modernisation des DAC</div>
                <p style="font-size: 0.9rem; color: #4a5568; line-height: 1.5;">
                    Installation de micro-stations météo et IoT dans les incubateurs agricoles de Keur Momar Sarr pour sécuriser 
                    les cultures de contre-saison des jeunes exploitants ruraux.
                </p>
                <hr style="margin: 10px 0; border: 0; border-top: 1px solid #eee;">
                <small style="color: #2e7d32; font-weight: bold;">🎯 Impact : +22% de rendement sur la pomme de terre et l'oignon</small>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="concept-card">
                <span class="gov-badge">🇸🇳 ZONE DES NIAYES</span>
                <div class="concept-title">Corridor Horticole de Précision</div>
                <p style="font-size: 0.9rem; color: #4a5568; line-height: 1.5;">
                    Planification des flux logistiques via notre plateforme de groupage depuis les Niayes (Thiès/Louga) 
                    vers Dakar pour stabiliser les prix du marché et réduire le gaspillage.
                </p>
                <hr style="margin: 10px 0; border: 0; border-top: 1px solid #eee;">
                <small style="color: #2e7d32; font-weight: bold;">🎯 Impact : Division par 2 des pertes post-récolte horticoles</small>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="concept-card">
                <span class="gov-badge">🇸🇳 BASSIN ARACHIDIER & DER/FJ</span>
                <div class="concept-title">Cartographie Prédictive des Sols</div>
                <p style="font-size: 0.9rem; color: #4a5568; line-height: 1.5;">
                    Analyse prédictive des sols sablonneux du bassin (Kaolack, Kaffrine) pour orienter la répartition des semences certifiées et des engrais subventionnés.
                </p>
                <hr style="margin: 10px 0; border: 0; border-top: 1px solid #eee;">
                <small style="color: #2e7d32; font-weight: bold;">🎯 Impact : Optimisation de la fertilisation azotée sur 1500 ha</small>
            </div>
            """, unsafe_allow_html=True)

    # =====================================================
    # ONGLET 2 : BUREAU D'ÉTUDES & DIAGNOSTIC INTERACTIF (QUESTIONS & CONCEPTION)
    # =====================================================
    with tab2:
        st.subheader("🛠️ Formulaire de Diagnostic & Conception de Projet")
        st.markdown(
            "Répondez aux questions ci-dessous concernant votre périmètre agricole ou votre programme régional. "
            "Notre moteur analytique va concevoir instantanément **une note d'étude préliminaire** personnalisée."
        )

        with st.form("diagnostic_form"):
            st.markdown("##### 📍 1. Localisation et Dimensionnement")
            col_z, col_s = st.columns(2)
            with col_z:
                bassin_geo = st.selectbox(
                    "Sélectionnez le bassin géographique :",
                    [
                        "Vallée du Fleuve Sénégal (Riz & Cultures irriguées)",
                        "Zone des Niayes (Maraîchage & Arboriculture intensive)",
                        "Bassin Arachidier (Grandes cultures pluviales & Maraîchage d'appoint)",
                        "Casamance (Mangues, Riziculture pluviale & Arboriculture)"
                    ]
                )
            with col_s:
                surface_projet = st.number_input("Superficie totale à aménager (en Hectares) :", min_value=1, max_value=10000, value=25, step=5)

            st.markdown("---")
            st.markdown("##### 💧 2. Ressources en Eau & Infrastructure")
            col_e, col_ir = st.columns(2)
            with col_e:
                source_energie = st.selectbox(
                    "Quelle est la source d'énergie principale pour l'exhaure de l'eau ?",
                    [
                        "Gasoil (Motopompes thermiques - coût élevé)",
                        "Solaire PV (Pompage solaire existant ou à concevoir)",
                        "Réseau SENELEC (Électricité réseau)",
                        "Pas d'infrastructure de pompage (Pluvial strict)"
                    ]
                )
            with col_ir:
                type_irrigation = st.selectbox(
                    "Quel est le système d'irrigation principal ?",
                    [
                        "Irrigation gravitaire (canaux à ciel ouvert)",
                        "Aspersion (canons ou asperseurs)",
                        "Goutte-à-goutte (micro-irrigation localisée)",
                        "Arrosage manuel / Système traditionnel"
                    ]
                )

            st.markdown("---")
            st.markdown("##### 🌾 3. Filières, Sols & Logistique")
            col_sol, col_perte = st.columns(2)
            with col_sol:
                type_sol = st.selectbox(
                    "Quel est le profil dominant de votre sol ?",
                    [
                        "Sol argileux / lourd (ex: Sols du Fleuve 'Faux-Holaldé')",
                        "Sol sableux / filtrant (ex: Sols des Niayes ou Dior)",
                        "Sol limoneux-sableux (Deck-Dior équilibré)"
                    ]
                )
            with col_perte:
                niveau_perte = st.select_slider(
                    "Quel est le niveau estimé de vos pertes post-récolte actuelles ?",
                    options=["Faible (<10%)", "Modéré (10% à 25%)", "Élevé (25% à 45% - Cas de la mangue/oignon)", "Critique (>45%)"],
                    value="Élevé (25% à 45% - Cas de la mangue/oignon)"
                )

            submit_diagnose = st.form_submit_button("🧪 Lancer la Modélisation & Générer l'Étude de Conception", use_container_width=True)

        if submit_diagnose:
            with st.spinner("Analyse des variables agro-climatiques et dimensionnement de l'architecture..."):
                
                # Modèle de calcul des besoins technologiques YouAgronoMe
                nb_capteurs_recom = max(3, int(surface_projet / 5)) # 1 capteur par 5ha, min 3
                
                # Économies d'eau estimées (m3/an)
                coef_economie = 0.35 if type_irrigation != "Goutte-à-goutte" else 0.15
                besoin_eau_standard = surface_projet * 7500 # m3 moyen/ha/an
                eau_economisee = int(besoin_eau_standard * coef_economie)
                
                # Économies financières sur l'énergie (FCFA/an)
                if "Gasoil" in source_energie:
                    gain_energie_annuel = int(surface_projet * 180000) # 180.000 FCFA d'économie par ha avec l'irrigation de précision
                    facteur_carbone = "Très élevé (Haute priorité de transition verte)"
                elif "Solaire" in source_energie:
                    gain_energie_annuel = int(surface_projet * 45000) # Moins de maintenance batterie/pompe
                    facteur_carbone = "Neutre (Excellente empreinte écologique)"
                else:
                    gain_energie_annuel = int(surface_projet * 95000)
                    facteur_carbone = "Modéré"

                # Estimation de la rentabilité logistique
                if "Niayes" in bassin_geo or "Casamance" in bassin_geo:
                    gain_logistique = "Optimisation du transport froid et groupage : réduction de 60% des invendus."
                    gain_financier_recolte = int(surface_projet * 400000) # Gain en valeur FCFA marchande récupérée
                else:
                    gain_logistique = "Planification des fenêtres de récolte pour le stockage et la commercialisation directe."
                    gain_financier_recolte = int(surface_projet * 250000)

                st.success("✨ Note de conception préliminaire générée avec succès !")

                # Section des indicateurs clés
                m1, m2, m3 = st.columns(3)
                with m1:
                    st.markdown(f'<div class="concept-card"><span class="metric-title">Capteurs IoT requis</span><br><span class="metric-value">{nb_capteurs_recom} Unités</span></div>', unsafe_allow_html=True)
                with m2:
                    st.markdown(f'<div class="concept-card"><span class="metric-title">Volume d\'Eau Préservé</span><br><span class="metric-value">{eau_economisee:,} m³/an</span></div>', unsafe_allow_html=True)
                with m3:
                    st.markdown(f'<div class="concept-card"><span class="metric-title">Économies Énergie</span><br><span class="metric-value">{gain_energie_annuel:,} FCFA/an</span></div>', unsafe_allow_html=True)

                # Rapport d'étude mis en forme
                etude_content = f"""📝 ÉTUDE DE CONCEPTION PRÉLIMINAIRE : ARCHITECTURE YOUAGRONOME
=====================================================================
BASSIN D'INTERVENTION : {bassin_geo}
DIMENSIONNEMENT       : {surface_projet} Hectares
PROFIL TECHNIQUE      : Énergie: {source_energie} | Irrigation: {type_irrigation}
=====================================================================

1. DIAGNOSTIC AGRO-TECHNIQUE & RECOMMANDATIONS
---------------------------------------------------------------------
* Type de Sol identifié : {type_sol}. 
  -> Recommandation : Ajuster les seuils d'alertes tensiométriques dans l'application mobile pour éviter l'asphyxie racinaire (sols lourds) ou le lessivage rapide (sols filtrants).
* Densité du réseau IoT : Déploiement de {nb_capteurs_recom} sondes connectées de profondeur double (30cm / 60cm) pour un suivi précis du front d'humectation.

2. TRANSITION ÉNERGÉTIQUE & RENTABILITÉ IRRIGATION
---------------------------------------------------------------------
* Bilan Carbone Actuel : {facteur_carbone}.
* Économie de carburant/électricité estimée : {gain_energie_annuel:,} FCFA par an grâce à l'arrêt automatique des pompes dès que la capacité de rétention du sol est atteinte.
* Réduction des pertes en eau douce : {eau_economisee:,} m3 préservés par an, prolongeant la disponibilité de la ressource en nappe.

3. STRATÉGIE LOGISTIQUE & VALORISATION DES RÉCOLTES
---------------------------------------------------------------------
* Diagnostic des Pertes : Actuellement évalué à "{niveau_perte}".
* Solution Logistique : {gain_logistique}
* Gain de chiffre d'affaires agricole estimé : +{gain_financier_recolte:,} FCFA / an sur le périmètre grâce à la valorisation des volumes sauvés de la pourriture.

4. CALENDRIER DE DÉPLOIEMENT ESTIMÉ (PILOTE DE 90 JOURS)
---------------------------------------------------------------------
* Semaines 1-2 : Cartographie GPS et prélèvements de sols pour calibrage.
* Semaine 3   : Installation physique de la passerelle de communication et des sondes.
* Semaines 4+ : Activation du tableau de bord d'irrigation et formation des exploitants.
"""

                st.markdown(f"<div class='study-box'><pre style='white-space: pre-wrap; font-family: monospace; font-size: 0.9rem; color: #2d3748;'>{etude_content}</pre></div>", unsafe_allow_html=True)

                # Formulaire d'envoi automatique pour l'étude
                sujet_mail = urllib.parse.quote(f"Demande d'Étude de Faisabilité YouAgronoMe : {surface_projet}ha - {bassin_geo.split('(')[0]}")
                corps_mail = urllib.parse.quote(
                    f"Bonjour l'équipe YouAgronoMe,\n\nNous venons de concevoir notre note d'étude préliminaire sur votre plateforme pour un projet de {surface_projet} hectares situé dans le bassin : {bassin_geo}.\n\nVoici nos spécifications de départ :\n- Énergie d'exhaure : {source_energie}\n- Type d'irrigation : {type_irrigation}\n- Type de sol : {type_sol}\n- Niveau de perte actuel : {niveau_perte}\n\nNous souhaitons planifier un rendez-vous ou une visite de terrain pour valider l'étude d'exécution technique.\n\nCordialement,\n[Indiquez votre Nom / Structure]"
                )

                st.write(" ")
                st.link_button(
                    "✉️ Soumettre cette étude de conception pour validation technique terrain", 
                    f"mailto:issayoume2012@gmail.com?subject={sujet_mail}&body={corps_mail}",
                    use_container_width=True
                )

    st.write("---")

    # =====================================================
    # 5. REJOINDRE NOTRE ÉCOSYSTÈME
    # =====================================================
    st.subheader("🤝 Une équipe mobile à votre service")
    st.markdown(
        "Nos techniciens et ingénieurs agronomes sillonnent le Sénégal pour calibrer nos équipements "
        "directement sur vos parcelles. Contactez-nous pour transformer cette étude virtuelle en réalité physique."
    )
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.info("📞 **Ligne Directe Bureau d'Études :** +221 77 747 31 70")
    with col_c2:
        st.info("✉️ **Courriel Officiel :** issayoume2012@gmail.com")
# CONTACT & ALLIANCE NATIONALE (VERSION STARTUP IA)
# =====================================================
# =====================================================
# CONTACT & ALLIANCE NATIONALE (VERSION STARTUP IA)
# =====================================================
elif selected == "Contact":

    # ================= 1. EN-TÊTE DE LA PAGE =================
    st.markdown("""
    <div style="text-align:center; margin-bottom: 25px;">
        <h1 style="color: #1b5e20;">🤝 Rejoignez l'Alliance YouAgronoMe</h1>
        <p style="font-size: 1.1rem; color: #555;">
            Une opportunité de co-développement ? Un projet pilote régional au Sénégal ? Échangeons dès aujourd'hui.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ================= 2. CARTES D'INFORMATION (SANS TRONCATURE) =================
    st.markdown("""
    <div style="display: flex; justify-content: space-between; gap: 15px; flex-wrap: wrap; margin-bottom: 25px;">
        <div style="flex: 1; min-width: 220px; background-color: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; text-align: center;">
            <span style="font-size: 0.9rem; color: #64748b; font-weight: 600;">📞 Standard d'Innovation</span>
            <div style="font-size: 1.2rem; font-weight: bold; color: #1e293b; margin-top: 5px;">+221 77 747 31 70</div>
        </div>
        <div style="flex: 1; min-width: 220px; background-color: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; text-align: center;">
            <span style="font-size: 0.9rem; color: #64748b; font-weight: 600;">📍 Hub d'Ancrage</span>
            <div style="font-size: 1.2rem; font-weight: bold; color: #1e293b; margin-top: 5px;">Saint-Louis, Sénégal</div>
        </div>
        <div style="flex: 1; min-width: 220px; background-color: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; text-align: center;">
            <span style="font-size: 0.9rem; color: #64748b; font-weight: 600;">⚡ Réactivité Sprint</span>
            <div style="font-size: 1.2rem; font-weight: bold; color: #1e293b; margin-top: 5px;">Moins de 12 heures</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")

    # ================= 3. FORMULAIRE & GUIDE DE SYNERGIE =================
    col_form, col_FAQ = st.columns([3, 2])

    with col_form:
        st.subheader("📩 Soumettre une initiative / Demander une démo")
        
        with st.form("contact_form", clear_on_submit=True):
            nom = st.text_input("Votre Nom complet / Institution *", placeholder="Ex: Direction de l'Horticulture, GIE Unité Maraîchère...")
            email = st.text_input("Votre Adresse Email Professionnelle *")
            
            departement = st.selectbox(
                "Objet stratégique de votre démarche :",
                [
                    "🏛️ Partenariat Institutionnel (Ministères / Directions / Agences)",
                    "🌾 Déploiement d'un Projet Pilote sur le Terrain",
                    "📊 Intégration de notre IA à vos données existantes",
                    "💡 Autre demande de collaboration"
                ]
            )
            
            msg = st.text_area("Présentez brièvement votre besoin ou idée d'alliance *", placeholder="Décrivez votre projet pilote, la région cible ou vos questions techniques...")

            submit_button = st.form_submit_button("Lancer la mise en relation")

            if submit_button:
                if not nom or not email or not msg:
                    st.error("⚠️ Veuillez remplir tous les champs obligatoires (marqués par un *).")
                elif "@" not in email:
                    st.error("⚠️ Veuillez entrer une adresse email valide.")
                else:
                    st.success(f"Félicitations {nom} ! Votre demande de contact axée sur '{departement}' a été reçue en priorité. Notre cellule d'innovation à Saint-Louis vous contactera sous peu à l'adresse : {email}.")

    with col_FAQ:
        st.subheader("💡 Guide rapide des Synergies")
        st.markdown(
            "En tant que startup agile, nous nous connectons rapidement aux processus des institutions publiques :"
        )
        
        with st.expander("🏛️ Intégration Ministères & Agences"):
            st.write("""
            YouAgronoMe est conçue pour s'imbriquer avec les plans d'action de l'État (ex: souveraineté alimentaire). 
            Nous fournissons des outils d'analyse de données (IA) faciles à adopter, sans lourdeurs administratives.
            """)
            
        with st.expander("🚀 Lancement de Projets Pilotes"):
            st.write("""
            Vous souhaitez tester notre technologie d'irrigation intelligente ou d'analyse prédictive sur une commune spécifique ? 
            Nous pouvons monter un projet pilote opérationnel en moins de 15 jours.
            """)
            
        with st.expander("📞 Urgences et Discussions Directes"):
            st.write("""
            Pour un échange rapide concernant une opportunité de financement (DER/FJ, 3FPT), un co-développement ou une démo en direct, appelez directement notre fondateur au **+221 77 747 31 70**.
            """)
            
        st.info("✉️ **Email direct de la direction :** issayoume2012@gmail.com")
