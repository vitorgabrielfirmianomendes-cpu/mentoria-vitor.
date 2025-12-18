import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Mentoria Mente Milionária - Vitor Gabriel", page_icon="💰", layout="centered")

# 2. Estilização Personalizada (Fundo Escuro e Efeitos)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url("https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=2071&auto=format&fit=crop");
        background-attachment: fixed;
        background-size: cover;
    }
    [data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 215, 0, 0.3);
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }
    h1, h2, h3, p, span {
        color: white !important;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #FFD700;
        color: black !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Título ---
st.title("🚀 Mentoria Mente Milionária")
st.subheader("Vitor Gabriel - Educação Financeira")

# --- SEÇÃO DO VÍDEO ---
video_url = "https://www.youtube.com/watch?v=HSXcvFVtsdM" 
st.video(video_url)

st.markdown("---")

# --- PRODUTOS ---
st.header("🛒 Escolha seu Plano")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💎 Mentoria Premium")
    st.write("Acesso vitalício + Suporte")
    st.markdown("## R$ 100,00")
    with st.expander("PAGAR COM PIX"):
        st.code("12022298675", language=None)
        st.write("Nome: Vitor Gabriel Firmiano")
        st.link_button("✅ JÁ PAGUEI! ACESSAR", "https://wa.me/27996704422?text=Fiz%20o%20PIX%20de%20100%20da%20Mentoria")

with col2:
    st.markdown("### 📚 E-book Avançado")
    st.write("Guia prático da riqueza")
    st.markdown("## R$ 20,00")
    with st.expander("PAGAR COM PIX"):
        st.code("12022298675", language=None)
        st.write("Nome: Vitor Gabriel Firmiano")
        st.link_button("✅ JÁ PAGUEI! ACESSAR", "https://wa.me/27996704422?text=Fiz%20o%20PIX%20de%2020%20do%20Ebook")

st.markdown("---")

# --- CRONOGRAMA ---
st.header("📅 Cronograma: Métodos Semanais")
st.markdown("""
* **Semana 1:** 🧠 Introdução e Mentalidade Financeira
* **Semana 2:** 📑 Diagnóstico e Organização
* **Semana 3:** 💸 Orçamento e Cortes de Gastos
* **Semana 4:** 🛡️ Reserva e Investimentos
* **Semana 5:** 📈 Escala e Multiplicação
* **Semana 6:** 🏁 Plano de Ação Final
""")

st.markdown("---")

# --- REDES SOCIAIS E BÔNUS ---
col_fb, col_eb = st.columns(2)
with col_fb:
    st.link_button("🔵 MEU FACEBOOK", "https://www.facebook.com/profile.php?id=61553400154748")

with col_eb:
    st.download_button(
        label="🎁 BAIXAR BRINDE GRÁTIS",
        data="Bem-vindo à sua jornada financeira! O primeiro passo é mudar sua mente.",
        file_name="Introducao_Mente_Milionaria.txt"
    )

st.caption("© 2024 Vitor Gabriel - Mentoria Mente Milionária.")