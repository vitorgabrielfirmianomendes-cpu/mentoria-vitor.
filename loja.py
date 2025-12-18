import streamlit as st

# Configuração da página
st.set_page_config(page_title="Mentoria & E-books - Vitor Gabriel", page_icon="💰", layout="centered")

# --- Título e Chamada Principal ---
st.title("🚀 Acelere sua Carreira com Vitor Gabriel")
st.subheader("Estratégias validadas para quem busca a Mente Milionária.")

# --- VÍDEO EXPLICATIVO ---
st.write("### 🎥 Assista: Como funciona a Mentoria")
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # Substitua pelo link do seu vídeo de IA
st.video(video_url)

st.markdown("---")

# --- PRODUTO 1: MENTORIA PREMIUM (VALOR ATUALIZADO) ---
st.header("💎 1. Mentoria Premium: Mente Milionária")
col1, col2 = st.columns([2, 1])

with col1:
    st.write("Um acompanhamento individual para escalar seus resultados.")
    st.markdown("""
    * 🎯 Planejamento Estratégico.
    * 🛠️ Execução e Ferramentas.
    * 📈 Escala e Resultados.
    """)

with col2:
    # VALOR ATUALIZADO PARA R$ 100,00
    st.metric(label="Investimento Especial", value="R$ 100,00")
    st.caption("Aproveite esta oferta!")

st.markdown("---")

# --- PRODUTO 2: E-BOOK PREMIUM (PAGO) ---
st.header("📚 2. E-book: O Guia Avançado da Riqueza")
col3, col4 = st.columns([2, 1])

with col3:
    st.write("""
    **Conteúdo Exclusivo:**
    - Estratégias de investimento para iniciantes.
    - Como criar fontes de renda passiva.
    - Hacks de produtividade dos milionários.
    """)

with col4:
    st.subheader("💰 R$ 20,00")
    st.write("Acesso imediato via PDF.")

st.markdown("---")

# --- SEÇÃO DE PAGAMENTO ---
st.header("💳 Como Adquirir")
st.write("Escolha seu produto e faça o PIX abaixo:")

col_pix1, col_pix2 = st.columns(2)

with col_pix1:
    st.markdown("""
    **Dados para Pagamento:**
    - **Chave PIX:** `12022298675`
    - **Favorecido:** Vitor Gabriel Firmiano
    
    **Valores Atualizados:**
    - Mentoria: **R$ 100,00**
    - E-book Premium: **R$ 20,00**
    """)

with col_pix2:
    st.markdown("**Após o PIX, envie o comprovante:**")
    st.link_button("✅ ENVIAR COMPROVANTE AGORA", "https://wa.me/27996704422?text=Oi%20Vitor,%20fiz%20o%20PIX!%20Quero%20acesso%20ao%20meu%20produto.", type="primary")

st.markdown("---")

# --- PRODUTO 3: BRINDE (GRATUITO) ---
st.header("🎁 Bônus: E-book de Introdução (Grátis)")
st.write("Comece sua jornada agora sem custo nenhum.")

conteudo_gratis = "Este é o seu guia inicial para a Mente Milionária..."

st.download_button(
    label="👉 BAIXAR E-BOOK GRÁTIS",
    data=conteudo_gratis,
    file_name="Introducao_Mente_Milionaria.txt"
)

st.markdown("---")
st.caption("© 2024 Vitor Gabriel - Todos os direitos reservados.")