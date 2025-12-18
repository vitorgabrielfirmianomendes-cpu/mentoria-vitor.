import streamlit as st

# Configuração da página
st.set_page_config(page_title="Mentoria Mente Milionária", page_icon="💰", layout="centered")

# --- Título e Chamada Principal ---
st.title("🚀 Mentoria Premium: Acelere sua Carreira")
st.subheader("Transforme seu potencial em resultados reais com as estratégias da Mente Milionária.")

# Imagem Chamativa Principal (Executivos/Sucesso)
st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=800", caption="Sua jornada para o sucesso começa aqui!") 

st.markdown("---")

# --- Seção Principal da Mentoria ---
col1, col2 = st.columns([2, 1])

with col1:
    st.header("💎 Mente Milionária")
    st.write("""
    Nossa mentoria é um programa intensivo para quem busca acelerar o crescimento financeiro.
    """)
    st.markdown("""
    **O que você vai aprender:**
    * 🎯 **Módulo 1:** Planejamento Estratégico.
    * 🛠️ **Módulo 2:** Execução e Ferramentas.
    * 📈 **Módulo 3:** Escala e Resultados.
    """)
    st.warning("⚠️ **Vagas Limitadas para esta turma!**")

with col2:
    st.write("### 💰 Investimento")
    st.metric(label="De R$ 997,00 por apenas", value="R$ 497,00")
    st.write("Pagamento único via PIX.")

st.markdown("---")

# --- NOVA SEÇÃO: PAGAMENTO VIA PIX ---
st.header("💳 Como obter a Mentoria (Acesso Imediato)")
st.write("Siga os passos abaixo para garantir sua vaga agora mesmo:")

col_pix1, col_pix2 = st.columns(2)

with col_pix1:
    st.markdown("""
    **1. Use nossa Chave PIX:**
    `12022298675` (Ex: seu e-mail ou CPF)
    
    **2. Valor:**
    R$ 497,00
    
    **3. Nome do Favorecido:**
    Vitor Gabriel Firmiano
    """)

with col_pix2:
    st.markdown("**4. Envie o Comprovante:**")
    # Link direto para o seu WhatsApp com mensagem pronta
    st.link_button("✅ ENVIAR COMPROVANTE AGORA", "https://wa.me/27996704422?text=Oi%20Vitor,%20fiz%20o%20PIX%20da%20mentoria!%20Aqui%20está%20o%20comprovante.", type="primary")
    st.caption("Após o envio, você receberá o link de acesso em até 5 minutos.")

st.markdown("---")

# --- Seção do E-book Gratuito ---
st.header("📚 BÔNUS: E-book O Guia da Mente Milionária")
col_eb1, col_eb2 = st.columns([1, 2])

with col_eb1:
    st.image("https://images.unsplash.com/photo-1589998059171-988d887df646?auto=format&fit=crop&q=80&w=300")

with col_eb2:
    st.write("Baixe agora o guia inicial para mudar sua mentalidade financeira gratuitamente.")
    st.download_button(
        label="👉 BAIXAR E-BOOK GRATUITO",
        data="Bem-vindo à Mente Milionária! O primeiro passo é o planejamento...", 
        file_name="Guia_Mente_Milionaria.txt",
        mime="text/plain"
    )

st.markdown("---")

# --- Rodapé ---
st.caption("© 2024 Vitor Gabriel - Mentoria Mente Milionária.")