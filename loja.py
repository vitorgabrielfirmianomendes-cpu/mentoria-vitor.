# --- REDES SOCIAIS E BÔNUS ---
col_fb, col_eb = st.columns(2)
with col_fb:
    st.link_button("🔵 MEU FACEBOOK", "https://www.facebook.com/profile.php?id=61553400154748")

with col_eb:
    # Criando o conteúdo do E-book de Brinde com Frases e Planilha
    conteudo_brinde = """
    🚀 BEM-VINDO À SUA JORNADA - MENTE MILIONÁRIA
    -------------------------------------------
    "O segredo da riqueza não é o quanto você ganha, mas como você gerencia o que tem."
    
    🌟 FRASES MOTIVACIONAIS PARA SUA SEMANA:
    1. "A disciplina é a ponte entre metas e realizações."
    2. "Trabalhe enquanto eles dormem, estude enquanto eles se divertem."
    3. "Sua mente é seu maior ativo. Invista nela primeiro."

    📊 AMOSTRA DE PLANILHA BÁSICA (MÉTODO 50-30-20):
    Use este modelo para começar HOJE:
    
    - 50% NECESSIDADES BÁSICAS (Aluguel, Comida, Luz)
    - 30% DESEJOS PESSOAIS (Lazer, iFood, Assinaturas)
    - 20% INVESTIMENTOS (Sua liberdade futura)

    [ ] Exemplo: Se você ganha R$ 2.000,00:
        R$ 1.000,00 para o básico
        R$ 600,00 para lazer
        R$ 400,00 para INVESTIR
    
    -------------------------------------------
    💎 QUER O MÉTODO COMPLETO E A PLANILHA AUTOMÁTICA?
    Adquira nossa Mentoria Premium ou o E-book Avançado no site!
    Vitor Gabriel - Mente Milionária
    """

    st.download_button(
        label="🎁 BAIXAR BRINDE + PLANILHA BÁSICA",
        data=conteudo_brinde,
        file_name="Brinde_Mente_Milionaria_Vitor.txt"
    )

st.caption("© 2024 Vitor Gabriel - Mentoria Mente Milionária.")