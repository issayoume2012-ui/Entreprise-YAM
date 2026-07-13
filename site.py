import streamlit as st
import time
import urllib.parse

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="YouAgronoMe",
    page_icon="🌾",
    layout="wide"
)

# =====================================================
# SESSION
# =====================================================

if "panier" not in st.session_state:
    st.session_state.panier = []

if "historique" not in st.session_state:
    st.session_state.historique = []

with st.spinner("Chargement..."):
    time.sleep(1)

# =====================================================
# INJECTION CSS POUR LA BANDE DE NAVIGATION BANNER XXL (RADIO CUSTOM)
# =====================================================
st.markdown("""
<style>
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

/* Ajustement pour les petits écrans (Tablettes / Mobiles) */
@media (max-width: 992px) {
    div[data-testid="stRadio"] > div[role="radiogroup"] > label {
        font-size: 15px !important;
        padding: 12px 5px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# SELECTION DU MENU VIA ST.RADIO (EN REMPLACEMENT DE OPTION_MENU)
# =====================================================
options_menu = [
    "🏠 Accueil", 
    "🛒 Produits", 
    "📦 Commande", 
    "📊 Réalisations", 
    "📞 Contact"
]

# Le st.radio utilise le CSS ci-dessus pour se transformer en barre horizontale haut de gamme
selected_raw = st.radio(
    "Navigation Menu",
    options=options_menu,
    horizontal=True
)

# Nettoyage de la chaîne pour la correspondance des conditions du code original
selected = selected_raw.split(" ")[1]

# =====================================================
# ACCUEIL
# =====================================================
if selected == "Accueil":

    st.markdown("""
    <style>
    /* Intégration d'une police moderne */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    .main .block-container {
        font-family: 'Plus Jakarta Sans', sans-serif;
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

    /* 📊 STYLE DYNAMIQUE DES CHIFFRES CLÉS (CUSTOM METRICS) */
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
    /* Couleurs spécifiques des stats */
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
    /* Effets de survol interactifs par thème */
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

    /* =======================================================
       RESPONSIVE DESIGN (TABLETTES & SMARTPHONES)
       ======================================================= */
    @media (max-width: 992px) {
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

    # HERO XXL
    st.markdown("""
    <div class="hero">
        <h1>🌾 YouAgronoMe</h1>
        <h2>Eau • Innovation • Sol • Plante</h2>
        <p>
            Nous optimisons les ressources vitales et déployons des technologies intelligentes 
            pour façonner une agriculture durable, résiliente et hautement productive.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # STATISTIQUES REFAITES (PLUS DYNAMIQUES)
    st.markdown("<div class='section-title'>📊 Chiffres Clés</div>", unsafe_allow_html=True)
    
    stat_cols = st.columns(4)
    
    with stat_cols[0]:
        st.markdown("""
        <div class="stat-card stat-plante">
            <div class="stat-number">+500</div>
            <div class="stat-label">👨‍🌾 Producteurs Accompagnés</div>
        </div>
        """, unsafe_allow_html=True)
        
    with stat_cols[1]:
        st.markdown("""
        <div class="stat-card stat-sol">
            <div class="stat-number">+150</div>
            <div class="stat-label">🌱 Exploitations Suivies</div>
        </div>
        """, unsafe_allow_html=True)
        
    with stat_cols[2]:
        st.markdown("""
        <div class="stat-card stat-eau">
            <div class="stat-number">+20</div>
            <div class="stat-label">📍 Zones d'Intervention</div>
        </div>
        """, unsafe_allow_html=True)
        
    with stat_cols[3]:
        st.markdown("""
        <div class="stat-card stat-innovation">
            <div class="stat-number">+40</div>
            <div class="stat-label">🤝 Partenaires Stratégiques</div>
        </div>
        """, unsafe_allow_html=True)

    # SERVICES
    st.markdown("<div class='section-title'>🚀 Nos Services</div>", unsafe_allow_html=True)

    services = [
        ("🌱 Conseils Agricoles", "Accompagnement technique adapté à chaque type de culture.", "card-plante"),
        ("💧 Irrigation Intelligente", "Gestion optimale, connectée et raisonnée des ressources précieuses en eau.", "card-eau"),
        ("🟤 Analyse des Sols", "Cartographie complète, suivi de la fertilité et aide à la régénération des sols arables.", "card-sol"),
        ("💻 Technologie Agritech", "Drones imageries, capteurs IoT et outils digitaux d'aide à la décision.", "card-innovation"),
        ("🛒 Accès aux Marchés", "Valorisation optimale des récoltes et création de débouchés fiables.", "card-plante"),
        ("📚 Formations & R&D", "Renforcement continu des compétences et vulgarisation des pratiques innovantes.", "card-innovation")
    ]

    cols = st.columns(3)
    for i, (titre, texte, theme_class) in enumerate(services):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="glass-base {theme_class}">
                <h3>{titre}</h3>
                <p>{texte}</p>
            </div>
            """, unsafe_allow_html=True)

    # MISSION & VISION
    st.markdown("<div class='section-title'>🎯 Notre Engagement</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="glass-base card-sol">
            <h3>🟤 Notre Mission</h3>
            <p>Régénérer les sols, maximiser l'efficience de l'eau et sécuriser les rendements des producteurs grâce au savoir-faire technique et aux alternatives écologiques.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="vision-nature">
            <h3>🌍 Notre Vision</h3>
            <p>Impulser la révolution agricole moderne au Sénégal, où l'innovation technologique s'harmonise parfaitement avec les cycles de la nature pour nourrir durablement.</p>
        </div>
        """, unsafe_allow_html=True)

    # DOMAINES D'INTERVENTION REFAITS (BADGES INTERACTIFS ET ANIMÉS)
    st.markdown("<div class='section-title'>🌾 Domaines d'Intervention</div>", unsafe_allow_html=True)

    domaines = [
        ("🥦 Maraîchage", "domaine-plante"),
        ("💧 Gestion de l'Eau", "domaine-eau"),
        ("🛸 Agritech & Drones", "domaine-innovation"),
        ("🌾 Cultures Vivrières", "domaine-sol"),
        ("🐐 Élevage Durable", "domaine-plante"),
        ("🧪 Hydroponie", "domaine-eau")
    ]

    cols = st.columns(3)
    for i, (domaine, theme_class) in enumerate(domaines):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="domaine-card {theme_class}">
                {domaine}
            </div>
            """, unsafe_allow_html=True)

    st.write("") 
    st.success("🌱 Ensemble, valorisons notre sol et notre eau grâce à l'innovation !")

# =====================================================
elif selected == "Produits":
    st.title("🌾 Notre Marché Agricole")
    st.markdown("Parcourez nos produits frais et ajoutez-les à votre panier.")
    
    # Barre de recherche et Catégories
    col_search, col_cat = st.columns([2, 1])
    with col_search:
        recherche = st.text_input("🔍 Rechercher un produit...", "")
    with col_cat:
        categorie_choisie = st.selectbox("📁 Catégorie", ["Tous", "Fruits & Légumes", "Céréales & Graines"])

    st.divider()

    # Liste enrichie avec une catégorie et un tag (ex: Promo, Nouveau, Stock Limité)
    # Format : (image, nom, description_prix, categorie, tag)
    produits = [
        ("to.jpg", "Tomates", "3500 FCFA par sac de 5Kg", "Fruits & Légumes", "🔥 Promo"),
        ("fr.jpg", "Fraises", "5000 FCFA par sachet de 2Kg", "Fruits & Légumes", ""),
        ("og.jpg", "Oignons", "2500 FCFA par sac de 5Kg", "Fruits & Légumes", ""),
        ("cr.jpg", "Carottes", "3000 FCFA par sac de 5Kg", "Fruits & Légumes", ""),
        ("pm.jpg", "Piments", "2000 FCFA par sac de 3Kg", "Fruits & Légumes", "⚡ Stock limité"),
        ("cc.jpg", "Concombres", "2800 FCFA par sac de 3Kg", "Fruits & Légumes", ""),
        ("pt.jpg", "Pommes de terre", "4500 FCFA par sachet de 5Kg", "Fruits & Légumes", ""),
        ("or.jpg", "Oranges", "4000 FCFA par sac de 3Kg", "Fruits & Légumes", ""),
        ("mangue.jpg", "Mangues", "3500 FCFA par panier de 5Kg", "Fruits & Légumes", "✨ Saison"),
        ("banane.jpg", "Bananes", "2500 FCFA par régime", "Fruits & Légumes", ""),
        ("mais.jpg", "Maïs", "7000 FCFA par sac de 25Kg", "Céréales & Graines", ""),
        ("arachide.jpg", "Arachides", "8500 FCFA par sac de 10Kg", "Céréales & Graines", ""),
        ("riz.jpg", "Riz local", "12000 FCFA par sac de 25Kg", "Céréales & Graines", "⭐ Top Qualité"),
        ("mil.jpg", "Mil", "9000 FCFA par sac de 20Kg", "Céréales & Graines", ""),
        ("pasteque.jpg", "Pastèques", "6000 FCFA l’unité", "Fruits & Légumes", ""),
        ("citron.jpg", "Citrons", "2000 FCFA par filet", "Fruits & Légumes", ""),
        ("niebe.jpg", "Niébé", "6500 FCFA par sac de 10Kg", "Céréales & Graines", ""),
        ("gombo.jpg", "Gombos", "2200 FCFA par panier", "Fruits & Légumes", ""),
        ("bissap.jpg", "Bissap", "3000 FCFA par sachet de 2Kg", "Céréales & Graines", ""),
        ("sesame.jpg", "Sésame", "7500 FCFA par sac de 10Kg", "Céréales & Graines", "")
    ]

    # Double filtrage : Recherche textuelle + Catégorie
    produits_filtres = [
        p for p in produits 
        if (recherche.lower() in p[1].lower()) and (categorie_choisie == "Tous" or p[3] == categorie_choisie)
    ]

    if not produits_filtres:
        st.warning("Aucun produit ne correspond à votre recherche.")
    else:
        cols = st.columns(4)
        for i, p in enumerate(produits_filtres):
            image, nom, description_prix, cat, tag = p
            
            with cols[i % 4]:
                with st.container(border=True):
                    # Affichage du Tag si présent
                    if tag:
                        st.markdown(f"<span style='background-color:#ffe0b2; color:#e65100; font-size:11px; padding:3px 8px; border-radius:10px; font-weight:bold;'>{tag}</span>", unsafe_allow_html=True)
                    else:
                        st.write("") # Espace vide pour l'alignement
                        
                    try:
                        st.image(image, use_container_width=True)
                    except:
                        st.info(f"📸 Image de {nom}")
                        
                    st.subheader(nom)
                    st.markdown(f"<p style='color: #2e7d32; font-weight: bold; font-size: 1.1em; margin-bottom: 5px;'>{description_prix}</p>", unsafe_allow_html=True)
                    
                    qte_ajout = st.number_input("Quantité", min_value=1, max_value=50, value=1, key=f"qte_{nom}_{i}")
                    
                    if st.button("🛒 Ajouter", key=f"btn_{nom}_{i}", type="primary", use_container_width=True):
                        deja_au_panier = False
                        for item in st.session_state.panier:
                            if item["produit"] == nom:
                                item["quantite"] += qte_ajout
                                deja_au_panier = True
                                break
                        
                        if not deja_au_panier:
                            st.session_state.panier.append({
                                "produit": nom,
                                "prix": description_prix,
                                "quantite": qte_ajout
                            })
                        st.toast(f"✅ {qte_ajout}x {nom} ajouté(s) au panier !")
# =====================================================
elif selected == "Commande":
    import urllib.parse
    from datetime import datetime, timedelta

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

        # Base de données géographique du Sénégal (14 Régions et leurs communes/localités majeures)
        geo_senegal = {
            "Dakar": ["Dakar Plateau", "Medina", "Grand Yoff", "Pikine", "Guediawaye", "Rufisque", "Diamniadio", "Parcelles Assainies", "Ngor", "Ouakam", "Mermoz", "Yoff"],
            "Thiès": ["Thiès Ville", "Mbour", "Saly", "Joal-Fadiouth", "Tivaouane", "Mboro", "Pout", "Khombole", "Popenguine"],
            "Diourbel": ["Diourbel Ville", "Touba Mosquée", "Mbacké", "Bambey"],
            "Saint-Louis": ["Saint-Louis Ville", "Richard-Toll", "Dagana", "Podor", "Ndioum", "Ross Béthio"],
            "Louga": ["Louga Ville", "Linguère", "Dahra", "Kebemer"],
            "Fatick": ["Fatick Ville", "Foundiougne", "Gossas", "Sokone", "Diofior"],
            "Kaolack": ["Kaolack Ville", "Nioro du Rip", "Guinguinéo", "Kahone"],
            "Kaffrine": ["Kaffrine Ville", "Koungheul", "Birkelane", "Malem Hodar"],
            "Tambacounda": ["Tambacounda Ville", "Bakel", "Goudiry", "Koumpentoum"],
            "Kolda": ["Kolda Ville", "Vélingara", "Medina Yoro Foulah"],
            "Ziguinchor": ["Ziguinchor Ville", "Bignona", "Oussouye", "Cap Skirring", "Kolda"],
            "Sédhiou": ["Sédhiou Ville", "Goudomp", "Bounkiling"],
            "Matam": ["Matam Ville", "Ourossogui", "Kanel", "Ranérou"],
            "Kedougou": ["Kédougou Ville", "Saraya", "Salemata"]
        }

        st.markdown("<h3 style='color: #2E7D32; margin-top: 30px;'>⚙️ Réseau Logistique National & Facturation</h3>", unsafe_allow_html=True)
        col_reg, col_com, col_promo = st.columns(3)
        
        with col_reg:
            region_selectionnee = st.selectbox("📍 Région du Sénégal *", list(geo_senegal.keys()))
            
        with col_com:
            commune_selectionnee = st.selectbox("🏙️ Commune / Localité *", geo_senegal[region_selectionnee])

        # Calcul dynamique des frais de transport et des délais selon la région choisie
        frais_livraison = 0
        delai_estime = ""

        if region_selectionnee == "Dakar":
            frais_livraison = 2500
            delai_estime = "⚡ Express : 24h chrono"
        elif region_selectionnee == "Thiès":
            frais_livraison = 3500
            delai_estime = "🚛 Rapide : 24h à 48h"
        elif region_selectionnee in ["Diourbel", "Fatick", "Kaolack", "Louga"]:
            frais_livraison = 4500
            delai_estime = "📦 48h à 72h maximum"
        else:
            # Régions périphériques et éloignées (Saint-Louis, Matam, Tamba, Casamance, Kédougou)
            frais_livraison = 6000
            delai_estime = "🗺️ Expédition Sud/Nord/Est : 72h à 96h (Via lignes partenaires)"

        with col_promo:
            code_promo = st.text_input("🎟️ Code Promo (Optionnel)", "").strip()
            remise = 0
            if code_promo.upper() == "YOU2026":
                remise = int(total_financier * 0.10)
                st.success("🎉 Code valide (-10%)")

        # Application de la tarification logistique finale
        total_final_net = total_financier + frais_livraison - remise
        points_gagnes = total_final_net // 1000

        # =====================================================================
        st.info(f"📍 Réseau d'acheminement : Région de {region_selectionnee} — Secteur {commune_selectionnee}\n\n⏱️ Délai logistique estimé : {delai_estime}")
        
        c_sub, c_liv, c_rem = st.columns(3)
        with c_sub:
            st.text(f"Sous-total : {total_financier:,} FCFA")
        with c_liv:
            st.text(f"Frais de transport : {frais_livraison:,} FCFA")
        with c_rem:
            if remise > 0:
                st.text(f"Réduction : -{remise:,} FCFA")
        
        st.metric(label="TOTAL NET À PAYER", value=f"{total_final_net:,} FCFA")
        st.success(f"🌱 Gain fidélité YouAgronoMe : +{points_gagnes} points sur cette commande.")
        #=====================================================================

        st.markdown("<h3 style='color: #2E7D32; margin-top: 30px;'>👤 Coordonnées du Destinataire & Planification</h3>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom complet *", placeholder="Ex: Issa Youme")
            telephone = st.text_input("Téléphone fonctionnel (WhatsApp de préférence) *", placeholder="Ex: 777473170")
            adresse = st.text_input("Complément d'adresse exacte *", placeholder="Rue, Quartier, Indications visuelles...")
        with col2:
            paiement = st.selectbox("Méthode de paiement", ["Présentiel", "Wave", "Orange Money"])
            
            # Calendrier de planification prenant en compte les délais minimums régionaux
            delai_jours = 1 if region_selectionnee == "Dakar" else (2 if region_selectionnee == "Thiès" else 3)
            date_min = datetime.now() + timedelta(days=delai_jours)
            date_livraison = st.date_input("Date de réception souhaitée", value=date_min, min_value=datetime.now())
            
            creneau_horaire = st.selectbox("Créneau horaire préféré", [
                "Matin (08h00 - 12h00)", 
                "Après-midi (13h00 - 17h00)", 
                "Fin de journée (17h00 - 20h00)"
            ])
            
        commentaire = st.text_area("Instructions spéciales pour le transporteur", placeholder="Ex: Livrer à la gare routière, appeler mon correspondant sur place, etc...")

        if paiement in ["Wave", "Orange Money"]:
            st.warning(f"💳 Moyen de Paiement Électronique Sélectionné : Merci d'exécuter votre transfert au **+221 77 747 31 70** dès soumission du formulaire.")

        with st.expander("📄 Bordereau de chargement numérique", expanded=False):
            for p in panier:
                st.write(f"• {p['produit']} x{p['quantite']} — ({p['prix']})")

        # Soumission globale
        if st.button("🚀 Soumettre ma commande globale", use_container_width=True, type="primary"):
            if not nom or not telephone or not adresse:
                st.error("⚠️ Erreur : Tous les champs munis d'un astérisque (*) sont obligatoires.")
            else:
                texte_produits = ""
                for p in panier:
                    texte_produits += f"• {p['produit']} x {p['quantite']} ({p['prix']})\n"

                # Payload textuel pour WhatsApp et Emails professionnels
                message = f"""🌾 NOUVELLE COMMANDE - YOUAGRONOME\n\n👤 CLIENT :\n• Nom : {nom}\n• Tél : {telephone}\n• Région : {region_selectionnee}\n• Commune : {commune_selectionnee}\n• Adresse : {adresse}\n\n📅 PROGRAMMATION LOGISTIQUE :\n• Date estimée : {date_livraison.strftime('%d/%m/%Y')}\n• Période : {creneau_horaire}\n\n📦 DETAIL DES ARTICLES :\n{texte_produits}\n💰 SOUS-TOTAL : {total_financier:,} FCFA\n🚚 LOGISTIQUE REGIONALE : {frais_livraison:,} FCFA\n📉 REMISE APPLIQUEE : {remise:,} FCFA\n💵 TOTAL NET GLOBAL : {total_final_net:,} FCFA\n\n⚙️ MODALITES :\n• Paiement : {paiement}\n• Note client : {commentaire if commentaire else 'Aucune description'}"""

                # Facture HTML Pro pour impression locale ou sauvegarde
                html_facture = f"""
                <div style="font-family: Arial, sans-serif; padding: 25px; border: 1px solid #ccffcc; max-width: 550px; border-radius: 12px; background-color: #ffffff; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    <h2 style="color: #1B5E20; text-align: center; margin-bottom: 0; font-weight: 800; letter-spacing: 1px;">YOUAGRONOME SÉNÉGAL</h2>
                    <p style="text-align: center; font-size: 12px; color: #777; margin-top: 5px;">Réseau National de Distribution Agro-alimentaire</p>
                    <hr style="border: 0.5px solid #e2e8f0; margin: 15px 0;">
                    <p style="font-size: 13px; line-height: 1.6; color: #2d3748;">
                        <b>Bénéficiaire :</b> {nom}<br>
                        <b>Téléphone :</b> {telephone}<br>
                        <b>Destination :</b> Région {region_selectionnee} — {commune_selectionnee}<br>
                        <b>Adresse de livraison :</b> {adresse}<br>
                        <b>Date programmée :</b> {date_livraison.strftime('%d/%m/%Y')} ({creneau_horaire})
                    </p>
                    <hr style="border: 0.5px solid #e2e8f0; margin: 15px 0;">
                    <h4 style="color: #2E7D32; margin-bottom: 10px;">Éléments de la Commande :</h4>
                    <p style="font-size: 13px; color: #4a5568; line-height: 1.6; background-color: #f7fafc; padding: 10px; border-radius: 6px;">{texte_produits.replace('\n', '<br>')}</p>
                    <hr style="border: 0.5px dashed #cbd5e0; margin: 15px 0;">
                    <table style="width: 100%; font-size: 14px; color: #4a5568; line-height: 2;">
                        <tr><td>Cumul Marchandise :</td><td style="text-align: right; font-weight: 600;">{total_financier:,} FCFA</td></tr>
                        <tr><td>Frais logistiques ({region_selectionnee}) :</td><td style="text-align: right; font-weight: 600;">{frais_livraison:,} FCFA</td></tr>
                        <tr style="color: #c53030;"><td>Déduction commerciale :</td><td style="text-align: right; font-weight: 600;">-{remise:,} FCFA</td></tr>
                        <tr style="font-size: 18px; font-weight: 800; color: #1B5E20;">
                            <td style="padding-top: 12px; border-top: 1px solid #edf2f7;">Total Net À Payer :</td>
                            <td style="text-align: right; padding-top: 12px; border-top: 1px solid #edf2f7;">{total_final_net:,} FCFA</td>
                        </tr>
                    </table>
                    <p style="font-size: 11px; text-align: center; color: #a0aec0; margin-top: 30px; font-style: italic; border-top: 1px solid #edf2f7; padding-top: 10px;">Merci pour votre commande. Service Client National YouAgronoMe.</p>
                </div>
                """

                whatsapp_link = "https://wa.me/" + NUMERO_WHATSAPP + "?text=" + urllib.parse.quote(message)
                email_link = f"mailto:{EMAIL_DEST}?subject=Commande Nationale YouAgronoMe - {nom}&body=" + urllib.parse.quote(message)

                # Sauvegarde au sein de la session utilisateur
                st.session_state.historique.append({
                    "client": nom,
                    "paiement": paiement,
                    "total": f"{total_final_net:,} FCFA",
                    "commande": panier.copy(),
                    "brut_texte": message,
                    "html_facture": html_facture
                })

                st.success("🎉 Votre bon de commande national a été généré avec succès !")
                c1, c2 = st.columns(2)
                with c1:
                    st.link_button("📱 Finaliser via WhatsApp", whatsapp_link, use_container_width=True)
                with c2:
                    st.link_button("📧 Archiver par Email", email_link, use_container_width=True)

        st.markdown("<br><hr>", unsafe_allow_html=True)
        if st.button("🧹 Vider entièrement le panier", use_container_width=True):
            st.session_state.panier = []
            st.rerun()

    # Section Historique et Téléchargements des Factures Officiels
    st.markdown("<h3 style='color: #4a5568; margin-top: 40px;'>📜 Vos Transactions Récentes</h3>", unsafe_allow_html=True)
    historique = st.session_state.historique

    if not historique:
        st.info("Aucune transaction enregistrée au cours de cette session active.")
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
                
                # Configuration des deux boutons de téléchargement côte à côte
                btn_txt, btn_html = st.columns(2)
                
                with btn_txt:
                    st.download_button(
                        label="📥 Télécharger le Reçu (TXT)",
                        data=cmd.get("brut_texte", "Aucune donnée"),
                        file_name=f"recu_youagronome_{idx}.txt",
                        mime="text/plain",
                        key=f"dl_txt_{idx}",
                        use_container_width=True
                    )
                
                with btn_html:
                    st.download_button(
                        label="🖨️ Télécharger la Facture (HTML Officiel)",
                        data=cmd.get("html_facture", "Aucune donnée"),
                        file_name=f"facture_youagronome_{idx}.html",
                        mime="text/html",
                        key=f"dl_html_{idx}",
                        use_container_width=True
                    )
# =====================================================

# =====================================================
# REALISATIONS (VERSION INTERACTIVE ET STRATÉGIQUE)
# =====================================================
elif selected == "Réalisations":
    
    # =========================
    # 1. STYLE CSS COMPLÉMENTAIRE
    # =========================
    st.markdown("""
    <style>
    /* Cartes de projets épurées */
    .project-card {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.02);
        margin-bottom: 20px;
    }
    .project-title {
        color: #1b5e20;
        font-weight: 700;
        font-size: 1.3rem;
        margin-bottom: 8px;
    }
    .project-badge {
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 15px;
    }
    /* Témoignage stylisé */
    .testimonial-bubble {
        background-color: #f9fbe7;
        border-left: 5px solid #c0ca33;
        padding: 15px 20px;
        border-radius: 0 15px 15px 0;
        margin-top: 15px;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # 2. EN-TÊTE
    # =========================
    st.title("🌱 Nos Réalisations & Impacts")
    st.markdown(
        "Explorez la manière dont YouAgronoMe transforme l'agriculture sénégalaise "
        "grâce à la data, une logistique optimisée et des partenariats durables."
    )
    st.write("---")

    # =========================
    # 3. PANORAMA DES CHIFFRES CLÉS (METRICS NATIVES)
    # =========================
    st.subheader("📊 Notre Impact Global en Chiffres")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="🌾 Terres Accompagnées", value="1 250 Ha", delta="+15% vs 2025")
    with col2:
        st.metric(label="👥 Producteurs Partenaires", value="450+", delta="+42 nouveaux")
    with col3:
        st.metric(label="🍎 Tonnes Distribuées", value="3 800 T", delta="+12% cette année")
    with col4:
        st.metric(label="⭐ Satisfaction globale", value="98.4%", delta="+0.4%")

    st.write("---")

    # =========================
    # 4. PORTFOLIO INTERACTIF (NOUVELLE FONCTIONNALITÉ)
    # =========================
    st.subheader("📂 Découvrez nos Projets Majeurs")
    
    # Utilisation de pills/segmented_control pour filtrer les projets en un clic
    domaine = st.pills(
        "Sélectionnez un domaine d'impact :",
        options=["🌾 Agroécologie & Production", "🚚 Supply Chain & Logistique", "💻 Agritech & Données"],
        default="🌾 Agroécologie & Production"
    )

    if domaine == "🌾 Agroécologie & Production":
        c_left, c_right = st.columns([1, 2])
        with c_left:
            st.image("https://images.unsplash.com/photo-1592982537447-7440770cbfc9?auto=format&fit=crop&w=600&q=80", caption="Irrigation intelligente")
        with c_right:
            st.markdown("""
            <div class="project-card">
                <span class="project-badge">SAINT-LOUIS</span>
                <div class="project-title">Optimisation Hydrique & Goutte-à-Goutte</div>
                <p>Déploiement de systèmes d'irrigation connectés de précision sur 150 hectares de cultures maraîchères dans la vallée du fleuve Sénégal.</p>
                <ul>
                    <li><b>Résultat :</b> Réduction de 30% de la consommation d'eau.</li>
                    <li><b>Rendement :</b> Augmentation de +18% sur les récoltes de tomates et d'oignons.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif domaine == "🚚 Supply Chain & Logistique":
        c_left, c_right = st.columns([1, 2])
        with c_left:
            st.image("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=600&q=80", caption="Logistique optimisée")
        with c_right:
            st.markdown("""
            <div class="project-card">
                <span class="project-badge">DAKAR & FLOUVE</span>
                <div class="project-title">Le Corridor Express Fraîcheur</div>
                <p>Mise en place d'une chaîne logistique réfrigérée reliant directement les groupements de producteurs de Saint-Louis aux marchés de gros de Dakar.</p>
                <ul>
                    <li><b>Zéro Gaspillage :</b> Division par 4 des pertes post-récolte (de 25% à moins de 6%).</li>
                    <li><b>Rapidité :</b> Transport sécurisé en moins de 6 heures.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif domaine == "💻 Agritech & Données":
        c_left, c_right = st.columns([1, 2])
        with c_left:
            st.image("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=80", caption="Technologie agricole")
        with c_right:
            st.markdown("""
            <div class="project-card">
                <span class="project-badge">TOUT LE SÉNÉGAL</span>
                <div class="project-title">Plateforme Prédictive YouAgri</div>
                <p>Application de suivi et d'aide à la décision basée sur les données météo et l'analyse des sols pour planifier les périodes optimales de semis.</p>
                <ul>
                    <li><b>Adoption :</b> Plus de 300 alertes SMS personnalisées envoyées chaque semaine aux agriculteurs.</li>
                    <li><b>Efficacité :</b> Amélioration de 15% de la qualité des intrants utilisés.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    st.write("---")

    # =========================
    # 5. SIMULATEUR D'IMPACT (INTERACTIF POUR ENGAGER L'UTILISATEUR)
    # =========================
    st.subheader("🧮 Simulez votre impact potentiel avec YouAgronoMe")
    st.info("Ajustez les paramètres ci-dessous pour découvrir l'impact estimé de nos solutions sur votre exploitation.")
    
    col_sim1, col_sim2 = st.columns(2)
    with col_sim1:
        surface = st.slider("Quelle est la surface de votre exploitation (en Hectares) ?", 1, 100, 10)
        culture = st.selectbox("Type de culture principale :", ["Tomates", "Oignons", "Riz", "Gombo / Autres maraîchers"])
    
    with col_sim2:
        # Calculs fictifs cohérents avec nos chiffres
        eau_economisee = surface * 350 # m3 estimés par Ha
        gain_financier = surface * 245000 # FCFA estimés par Ha
        
        st.markdown(f"""
        <div style="background-color: #f1f8e9; padding: 20px; border-radius: 12px; border: 1px solid #c8e6c9;">
            <h4 style="color: #2e7d32; margin-top:0;">💡 Estimations d'impact pour {surface} Ha de {culture} :</h4>
            <p>💧 <b>Économie d'eau potentielle :</b> {eau_economisee:,} m³/an</p>
            <p>📈 <b>Gain de productivité net estimé :</b> +18% à +22%</p>
            <p>💵 <b>Augmentation moyenne des revenus :</b> ~ {gain_financier:,} FCFA / an</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # =========================
    # 6. TÉMOIGNAGES FILTRABLES (NOUVELLE FONCTIONNALITÉ)
    # =========================
    st.subheader("🗣️ Parole à l'Écosystème")
    
    profil_selectionne = st.radio(
        "Filtrer les témoignages par profil :",
        ["Tous", "👩‍🌾 Producteurs", "🏢 Clients / Acheteurs"],
        horizontal=True
    )

    temoignages_data = [
        {"nom": "Awa Ndiaye", "role": "Producteurs", "desc": "Productrice à Saint-Louis", "texte": "Grâce aux débouchés de YouAgronoMe, mes produits frais trouvent preneur en un temps record. La chaîne de distribution est ultra performante et transparente."},
        {"nom": "Khady Diop", "role": "Producteurs", "desc": "Maraîchère Émérite", "texte": "L'interface simplifie absolument tout le parcours. En quelques clics, l'ensemble de ma récolte est planifié, sécurisé et vendu efficacement."},
        {"nom": "Aissatou Diallo", "role": "Clients / Acheteurs", "desc": "Responsable Centrale d'Achat", "texte": "Une régularité de qualité impressionnante et des grilles de prix très compétitives par rapport au marché classique. Nous sécurisons nos approvisionnements à long terme."},
        {"nom": "Fatou Sow", "role": "Clients / Acheteurs", "desc": "Grossiste alimentaire", "texte": "Un service professionnel, rigoureux et surtout d'une fiabilité remarquable. C'est le partenaire stratégique idéal pour gérer la fluidité de nos stocks."}
    ]

    # Filtrage de la liste
    temoignages_filtres = [
        t for t in temoignages_data 
        if profil_selectionne == "Tous" or t["role"] in profil_selectionne
    ]

    # Affichage dynamique sur deux colonnes
    t_cols = st.columns(2)
    for index, t in enumerate(temoignages_filtres):
        with t_cols[index % 2]:
            st.markdown(f"""
            <div class="project-card">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div style="width: 45px; height: 45px; border-radius: 50%; background-color:#2e7d32; color:white; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:1.2rem;">
                        {t['nom'][0]}
                    </div>
                    <div>
                        <strong style="color: #1b5e20; font-size:1.1rem;">{t['nom']}</strong><br>
                        <small style="color: #666;">{t['desc']}</small>
                    </div>
                </div>
                <div class="testimonial-bubble">
                    "{t['texte']}"
                </div>
            </div>
            """, unsafe_allow_html=True)
# CONTACT
# =====================================================
import streamlit as st

def html_block(code):
    st.markdown(code, unsafe_allow_html=True)

if selected == "Contact":

    # ================= HEADER =================
    html_block("""
    <div style="text-align:center; margin-bottom: 20px;">
        <h1>🤝 Contactez YouAgronoMe</h1>
        <p>Une question, un partenariat ou besoin d'assistance ? Notre équipe vous répond.</p>
    </div>
    """)

    # ================= NOUVELLE FONCTIONNALITÉ : CHIFFRES CLÉS & INFOS =================
    # Utilisation des composants natifs Streamlit pour un rendu propre et moderne
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="📞 Téléphone", value="777473170")
    with c2:
        st.metric(label="📍 Bureau Principal", value="Saint-Louis")
    with c3:
        st.metric(label="⏱ Temps de réponse", value="< 24h")

    st.write("---")

    # ================= COLUMNS (FORMULAIRE & FAQ) =================
    col_form, col_FAQ = st.columns([3, 2])

    with col_form:
        st.subheader("📩 Envoyez-nous un message")
        
        # Formulaire amélioré avec de nouvelles fonctionnalités
        with st.form("contact_form", clear_on_submit=True):
            nom = st.text_input("Votre Nom complet *")
            email = st.text_input("Votre Adresse Email *")
            
            # Nouvelle fonctionnalité : Cibler le bon département
            departement = st.selectbox(
                "À quel département s'adresse votre message ?",
                ["🤝 Partenariats & Investissements", "🎓 Opérations & Formations", "🚜 Support Commercial", "❓ Autre demande"]
            )
            
            msg = st.text_area("Votre Message *", placeholder="Écrivez votre message ici...")

            submit_button = st.form_submit_button("Envoyer le message")

            # Nouvelle fonctionnalité : Validation des champs obligatoire
            if submit_button:
                if not nom or not email or not msg:
                    st.error("Veuillez remplir tous les champs obligatoires (marqués par un *).")
                elif "@" not in email:
                    st.error("Veuillez entrer une adresse email valide.")
                else:
                    # Ici, vous pourrez ajouter votre logique d'envoi d'email ou de stockage en base de données
                    st.success(f"Merci {nom} ! Votre message a bien été transmis au département **{departement}**. Nous vous recontacterons à l'adresse {email}.")

    with col_FAQ:
        st.subheader("💡 Informations utiles")
        
        # Nouvelle fonctionnalité : FAQ interactive pour désengorger le support
        with st.expander("💼 Vous êtes un potentiel partenaire ?"):
            st.write("""
            Sélectionnez le département **Partenariats** dans le formulaire. 
            Notre équipe dédiée aux alliances stratégiques vous répondra sous 48 heures ouvrées.
            """)
            
        with st.expander("🚜 Support technique & Commercial"):
            st.write("""
            Pour toute urgence liée à vos commandes ou au déploiement sur le terrain à Saint-Louis, 
            privilégiez l'appel direct au **+221 777473170** du lundi au vendredi (8h - 17h).
            """)
            
        # Rappel de l'email direct en dehors du formulaire
        st.info("✉️ **Email direct :** issayoume2012@gmail.com")
