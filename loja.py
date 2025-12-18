import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Mentoria Mente Milionária - Vitor Gabriel", page_icon="💰", layout="centered")

# 2. Plano de Fundo
def add_bg_from_url():
    img_url = "https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=2071&auto=format&fit=crop" 
    st.markdown(
         f"""
         <style>
         .stApp {{ background-image: url("{img_url}"); background-attachment: fixed; background-size: cover; }}
         div[data-testid="stVerticalBlock"] > div:not(:first-child) {{
             background-color: rgba(255, 255, 255, 0.90);
             padding: 20px; border-radius: 15px; margin-bottom: 20px;
             box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
         }}
         h1, h2, h3 {{ color: #1a1a1a !important; }}
         </style>
         """, unsafe_allow_html=True
     )

add_bg_from_url()

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
    st.subheader("R$ 100,00")
    if st.button("PAGAR MENTORIA (PIX)"):
        st.success("✅ CHAVE PIX: 12022298675")
        st.info("Copie a chave acima, pague no seu banco e envie o comprovante abaixo.")
        st.link_button("ENVIAR COMPROVANTE AGORA", "https://wa.me/27996704422?text=Fiz%20o%20PIX%20de%20100%20reais%20da%20Mentoria!")

with col2:
    st.markdown("### 📚 E-book Avançado")
    st.write("Guia prático da riqueza")
    st.subheader("R$ 20,00")
    if st.button("PAGAR E-BOOK (PIX)"):
        st.success("✅ CHAVE PIX: 12022298675")
        st.info("Copie a chave acima, pague no seu banco e envie o comprovante abaixo.")
        st.link_button("ENVIAR COMPROVANTE AGORA", "https://wa.me/27996704422?text=Fiz%20o%20PIX%20de%2020%20reais%20do%20Ebook!")

st.markdown("---")

# --- NOVO: CRONOGRAMA SEMANAL DO E-BOOK ---
st.header("📅 Cronograma: Métodos Semanais")
st.write("Veja o que você vai aprender passo a passo:")

with st.container():
    st.markdown("""
    * **Semana 1:** 🧠 Introdução e Mentalidade Financeira (Mindset)
    * **Semana 2:** 📑 Diagnóstico e Organização das Dívidas
    * **Semana 3:** 💸 Criando um Orçamento e Cortando Gastos
    * **Semana 4:** 🛡️ Reserva de Emergência e Primeiros Investimentos
    * **Semana 5:** 📈 Escala e Multiplicação de Renda
    * **Semana 6:** 🏁 Revisão Final e Plano de Ação para o Futuro
    """)

st.markdown("---")

# --- BOTÃO GERAL DE PAGAMENTO ---
st.header("💳 Pagar e Acessar Agora")
st.write("Clique abaixo para ver os detalhes do pagamento único:")

with st.expander("CLIQUE AQUI PARA VER DADOS DO PIX"):
    st.write("**Nome:** Vitor Gabriel Firmiano")
    st.write("**Chave PIX:** `12022298675` (Celular/CPF)")
    st.write("---")
    st.write("Após o pagamento, você receberá o acesso imediato pelo WhatsApp.")
    st.link_button("✅ JÁ PAGUEI! QUERO MEU ACESSO", "https://wa.me/27996704422?text=Oi%20Vitor,%20já%20realizei%20o%20pagamento%20e%20quero%20meu%20acesso!")

st.markdown("---")

# --- REDES SOCIAIS E BÔNUS ---
st.link_button("🔵 MEU FACEBOOK", "https://www.facebook.com/profile.php?id=61553400154748")

st.download_button(
    label="🎁 BAIXAR E-BOOK GRÁTIS (INTRODUÇÃO)",
    data="Conteúdo do brinde: Comece sua jornada aqui!",
    file_name="Introducao_Mente_Milionaria.txt"
)

st.caption("© 2024 Vitor Gabriel - Mentoria Mente Milionária.")