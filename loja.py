import streamlit as st

# Configuração da página
st.set_page_config(page_title="Mentoria Mente Milionária - Vitor Gabriel", page_icon="💰", layout="centered")

# --- Título e Chamada Principal ---
st.title("🚀 Domine sua Liberdade Financeira")
st.subheader("Transforme sua mentalidade com a Mentoria de Vitor Gabriel")

# --- SEÇÃO DO VÍDEO (INTERPRETAÇÃO COM IA) ---
st.write("### 🎥 Assista: O Poder da Educação Financeira")
# DICA: Quando criar seu vídeo na IA (HeyGen/D-ID), suba no YouTube e cole o link abaixo:
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
st.video(video_url)

st.info("""
**Por que aprender Educação Financeira?**
* 🧠 **Interpretação Inteligente:** Entenda como o dinheiro funciona no mundo real.
* 🛡️ **Segurança:** Proteja seu futuro e da sua família.
* 🗽 **Libertade:** Pare de trabalhar pelo dinheiro e faça o dinheiro trabalhar para você.
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