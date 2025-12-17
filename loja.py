import streamlit as st

# Configurações da página
st.set_page_config(page_title="Minha Mentoria VIP", page_icon="🚀")

# --- CABEÇALHO ---
st.title("🚀 Mentoria Premium: Acelere sua Carreira")
st.subheader("Aprenda diretamente comigo as estratégias que funcionam.")

# --- SOBRE A MENTORIA ---
col1, col2 = st.columns(2)

with col1:
    # Use o link que você encontrou antes:
    st.image("https://projetocapacitacao.com.br/wp-content/uploads/2024/12/Inserir-um-titulo-2-1024x576.webp", caption="Mente Milionária")

with col2:
    st.write("""
    ### O que você vai aprender:
    * **Módulo 1:** Planejamento Estratégico.
    * **Módulo 2:** Execução e Ferramentas.
    * **Módulo 3:** Escala e Resultados.
    
    **Investimento:** R$ 497,00
    """)
    
    # Link de venda (Substitua o número abaixo pelo seu WhatsApp real)
    link_venda = "https://wa.me/5511999999999?text=Quero+contratar+a+mentoria"
    
    if st.button("QUERO COMEÇAR AGORA"):
        st.write("Redirecionando para o WhatsApp...")
        st.link_button("CLIQUE AQUI PARA CONCLUIR", link_venda)

# --- DEPOIMENTOS ---
st.divider()
st.write("### O que dizem meus alunos:")
st.info("'Essa mentoria mudou meu jogo profissional em apenas 1 mês!' - João Silva")