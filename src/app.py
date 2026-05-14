import os
import sys
import subprocess


if os.environ.get("STREAMLIT_RUN_MODE") != "1":
    os.environ["STREAMLIT_RUN_MODE"] = "1"

    subprocess.run([
        sys.executable,
        "-m",
        "streamlit",
        "run",
        os.path.abspath(__file__)
    ])

    sys.exit()


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
                --text-title: #1f2937;
                --text-muted: #4b5563;
                --border-color: #e5e7eb;
                --shadow-color: rgba(15, 23, 42, 0.08);
                --button-bg: #ffffff;
                --button-text: #111827;
                --input-bg: #ffffff;
                --input-text: #111827;
            }

            @media (prefers-color-scheme: dark) {
                :root {
                    --bg-1: #0f172a;
                    --bg-2: #111827;
                    --card-bg: #1e293b;
                    --text-main: #f9fafb;
                    --text-title: #ffffff;
                    --text-muted: #cbd5e1;
                    --border-color: #475569;
                    --shadow-color: rgba(0, 0, 0, 0.45);
                    --button-bg: #334155;
                    --button-text: #ffffff;
                    --input-bg: #0f172a;
                    --input-text: #ffffff;
                }
            }

            .stApp {
                background: linear-gradient(180deg, var(--bg-1) 0%, var(--bg-2) 100%);
                color: var(--text-main) !important;
            }

            h1, h2, h3, h4, h5, h6,
            p, span, label, div {
                color: var(--text-main) !important;
            }

            [data-testid="stMarkdownContainer"] {
                color: var(--text-main) !important;
            }

            [data-testid="stMarkdownContainer"] p,
            [data-testid="stMarkdownContainer"] span,
            [data-testid="stMarkdownContainer"] h1,
            [data-testid="stMarkdownContainer"] h2,
            [data-testid="stMarkdownContainer"] h3 {
                color: var(--text-main) !important;
            }

            .main-title {
                text-align: center;
                font-size: 2.4rem;
                font-weight: 800;
                color: var(--text-title) !important;
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
                background: var(--card-bg);
                color: var(--text-main) !important;
                padding: 1.5rem;
                border-radius: 18px;
                box-shadow: 0 8px 24px var(--shadow-color);
                border: 1px solid var(--border-color);
                margin-bottom: 1.5rem;
            }

            .intro-card h3,
            .result-card h3 {
                color: var(--text-title) !important;
                margin-top: 0;
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
                color: var(--text-title) !important;
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
                border: 1px solid var(--border-color);
                padding: 0.75rem 1rem;
                font-weight: 700;
                transition: all 0.25s ease-in-out;
                box-shadow: 0 4px 12px var(--shadow-color);
            }

            div.stButton > button p,
            div.stButton > button span {
                color: var(--button-text) !important;
            }

            div.stButton > button:hover {
                transform: translateY(-3px) scale(1.02);
                box-shadow: 0 8px 18px var(--shadow-color);
                border: 1px solid var(--text-muted);
            }

            div.stButton > button:active {
                transform: translateY(0px) scale(0.98);
            }

            [data-testid="stMetric"] {
                background: var(--card-bg);
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

            [data-testid="stMetricValue"] {
                color: var(--text-title) !important;
            }

            .footer-note {
                text-align: center;
                color: var(--text-muted) !important;
                font-size: 0.9rem;
                margin-top: 1.2rem;
            }

            div[data-baseweb="select"] > div {
                background-color: var(--input-bg) !important;
                color: var(--input-text) !important;
                border-color: var(--border-color) !important;
            }

            div[data-baseweb="select"] span {
                color: var(--input-text) !important;
            }

            div[data-baseweb="popover"] {
                background-color: var(--card-bg) !important;
                color: var(--text-main) !important;
            }

            div[data-baseweb="option"] {
                background-color: var(--card-bg) !important;
                color: var(--text-main) !important;
            }

            div[data-baseweb="input"] input {
                background-color: var(--input-bg) !important;
                color: var(--input-text) !important;
            }

            input {
                color: var(--input-text) !important;
                background-color: var(--input-bg) !important;
            }

            .stRadio label,
            .stSelectbox label,
            .stNumberInput label {
                color: var(--text-main) !important;
            }

            .stRadio p,
            .stRadio span {
                color: var(--text-main) !important;
            }

            [data-testid="stExpander"] {
                background-color: var(--card-bg) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: 12px;
            }

            [data-testid="stExpander"] p,
            [data-testid="stExpander"] span,
            [data-testid="stExpander"] label {
                color: var(--text-main) !important;
            }

            [data-testid="stAlert"] p,
            [data-testid="stAlert"] span,
            [data-testid="stAlert"] div {
                color: inherit !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
def iniciar_estado():
    valores_iniciais = {
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
        "feedback_texto": "",
        "resposta_radio": None,
        "resposta_digitada": 0,
        "mostrar_ajuda": False,
    }

    for chave, valor in valores_iniciais.items():
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
    st.session_state.resposta_radio = None
    st.session_state.resposta_digitada = 0


def reiniciar_atividade():
    st.session_state.pagina = "inicio"
    st.session_state.operacao = "Todas"
    st.session_state.nivel = "Fácil"
    st.session_state.questao_atual = 1
    st.session_state.total_questoes = TOTAL_QUESTOES
    st.session_state.pontuacao = 0
    st.session_state.erros = 0
    st.session_state.mostrar_ajuda = False
    limpar_questao()


def iniciar_quiz(operacao, nivel):
    st.session_state.pagina = "quiz"
    st.session_state.operacao = operacao
    st.session_state.nivel = nivel
    st.session_state.questao_atual = 1
    st.session_state.pontuacao = 0
    st.session_state.erros = 0
    st.session_state.mostrar_ajuda = False
    limpar_questao()


def escolher_operacao(operacao):
    if operacao != "Todas":
        return operacao

    return random.choice(["Soma", "Subtração", "Multiplicação", "Divisão"])


def gerar_valores(operacao, nivel):
    if nivel == "Fácil":
        if operacao == "Soma":
            a = random.randint(1, 10)
            b = random.randint(1, 10)
        elif operacao == "Subtração":
            a = random.randint(2, 20)
            b = random.randint(1, a)
        elif operacao == "Multiplicação":
            a = random.randint(1, 10)
            b = random.randint(1, 10)
        else:
            b = random.randint(1, 10)
            resultado = random.randint(1, 10)
            a = b * resultado

        return a, b

    if nivel == "Médio":
        if operacao == "Soma":
            a = random.randint(10, 50)
            b = random.randint(10, 50)
        elif operacao == "Subtração":
            a = random.randint(20, 99)
            b = random.randint(10, a)
        elif operacao == "Multiplicação":
            a = random.randint(2, 12)
            b = random.randint(2, 15)
        else:
            b = random.randint(2, 12)
            resultado = random.randint(2, 15)
            a = b * resultado

        return a, b

    if operacao == "Soma":
        a = random.randint(50, 200)
        b = random.randint(50, 200)
    elif operacao == "Subtração":
        a = random.randint(100, 300)
        b = random.randint(50, a)
    elif operacao == "Multiplicação":
        a = random.randint(10, 25)
        b = random.randint(5, 20)
    else:
        b = random.randint(5, 20)
        resultado = random.randint(10, 25)
        a = b * resultado

    return a, b


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
        deslocamento = random.randint(-10, 10)

        if deslocamento == 0:
            deslocamento = 1

        alternativa = resposta_correta + deslocamento

        if alternativa < 0:
            alternativa = abs(alternativa) + random.randint(1, 3)

        alternativas.add(alternativa)

    lista = list(alternativas)
    random.shuffle(lista)

    return lista


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


def verificar_resposta():
    if st.session_state.modo_resposta == "alternativas":
        resposta_usuario = st.session_state.resposta_radio

        if resposta_usuario is None:
            st.warning("Selecione uma alternativa antes de responder.")
            return
    else:
        resposta_usuario = int(st.session_state.resposta_digitada)

    if resposta_usuario == st.session_state.resposta_correta:
        st.session_state.pontuacao += 1
        st.session_state.feedback_tipo = "success"
        st.session_state.feedback_texto = "Resposta correta! Muito bem, continue para a próxima questão."
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
                Ao final, você verá seu desempenho com acertos, erros e aproveitamento.
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
        st.write("**Fácil:** contas simples com alternativas para seleção.")
        st.write("**Médio:** contas um pouco maiores com resposta digitada.")
        st.write("**Difícil:** contas mais desafiadoras, mantendo as operações básicas.")

    col_a, col_b = st.columns(2)

    with col_a:
        if st.button("Iniciar atividade", use_container_width=True):
            iniciar_quiz(operacao, nivel)
            st.rerun()

    with col_b:
        if st.button("Como usar", use_container_width=True):
            st.session_state.mostrar_ajuda = True
            st.rerun()

    if st.session_state.mostrar_ajuda:
        st.markdown("### Como usar")
        st.write("1. Escolha a operação matemática desejada.")
        st.write("2. Selecione o nível de dificuldade.")
        st.write("3. Clique em **Iniciar atividade**.")
        st.write("4. Responda às 10 questões.")
        st.write("5. Veja seu resultado final e refaça a atividade se quiser praticar novamente.")

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
            <div class="instruction-text">Leia a questão com atenção e informe sua resposta.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if not st.session_state.respondido:
        if st.session_state.modo_resposta == "alternativas":
            st.radio(
                "Escolha uma alternativa:",
                st.session_state.alternativas,
                key="resposta_radio",
                index=None
            )
        else:
            st.number_input(
                "Digite sua resposta:",
                step=1,
                format="%d",
                key="resposta_digitada"
            )

        col_a, col_b = st.columns(2)

        with col_a:
            if st.button("Responder", use_container_width=True):
                verificar_resposta()
                st.rerun()

        with col_b:
            if st.button("← Voltar", use_container_width=True):
                reiniciar_atividade()
                st.rerun()

    else:
        if st.session_state.feedback_tipo == "success":
            st.success(st.session_state.feedback_texto)
        else:
            st.error(st.session_state.feedback_texto)

        col_a, col_b = st.columns(2)

        with col_a:
            if st.button("Próxima →", use_container_width=True):
                avancar_questao()
                st.rerun()

        with col_b:
            if st.button("← Voltar ao início", use_container_width=True):
                reiniciar_atividade()
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
        if st.button("Voltar ao início", use_container_width=True):
            reiniciar_atividade()
            st.rerun()


aplicar_estilo()
iniciar_estado()

if st.session_state.pagina == "inicio":
    tela_inicio()
elif st.session_state.pagina == "quiz":
    tela_quiz()
else:
    tela_resultado()
