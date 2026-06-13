
# CONSEILimport streamlit as st
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
    "💡 Conseils", 
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
    
    recherche = st.text_input("🔍 Rechercher un produit...", "")
    st.divider()

    produits = [
        ("to.jpg", "Tomates", "3500 FCFA par sac de 5Kg"),
        ("fr.jpg", "Fraises", "5000 FCFA par sachet de 2Kg"),
        ("og.jpg", "Oignons", "2500 FCFA par sac de 5Kg"),
        ("cr.jpg", "Carottes", "3000 FCFA par sac de 5Kg"),
        ("pm.jpg", "Piments", "2000 FCFA par sac de 3Kg"),
        ("cc.jpg", "Concombres", "2800 FCFA par sac de 3Kg"),
        ("pt.jpg", "Pommes de terre", "4500 FCFA par sachet de 5Kg"),
        ("or.jpg", "Oranges", "4000 FCFA par sac de 3Kg"),
        ("mangue.jpg", "Mangues", "3500 FCFA par panier de 5Kg"),
        ("banane.jpg", "Bananes", "2500 FCFA par régime"),
        ("mais.jpg", "Maïs", "7000 FCFA par sac de 25Kg"),
        ("arachide.jpg", "Arachides", "8500 FCFA par sac de 10Kg"),
        ("riz.jpg", "Riz local", "12000 FCFA par sac de 25Kg"),
        ("mil.jpg", "Mil", "9000 FCFA par sac de 20Kg"),
        ("pasteque.jpg", "Pastèques", "6000 FCFA l’unité"),
        ("citron.jpg", "Citrons", "2000 FCFA par filet"),
        ("niebe.jpg", "Niébé", "6500 FCFA par sac de 10Kg"),
        ("gombo.jpg", "Gombos", "2200 FCFA par panier"),
        ("bissap.jpg", "Bissap", "3000 FCFA par sachet de 2Kg"),
        ("sesame.jpg", "Sésame", "7500 FCFA par sac de 10Kg")
    ]

    produits_filtres = [p for p in produits if recherche.lower() in p[1].lower()]

    if not produits_filtres:
        st.warning("Aucun produit ne correspond à votre recherche.")
    else:
        cols = st.columns(4)
        for i, p in enumerate(produits_filtres):
            image, nom, description_prix = p
            
            with cols[i % 4]:
                with st.container(border=True):
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

        # On utilise une boucle standard pour éviter les problèmes d'index avec pop()
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

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f8f9fa, #e8f5e9); padding: 20px; border-radius: 12px; margin: 20px 0; border-left: 6px solid #2E7D32;">
            <h4 style="margin: 0; color: #4a5568;">Total global ({total_articles} articles)</h4>
            <h2 style="margin: 5px 0 0 0; color: #1B5E20; font-weight: 800;">{total_financier:,} FCFA</h2>
            <p style="margin: 0; font-size: 12px; color: #718096;">* Hors frais de livraison / transport</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<h3 style='color: #2E7D32; margin-top: 30px;'>👤 Coordonnées & Livraison</h3>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom complet *", placeholder="Ex: Issa Youme")
            telephone = st.text_input("Téléphone *", placeholder="Ex: 777473170")
            adresse = st.text_input("Adresse de livraison exacte *", placeholder="Quartier, Rue, Ville...")
        with col2:
            paiement = st.selectbox("Méthode de paiement", ["Présentiel", "Wave", "Orange Money"])
            commentaire = st.text_area("Instructions spéciales", placeholder="Ex: Entrée en face de la mosquée, livrer avant midi...")

        if paiement in ["Wave", "Orange Money"]:
            st.warning(f"💳 Service de transfert mobile actif : Merci d'effectuer le paiement au **+221 77 747 31 70** après envoi du formulaire.")

        with st.expander("📄 Bordereau numérique de commande", expanded=False):
            for p in panier:
                st.write(f"• {p['produit']} x{p['quantite']} — ({p['prix']})")

        if st.button("🚀 Soumettre ma commande globale", use_container_width=True, type="primary"):
            if not nom or not telephone or not adresse:
                st.error("⚠️ Tous les champs obligatoires (*) doivent être remplis.")
            else:
                texte_produits = ""
                for p in panier:
                    texte_produits += f"• {p['produit']} x {p['quantite']} ({p['prix']})\n"

                message = f"""🌾 NOUVELLE COMMANDE - YOUAGRONOME\n\n👤 CLIENT :\n• Nom : {nom}\n• Tél : {telephone}\n• Adresse : {adresse}\n\n📦 ARTICLES COMMANDÉS :\n{texte_produits}\n💰 TOTAL ESTIMÉ : {total_financier:,} FCFA\n\n⚙️ LOGISTIQUE :\n• Paiement : {paiement}\n• Note : {commentaire if commentaire else 'Aucune description'}"""

                whatsapp_link = "https://wa.me/" + NUMERO_WHATSAPP + "?text=" + urllib.parse.quote(message)
                email_link = f"mailto:{EMAIL_DEST}?subject=Commande Pro YouAgronoMe&body=" + urllib.parse.quote(message)

                st.session_state.historique.append({
                    "client": nom,
                    "paiement": paiement,
                    "total": f"{total_financier:,} FCFA",
                    "commande": panier.copy()
                })

                st.success("🎉 Votre bon de commande a été généré avec succès !")
                c1, c2 = st.columns(2)
                with c1:
                    st.link_button("📱 Finaliser sur WhatsApp", whatsapp_link, use_container_width=True)
                with c2:
                    st.link_button("📧 Archiver par Email", email_link, use_container_width=True)

        st.markdown("<br><hr>", unsafe_allow_html=True)
        if st.button("🧹 Vider entièrement le panier", use_container_width=True):
            st.session_state.panier = []
            st.rerun()

    st.markdown("<h3 style='color: #4a5568; margin-top: 40px;'>📜 Vos Transactions Récentes</h3>", unsafe_allow_html=True)
    historique = st.session_state.historique

    if not historique:
        st.info("Aucune commande dans votre session courante.")
    else:
        for idx, cmd in enumerate(reversed(historique), start=1):
            with st.expander(f"📦 Reçu de Commande #{idx} — {cmd['client']} ({cmd['total']})"):
                st.markdown(f"**Mode de Règlement :** `{cmd['paiement']}`")
                for p in cmd["commande"]:
                    st.write(f"• {p['produit']} (x{p['quantite']})")
 XXL 🌍
# =====================================================
elif selected == "Conseils":

    # =====================================================
    # ENGINE STYLING PREMIUM (CSS ADVANCED)
    # =====================================================
    st.markdown("""
    <style>
    /* Hero Banner XXL */
    .conseil-hero {
        padding: 65px 40px;
        border-radius: 24px;
        text-align: center;
        color: white;
        background: linear-gradient(135deg, rgba(27, 94, 32, 0.9), rgba(1, 87, 155, 0.75)), 
                    url('https://images.unsplash.com/photo-1464226184884-fa280b87c399');
        background-size: cover;
        background-position: center;
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(27, 94, 32, 0.2);
    }
    .conseil-hero h1 {
        font-size: 42px !important;
        font-weight: 900 !important;
        margin-bottom: 12px !important;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
    }
    .conseil-hero p {
        font-size: 18px !important;
        opacity: 0.95;
        max-width: 700px;
        margin: 0 auto !important;
    }

    /* Cartes XXL Premium */
    .conseil-card {
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid #e2e8f0;
        padding: 30px 24px;
        border-radius: 20px;
        min-height: 310px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.04);
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        margin-bottom: 20px;
    }
    .conseil-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 35px rgba(27, 94, 32, 0.12);
        border-color: #2E7D32;
    }
    .conseil-icon {
        font-size: 55px;
        line-height: 1;
        margin-bottom: 15px;
        filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));
    }
    .conseil-title {
        color: #1A202C;
        font-size: 22px;
        font-weight: 800;
        margin: 0 0 15px 0;
        border-bottom: 2px solid #e8f5e9;
        padding-bottom: 8px;
    }
    .conseil-item {
        font-size: 14px;
        color: #4A5568;
        margin: 8px 0 !important;
        display: flex;
        align-items: center;
        font-weight: 500;
    }

    /* Stylisation des expanders natifs sous les cartes */
    .stExpander {
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02) !important;
        background: #fafafa !important;
        margin-bottom: 25px;
    }
    
    /* Citation Callout */
    .quote-box {
        background: #f0f7f4;
        border-left: 5px solid #2E7D32;
        padding: 20px;
        border-radius: 4px 16px 16px 4px;
        margin: 30px 0;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

    # HERO BANNER XXL
    st.markdown("""
    <div class="conseil-hero">
        <h1>🌾 Hub de Performance Agronomique</h1>
        <p>Optimisez vos structures d'exploitation, accélérez vos rendements et basculez vers une agriculture de précision moderne.</p>
    </div>
    """, unsafe_allow_html=True)

    # DATASET COMPLET & AMÉLIORÉ
    conseils = [
        (
            "💧", "Irrigation Intelligente",
            ["Arroser aux heures stratégiques", "Déployer le goutte-à-goutte", "Piloter via capteurs d'humidité", "Réduire le taux d'évaporation"],
            "**Focus Technique :** L'apport hydrique optimal se situe avant 7h ou après 18h. Le goutte-à-goutte permet d'économiser jusqu'à 45% de ressources en eau tout en ciblant directement l'appareil racinaire."
        ),
        (
            "🌱", "Fertilisation Équilibrée",
            ["Privilégier l'amendement organique", "Fractionner les apports nutritifs", "Analyser le profil de sol (N-P-K)", "Éviter la saturation chimique"],
            "**Focus Technique :** Le compost mûr améliore la structure globale du sol. Avant tout apport d'engrais, effectuez un test de pH pour maximiser l'assimilation des nutriments par la plante."
        ),
        (
            "🐛", "Protection Phytosanitaire",
            ["Mettre en place un diagnostic précoce", "Formuler des biopesticides locaux", "Appliquer la rotation des cultures", "Isoler immédiatement les foyers"],
            "**Focus Technique :** Utilisez des solutions à base de neem ou de piment pour repousser les nuisibles naturellement. Alterner les familles de cultures casse le cycle de reproduction des bio-agresseurs."
        ),
        (
            "🌾", "Conduite de Culture",
            ["Sélectionner des semences certifiées", "Respecter les densités de semis", "Exécuter des sarclages rigoureux", "Planifier les fenêtres de récolte"],
            "**Focus Technique :** Un espacement précis garantit à chaque plant un accès parfait à la lumière et aux nutriments. Le désherbage des 30 premiers jours est crucial pour éviter la concurrence."
        ),
        (
            "🌍", "Agroécologie & Durabilité",
            ["Régénérer le tissu microbien", "Pratiquer le paillage systématique", "Valoriser la biomasse résiduelle", "Soutenir les écosystèmes utiles"],
            "**Focus Technique :** Le paillage conserve l'humidité, empêche la pousse des herbes adventices et nourrit la faune du sol en se décomposant. C'est le pilier de l'agriculture de conservation."
        ),
        (
            "📈", "Business & Stratégie",
            ["Analyser les courbes des marchés", "Standardiser la qualité produit", "Créer des circuits courts de vente", "Intégrer les outils de suivi"],
            "**Focus Technique :** Suivez les fluctuations de prix sur les marchés locaux avant la récolte pour négocier efficacement. Le tri et le calibrage rigoureux augmentent la valeur perçue de 25%."
        )
    ]

    # AFFICHAGE DE LA GRILLE DE CARTES (3 Colonnes)
    cols = st.columns(3)

    for i, (icon, titre, points, detail) in enumerate(conseils):
        with cols[i % 3]:
            # Rendu HTML de la carte supérieure
            lignes_html = "".join([f'<div class="conseil-item">✅ {p}</div>' for p in points])
            st.markdown(f"""
            <div class="conseil-card">
                <div class="conseil-icon">{icon}</div>
                <h3 class="conseil-title">{titre}</h3>
                <div>{lignes_html}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Module Streamlit dépliable intégré directement sous la carte correspondante
            with st.expander("🔍 Voir protocole complet"):
                st.markdown(detail)

    # =====================================================
    # OUTILS SECTORIELS XXL ADJACENTS
    # =====================================================
    st.markdown("---")
    
    # =====================================================
    # OUTILS SECTORIELS XXL ADJACENTS (PILOTAGE & CONTACT)
    # =====================================================
    st.markdown("---")
    
    c_gauche, c_droite = st.columns([5, 5])
    
    with c_gauche:
        st.markdown("<h3 style='color: #1B5E20; margin-top:0;'>🎯 Recommandation Stratégique</h3>", unsafe_allow_html=True)
        st.info("""
        **Loi de l'optimum :** Pour maximiser vos rendements de manière exponentielle, n'isolez jamais vos actions. 
        Le succès réside dans le triptyque : **Semence certifiée + Gestion hydrique localisée + Suivi nutritionnel organique rigoureux.**
        """)
        
        st.markdown("""
        <div class="quote-box">
            "Le sol n'est pas une simple surface de dépôt, c'est un organisme vivant qu'il faut nourrir pour qu'il nous nourrisse en retour."
        </div>
        """, unsafe_allow_html=True)

    with c_droite:
        st.markdown("<h3 style='color: #01579B; margin-top:0;'>🧮 Simulateur de Rendement & Irrigation Pro</h3>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("<p style='font-weight:600; margin-bottom:10px;'>Sélectionnez vos paramètres de parcelle :</p>", unsafe_allow_html=True)
            
            # Base de données agronomique interne pour affiner les calculs
            data_cultures = {
                "Tomates 🍅": {"besoin_eau": 6, "rendement_m2": 4.5},
                "Oignons 🧅": {"besoin_eau": 5, "rendement_m2": 3.8},
                "Fraises 🍓": {"besoin_eau": 4, "rendement_m2": 2.5},
                "Carottes 🥕": {"besoin_eau": 4.5, "rendement_m2": 4.0},
                "Pommes de terre 🥔": {"besoin_eau": 5.5, "rendement_m2": 3.5},
                "Riz / Maïs 🌾": {"besoin_eau": 8, "rendement_m2": 1.2}
            }
            
            culture_choisie = st.selectbox("Type de culture cible", list(data_cultures.keys()))
            surface = st.number_input("Surface totale d'exploitation (en $m^2$)", min_value=10, max_value=500000, value=500, step=50)
            
            # Extraction des constantes agronomiques
            besoin_unitaire = data_cultures[culture_choisie]["besoin_eau"]
            rendement_unitaire = data_cultures[culture_choisie]["rendement_m2"]
            
            # Calculs algorithmiques
            besoin_eau_total = surface * besoin_unitaire
            rendement_estime_kg = surface * rendement_unitaire
            
            # Affichage des métriques de précision
            m1, m2 = st.columns(2)
            with m1:
                st.metric(
                    label="Volume d'eau requis / jour", 
                    value=f"{besoin_eau_total:,} Litres", 
                    delta=f"{besoin_unitaire} L / $m^2$"
                )
            with m2:
                if rendement_estime_kg >= 1000:
                    rendement_propre = f"{rendement_estime_kg/1000:.2f} Tonnes"
                else:
                    rendement_propre = f"{rendement_estime_kg:,} Kg"
                    
                st.metric(
                    label="Rendement moyen estimé", 
                    value=rendement_propre,
                    delta="Objectif optimal"
                )
            
            st.caption(f"ℹ️ Paramétrage optimisé pour la culture de type **{culture_choisie}** en zone maraîchère sahélienne.")

    # =====================================================
    # BANDEAU XXL : CELLULE CONSEIL ET SUIVI YAM
    # =====================================================
    st.markdown("<br>", unsafe_allow_html=True)
    
    EMAIL_CONSEIL = "ConseilSuiviYAM@gmail.com"
    sujet_mail = "Demande d'accompagnement et de suivi de parcelle - YouAgronoMe"
    corps_mail = f"Bonjour la cellule Conseil & Suivi YAM,\n\nJe souhaiterais obtenir un suivi personnalisé pour ma culture de {culture_choisie} sur une surface de {surface} m2.\n\nMerci de me recontactez."
    
    import urllib.parse
    mail_link = f"mailto:{EMAIL_CONSEIL}?subject={urllib.parse.quote(sujet_mail)}&body={urllib.parse.quote(corps_mail)}"
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #111827, #1f2937); border-radius: 20px; padding: 35px; color: white; margin-top: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.15); border: 1px solid #374151;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
            <div style="flex: 1; min-width: 300px;">
                <span style="background: #2E7D32; color: white; padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">Expertise Technique</span>
                <h3 style="margin: 10px 0 6px 0; color: white; font-weight: 800; font-size: 24px;">Cellule Conseil & Suivi YAM</h3>
                <p style="margin: 0; color: #9ca3af; font-size: 15px;">Besoin d'analyses de sol approfondies, de plans de fertilisation sur-mesure ou d'un suivi agronomique complet par nos ingénieurs ?</p>
                <p style="margin: 5px 0 0 0; color: #34d399; font-weight: 600; font-size: 14px;">📧 Contact direct : {EMAIL_CONSEIL}</p>
            </div>
            <div style="min-width: 220px; text-align: right;">
                <a href="{mail_link}" style="text-decoration: none;">
                    <button style="background: #2E7D32; color: white; border: none; padding: 14px 28px; font-size: 15px; font-weight: 700; border-radius: 12px; cursor: pointer; width: 100%; transition: background 0.2s;">
                        🚀 Contacter la Cellule
                    </button>
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
# =====================================================
# =====================================================
# REALISATIONS (VERSION ULTIME MONDIALE XXXL)
# =====================================================
elif selected == "Réalisations":
    # =========================
    # 1. DESIGN & CSS CORPORATE ULTRA-PREMIUM
    # =========================
    st.markdown("""
    <style>
    /* ---- CONFIGURATION DE PAGE / TEXTES ---- */
    .hero-title {
        font-size: 3.8rem !important;
        font-weight: 900 !important;
        color: #1b5e20;
        line-height: 1.1;
        margin-bottom: 20px;
        letter-spacing: -2px;
    }
    
    .hero-subtitle {
        font-size: 1.4rem !important;
        color: #4e5d4e;
        max-width: 950px;
        line-height: 1.7;
        margin-bottom: 60px;
    }

    .section-headline {
        font-size: 2.4rem !important;
        font-weight: 800 !important;
        color: #2e7d32;
        margin-top: 60px;
        margin-bottom: 40px;
        position: relative;
        padding-bottom: 15px;
        letter-spacing: -0.5px;
    }
    
    .section-headline::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 80px;
        height: 5px;
        background-color: #ffb300;
        border-radius: 3px;
    }

    /* ---- GRID KPI PREMIUM (STRIP-DOWN TO 1 FOCUS) ---- */
    .kpi-global-container {
        display: flex;
        justify-content: center;
        width: 100%;
        margin-bottom: 60px;
    }

    .kpi-premium-box {
        width: 100%;
        max-width: 500px;
        background: linear-gradient(135deg, #ffffff, #f4f9f4);
        border: 1px solid #e0ebd3;
        border-radius: 24px;
        padding: 45px 30px;
        text-align: center;
        border-bottom: 8px solid #2e7d32;
        box-shadow: 0 20px 45px rgba(46, 125, 50, 0.06);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    }

    .kpi-premium-box:hover {
        transform: translateY(-10px);
        box-shadow: 0 30px 60px rgba(46, 125, 50, 0.15);
        border-color: #ffb300;
    }

    .kpi-premium-val {
        font-size: 5rem !important; /* Taille XXXL pour un impact maximal */
        font-weight: 950 !important;
        color: #1b5e20;
        margin: 0;
        line-height: 1;
        white-space: nowrap;
        letter-spacing: -2px;
    }

    .kpi-premium-lbl {
        font-size: 1.1rem !important;
        font-weight: 800;
        color: #43a047;
        margin-top: 20px !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* ---- CARDS TEMOIGNAGES INTERNATIONAUX ---- */
    .testimonial-global-card {
        background: #ffffff;
        border: 1px solid #eaeaea;
        border-radius: 24px;
        padding: 40px;
        margin-bottom: 30px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.03);
        position: relative;
        transition: all 0.3s ease;
    }
    
    .testimonial-global-card:hover {
        box-shadow: 0 25px 50px rgba(46, 125, 50, 0.09);
        border-color: #2e7d32;
    }

    /* Guillemet géant de style éditorial */
    .testimonial-global-card::before {
        content: "“";
        position: absolute;
        top: -15px;
        right: 35px;
        font-size: 10rem;
        color: rgba(255, 179, 0, 0.14);
        font-family: "Georgia", serif;
    }

    .client-profile-meta {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 25px;
    }

    /* Avatar stylisé en CSS pur */
    .client-avatar-placeholder {
        width: 55px;
        height: 55px;
        background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #1b5e20;
        font-weight: 800;
        font-size: 1.3rem;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
    }

    .client-title-block {
        display: flex;
        flex-direction: column;
    }

    .client-main-name {
        font-size: 1.4rem !important;
        font-weight: 800;
        color: #1b5e20;
        margin: 0;
    }

    .client-badge-role {
        align-self: flex-start;
        font-size: 0.8rem !important;
        font-weight: 700;
        color: #c48b00;
        background: #fff8e1;
        padding: 4px 14px;
        border-radius: 30px;
        margin-top: 6px;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }

    .testimonial-quote-text {
        font-size: 1.15rem !important;
        color: #37474f;
        line-height: 1.7;
        font-style: italic;
        background: #fbfcfd;
        padding: 22px;
        border-left: 5px solid #ffb300;
        border-radius: 0 20px 20px 0;
        margin: 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # 2. HERO SECTION XXXL
    # =========================
    st.markdown('<h1 class="hero-title">🌱 Nos Réalisations & Impacts</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">YouAgronoMe déploie des standards technologiques et logistiques mondiaux pour catalyser l\'agriculture de demain. Nous transformons des données complexes en performances agricoles visibles et durables.</p>', unsafe_allow_html=True)

    # =========================
    # 3. FOCUS STATISTIQUE UNIQUE (XXXL EFFECT)
    # =========================
    st.markdown("""
    <div class="kpi-global-container">
        <div class="kpi-premium-box">
            <p class="kpi-premium-val">98%</p>
            <p class="kpi-premium-lbl">Taux de Satisfaction Global</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><hr style='border: 0; height: 1px; background: #e0e0e0;'><br>", unsafe_allow_html=True)

    # =========================
    # 4. SECTION TÉMOIGNAGES CORPORATE
    # =========================
    st.markdown('<h2 class="section-headline">🗣️ Parole à l\'Écosystème</h2>', unsafe_allow_html=True)

    temoins = [
        ("Awa Ndiaye", "Agricultrice", "Grâce aux débouchés de YouAgronoMe, mes produits frais trouvent preneur en un temps record. La chaîne de distribution est ultra performante et transparente."),
        ("Aissatou Diallo", "Cliente Grand Compte", "Une régularité de qualité impressionnante et des grilles de prix très compétitives par rapport au marché classique. Nous sécurisons nos approvisionnements à long terme."),
        ("Fatou Sow", "Commerçante", "Un service professionnel, rigoureux et surtout d'une fiabilité remarquable. C'est le partenaire stratégique idéal pour gérer la fluidité de nos stocks."),
        ("Khady Diop", "Productrice Émérite", "L'interface simplifie absolument tout le parcours. En quelques clics, l'ensemble de ma récolte est planifié, sécurisé et vendu efficacement.")
    ]

    # Dispatching parfait sur 2 colonnes larges
    cols = st.columns(2)

    for i, (nom, role, texte) in enumerate(temoins):
        initiale = nom[0] if nom else "U"
        
        with cols[i % 2]:
            st.markdown(f"""
            <div class="testimonial-global-card">
                <div class="client-profile-meta">
                    <div class="client-avatar-placeholder">{initiale}</div>
                    <div class="client-title-block">
                        <span class="client-main-name">{nom}</span>
                        <span class="client-badge-role">{role}</span>
                    </div>
                </div>
                <blockquote class="testimonial-quote-text">
                    "{texte}"
                </blockquote>
            </div>
            """, unsafe_allow_html=True)
# CONTACT
# =====================================================
import streamlit as st

def html_block(code):
    st.markdown(code, unsafe_allow_html=True)


if selected == "Contact":

    # ================= CSS =================
    html_block("""
    <style>
    .contact-card{
        background:#fff;
        padding:20px;
        border-radius:12px;
        border:1px solid #ddd;
    }
    .contact-title{
        color:#2e7d32;
        font-weight:bold;
    }
    </style>
    """)

    # ================= HEADER =================
    html_block("""
    <div style="text-align:center">
        <h1>🤝 Contact</h1>
        <p>Contactez YouAgronoMe</p>
    </div>
    """)

    # ================= COLUMNS =================
    c1, c2 = st.columns(2)

    with c1:
        html_block("""
        <div class="contact-card">
            <div class="contact-title">Infos</div>
            📞 +221 33 969 48 83<br>
            📧 isseyoume212@gmail.com<br>
            📍 Saint-Louis
        </div>
        """)

    with c2:
        html_block("""
        <div class="contact-card">
            <div class="contact-title">Départements</div>
            🤝 Partenariats<br>
            🎓 Opérations<br>
            🚜 Commercial
        </div>
        """)

    # ================= FORM =================
    with st.form("contact"):
        nom = st.text_input("Nom")
        email = st.text_input("Email")
        msg = st.text_area("Message")

        ok = st.form_submit_button("Envoyer")

        if ok:
            st.success("Message envoyé ✔")
