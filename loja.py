import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Mentoria Mente Milionária - Vitor Gabriel", page_icon="💰", layout="centered")

# 2. Estilização Geral (Visual 3D e Dark)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
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
        margin-bottom: 25px;
    }
    h1, h2, h3, p, span, li {
        color: white !important;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background-color: #FFD700;
        color: black !important;
        font-weight: bold;
        border: none;
    }
    /* Estilo do fundo dentro da área de brinde */
    .area-brinde {
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                          url('https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?q=80&w=2071&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        padding: 40px;
        border-radius: 15px;
        border: 2px solid #FFD700;
        text-align: center;
        margin-bottom: 20px;
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
        st.link_button("✅ JÁ PAGUEI!", "https://wa.me/27996704422?text=Fiz%20o%20PIX%20de%20100")

with col2:
    st.markdown("### 📚 E-book Avançado")
    st.write("Guia prático da riqueza")
    st.markdown("## R$ 20,00")
    with st.expander("PAGAR COM PIX"):
        st.code("12022298675", language=None)
        st.link_button("✅ JÁ PAGUEI!", "https://wa.me/27996704422?text=Fiz%20o%20PIX%20de%2020")

st.markdown("---")

# --- CRONOGRAMA ---
st.header("📅 Cronograma Semanal")
st.markdown("""
* **Semana 1:** 🧠 Mindset Milionário
* **Semana 2:** 📑 Organização de Dívidas
* **Semana 3:** 💸 Orçamento Inteligente
* **Semana 4:** 🛡️ Reserva de Emergência
* **Semana 5:** 📈 Multiplicação de Renda
* **Semana 6:** 🏁 Plano de Ação Final
""")

st.markdown("---")

# --- ÁREA DE BRINDE COM FUNDO INTERNO ---
st.header("🎁 Bônus Gratuito")

# Div HTML para criar o fundo dentro da área
st.markdown("""
    <div class="area-brinde">
        <h2 style="color: #FFD700 !important; text-shadow: 2px 2px 8px #000;">CONTEÚDO EXCLUSIVO</h2>
        <p style="font-size: 18px; text-shadow: 1px 1px 4px #000;">Baixe agora sua planilha básica e frases motivacionais.</p>
    </div>
    """, unsafe_allow_html=True)

# Conteúdo do download
brinde_texto = (
    "PROJETO MENTE MILIONARIA - VITOR GABRIEL\n"
    "==========================================\n\n"
    "FRASES MOTIVACIONAIS:\n"
    "1. A disciplina e a chave da liberdade.\n"
    "2. Invista em conhecimento, rende os melhores juros.\n\n"
    "PLANILHA BASICA 50-30-20:\n"
    "50% Necessidades | 30% Lazer | 20% Investir\n\n"
    "ADQUIRA O CONTEUDO COMPLETO NO SITE!"
)

st.download_button(
    label="📥 BAIXAR BRINDE + PLANILHA AGORA",
    data=brinde_texto,
    file_name="Brinde_Mente_Milionaria.txt",
    mime="text/plain",
    use_container_width=True
)

st.markdown("---")
st.link_button("🔵 MEU FACEBOOK", "https://www.facebook.com/profile.php?id=61553400154748")
st.caption("© 2024 Vitor Gabriel - Mentoria Mente Milionária.")