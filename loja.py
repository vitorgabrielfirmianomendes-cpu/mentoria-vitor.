import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Mentoria Mente Milionária - Vitor Gabriel", page_icon="💰", layout="centered")

# 2. Estilização Personalizada (Fundo 3D Dark e Efeitos)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url("https://images.unsplash.com/photo-1639762681485-074b7f938ba0?q=80&w=2070&auto=format&fit=crop");
        background-attachment: fixed;
        background-size: cover;
    }
    [data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 215, 0, 0.2);
        backdrop-filter: blur(15px);
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 25px;
    }
    h1, h2, h3, p, span, li {
        color: white !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #FFD700;
        color: black !important;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #FFF;
        transform: scale(1.02);
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
        st.link_button("✅ JÁ PAGUEI! ENVIAR COMPROVANTE", "https://wa.me/27996704422?text=Fiz%20o%20PIX%20de%20100%20da%20Mentoria")

with col2:
    st.markdown("### 📚 E-book Avançado")
    st.write("Guia prático da riqueza")
    st.markdown("## R$ 20,00")
    with st.expander("PAGAR COM PIX"):
        st.code("12022298675", language=None)
        st.write("Nome: Vitor Gabriel Firmiano")
        st.link_button("✅ JÁ PAGUEI! ENVIAR COMPROVANTE", "https://wa.me/27996704422?text=Fiz%20o%20PIX%20de%2020%20do%20Ebook")

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
    # Conteúdo do brinde formatado corretamente para não dar erro
    brinde_texto = (
        "PROJETO MENTE MILIONARIA - VITOR GABRIEL\n"
        "==========================================\n\n"
        "FRASES PARA MUDAR SUA MENTE:\n"
        "1. A disciplina e a mae do sucesso.\n"
        "2. Nao trabalhe pelo dinheiro, faca o dinheiro trabalhar por voce.\n\n"
        "EXEMPLO DE PLANILHA (METODO 50-30-20):\n"
        "------------------------------------------\n"
        "- 50% para Essenciais (Moradia, Saude)\n"
        "- 30% para Estilo de Vida (Lazer, Hobbies)\n"
        "- 20% para Futuro (Investimentos)\n\n"
        "Se voce ganha 2000 reais, sua meta e:\n"
        "Essenciais: 1000 | Lazer: 600 | Investir: 400\n\n"
        "==========================================\n"
        "QUER O METODO COMPLETO? ACESSE O SITE E ADQUIRA A MENTORIA!"
    )

    st.download_button(
        label="🎁 BAIXAR BRINDE + PLANILHA BÁSICA",
        data=brinde_texto,
        file_name="Brinde_Mente_Milionaria.txt",
        mime="text/plain"
    )

st.caption("© 2024 Vitor Gabriel - Mentoria Mente Milionária.")