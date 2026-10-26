import streamlit as st

def calcular_mace_z(idade: float, escolaridade: float, pontuacao_obtida: float):
    """
    Calcula a pontuação esperada e o Z-Score do M-ACE para a população portuguesa.
    Normas: Peixoto et al. (2021)
    """
    pontuacao_esperada = (-0.160 * idade) + (0.297 * escolaridade) + 34.816
    sd_amostra = 3.27
    z_score = (pontuacao_obtida - pontuacao_esperada) / sd_amostra
    return pontuacao_esperada, z_score

# Configuração da Página
st.set_page_config(
    page_title="Calculadora M-ACE (Versão Portuguesa)",
    page_icon="🧠",
    layout="centered"
)

# Título e Descrição
st.title("🧠 Calculadora de Z-Score: M-ACE")
st.markdown("""
Esta aplicação calcula a pontuação esperada e o **Z-Score** para a versão portuguesa do 
**Mini-Addenbrooke's Cognitive Examination (M-ACE)**, ajustados para a idade e escolaridade do sujeito 
*(Peixoto et al., 2021)*.
""")

st.divider()

# Formulário de Entrada
with st.form(key="mace_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        idade = st.number_input(
            "Idade (anos):",
            min_value=50,
            max_value=100,
            value=70,
            step=1,
            help="Idade do participante em anos."
        )
        escolaridade = st.number_input(
            "Escolaridade (anos completos):",
            min_value=0,
            max_value=25,
            value=4,
            step=1,
            help="Anos de escolaridade formal concluídos."
        )

    with col2:
        pontuacao_obtida = st.number_input(
            "Pontuação Bruta no M-ACE (0-30):",
            min_value=0,
            max_value=30,
            value=24,
            step=1,
            help="Resultado total obtido no M-ACE."
        )
    
    submit_button = st.form_submit_button(label="Calcular Z-Score", use_container_width=True)

# Apresentação dos Resultados
if submit_button:
    esperada, z_score = calcular_mace_z(idade, escolaridade, pontuacao_obtida)
    
    st.markdown("### Resultados")
    
    res_col1, res_col2, res_col3 = st.columns(3)
    res_col1.metric("Pontuação Obtida", f"{pontuacao_obtida}")
    res_col2.metric("Pontuação Esperada", f"{esperada:.2f}")
    res_col3.metric("Z-Score", f"{z_score:.2f}")
    
    st.divider()
    
    # Classificação / Interpretação Psicométrica
    st.markdown("### Interpretação do Z-Score")
    if z_score >= -1.0:
        st.success(f"**Z-Score = {z_score:.2f}**: Desempenho dentro do esperado para a idade e escolaridade (≥ -1.0 DP).")
    elif -1.5 <= z_score < -1.0:
        st.warning(f"**Z-Score = {z_score:.2f}**: Ligeiramente abaixo do esperado (-1.0 a -1.5 DP). Recomenda-se acompanhamento.")
    else:
        st.error(f"**Z-Score = {z_score:.2f}**: Significativamente abaixo do esperado (< -1.5 DP). Sugere necessidade de avaliação neuropsicológica aprofundada.")

# Rodapé informativo
st.caption("Normas: Peixoto, B., Machado, A., Peixoto, M., Pimentel, P., & Baeta, É. (2021). Normative data of the Portuguese version of the Mini-Addenbrooke's Cognitive Examination. Porto Biomedical Journal, 6(5), e138.")