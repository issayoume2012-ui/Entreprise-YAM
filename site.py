import streamlit as st
import time
import urllib.parse

if "panier" not in st.session_state:
    st.session_state.panier = []

if "historique" not in st.session_state:
    st.session_state.historique = []

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="YouAgronoMe",
    page_icon="🌾",
    layout="wide"
)

with st.spinner("Chargement..."):
    time.sleep(1)

# =====================================================
# CSS MODERNE
# =====================================================

st.markdown("""

<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;900&display=swap');

html, body, [class*="css"]{
font-family:'Poppins',sans-serif;
}

#MainMenu, footer, header{
visibility:hidden;
}

.stApp{

background:
linear-gradient(
135deg,
#f6fff7,
#edf8f1,
white
);

}

/* NAVBAR */

.nav{

background:white;

padding:15px;

border-radius:20px;

box-shadow:
0 5px 20px rgba(0,0,0,.08);

margin-bottom:25px;

}

/* HERO */

.hero{

padding:80px 50px;

border-radius:30px;

background:
linear-gradient(
135deg,
#1b4332,
#2d6a4f,
#40916c
);

color:white;

text-align:center;

margin-bottom:35px;

box-shadow:
0 15px 35px rgba(0,0,0,.12);

}

.hero h1{

font-size:65px;

font-weight:900;

margin-bottom:10px;

}

.hero p{

font-size:22px;

opacity:.95;

}

/* KPI */

.metric{

background:white;

padding:25px;

border-radius:20px;

text-align:center;

box-shadow:
0 6px 18px rgba(0,0,0,.08);

}

/* CARD */

.card{

background:white;

padding:22px;

border-radius:22px;

box-shadow:
0 8px 20px rgba(0,0,0,.08);

margin-bottom:25px;

transition:.3s;

height:100%;

}

.card:hover{

transform:translateY(-5px);

}

/* IMAGES */

[data-testid="stImage"] img{

border-radius:18px;

height:240px !important;

object-fit:cover;

}

/* MENU */

div[role="radiogroup"]{

justify-content:center;

gap:15px;

}

div[role="radiogroup"] label{

background:white;

padding:12px 18px;

border-radius:12px;

box-shadow:
0 3px 10px rgba(0,0,0,.06);

}

/* FOOTER */

.footer{

text-align:center;

padding:25px;

opacity:.7;

}

</style>

""", unsafe_allow_html=True)

# =====================================================
# MENU
# =====================================================

st.markdown("<div class='nav'>", unsafe_allow_html=True)

selected = st.radio(

    "",

    [

    "Accueil",
    "À propos",
    "Produits",
    "Commande",
    "Conseils",
    "Réalisations",
    "Contact"

    ],

    horizontal=True,

    label_visibility="collapsed"

)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# ACCUEIL
# =====================================================
# =====================================================
# ACCUEIL
# =====================================================

if selected == "Accueil":

    st.markdown("""
    <style>

    .hero{
        padding:60px 30px;
        border-radius:25px;
        background:
        linear-gradient(rgba(0,70,20,0.75),
        rgba(30,120,40,0.65)),
        url("https://images.unsplash.com/photo-1500937386664-56d1dfef3854");

        background-size:cover;
        background-position:center;
        text-align:center;
        color:white;
        margin-bottom:30px;
    }

    .hero h1{
        font-size:60px;
        margin-bottom:10px;
    }

    .hero p{
        font-size:22px;
    }

    .agri-card{
        background:white;
        padding:25px;
        border-radius:20px;
        text-align:center;
        box-shadow:0 4px 15px rgba(0,0,0,.08);
        min-height:180px;
        transition:.3s;
    }

    .agri-card:hover{
        transform:translateY(-5px);
    }

    .agri-icon{
        font-size:40px;
        margin-bottom:10px;
    }

    .agri-card h4{
        color:#1b5e20;
        margin-bottom:10px;
    }

    </style>
    """, unsafe_allow_html=True)

    # HERO
    st.markdown("""
    <div class="hero">
        <h1>🌾 YouAgronoMe</h1>
        <p>Agriculture intelligente • Durable • Innovante</p>
    </div>
    """, unsafe_allow_html=True)

    # CARTES STATISTIQUES
    stats = [
        ("🌱", "Innovation", "Nouvelles techniques agricoles"),
        ("📊", "Suivi", "Conseils et accompagnement"),
        ("🛒", "Marché", "Disponible partout au Sénégal"),
        ("👨‍🌾", "Experts", "Ingénieurs et spécialistes")
    ]

    cols = st.columns(4)

    for i, (icon, title, desc) in enumerate(stats):
        with cols[i]:
            st.markdown(
                f"""
                <div class="agri-card">
                    <div class="agri-icon">{icon}</div>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
# =====================================================
# A PROPOS
# =====================================================

elif selected=="À propos":

    st.markdown("""

    <div class='card'>

    YouAgronoMe accompagne le développement
    d’une agriculture moderne, durable
    et performante à Saint-Louis.

    Créée en 2024.

    </div>

    """, unsafe_allow_html=True)
   

# =====================================================
# =====================================================
# =====================================================
# =====================================================
# INITIALISATION
# =====================================================

import urllib.parse

if "panier" not in st.session_state:
    st.session_state.panier = []

if "historique" not in st.session_state:
    st.session_state.historique = []

# =====================================================
# =====================================================
# INITIALISATION
# =====================================================

import streamlit as st
import urllib.parse

if "panier" not in st.session_state:
    st.session_state.panier = []

if "historique" not in st.session_state:
    st.session_state.historique = []

# =====================================================
# PRODUITS + PANIER + COMMANDE + PAIEMENT + HISTORIQUE
# =====================================================

# =====================================================
# Initialisation panier
if "panier" not in st.session_state:
    st.session_state.panier = []

# =====================================================
# PRODUITS
# =====================================================

elif selected == "Produits":
    st.title("🌾 Produits disponibles")
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

    cols = st.columns(5)

    for i, p in enumerate(produits):

        image, nom, prix = p

        with cols[i % 5]:
            st.image(
                image,
                use_container_width=True
            )

            st.markdown(
                f"""
                <div class='card'>
                <h4>{nom}</h4>
                <p>{prix}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            qte = st.number_input(
                "Qté",
                1,
                100,
                1,
                key=f"qte_{i}"
            )

            if st.button(
                "🛒 Ajouter",
                key=f"add_{i}"
            ):

                st.session_state.panier.append({

                    "produit": nom,

                    "prix": prix,

                    "quantite": qte

                })

                st.success(
                    "Ajouté au panier"
                )

# =====================================================
# =====================================================
# =====================================================
# COMMANDE
# =====================================================

elif selected == "Commande":

    import urllib.parse

    st.title("📦 Commande")
# =====================================================
# =====================================================
# COMMANDE
# =====================================================

elif selected == "Commande":

    import urllib.parse

    numero_whatsapp = "221777473170"
    email_dest = "issayoume2012@gmail.com"

    if "panier" not in st.session_state:
        st.session_state.panier = []

    if "historique" not in st.session_state:
        st.session_state.historique = []

    st.title("📦 Commande")

    # =====================================================
    # PANIER
    # =====================================================

    st.subheader("🛒 Panier")

    if len(st.session_state.panier) == 0:

        st.warning(
            "Votre panier est vide"
        )

    else:

        total_articles = 0

        for i, item in enumerate(
            st.session_state.panier
        ):

            c1, c2, c3, c4 = st.columns(
                [4,2,3,1]
            )

            c1.write(item["produit"])

            c2.write(
                f"x {item['quantite']}"
            )

            c3.write(
                item["prix"]
            )

            total_articles += item[
                "quantite"
            ]

            if c4.button(
                "❌",
                key=f"sup_{i}"
            ):

                st.session_state.panier.pop(i)
                st.rerun()

        st.info(
            f"{total_articles} article(s) dans le panier"
        )

        st.markdown("---")

        # =====================================================
        # INFOS CLIENT
        # =====================================================

        nom = st.text_input(
            "Nom complet"
        )

        telephone = st.text_input(
            "Téléphone"
        )

        adresse = st.text_input(
            "Adresse"
        )

        commentaire = st.text_area(
            "Commentaire"
        )

        paiement = st.radio(

            "Mode paiement",

            [

                "Présentiel",

                "Wave",

                "Orange Money"

            ]

        )

        if paiement == "Wave":

            st.success(
                "Wave : 221 77 747 31 70"
            )

        elif paiement == "Orange Money":

            st.success(
                "Orange Money : 221 77 747 31 70"
            )

        # =====================================================
        # VALIDATION
        # =====================================================

        if st.button(
            "✅ Préparer commande"
        ):

            texte = f"""
Nouvelle commande YouAgronoMe

Nom : {nom}

Téléphone : {telephone}

Adresse : {adresse}

Paiement : {paiement}

Commentaire : {commentaire}

Produits :
"""

            for p in st.session_state.panier:

                texte += f"""

• {p['produit']}
Qté : {p['quantite']}
Prix : {p['prix']}
"""

            # sauvegarde historique
            st.session_state.historique.append({

                "client": nom,

                "paiement": paiement,

                "commande":
                st.session_state.panier.copy()

            })

            whatsapp_link = (

                "https://wa.me/"
                + numero_whatsapp
                + "?text="
                + urllib.parse.quote(
                    texte
                )

            )

            email_link = (

                f"mailto:{email_dest}"

                f"?subject=Commande"

                f"&body="

                + urllib.parse.quote(
                    texte
                )

            )

            st.success(
                "Commande prête ✅"
            )

            c1, c2 = st.columns(2)

            with c1:

                st.link_button(

                    "📱 Envoyer WhatsApp",

                    whatsapp_link,

                    use_container_width=True

                )

            with c2:

                st.link_button(

                    "📧 Envoyer Email",

                    email_link,

                    use_container_width=True

                )

            if st.button(
                "🧹 Vider panier"
            ):

                st.session_state.panier = []
                st.rerun()

    # =====================================================
    # HISTORIQUE
    # =====================================================

    st.markdown("---")

    st.subheader(
        "📜 Historique commandes"
    )

    if len(
        st.session_state.historique
    ) == 0:

        st.write(
            "Aucune commande"
        )

    else:

        for i, hist in enumerate(

            st.session_state.historique,

            start=1

        ):

            st.markdown(
                f"### Commande {i}"
            )

            st.write(
                f"Client : {hist['client']}"
            )

            st.write(
                f"Paiement : {hist['paiement']}"
            )

            for prod in hist[
                "commande"
            ]:

                st.write(

                    f"• {prod['produit']} x {prod['quantite']}"

                )
# =====================================================
# CONSEILS
# =====================================================

elif selected == "Conseils":

    conseils = {
        "💧 Irrigation intelligente": [
            "Utiliser le goutte-à-goutte pour économiser l’eau",
            "Arroser tôt le matin ou le soir",
            "Contrôler régulièrement l’humidité du sol"
        ],

        "🌱 Gestion durable des sols": [
            "Ajouter du compost organique",
            "Faire la rotation des cultures",
            "Limiter l’érosion du sol"
        ],

        "🛡 Protection des cultures": [
            "Surveiller les ravageurs régulièrement",
            "Utiliser des solutions biologiques",
            "Éliminer les plantes infectées"
        ],

        "♻ Agriculture durable": [
            "Réduire l’utilisation des produits chimiques",
            "Favoriser les cultures locales",
            "Recycler les déchets agricoles"
        ],

        "🚜 Agriculture moderne": [
            "Utiliser des outils numériques",
            "Suivre les prévisions météo",
            "Adopter des équipements modernes"
        ]
    }

    choix = st.radio(
        "",
        list(conseils.keys()),
        horizontal=True
    )
    st.write("Voir Direction Conseil et Accompagnement pour plus d'information : DCA@gmail.com")

    # Sous-titre dynamique
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(90deg,#2E7D32,#4CAF50);
            padding:15px;
            border-radius:12px;
            margin-bottom:20px;
            color:white;
            text-align:center;
            font-size:28px;
            font-weight:bold;
            box-shadow:0 3px 8px rgba(0,0,0,0.2);
        ">
            {choix}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Contenu stylisé
    for element in conseils[choix]:
        st.markdown(
            f"""
            <div style="
                background:white;
                padding:15px;
                margin:10px 0;
                border-left:6px solid #4CAF50;
                border-radius:10px;
                box-shadow:0px 2px 6px rgba(0,0,0,0.1);
                font-size:17px;
            ">
                ✅ {element}
            </div>
            """,
            unsafe_allow_html=True
        )
# =====================================================
# REALISATIONS
# =====================================================

elif selected=="Réalisations":

    temoins = [

    ("T1.jpg","Awa Ndiaye, agricultrice et partenaire : Depuis que j’achète mes produits chez YouAgronoMe, je trouve toujours des produits frais, de qualité et à bon prix. La livraison est rapide et le service est sérieux. Je recommande vivement !"), 
    ("T2.jpg","Aissatou,cliente satisfaite : Les produits sont frais, bien emballés et les prix sont accessibles. J’ai acheté du maïs et des arachides et j’ai été très satisfait de la qualité. Je reviendrai acheter encore."),
    ("T3.jpg","Fatou Sow, commerçante: J’ai commandé plusieurs produits agricoles et j’ai été impressionné par la qualité. Les prix sont corrects et le service est très professionnel. Je recommande sans hésiter."),
    ("T4.jpg","Khady, productrice agricole : Grâce à YouAgronoMe, je trouve facilement des produits locaux de bonne qualité. Les commandes sont simples et les produits arrivent toujours en bon état.")

    ]

    cols = st.columns(2)

    for i,t in enumerate(temoins):

        with cols[i%2]:

            st.image(t[0])

            st.markdown(

            f"<div class='card'>{t[1]}</div>",

            unsafe_allow_html=True

            )

# =====================================================
# CONTACT
# =====================================================

elif selected=="Contact":

    c1,c2 = st.columns(2)

    with c1:

        st.markdown("""

        <div class='card'>

        📞 +221 33 969 48 83

        📧 isseyoume212@gmail.com

        📍 Saint-Louis, Sénégal

        </div>

        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""

        <div class='card'>
        Plus d'information 

        🤝 Direction Partenariat : partYAM@gmail.com

        🎓 Bureau des Opérations : boYAM@gmail.com

        🚜 Direction Management, Commerciale et Information: dmciYAM@gmail.com

        </div>

        """, unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""

<div class='footer'>

© 2025 YouAgronoMe • Agriculture intelligente 🌾

</div>

""", unsafe_allow_html=True)
