import streamlit as st
import time

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

if selected=="Accueil":

    st.markdown("""

    <div class="hero">

    <h1>🌾 YouAgronoMe</h1>

    <p>

    Agriculture intelligente • Durable • Innovante

    </p>

    </div>

    """, unsafe_allow_html=True)

    cols = st.columns(4)

    stats = [

        ("120+","Producteurs"),
        ("20T+","Production"),
        ("90%","Satisfaction"),
        ("2024","Création")

    ]

    for c,s in zip(cols,stats):

        with c:

            st.markdown(f"""

            <div class="metric">

            <h2>{s[0]}</h2>

            <p>{s[1]}</p>

            </div>

            """, unsafe_allow_html=True)

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
# PRODUITS
# =====================================================

elif selected=="Produits":

    produits=[

    ("to.jpg","Tomates","3500 FCFA"),
    ("fr.jpg","Fraises","5000 FCFA"),
    ("og.jpg","Oignons","2500 FCFA"),
    ("cr.jpg","Carottes","3000 FCFA"),
    ("pm.jpg","Piments","2000 FCFA"),
    ("cc.jpg","Concombres","2800 FCFA"),
    ("pt.jpg","Pommes de terre","4500 FCFA"),
    ("or.jpg","Oranges","4000 FCFA")

    ]

    cols = st.columns(4)

    for i,p in enumerate(produits):

        with cols[i%4]:

            st.image(p[0])

            st.markdown(f"""

            <div class='card'>

            <h3>{p[1]}</h3>

            💰 {p[2]}

            </div>

            """, unsafe_allow_html=True)

# =====================================================
# CONSEILS
# =====================================================

elif selected=="Conseils":

    conseils = [

        "💧 Irrigation intelligente",
        "🌱 Gestion durable des sols",
        "🛡 Protection des cultures",
        "♻ Agriculture durable",
        "🚜 Agriculture moderne"

    ]

    for c in conseils:

        st.markdown(

        f"<div class='card'>{c}</div>",

        unsafe_allow_html=True

        )

# =====================================================
# REALISATIONS
# =====================================================

elif selected=="Réalisations":

    temoins = [

    ("T1.jpg","Aminata"),
    ("T2.jpg","Aissatou"),
    ("T3.jpg","Fatou"),
    ("T4.jpg","Khady")

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

        📞 +221 77 969 48 83

        📧 isseyoume212@gmail.com

        📍 Saint-Louis, Sénégal

        </div>

        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""

        <div class='card'>

        🤝 Partenariats

        🎓 Stages

        🚜 Support agricole

        </div>

        """, unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""

<div class='footer'>

© 2026 YouAgronoMe • Agriculture intelligente 🌾

</div>

""", unsafe_allow_html=True)