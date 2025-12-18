import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Mentoria Mente Milionária - Vitor Gabriel", page_icon="💰", layout="centered")

# 2. Código para adicionar o Plano de Fundo (CSS)
def add_bg_from_url():
    img_url = "https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=2071&auto=format&fit=crop" 
    
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("{img_url}");
             background-attachment: fixed;
             background-size: cover;
         }}
         
         div[data-testid="stVerticalBlock"] > div:not(:first-child) {{
             background-color: rgba(255, 255, 255, 0.90);
             padding: 20px;
             border-radius: 15px;
             margin-bottom: 20px;
             box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
         }}
         
         h1, h2, h3 {{
             color: #1a1a1a !important;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

# --- Título e Chamada Principal ---
st.title("🚀 Domine sua Liberdade Financeira")
st.subheader("Transforme sua mentalidade com a Mentoria de Vitor Gabriel")

# --- SEÇÃO DO VÍDEO ---
st.write("### 🎥 Assista: O Poder da Educação Financeira")
video_url = "https://www.youtube.com/watch?v=HSXcvFVtsdM" 
st.video(video_url)

st.info("""
**Por que aprender Educação Financeira?**
* 🧠 **Interpretação Inteligente:** Entenda como o dinheiro funciona no mundo real.
* 🛡️ **Segurança:** Proteja seu futuro e da sua família.
* 🗽 **Liberdade:** Pare de trabalhar pelo dinheiro e faça o dinheiro trabalhar para você.
""")

st.markdown("---")

# --- PRODUTO 1: MENTORIA PREMIUM ---
st.header("💎 1. Mentoria Premium: Mente Milionária")
col1, col2 = st.columns([2, 1])

with col1:
    st.write("**O próximo nível da sua jornada financeira.**")
    st.markdown("""
    * 🎯 **Módulo 1:** Planejamento e Diagnóstico Financeiro.
    * 🛠️ **Módulo 2:** Ferramentas de Gestão e Mentalidade.
    * 📈 **Módulo 3:** Estratégias de Escala e Multiplicação.
    """)

with col2:
    st.metric(label="Oferta Especial", value="R$ 100,00")
    st.caption("Investimento único.")

st.markdown("---")

# --- PRODUTO 2: E-BOOK PREMIUM (PAGO) ---
st.header("📚 2. E-book: O Guia Avançado da Riqueza")
col3, col4 = st.columns([2, 1])

with col3:
    st.write("""
    **O que você vai encontrar:**
    - Hacks de produtividade financeira.
    - Como sair das dívidas e começar a investir.
    - O mapa para a independência.
    """)

with col4:
    st.subheader("💰 R$ 20,00")
    st.write("Acesso imediato.")

st.markdown("---")

# --- SEÇÃO DE PAGAMENTO ---
st.header("💳 Garanta seu Acesso")
st.write("Escolha seu produto e realize o PIX:")

col_pix1, col_pix2 = st.columns(2)

with col_pix1:
    st.markdown("""
    **Dados PIX:**
    - **Chave:** `12022298675`
    - **Nome:** Vitor Gabriel Firmiano
    
    **Valores:**
    - Mentoria: **R$ 100,00**
    - E-book Premium: **R$ 20,00**
    """)

with col_pix2:
    st.markdown("**Confirmação:**")
    st.link_button("✅ ENVIAR COMPROVANTE NO WHATSAPP", "https://wa.me/27996704422?text=Oi%20Vitor,%20fiz%20o%20PIX!%20Quero%20acesso%20ao%20meu%20produto.", type="primary")

st.markdown("---")

# --- SEÇÃO REDES SOCIAIS ---
st.header("📱 Acompanhe meu trabalho")
st.write("Link da minha página oficial:")

# LINK EXIBIDO DIRETAMENTE NO BOTÃO
st.link_button("facebook.com/profile.php?id=61553400154748", "https://www.facebook.com/profile.php?id=61553400154748")

st.markdown("---")

# --- PRODUTO 3: BRINDE (GRATUITO) ---
st.header("🎁 Bônus: E-book de Introdução (Grátis)")
st.write("Dê o primeiro passo agora mesmo.")

conteudo_gratis = "Bem-vindo ao início da sua transformação financeira..."

st.download_button(
    label="👉 BAIXAR E-BOOK GRÁTIS",
    data=conteudo_gratis,
    file_name="Introducao_Mente_Milionaria.txt"
)

st.markdown("---")
st.caption("© 2024 Vitor Gabriel - Mentoria Mente Milionária.")