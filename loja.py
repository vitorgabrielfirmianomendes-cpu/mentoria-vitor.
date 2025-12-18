import streamlit as st
import random
import streamlit.components.v1 as components # <-- ESSENCIAL PARA O ANÚNCIO

# 1. Configuração da página
st.set_page_config(page_title="Mentoria Mente Milionária - Vitor Gabriel", page_icon="💰", layout="centered")

# 2. Estilização Geral (Visual 3D, Glassmorphism e Dark)
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
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
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
    .area-brinde {
        background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                          url('https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?q=80&w=2071&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        padding: 40px;
        border-radius: 15px;
        border: 2px solid #FFD700;
        text-align: center;
        margin-bottom: 15px;
    }
    .roleta-box {
        background-color: rgba(255, 215, 0, 0.15);
        border: 2px solid #FFD700;
        border-radius: 15px;
        padding: 25px;
        margin-top: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Título ---
st.title("🚀 Mentoria Mente Milionária")
st.subheader("Vitor Gabriel - Educação Financeira")

# --- BLOCO DE ANÚNCIO (ADSTERRA CORRIGIDO) ---
ad_code = """
<div style="text-align:center;">
    <script type="text/javascript">
        atOptions = {
            'key' : '1ebc8dbeefa60f968702e5fb7af0e964',
            'format' : 'iframe',
            'height' : 90,
            'width' : 728,
            'params' : {}
        };
    </script>
    <script type="text/javascript" src="//www.highperformanceformat.com/1ebc8dbeefa60f968702e5fb7af0e964/invoke.js"></script>
</div>
"""
components.html(ad_code, height=110)

# --- VÍDEO ---
st.video("https://www.youtube.com/watch?v=HSXcvFVtsdM")

st.markdown("---")

# --- PRODUTOS ---
st.header("🛒 Escolha seu Plano")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💎 Mentoria Premium\n## R$ 100,00")
    with st.expander("PAGAR COM PIX"):
        st.code("12022298675", language=None)
        st.link_button("✅ JÁ PAGUEI! ACESSAR", "https://wa.me/27996704422?text=Fiz%20PIX%20Mentoria")

with col2:
    st.markdown("### 📚 E-book Avançado\n## R$ 20,00")
    with st.expander("PAGAR COM PIX"):
        st.code("12022298675", language=None)
        st.link_button("✅ JÁ PAGUEI! ACESSAR", "https://wa.me/27996704422?text=Fiz%20PIX%20Ebook")

st.markdown("---")

# --- ÁREA DE BRINDE MONETIZADA ---
st.header("🎁 Bônus: Checklist Mentalidade Milionária")
with st.container():
    st.markdown('<div class="area-brinde"><h2>7 MUDANÇAS MENTAIS</h2><p>Baixe agora e comece a lucrar.</p></div>', unsafe_allow_html=True)
    
    # 🔗 SEU LINK DE LUCRO DO SHRINKME (CORRIGIDO)
    link_de_lucro = "https://shrinkme.click/xnPqF" 
    
    st.link_button("📥 BAIXAR CHECKLIST AGORA", link_de_lucro, use_container_width=True)
    st.info("💡 **Dica de acesso:** Clique no botão, aguarde os segundos do anúncio e clique em 'Get Link' para abrir seu arquivo.")

st.markdown("---")

# --- ROLETA ---
st.header("✨ Gire a Roleta e Ganhe uma Dica Milionária!")
with st.container():
    st.markdown('<div class="roleta-box">', unsafe_allow_html=True)
    if st.button("🍀 GIRAR ROLETA DA SORTE 🍀"):
        dicas = ["Invista em você.", "Pense longo prazo.", "Crie renda passiva.", "Disciplina é liberdade."]
        st.success(f"**VOCÊ GANHOU UMA DICA:** {random.choice(dicas)}")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")