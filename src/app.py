import os
import sys
import subprocess


def abrir_com_streamlit():
    if os.environ.get("RODANDO_COM_STREAMLIT") != "1":
        os.environ["RODANDO_COM_STREAMLIT"] = "1"

        subprocess.run([
            sys.executable,
            "-m",
            "streamlit",
            "run",
            os.path.abspath(__file__)
        ])

        sys.exit()


abrir_com_streamlit()


import random
import streamlit as st


st.set_page_config(
    page_title="Pratique Matemática Básica",
    page_icon="🧮",
    layout="centered"
)


TOTAL_QUESTOES = 10


def aplicar_estilo():
    st.markdown(
        """
        <style>
            :root {
                --bg-1: #f7f9fc;
                --bg-2: #eef3f8;
                --card-bg: #ffffff;
                --text-main: #111827;
                --text-muted: #374151;
                --border-color: #d1d5db;
                --shadow-color: rgba(15, 23, 42, 0.10);
                --button-bg: #ffffff;
                --button-hover: #f3f4f6;
                --button-text: #111827;
                --input-bg: #ffffff;
                --input-text: #111827;
                --input-border: #9ca3af;
            }

            @media (prefers-color-scheme: dark) {
                :root {
                    --bg-1: #020617;
                    --bg-2: #0f172a;
                    --card-bg: #1e293b;
                    --text-main: #f8fafc;
                    --text-muted: #e2e8f0;
                    --border-color: #64748b;
                    --shadow-color: rgba(0, 0, 0, 0.50);
                    --button-bg: #334155;
                    --button-hover: #475569;
                    --button-text: #ffffff;
                    --input-bg: #0f172a;
                    --input-text: #ffffff;
                    --input-border: #94a3b8;
                }
            }

            html, body, .stApp {
                background: linear-gradient(180deg, var(--bg-1), var(--bg-2)) !important;
                color: var(--text-main) !important;
            }

            [data-testid="stAppViewContainer"] {
                background: linear-gradient(180deg, var(--bg-1), var(--bg-2)) !important;
                color: var(--text-main) !important;
            }

            [data-testid="stHeader"] {
                background: transparent !important;
            }

            .block-container {
                color: var(--text-main) !important;
            }

            h1, h2, h3, h4, h5, h6,
            p, span, label, div {
                color: var(--text-main) !important;
            }

            .main-title {
                text-align: center;
                font-size: 2.4rem;
                font-weight: 800;
                color: var(--text-main) !important;
                margin-bottom: 0.2rem;
            }

            .subtitle {
                text-align: center;
                color: var(--text-muted) !important;
                font-size: 1rem;
                margin-bottom: 1.5rem;
            }

            .intro-card,
            .question-card,
            .result-card {
                background: var(--card-bg) !important;
                color: var(--text-main) !important;
                padding: 1.5rem;
                border-radius: 18px;
                box-shadow: 0 8px 24px var(--shadow-color);
                border: 1px solid var(--border-color);
                margin-bottom: 1.5rem;
            }

            .intro-card p,
            .result-card p {
                color: var(--text-muted) !important;
                line-height: 1.6;
            }

            .question-card {
                text-align: center;
                margin-top: 1rem;
                margin-bottom: 1rem;
            }

            .question-text {
                font-size: 2rem;
                font-weight: 800;
                color: var(--text-main) !important;
                margin-bottom: 0.5rem;
            }

            .instruction-text {
                color: var(--text-muted) !important;
                font-size: 1rem;
            }

            div.stButton > button {
                background-color: var(--button-bg) !important;
                color: var(--button-text) !important;
                border-radius: 12px;
                border: 1px solid var(--border-color) !important;
                padding: 0.75rem 1rem;
                font-weight: 700;
                transition: all 0.25s ease-in-out;
                box-shadow: 0 4px 12px var(--shadow-color);
            }

            div.stButton > button:hover {
                background-color: var(--button-hover) !important;
                color: var(--button-text) !important;
                transform: translateY(-2px);
                box-shadow: 0 8px 18px var(--shadow-color);
            }

            div.stButton > button p,
            div.stButton > button span {
                color: var(--button-text) !important;
            }

            [data-testid="stMetric"] {
                background: var(--card-bg) !important;
                padding: 1rem;
                border-radius: 16px;
                border: 1px solid var(--border-color);
                box-shadow: 0 4px 14px var(--shadow-color);
            }

            [data-testid="stMetric"] label,
            [data-testid="stMetric"] div,
            [data-testid="stMetric"] span {
                color: var(--text-main) !important;
            }

            div[data-baseweb="select"] > div {
                background-color: var(--input-bg) !important;
                color: var(--input-text) !important;
                border: 1px solid var(--input-border) !important;
            }

            div[data-baseweb="select"] span,
            div[data-baseweb="select"] div {
                color: var(--input-text) !important;
            }

            div[data-baseweb="input"] {
                background-color: var(--input-bg) !important;
            }

            div[data-baseweb="input"] input,
            input {
                background-color: var(--input-bg) !important;
                color: var(--input-text) !important;
            }

            [role="radiogroup"] label {
                color: var(--text-main) !important;
            }

            [data-testid="stExpander"] {
                background-color: var(--card-bg) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: 12px;
            }

            [data-testid="stAlert"] p,
            [data-testid="stAlert"] span,
            [data-testid="stAlert"] div {
                color: inherit !important;
            }

            .footer-note {
                text-align: center;
                color: var(--text-muted) !important;
                font-size: 0.9rem;
                margin-top: 1.2rem;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def iniciar_estado():
    dados_iniciais = {
        "pagina": "inicio",
        "operacao": "Todas",
        "nivel": "Fácil",
        "questao_atual": 1,
        "total_questoes": TOTAL_QUESTOES,
        "pontuacao": 0,
        "erros": 0,
        "enunciado": "",
        "resposta_correta": 0,
        "alternativas": [],
        "modo_resposta": "alternativas",
        "respondido": False,
        "feedback_tipo": "",
        "feedback_texto": ""
    }

    for chave, valor in dados_iniciais.items():
        if chave not in st.session_state:
            st.session_state[chave] = valor


def limpar_questao():
    st.session_state.enunciado = ""
    st.session_state.resposta_correta = 0
    st.session_state.alternativas = []
    st.session_state.modo_resposta = "alternativas"
    st.session_state.respondido = False
    st.session_state.feedback_tipo = ""
    st.session_state.feedback_texto = ""


def voltar_tela_inicial():
    st.session_state.pagina = "inicio"
    st.session_state.questao_atual = 1
    st.session_state.pontuacao = 0
    st.session_state.erros = 0
    limpar_questao()


def iniciar_quiz(operacao, nivel):
    st.session_state.pagina = "quiz"
    st.session_state.operacao = operacao
    st.session_state.nivel = nivel
    st.session_state.questao_atual = 1
    st.session_state.pontuacao = 0
    st.session_state.erros = 0
    limpar_questao()


def escolher_operacao(operacao):
    if operacao == "Todas":
        return random.choice(["Soma", "Subtração", "Multiplicação", "Divisão"])

    return operacao


def gerar_valores(operacao, nivel):
    if nivel == "Fácil":
        if operacao == "Soma":
            return random.randint(1, 10), random.randint(1, 10)

        if operacao == "Subtração":
            a = random.randint(2, 20)
            b = random.randint(1, a)
            return a, b

        if operacao == "Multiplicação":
            return random.randint(1, 10), random.randint(1, 10)

        b = random.randint(1, 10)
        resultado = random.randint(1, 10)
        return b * resultado, b

    if nivel == "Médio":
        if operacao == "Soma":
            return random.randint(10, 50), random.randint(10, 50)

        if operacao == "Subtração":
            a = random.randint(20, 99)
            b = random.randint(10, a)
            return a, b

        if operacao == "Multiplicação":
            return random.randint(2, 12), random.randint(2, 15)

        b = random.randint(2, 12)
        resultado = random.randint(2, 15)
        return b * resultado, b

    if operacao == "Soma":
        return random.randint(50, 200), random.randint(50, 200)

    if operacao == "Subtração":
        a = random.randint(100, 300)
        b = random.randint(50, a)
        return a, b

    if operacao == "Multiplicação":
        return random.randint(10, 25), random.randint(5, 20)

    b = random.randint(5, 20)
    resultado = random.randint(10, 25)
    return b * resultado, b


def montar_enunciado_e_resposta(operacao, a, b):
    if operacao == "Soma":
        return f"Quanto é {a} + {b}?", a + b

    if operacao == "Subtração":
        return f"Quanto é {a} - {b}?", a - b

    if operacao == "Multiplicação":
        return f"Quanto é {a} × {b}?", a * b

    return f"Quanto é {a} ÷ {b}?", a // b


def gerar_alternativas(resposta_correta):
    alternativas = {resposta_correta}

    while len(alternativas) < 4:
        erro = random.randint(-10, 10)

        if erro == 0:
            erro = 1

        alternativa = resposta_correta + erro

        if alternativa < 0:
            alternativa = abs(alternativa) + random.randint(1, 3)

        alternativas.add(alternativa)

    alternativas = list(alternativas)
    random.shuffle(alternativas)

    return alternativas


def gerar_questao():
    operacao_escolhida = escolher_operacao(st.session_state.operacao)
    a, b = gerar_valores(operacao_escolhida, st.session_state.nivel)
    enunciado, resposta = montar_enunciado_e_resposta(operacao_escolhida, a, b)

    st.session_state.enunciado = enunciado
    st.session_state.resposta_correta = resposta

    if st.session_state.nivel == "Fácil":
        st.session_state.modo_resposta = "alternativas"
        st.session_state.alternativas = gerar_alternativas(resposta)
    else:
        st.session_state.modo_resposta = "digitado"
        st.session_state.alternativas = []


def verificar_resposta(resposta_usuario):
    if resposta_usuario is None:
        st.warning("Escolha uma resposta antes de continuar.")
        return

    resposta_usuario = int(resposta_usuario)

    if resposta_usuario == st.session_state.resposta_correta:
        st.session_state.pontuacao += 1
        st.session_state.feedback_tipo = "success"
        st.session_state.feedback_texto = "Resposta correta! Muito bem."
    else:
        st.session_state.erros += 1
        st.session_state.feedback_tipo = "error"
        st.session_state.feedback_texto = (
            f"Resposta incorreta. A resposta certa era {st.session_state.resposta_correta}."
        )

    st.session_state.respondido = True


def avancar_questao():
    if st.session_state.questao_atual >= st.session_state.total_questoes:
        st.session_state.pagina = "resultado"
    else:
        st.session_state.questao_atual += 1
        limpar_questao()


def mostrar_cabecalho():
    st.markdown(
        '<div class="main-title">🧮 Pratique Matemática Básica</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Soma • Subtração • Multiplicação • Divisão</div>',
        unsafe_allow_html=True
    )


def tela_inicio():
    mostrar_cabecalho()

    st.markdown(
        """
        <div class="intro-card">
            <h3>Bem-vindo à atividade</h3>
            <p>
                Este sistema foi criado para ajudar no treino de operações matemáticas básicas
                de forma simples, visual e progressiva.
            </p>
            <p>
                Escolha a operação, selecione o nível de dificuldade e responda às questões.
                Ao final, você verá seu desempenho.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Configurações da atividade")

    operacao = st.selectbox(
        "Escolha a operação:",
        ["Todas", "Soma", "Subtração", "Multiplicação", "Divisão"]
    )

    nivel = st.selectbox(
        "Escolha o nível:",
        ["Fácil", "Médio", "Difícil"]
    )

    with st.expander("Entenda os níveis"):
        st.write("**Fácil:** contas simples com alternativas.")
        st.write("**Médio:** contas maiores com resposta digitada.")
        st.write("**Difícil:** contas mais desafiadoras com resposta digitada.")

    if st.button("Iniciar atividade", use_container_width=True):
        iniciar_quiz(operacao, nivel)
        st.rerun()

    st.markdown(
        '<div class="footer-note">Projeto desenvolvido para apoio ao aprendizado de matemática básica.</div>',
        unsafe_allow_html=True
    )


def tela_quiz():
    mostrar_cabecalho()

    if st.session_state.enunciado == "":
        gerar_questao()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Questão", f"{st.session_state.questao_atual}/{st.session_state.total_questoes}")

    with col2:
        st.metric("Acertos", st.session_state.pontuacao)

    with col3:
        st.metric("Erros", st.session_state.erros)

    st.markdown(
        f"""
        <div class="question-card">
            <div class="question-text">{st.session_state.enunciado}</div>
            <div class="instruction-text">Leia com atenção e informe sua resposta.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if not st.session_state.respondido:
        resposta_usuario = None

        if st.session_state.modo_resposta == "alternativas":
            resposta_usuario = st.radio(
                "Escolha uma alternativa:",
                st.session_state.alternativas,
                key=f"resposta_radio_{st.session_state.questao_atual}",
                index=None
            )
        else:
            resposta_usuario = st.number_input(
                "Digite sua resposta:",
                step=1,
                format="%d",
                key=f"resposta_digitada_{st.session_state.questao_atual}"
            )

        if st.button("Responder", use_container_width=True):
            verificar_resposta(resposta_usuario)
            st.rerun()

    else:
        if st.session_state.feedback_tipo == "success":
            st.success(st.session_state.feedback_texto)
        else:
            st.error(st.session_state.feedback_texto)

        if st.button("Próxima →", use_container_width=True):
            avancar_questao()
            st.rerun()


def tela_resultado():
    mostrar_cabecalho()

    st.markdown(
        """
        <div class="result-card">
            <h3>Resultado da atividade</h3>
            <p>Confira abaixo seu desempenho final nesta rodada de exercícios.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    acertos = st.session_state.pontuacao
    erros = st.session_state.erros
    total = st.session_state.total_questoes
    aproveitamento = int((acertos / total) * 100)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Acertos", acertos)

    with col2:
        st.metric("Erros", erros)

    with col3:
        st.metric("Aproveitamento", f"{aproveitamento}%")

    if aproveitamento >= 80:
        st.success("Ótimo resultado! Você demonstrou bom domínio das operações praticadas.")
    elif aproveitamento >= 50:
        st.info("Bom trabalho! Você está evoluindo, mas ainda pode praticar mais.")
    else:
        st.warning("Continue praticando. Repetir a atividade ajuda a melhorar o desempenho.")

    col_a, col_b = st.columns(2)

    with col_a:
        if st.button("Refazer atividade", use_container_width=True):
            iniciar_quiz(st.session_state.operacao, st.session_state.nivel)
            st.rerun()

    with col_b:
        if st.button("Voltar para tela inicial", use_container_width=True):
            voltar_tela_inicial()
            st.rerun()


aplicar_estilo()
iniciar_estado()

if st.session_state.pagina == "inicio":
    tela_inicio()
elif st.session_state.pagina == "quiz":
    tela_quiz()
elif st.session_state.pagina == "resultado":
    tela_resultado()
