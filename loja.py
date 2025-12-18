import streamlit as st
import random

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
    /* Estilo da área de brinde com fundo de imagem */
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
    .card-mentalidade {
        background: rgba(255, 215, 0, 0.1);
        padding: 12px;
        border-left: 5px solid #FFD700;
        margin-bottom: 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    /* Estilo para a roleta */
    .roleta-box {
        background-color: rgba(255, 215, 0, 0.15); /* Fundo dourado suave */
        border: 2px solid #FFD700; /* Borda dourada */
        border-radius: 15px;
        padding: 25px;
        margin-top: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Título e Cabeçalho ---
st.title("🚀 Mentoria Mente Milionária")
st.subheader("Vitor Gabriel - Educação Financeira")

# --- SEÇÃO DO VÍDEO ---
video_url = "https://www.youtube.com/watch?v=HSXcvFVtsdM" 
st.video(video_url)

st.markdown("---")

# --- SEÇÃO DE PRODUTOS ---
st.header("🛒 Escolha seu Plano")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💎 Mentoria Premium")
    st.write("Acesso vitalício + Suporte VIP")
    st.markdown("## R$ 100,00")
    with st.expander("PAGAR COM PIX"):
        st.code("12022298675", language=None)
        st.write("Titular: Vitor Gabriel Firmiano")
        st.link_button("✅ JÁ PAGUEI! ACESSAR", "https://wa.me/27996704422?text=Fiz%20o%20PIX%20de%20100%20da%20Mentoria")

with col2:
    st.markdown("### 📚 E-book Avançado")
    st.write("Guia prático da riqueza")
    st.markdown("## R$ 20,00")
    with st.expander("PAGAR COM PIX"):
        st.code("12022298675", language=None)
        st.write("Titular: Vitor Gabriel Firmiano")
        st.link_button("✅ JÁ PAGUEI! ACESSAR", "https://wa.me/27996704422?text=Fiz%20o%20PIX%20de%2020%20do%20Ebook")

st.markdown("---")

# --- ÁREA DE BRINDE (ISCA DIGITAL) ---
st.header("🎁 Bônus: Checklist Mentalidade Milionária")

with st.container():
    # Quadro com imagem de fundo
    st.markdown("""
        <div class="area-brinde">
            <h2 style="color: #FFD700 !important; text-shadow: 2px 2px 10px #000;">7 MUDANÇAS MENTAIS</h2>
            <p style="text-shadow: 1px 1px 5px #000;">O guia que você precisa para começar a enriquecer.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Lista visual das mudanças
    st.markdown("""
    <div class="card-mentalidade">🧠 1. De Escassez para Abundância</div>
    <div class="card-mentalidade">🛠️ 2. Foco em Soluções, Não em Problemas</div>
    <div class="card-mentalidade">⏳ 3. Pensar no Longo Prazo</div>
    <div class="card-mentalidade">📖 4. Investir em Conhecimento</div>
    <div class="card-mentalidade">💎 5. Trabalhar por Valor, Não por Tempo</div>
    <div class="card-mentalidade">🎮 6. Assumir Responsabilidade Total</div>
    <div class="card-mentalidade">🏃 7. Executar Mesmo com Medo</div>
    """, unsafe_allow_html=True)

    # Conteúdo do arquivo de texto (Isca Bridge)
    brinde_texto = (
        "CHECKLIST MENTALIDADE MILIONARIA - VITOR GABRIEL\n"
        "==============================================\n\n"
        "1. DE ESCASSEZ PARA ABUNDANCIA: O dinheiro e resultado de valor gerado.\n"
        "2. FOCO EM SOLUCOES: Milionarios resolvem problemas.\n"
        "3. PENSAR NO LONGO PRAZO: Nao troque liberdade por prazer imediato.\n"
        "4. INVESTIR EM CONHECIMENTO: Seu maior ativo e sua mente.\n"
        "5. TRABALHAR POR VALOR: Gere impacto para ganhar mais.\n"
        "6. RESPONSABILIDADE TOTAL: Voce e o dono dos seus resultados.\n"
        "7. EXECUCAO COM MEDO: Nao espere o momento perfeito. Comece!\n\n"
        "==============================================\n"
        "QUER O METODO COMPLETO? CLIQUE NO LINK DO SITE E ADQUIRA A MENTORIA!"
    )

    st.download_button(
        label="📥 BAIXAR CHECKLIST COMPLETO (GRÁTIS)",
        data=brinde_texto,
        file_name="Checklist_Mente_Milionaria.txt",
        mime="text/plain",
        use_container_width=True
    )

st.markdown("---")

# --- SEÇÃO DA ROLETA DA SORTE ---
st.header("✨ Gire a Roleta e Ganhe uma Dica Milionária!")

dicas_milionarias = [
    "Dica 1: Invista em você mesmo. Conhecimento é o ativo que mais rende.",
    "Dica 2: Faça o dinheiro trabalhar para você, não o contrário. Comece a investir hoje!",
    "Dica 3: Economize primeiro, gaste depois. Seu futuro financeiro agradece.",
    "Dica 4: Cerque-se de pessoas que te inspiram a crescer. Sua rede é seu patrimônio.",
    "Dica 5: Tenha um plano claro para seu dinheiro. Orçamento é a base da riqueza.",
    "Dica 6: Aja como se fosse impossível falhar. Sua mentalidade cria sua realidade.",
    "Dica 7: Aprenda a dizer 'não' para gastos desnecessários. Disciplina é poder.",
    "Dica 8: Diversifique suas fontes de renda. Nunca dependa de uma só.",
    "Dica 9: Automatize suas economias e investimentos. Torne o processo fácil.",
    "Dica 10: Seja paciente. A riqueza se constrói com consistência, não com velocidade."
]

with st.container():
    st.markdown('<div class="roleta-box">', unsafe_allow_html=True)
    st.markdown("<h3>Pronto para sua dica de ouro?</h3>", unsafe_allow_html=True)
    
    if st.button("🍀 GIRAR ROLETA DA SORTE 🍀", key="roleta_button"):
        dica_sorteada = random.choice(dicas_milionarias)
        st.success(f"**VOCÊ GANHOU!** 🎉 Aqui está sua dica milionária: \n\n {dica_sorteada}")
        st.info("Gire novamente para outra dica!")
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- CRONOGRAMA ---
st.header("📅 O que você vai aprender")
st.markdown("""
* **Semana 1:** Mindset Milionário | **Semana 2:** Organização de Dívidas
* **Semana 3:** Orçamento Inteligente | **Semana 4:** Reserva de Emergência
* **Semana 5:** Multiplicação de Renda | **Semana 6:** Plano de Ação Final
""")

st.markdown("---")

# --- RODAPÉ ---
st.link_button("🔵 VISITAR MEU FACEBOOK", "https://www.facebook.com/profile.php?id=61553400154748")
st.caption("© 2024 Vitor Gabriel - Mentoria Mente Milionária.")