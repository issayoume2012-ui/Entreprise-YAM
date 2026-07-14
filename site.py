import streamlit as st
import time
import urllib.parse
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
# PRODUITS (VERSION PROFESSIONNELLE & TRACABILITÉ TERROIR)
# =====================================================
elif selected == "Produits":

    st.markdown("<h1 style='text-align: center; color: #1B5E20; font-weight: 800;'>🌾 Notre Marché Agricole en Direct</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; color: #4a5568; max-width: 700px; margin: 0 auto 25px auto;'>
        Commandez des produits de qualité issus du circuit court. Nous travaillons sans intermédiaire avec les GIE (Groupements d'Intérêt Économique) du Fleuve et des Niayes pour vous garantir fraîcheur et juste rémunération des producteurs.
    </p>
    """, unsafe_allow_html=True)

    # Bandeau d'engagement de la coopérative
    st.info("🥦 **Garantie Fraîcheur & Qualité** : Tous nos fruits et légumes sont récoltés à maturité, triés manuellement, puis conditionnés dans notre hub logistique de Sor (Saint-Louis) avant expédition.")

    # Barre de recherche et filtres de catégorie
    col_search, col_cat = st.columns([2, 1])
    with col_search:
        recherche = st.text_input("🔍 Rechercher un produit (ex: Riz, Tomates...)", "")
    with col_cat:
        categorie_choisie = st.selectbox("📁 Filtrer par filière", ["Toutes", "Fruits & Légumes", "Céréales & Graines"])

    st.divider()

    # Base de données produits enrichie (Données réelles du marché local sénégalais)
    # Structure : (Image, Nom, Prix (Numérique), Conditionnement, Catégorie, Tag, Origine Terroir, Stock disponible)
    produits = [
        ("to.jpg", "Tomates fraîches", 3500, "Sac de 5Kg", "Fruits & Légumes", "🔥 Prix Producteur", "Niayes", "En stock"),
        ("fr.jpg", "Fraises locales", 5000, "Sachet de 2Kg", "Fruits & Légumes", "✨ Spécialité", "Thiès (Mboro)", "Stock limité"),
        ("og.jpg", "Oignons rouges", 2500, "Sac de 5Kg", "Fruits & Légumes", "", "Vallée du Fleuve", "En stock"),
        ("cr.jpg", "Carottes lavées", 3000, "Sac de 5Kg", "Fruits & Légumes", "", "Zone des Niayes", "En stock"),
        ("pm.jpg", "Piments Verts / Rouges", 2000, "Sac de 3Kg", "Fruits & Légumes", "⚡ Récolte fraîche", "Louga", "En stock"),
        ("cc.jpg", "Concombres", 2800, "Sac de 3Kg", "Fruits & Légumes", "", "Zone des Niayes", "En stock"),
        ("pt.jpg", "Pommes de terre local", 4500, "Sachet de 5Kg", "Fruits & Légumes", "", "Vallée du Fleuve", "En stock"),
        ("or.jpg", "Oranges douces", 4000, "Sac de 3Kg", "Fruits & Légumes", "", "Casamance", "En stock"),
        ("mangue.jpg", "Mangues Kent", 3500, "Panier de 5Kg", "Fruits & Légumes", "🥭 Saison", "Pout / Niayes", "Stock limité"),
        ("banane.jpg", "Bananes douces", 2500, "Régime (~4-5kg)", "Fruits & Légumes", "", "Tambacounda", "En stock"),
        ("mais.jpg", "Maïs grain jaune", 7000, "Sac de 25Kg", "Céréales & Graines", "", "Bassin Arachidier", "En stock"),
        ("arachide.jpg", "Arachides décortiquées", 8500, "Sac de 10Kg", "Céréales & Graines", "", "Kaolack", "En stock"),
        ("riz.jpg", "Riz local brisé", 12000, "Sac de 25Kg", "Céréales & Graines", "⭐ Souveraineté", "Vallée du Fleuve (Podor)", "En stock"),
        ("mil.jpg", "Mil Souna", 9000, "Sac de 20Kg", "Céréales & Graines", "", "Région de Fatick", "En stock"),
        ("pasteque.jpg", "Pastèques", 6000, "Gros calibre (L'unité)", "Fruits & Légumes", "", "Kaffrine", "En stock"),
        ("citron.jpg", "Citrons verts", 2000, "Filet de 2.5kg", "Fruits & Légumes", "", "Thiès", "En stock"),
        ("niebe.jpg", "Niébé (Haricot)", 6500, "Sac de 10Kg", "Céréales & Graines", "", "Louga (Kébémer)", "En stock"),
        ("gombo.jpg", "Gombos frais", 2200, "Panier de 3Kg", "Fruits & Légumes", "", "Faye (Saint-Louis)", "En stock"),
        ("bissap.jpg", "Bissap Rouge (Fleurs)", 3000, "Sachet de 2Kg", "Céréales & Graines", "🌺 Qualité Supérieure", "Kaolack", "En stock"),
        ("sesame.jpg", "Graines de sésame", 7500, "Sac de 10Kg", "Céréales & Graines", "", "Sédhiou", "En stock")
    ]

    # Filtrage algorithmique des produits
    produits_filtres = [
        p for p in produits 
        if (recherche.lower() in p[1].lower() or recherche.lower() in p[6].lower()) 
        and (categorie_choisie == "Toutes" or p[4] == categorie_choisie)
    ]

    if not produits_filtres:
        st.warning("🔍 Aucun produit ne correspond à vos critères de recherche.")
    else:
        # Grille de présentation épurée de 4 colonnes
        cols = st.columns(4)
        for i, p in enumerate(produits_filtres):
            image, nom, prix, conditionnement, cat, tag, origine, dispo = p
            
            with cols[i % 4]:
                with st.container(border=True):
                    # En-tête de la fiche produit (Tag & Disponibilité)
                    col_t1, col_t2 = st.columns([3, 2])
                    with col_t1:
                        if tag:
                            st.markdown(f"<span style='background-color:#E8F5E9; color:#2E7D32; font-size:10px; padding:3px 8px; border-radius:10px; font-weight:bold; text-transform:uppercase;'>{tag}</span>", unsafe_allow_html=True)
                        else:
                            st.write("")
                    with col_t2:
                        color_dispo = "#2E7D32" if dispo == "En stock" else "#E65100"
                        st.markdown(f"<p style='color: {color_dispo}; font-size: 11px; text-align: right; margin: 0; font-weight: 600;'>● {dispo}</p>", unsafe_allow_html=True)
                    
                    # Image du produit
                    try:
                        st.image(image, use_container_width=True)
                    except:
                        st.markdown(f"<div style='height:120px; background-color:#F7FAF0; display:flex; align-items:center; justify-content:center; border-radius:8px; border: 1px dashed #C8E6C9; margin-bottom: 8px;'><span style='color:#2E7D32; font-size:2rem;'>📦</span></div>", unsafe_allow_html=True)
                        
                    # Informations Produit
                    st.markdown(f"<h4 style='margin: 8px 0 2px 0; color: #2D3748; font-weight: 700; font-size: 1.1rem;'>{nom}</h4>", unsafe_allow_html=True)
                    st.markdown(f"<p style='color: #718096; font-size: 12px; margin: 0 0 10px 0;'>📍 Origine : <b>{origine}</b></p>", unsafe_allow_html=True)
                    
                    # Prix & Conditionnement
                    st.markdown(f"""
                    <div style="background-color: #F8FAFC; padding: 8px; border-radius: 6px; border: 1px solid #E2E8F0; margin-bottom: 12px;">
                        <span style="font-size: 14px; color: #2E7D32; font-weight: 800; display: block;">{prix:,} FCFA</span>
                        <span style="font-size: 11px; color: #718096;">Format : {conditionnement}</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Action d'achat
                    qte_ajout = st.number_input("Quantité", min_value=1, max_value=100, value=1, key=f"qte_{nom}_{i}", label_visibility="collapsed")
                    
                    if st.button("🛒 Ajouter au Panier", key=f"btn_{nom}_{i}", type="primary", use_container_width=True):
                        deja_au_panier = False
                        texte_prix_complet = f"{prix} FCFA par {conditionnement}"
                        
                        # Vérification des doublons dans le panier
                        for item in st.session_state.panier:
                            if item["produit"] == nom:
                                item["quantite"] += qte_ajout
                                deja_au_panier = True
                                break
                        
                        if not deja_au_panier:
                            st.session_state.panier.append({
                                "produit": nom,
                                "prix": texte_prix_complet,
                                "quantite": qte_ajout
                            })
                        
                        st.toast(f"✅ {qte_ajout}x {nom} ajouté(s) à votre panier !", icon="🛒")
# =====================================================
# COMMANDE
# =====================================================
elif selected == "Commande":

    st.markdown("<h1 style='text-align: center; color: #1B5E20; font-weight: 800;'>📦 Votre E-Panier & Facturation</h1>", unsafe_allow_html=True)

    NUMERO_WHATSAPP = "221777473170"
    EMAIL_DEST = "issayoume2012@gmail.com"
    panier = st.session_state.panier

    if not panier:
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: #fffcf5; border: 1px dashed #ffe0b2; border-radius: 16px; margin: 20px 0;">
            <h2 style="color: #e65100; margin: 0 0 10px 0;">🛒 Votre panier est vide</h2>
            <p style="color: #666; margin: 0;">Explorez l'onglet <b>Produits</b> pour composer votre panier en quelques clics.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color: #2E7D32; margin-bottom: 15px;'>🛒 Vérification des articles</h3>", unsafe_allow_html=True)

        total_articles = 0
        total_financier = 0

        # Affichage et gestion des articles présents dans le panier
        for i, item in enumerate(list(panier)):
            try:
                partie_prix = item["prix"].split("FCFA")[0]
                prix_numerique = int(''.join(filter(str.isdigit, partie_prix)))
            except:
                prix_numerique = 0
                
            sous_total = prix_numerique * item["quantite"]
            total_financier += sous_total
            total_articles += item["quantite"]

            with st.container():
                c1, c2, c3, c4 = st.columns([4, 2, 3, 1])
                with c1:
                    st.markdown(f"<p style='font-size: 16px; font-weight: 600; margin:0;'>🍏 {item['produit']}</p>", unsafe_allow_html=True)
                    st.markdown(f"<p style='font-size: 12px; color: #718096; margin:0;'>{item['prix']}</p>", unsafe_allow_html=True)
                with c2:
                    st.markdown(f"<p style='font-size: 16px; margin:0; text-align: center;'><b>{item['quantite']}</b> unitaire(s)</p>", unsafe_allow_html=True)
                with c3:
                    st.markdown(f"<p style='font-size: 16px; font-weight: 700; color:#2E7D32; margin:0;'>{sous_total:,} FCFA</p>", unsafe_allow_html=True)
                with c4:
                    if st.button("❌", key=f"supprimer_{i}"):
                        st.session_state.panier.pop(i)
                        st.rerun()
                st.markdown("<hr style='margin: 8px 0; border: 0.5px solid #edf2f7;'>", unsafe_allow_html=True)

        # Base de données géographique du Sénégal avec quartiers détaillés
        @st.cache_data
        def get_geo_senegal_detail():
            return {
                "Dakar": [
                    "Dakar Plateau", "Médina", "Fann / Point E / Amitié", "Mermoz / Sacré-Cœur", 
                    "Ouakam", "Ngor", "Almadies", "Yoff", "Grand Yoff", "Parcelles Assainies", 
                    "Guédiawaye", "Pikine", "Thiaroye", "Keur Massar", "Rufisque", "Diamniadio"
                ],
                "Saint-Louis": [
                    "SND (Saint-Louis île)", "Sor", "Ndiolofène", "Balacos", "Guet Ndar", 
                    "Goxu Mbacc", "Bango", "Hydrobase", "Rao", "Richard-Toll", "Dagana", 
                    "Podor", "Ndioum", "Ross Béthio"
                ],
                "Thiès": [
                    "Thiès Ville (Mbourène / Grand Thiès)", "Dixième", "Saly Portudal", 
                    "Mbour Ville", "Somone", "Ngaparou", "Joal-Fadiouth", "Tivaouane", 
                    "Mboro", "Pout", "Khombole", "Popenguine"
                ],
                "Diourbel": ["Diourbel Ville", "Touba Mosquée", "Mbacké", "Bambey"],
                "Louga": ["Louga Ville", "Linguère", "Dahra", "Kébémer"],
                "Fatick": ["Fatick Ville", "Foundiougne", "Gossas", "Sokone", "Diofior"],
                "Kaolack": ["Kaolack Ville", "Nioro du Rip", "Guinguinéo", "Kahone"],
                "Kaffrine": ["Kaffrine Ville", "Koungheul", "Birkelane", "Malem Hodar"],
                "Tambacounda": ["Tambacounda Ville", "Bakel", "Goudiry", "Koumpentoum"],
                "Kolda": ["Kolda Ville", "Vélingara", "Médina Yoro Foulah"],
                "Ziguinchor": ["Ziguinchor Ville", "Bignona", "Oussouye", "Cap Skirring"],
                "Sédhiou": ["Sédhiou Ville", "Goudomp", "Bounkiling"],
                "Matam": ["Matam Ville", "Ourossogui", "Kanel", "Ranérou"],
                "Kédougou": ["Kédougou Ville", "Saraya", "Salémata"]
            }

        geo_senegal = get_geo_senegal_detail()

        st.markdown("<h3 style='color: #2E7D32; margin-top: 30px;'>⚙️ Réseau Logistique National & Facturation</h3>", unsafe_allow_html=True)
        col_reg, col_com, col_promo = st.columns(3)
        
        with col_reg:
            region_selectionnee = st.selectbox("📍 Région du Sénégal *", list(geo_senegal.keys()))
            
        with col_com:
            commune_selectionnee = st.selectbox("🏙️ Quartier / Commune / Zone *", geo_senegal[region_selectionnee])

        # Tarification logistique réelle selon la proximité territoriale
        frais_livraison = 0
        delai_estime = ""

        if region_selectionnee == "Saint-Louis":
            # Notre hub d'ancrage local
            if commune_selectionnee in ["SND (Saint-Louis île)", "Sor", "Ndiolofène", "Balacos", "Guet Ndar", "Goxu Mbacc", "Bango", "Hydrobase"]:
                frais_livraison = 1500
                delai_estime = "⚡ Proximité Hub : Livraison dans la journée"
            else:
                frais_livraison = 3000
                delai_estime = "🚛 Régional Saint-Louis : 24h à 48h"
        elif region_selectionnee == "Dakar":
            frais_livraison = 2500
            delai_estime = "⚡ Axe Dakar Express : Livraison sous 24h"
        elif region_selectionnee == "Thiès":
            frais_livraison = 3500
            delai_estime = "🚛 Axe Thiès/Mbour : Livraison sous 24h à 48h"
        elif region_selectionnee in ["Diourbel", "Fatick", "Kaolack", "Louga"]:
            frais_livraison = 4500
            delai_estime = "📦 Expédition Centre : 48h à 72h"
        else:
            # Zones plus lointaines (Casamance, Sénégal Oriental, Nord Est)
            frais_livraison = 5500
            delai_estime = "🗺️ Expédition Longue Distance : 72h à 96h via lignes partenaires"

        with col_promo:
            code_promo = st.text_input("🎟️ Code Promo (Optionnel)", "").strip()
            remise = 0
            if code_promo.upper() == "YOU2026":
                remise = int(total_financier * 0.10)
                st.success("🎉 Code valide (-10%)")

        # Application de la tarification finale
        total_final_net = total_financier + frais_livraison - remise
        points_gagnes = total_final_net // 1000

        st.info(f"📍 Réseau de livraison : Région de {region_selectionnee} — Secteur {commune_selectionnee}\n\n⏱️ Délai de transport estimé : {delai_estime}")
        
        c_sub, c_liv, c_rem = st.columns(3)
        with c_sub:
            st.text(f"Sous-total : {total_financier:,} FCFA")
        with c_liv:
            st.text(f"Frais de transport : {frais_livraison:,} FCFA")
        with c_rem:
            if remise > 0:
                st.text(f"Réduction : -{remise:,} FCFA")
        
        st.metric(label="TOTAL NET À PAYER", value=f"{total_final_net:,} FCFA")
        st.success(f"🌱 Points fidélité collectés : +{points_gagnes} points sur cette commande.")

        st.markdown("<h3 style='color: #2E7D32; margin-top: 30px;'>👤 Coordonnées du Destinataire & Planification</h3>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom complet *", placeholder="Ex: Issa Youme")
            telephone = st.text_input("Téléphone fonctionnel (WhatsApp de préférence) *", placeholder="Ex: 777473170")
            adresse = st.text_input("Complément d'adresse exacte *", placeholder="Maison, Rue, Indications visuelles (ex: à côté de la Mosquée)...")
        with col2:
            paiement = st.selectbox("Méthode de paiement", ["Présentiel (À la livraison)", "Wave", "Orange Money"])
            
            # Calcul des jours de marge réels pour la livraison
            delai_jours = 1 if region_selectionnee in ["Saint-Louis", "Dakar"] else (2 if region_selectionnee == "Thiès" else 3)
            date_min = datetime.now() + timedelta(days=delai_jours)
            date_livraison = st.date_input("Date de réception souhaitée", value=date_min, min_value=datetime.now())
            
            creneau_horaire = st.selectbox("Créneau horaire préféré", [
                "Matin (08h00 - 12h00)", 
                "Après-midi (13h00 - 17h00)", 
                "Fin de journée (17h00 - 20h00)"
            ])
            
        commentaire = st.text_area("Instructions spéciales pour le livreur", placeholder="Ex: Déposer chez le gardien, appeler 10 minutes avant d'arriver...")

        if paiement in ["Wave", "Orange Money"]:
            st.warning(f"💳 Paiement mobile sélectionné : Merci d'effectuer votre transfert au **+221 77 747 31 70** une fois votre commande envoyée.")

        with st.expander("📄 Bordereau de chargement", expanded=False):
            for p in panier:
                st.write(f"• {p['produit']} x{p['quantite']} — ({p['prix']})")

        # Soumission de la commande
        if st.button("🚀 Confirmer et Commander", use_container_width=True, type="primary"):
            if not nom or not telephone or not adresse:
                st.error("⚠️ Erreur : Les champs obligatoires (*) doivent être remplis.")
            else:
                texte_produits = ""
                for p in panier:
                    texte_produits += f"• {p['produit']} x {p['quantite']} ({p['prix']})\n"

                # Création du message de commande
                message = f"""🌾 COMMANDE YOUAGRONOME SÉNÉGAL\n\n👤 DESTINATAIRE :\n• Nom : {nom}\n• Tél : {telephone}\n• Région : {region_selectionnee}\n• Secteur/Quartier : {commune_selectionnee}\n• Adresse précise : {adresse}\n\n📅 LOGISTIQUE DE LIVRAISON :\n• Date souhaitée : {date_livraison.strftime('%d/%m/%Y')}\n• Tranche horaire : {creneau_horaire}\n\n📦 DÉTAILS DU PANIER :\n{texte_produits}\n💰 SOUS-TOTAL : {total_financier:,} FCFA\n🚚 LOGISTIQUE TERRAIN : {frais_livraison:,} FCFA\n📉 REMISE CODE : {remise:,} FCFA\n💵 TOTAL NET GLOBAL : {total_final_net:,} FCFA\n\n💳 MODE DE RÈGLEMENT :\n• Choix : {paiement}\n• Instructions : {commentaire if commentaire else 'Aucune consigne particulière.'}"""

                # Modèle HTML de Facture Pro sans fioritures superflues
                html_facture = f"""
                <div style="font-family: Arial, sans-serif; padding: 25px; border: 1px solid #ccffcc; max-width: 550px; border-radius: 12px; background-color: #ffffff; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    <h2 style="color: #1B5E20; text-align: center; margin-bottom: 0; font-weight: 800; letter-spacing: 1px;">YOUAGRONOME SÉNÉGAL</h2>
                    <p style="text-align: center; font-size: 12px; color: #777; margin-top: 5px;">Réseau de Distribution de Proximité</p>
                    <hr style="border: 0.5px solid #e2e8f0; margin: 15px 0;">
                    <p style="font-size: 13px; line-height: 1.6; color: #2d3748;">
                        <b>Destinataire :</b> {nom}<br>
                        <b>Téléphone :</b> {telephone}<br>
                        <b>Zone géographique :</b> {region_selectionnee} — {commune_selectionnee}<br>
                        <b>Adresse exacte :</b> {adresse}<br>
                        <b>Date programmée :</b> {date_livraison.strftime('%d/%m/%Y')} ({creneau_horaire})
                    </p>
                    <hr style="border: 0.5px solid #e2e8f0; margin: 15px 0;">
                    <h4 style="color: #2E7D32; margin-bottom: 10px;">Articles Commandés :</h4>
                    <p style="font-size: 13px; color: #4a5568; line-height: 1.6; background-color: #f7fafc; padding: 10px; border-radius: 6px;">{texte_produits.replace('\n', '<br>')}</p>
                    <hr style="border: 0.5px dashed #cbd5e0; margin: 15px 0;">
                    <table style="width: 100%; font-size: 14px; color: #4a5568; line-height: 2;">
                        <tr><td>Total Articles :</td><td style="text-align: right; font-weight: 600;">{total_financier:,} FCFA</td></tr>
                        <tr><td>Livraison ({commune_selectionnee}) :</td><td style="text-align: right; font-weight: 600;">{frais_livraison:,} FCFA</td></tr>
                        <tr style="color: #c53030;"><td>Code de réduction :</td><td style="text-align: right; font-weight: 600;">-{remise:,} FCFA</td></tr>
                        <tr style="font-size: 18px; font-weight: 800; color: #1B5E20;">
                            <td style="padding-top: 12px; border-top: 1px solid #edf2f7;">Montant Global Net :</td>
                            <td style="text-align: right; padding-top: 12px; border-top: 1px solid #edf2f7;">{total_final_net:,} FCFA</td>
                        </tr>
                    </table>
                    <p style="font-size: 11px; text-align: center; color: #a0aec0; margin-top: 30px; font-style: italic; border-top: 1px solid #edf2f7; padding-top: 10px;">YouAgronoMe - Jeune entreprise sénégalaise au service de nos terroirs.</p>
                </div>
                """

                whatsapp_link = "https://wa.me/" + NUMERO_WHATSAPP + "?text=" + urllib.parse.quote(message)
                email_link = f"mailto:{EMAIL_DEST}?subject=Commande YouAgronoMe - {nom}&body=" + urllib.parse.quote(message)

                # Sauvegarde au sein de l'historique
                st.session_state.historique.append({
                    "client": nom,
                    "paiement": paiement,
                    "total": f"{total_final_net:,} FCFA",
                    "commande": panier.copy(),
                    "brut_texte": message,
                    "html_facture": html_facture
                })

                st.success("🎉 Votre bon de commande a bien été enregistré !")
                c1, c2 = st.columns(2)
                with c1:
                    st.link_button("📱 Envoyer sur WhatsApp", whatsapp_link, use_container_width=True)
                with c2:
                    st.link_button("📧 Envoyer par E-mail", email_link, use_container_width=True)

        st.markdown("<br><hr>", unsafe_allow_html=True)
        if st.button("🧹 Vider entièrement le panier", use_container_width=True):
            st.session_state.panier = []
            st.rerun()

    # Section Historique de session
    st.markdown("<h3 style='color: #4a5568; margin-top: 40px;'>📜 Vos commandes enregistrées</h3>", unsafe_allow_html=True)
    historique = st.session_state.historique

    if not historique:
        st.info("Aucun achat enregistré lors de cette visite en ligne.")
    else:
        for idx, cmd in enumerate(reversed(historique), start=1):
            with st.expander(f"📦 Commande #{idx} — {cmd['client']} ({cmd['total']})"):
                st.markdown(f"**Règlement choisi :** `{cmd['paiement']}`")
                
                if "html_facture" in cmd:
                    st.markdown(cmd["html_facture"], unsafe_allow_html=True)
                    st.write("")
                else:
                    for p in cmd["commande"]:
                        st.write(f"• {p['produit']} (x{p['quantite']})")
                
                btn_txt, btn_html = st.columns(2)
                
                with btn_txt:
                    st.download_button(
                        label="📥 Reçu (Format Texte)",
                        data=cmd.get("brut_texte", "Aucune donnée"),
                        file_name=f"recu_youagronome_{idx}.txt",
                        mime="text/plain",
                        key=f"dl_txt_{idx}",
                        use_container_width=True
                    )
                
                with btn_html:
                    st.download_button(
                        label="🖨️ Facture (Format Imprimable)",
                        data=cmd.get("html_facture", "Aucune donnée"),
                        file_name=f"facture_youagronome_{idx}.html",
                        mime="text/html",
                        key=f"dl_html_{idx}",
                        use_container_width=True
                    )
# =====================================================
# =====================================================
# ALLIANCES ET CO-CONSTRUCTION INSTITUTIONNELLE (NOUVELLE VERSION)
# =====================================================
elif selected == "Réalisations":
    
    # Style CSS épuré et professionnel
    st.markdown("""
    <style>
    .concept-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.01);
        margin-bottom: 20px;
    }
    .concept-title {
        color: #1b5e20;
        font-weight: 700;
        font-size: 1.2rem;
        margin-bottom: 8px;
    }
    .gov-badge {
        background-color: #e3f2fd;
        color: #0d47a1;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 12px;
    }
    .proposal-box {
        background-color: #f1f8e9;
        border-left: 5px solid #2e7d32;
        padding: 20px;
        border-radius: 4px 16px 16px 4px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # 1. EN-TÊTE DE LA JEUNE POUSSE
    # =========================
    st.title("🏛️ Hub National d'Innovation & Alliances")
    st.markdown(
        "**YouAgronoMe** est une jeune entreprise agritech sénégalaise en pleine émergence. "
        "Notre mission est de servir de **bras technologique** pour les agences, directions et ministères du Sénégal "
        "afin d'accélérer la souveraineté alimentaire nationale par l'IA et la logistique de précision."
    )
    st.write("---")

    # =========================
    # 2. NOS CHANTIERS CO-CONSTRUITS (NOTRE VISION EN ACTION)
    # =========================
    st.subheader("💡 Nos Piliers de Co-Développement")
    st.markdown("Découvrez comment nous traduisons les objectifs de l'État en solutions concrètes sur le terrain :")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="concept-card">
            <span class="gov-badge">🇸🇳 MINISTÈRE DE L'AGRICULTURE (MASAE)</span>
            <div class="concept-title">Data-Souveraineté & Cartographie par IA</div>
            <p style="font-size: 0.9rem; color: #555;">
                Optimisation de la distribution des semences et engrais. En utilisant nos algorithmes de prédiction météo et d'analyse des sols, nous aidons à cibler les zones prioritaires pour maximiser les rendements nationaux.
            </p>
            <small style="color: #2e7d32; font-weight: bold;">🎯 Objectif : Réduction du gaspillage d'intrants</small>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="concept-card">
            <span class="gov-badge">🇸🇳 ANIDA / ANCAR</span>
            <div class="concept-title">Modernisation des DAC (Domaines Agricoles Communautaires)</div>
            <p style="font-size: 0.9rem; color: #555;">
                Introduction de nos micro-systèmes d'irrigation intelligente et de capteurs IoT low-cost pour transformer les exploitations des jeunes ruraux en fermes intelligentes et résilientes.
            </p>
            <small style="color: #2e7d32; font-weight: bold;">🎯 Objectif : Fixer les jeunes dans leurs terroirs</small>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="concept-card">
            <span class="gov-badge">🇸🇳 DER/FJ & PROGRAMMES JEUNES</span>
            <div class="concept-title">Agri-Logistique Urbain-Rural Sécurisée</div>
            <p style="font-size: 0.9rem; color: #555;">
                Mise à disposition de notre plateforme e-panier et de notre réseau d'acheminement régional pour désenclaver les micro-producteurs financés par l'État et leur garantir un accès direct aux marchés urbains.
            </p>
            <small style="color: #2e7d32; font-weight: bold;">🎯 Objectif : Rentabilité immédiate des financements publics</small>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="concept-card">
            <span class="gov-badge">🇸🇳 SENELEC / DIRECTION DU NUMÉRIQUE</span>
            <div class="concept-title">Agritech Verte & Bas Carbone</div>
            <p style="font-size: 0.9rem; color: #555;">
                Couplage de notre technologie de suivi parcellaire avec les initiatives de transition énergétique pour réduire la facture d'électricité liée au pompage agricole à grande échelle.
            </p>
            <small style="color: #2e7d32; font-weight: bold;">🎯 Objectif : Agriculture à faible empreinte carbone</small>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # =====================================================
    # 3. INTERACTIF : SYNERGIE IA & PROTOCOLES D'ACCORD (MOU)
    # =====================================================
    st.subheader("🤖 Concepteur d'Alliances Stratégiques (IA)")
    st.markdown(
        "**Agent public ou décideur étatique ?** Sélectionnez votre département et vos priorités "
        "pour que notre IA structure instantanément un projet de collaboration opérationnelle prêt à être examiné."
    )

    # Formulaire de ciblage
    col_gov, col_opt = st.columns(2)
    
    with col_gov:
        structure = st.selectbox(
            "Sélectionnez votre Structure / Agence :",
            [
                "Ministère de l'Agriculture, de la Souveraineté Alimentaire et de l'Élevage (MASAE)",
                "Agence Nationale d'Insertion et de Développement Agricole (ANIDA)",
                "Agence Nationale de Conseil Agricole et Rural (ANCAR)",
                "Délégation Générale à l'Entrepreneuriat Rapide des Femmes et des Jeunes (DER/FJ)",
                "Fonds de Financement de la Formation Professionnelle (3FPT)"
            ]
        )
        
        defi_majeur = st.selectbox(
            "Votre défi prioritaire sur le terrain :",
            [
                "Maîtrise de l'eau et irrigation solaire économique",
                "Désenclavement commercial et réduction des pertes de transport",
                "Digitalisation des données parcellaires des petits exploitants",
                "Insertion et viabilité économique des groupements de femmes/jeunes",
                "Formation des producteurs aux technologies agritech"
            ]
        )

    with col_opt:
        localite_cible = st.text_input("Région/Zone pilote d'intervention :", placeholder="Ex: Vallée du Fleuve, Niayes, Casamance, Bassin Arachidier")
        budget_approche = st.selectbox("Mécanisme de mise en œuvre souhaité :", ["Co-financement public/privé", "Appui technique sans coût pour l'État", "Projet pilote d'incubation"])

    # Action IA
    generer_mou = st.button("⚡ Structurer le Projet Pilote par l'IA", use_container_width=True, type="primary")

    if generer_mou:
        if not localite_cible:
            st.error("⚠️ Veuillez spécifier une région ou zone pilote pour adapter l'algorithme.")
        else:
            with st.spinner("Analyse des directives ministérielles et génération du document..."):
                sigle_structure = structure.split("(")[-1].replace(")", "") if "(" in structure else "l'État"
                
                # Génération du plan de projet structuré et percutant
                projet_mou = f"""
📋 PROJET DE COLLABORATION STRATÉGIQUE (MOU)
=====================================================
PARTIES : YouAgronoMe Sénégal  x  {structure}
CADRE D’INTERVENTION : Zone pilote de {localite_cible}
=====================================================

1. OBJECTIF DE L'ALLIANCE :
Intégrer les solutions agritech de YouAgronoMe pour répondre au défi national :
" {defi_majeur} ".

2. RÉPARTITION DES RÔLES :
👉 Pour {sigle_structure} : 
   - Facilitation de l'accès aux données de terrain et identification des groupements bénéficiaires.
   - Intégration du projet pilote dans les agendas régionaux de développement.
👉 Pour YouAgronoMe :
   - Déploiement de notre plateforme de suivi assistée par IA pour optimiser les décisions de culture.
   - Garantie d'achat/transit logistique des récoltes produites via notre e-panier intelligent.

3. OUTCOMES ATTENDUS (PILOTE 6 MOIS) :
   - Digitalisation de 100% des producteurs impliqués dans la zone.
   - Baisse de 25% des pertes post-récolte sur l'axe {localite_cible} -> Dakar.
   - Rapports d'analyse de rendement générés automatiquement par notre IA pour vos services de statistiques.

4. MODE DE FINANCEMENT :
   - Approche : {budget_approche}
"""
                st.success("✨ Proposition d'alliance générée avec succès !")
                st.markdown(f"<div class='proposal-box'><pre style='white-space: pre-wrap;'>{projet_mou}</pre></div>", unsafe_allow_html=True)
                
                # Oublions les formulaires complexes : on lance une communication directe par mail
                sujet_mail = urllib.parse.quote(f"Proposition d'Alliance Technologique : YouAgronoMe & {sigle_structure}")
                corps_mail = urllib.parse.quote(f"Bonjour,\n\nEn tant que jeune entreprise innovante du Sénégal, nous avons le plaisir de vous soumettre notre concept d'intégration technologique pour relever le défi suivant : {defi_majeur}.\n\nVous trouverez notre ébauche de projet pilote en pièce jointe.\n\nRestant à votre disposition,\nL'équipe de direction YouAgronoMe.")
                
                st.link_button(
                    "✉️ Envoyer cette proposition au Cabinet de Direction", 
                    f"mailto:cabinet@youagronome.com?subject={sujet_mail}&body={corps_mail}",
                    use_container_width=True
                )

    st.write("---")

    # =====================================================
    # 4. REJOINDRE NOTRE ÉCOSYSTÈME
    # =====================================================
    st.subheader("🤝 Rejoignez la dynamique")
    st.markdown(
        "Vous êtes un représentant d'une collectivité locale ou d'un service déconcentré de l'État ? "
        "Notre équipe est mobile et prête à venir faire une démonstration de notre plateforme au sein de vos bureaux de développement régionaux."
    )
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.info("📞 **Ligne Directe Partenariats :** +221 77 747 31 70")
    with col_c2:
        st.info("✉️ **Courriel Officiel :** issayoume2012@gmail.com")
# =====================================================
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
