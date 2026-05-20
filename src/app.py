import os
import random
import subprocess
import sys


def abrir_com_streamlit():
    if os.environ.get("RODANDO_COM_STREAMLIT") != "1":
        os.environ["RODANDO_COM_STREAMLIT"] = "1"

        subprocess.run([
            sys.executable,
            "-m",
            "streamlit",
            "run",
            os.path.abspath(__file__),
        ])

        sys.exit()


abrir_com_streamlit()


import streamlit as st


st.set_page_config(
    page_title="Pratique Matemática Básica",
    page_icon="🧮",
    layout="centered",
)


TOTAL_QUESTOES = 10
FRUTAS = ["🍎", "🍌", "🍇", "🍊", "🍓", "⭐"]
MENSAGENS_ACERTO = [
    "Muito bem! Você acertou! 🎉",
    "Parabéns! Resposta correta! ✅",
    "Arrasou na conta! 🌟",
    "Isso aí! Seu raciocínio brilhou! ✨",
]
MENSAGENS_ERRO = [
    "Quase lá! Tente novamente na próxima! 😊",
    "Ops! Essa não foi, mas continue tentando! 💪",
    "Boa tentativa! Errar também ajuda a aprender. 🌈",
    "Não desanime! A próxima pode ser sua. 🚀",
]


def aplicar_estilo():
    st.markdown(
        """
        <style>
            :root {
                --bg-start: #fff7d6;
                --bg-mid: #e6f7ff;
                --bg-end: #f4edff;
                --surface: rgba(255, 255, 255, 0.92);
                --surface-strong: #ffffff;
                --text-main: #243044;
                --text-muted: #526071;
                --brand: #4f8cff;
                --brand-2: #ff8fb3;
                --brand-3: #38c7a5;
                --warning: #ffbc42;
                --success: #1fbf75;
                --error: #ef5b72;
                --border: rgba(79, 140, 255, 0.20);
                --shadow: rgba(36, 48, 68, 0.14);
                --input-bg: #ffffff;
                --option-bg: #eef6ff;
                --option-border: #6aa2ff;
                --option-hover: #dcecff;
            }

            @media (prefers-color-scheme: dark) {
                :root {
                    --bg-start: #19233a;
                    --bg-mid: #112f3d;
                    --bg-end: #281d3d;
                    --surface: rgba(27, 37, 59, 0.94);
                    --surface-strong: #202b43;
                    --text-main: #f8fbff;
                    --text-muted: #d3def0;
                    --brand: #7fb0ff;
                    --brand-2: #ff9dc2;
                    --brand-3: #5be0c0;
                    --warning: #ffd166;
                    --success: #57d68d;
                    --error: #ff7b91;
                    --border: rgba(255, 255, 255, 0.16);
                    --shadow: rgba(0, 0, 0, 0.38);
                    --input-bg: #172138;
                    --option-bg: #263653;
                    --option-border: #8fbaff;
                    --option-hover: #314467;
                }
            }

            * {
                box-sizing: border-box;
            }

            html, body, .stApp,
            [data-testid="stAppViewContainer"] {
                background:
                    radial-gradient(circle at top left, rgba(255, 143, 179, 0.24), transparent 30rem),
                    radial-gradient(circle at bottom right, rgba(56, 199, 165, 0.22), transparent 28rem),
                    linear-gradient(135deg, var(--bg-start), var(--bg-mid) 48%, var(--bg-end)) !important;
                color: var(--text-main) !important;
            }

            [data-testid="stHeader"] {
                background: transparent !important;
            }

            .block-container {
                max-width: 920px;
                padding-top: 1.5rem;
                padding-bottom: 2rem;
                color: var(--text-main) !important;
            }

            h1, h2, h3, h4, h5, h6,
            p, span, label, div {
                color: var(--text-main) !important;
            }

            @keyframes floatIn {
                from {
                    opacity: 0;
                    transform: translateY(12px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            @keyframes happyPop {
                0% { transform: scale(0.96); }
                55% { transform: scale(1.03); }
                100% { transform: scale(1); }
            }

            @keyframes gentleShake {
                0%, 100% { transform: translateX(0); }
                20% { transform: translateX(-7px); }
                40% { transform: translateX(7px); }
                60% { transform: translateX(-4px); }
                80% { transform: translateX(4px); }
            }

            .app-shell {
                animation: floatIn 0.42s ease both;
            }

            .hero {
                text-align: center;
                padding: 1.35rem 1rem 1.1rem;
            }

            .main-title {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 0.55rem;
                flex-wrap: wrap;
                margin: 0;
                color: var(--text-main) !important;
                font-size: clamp(2rem, 6vw, 3.15rem);
                font-weight: 900;
                letter-spacing: 0;
                line-height: 1.08;
            }

            .subtitle {
                color: var(--text-muted) !important;
                font-size: clamp(1rem, 2.8vw, 1.15rem);
                margin: 0.7rem auto 0;
                max-width: 680px;
                line-height: 1.5;
            }

            .panel,
            .question-panel,
            .feedback-card,
            .result-panel {
                background: var(--surface) !important;
                border: 1px solid var(--border);
                border-radius: 22px;
                box-shadow: 0 18px 48px var(--shadow);
                color: var(--text-main) !important;
                margin: 0.95rem 0;
                padding: clamp(1rem, 4vw, 1.6rem);
                animation: floatIn 0.42s ease both;
            }

            .panel h3,
            .result-panel h3 {
                margin: 0 0 0.55rem;
                font-size: clamp(1.35rem, 4vw, 1.7rem);
                line-height: 1.2;
            }

            .panel p,
            .result-panel p,
            .helper-text {
                color: var(--text-muted) !important;
                line-height: 1.65;
                margin: 0.4rem 0;
            }

            .choice-title {
                font-size: 1.1rem;
                font-weight: 800;
                margin: 1.2rem 0 0.4rem;
            }

            .badge-row {
                display: flex;
                flex-wrap: wrap;
                gap: 0.55rem;
                justify-content: center;
                margin-top: 1rem;
            }

            .soft-badge {
                background: linear-gradient(135deg, rgba(79, 140, 255, 0.16), rgba(56, 199, 165, 0.15));
                border: 1px solid var(--border);
                border-radius: 999px;
                color: var(--text-main) !important;
                font-weight: 800;
                padding: 0.45rem 0.85rem;
                white-space: nowrap;
            }

            .question-panel {
                text-align: center;
                border-color: rgba(255, 188, 66, 0.45);
            }

            .question-kicker {
                color: var(--text-muted) !important;
                font-size: 0.95rem;
                font-weight: 800;
                margin-bottom: 0.55rem;
                text-transform: uppercase;
            }

            .question-text {
                color: var(--text-main) !important;
                font-size: clamp(2rem, 8vw, 3.3rem);
                font-weight: 900;
                line-height: 1.18;
                margin-bottom: 0.75rem;
                overflow-wrap: anywhere;
            }

            .instruction-text {
                color: var(--text-muted) !important;
                font-size: 1rem;
                line-height: 1.5;
            }

            .fruit-line {
                display: inline-block;
                max-width: 100%;
                overflow-wrap: anywhere;
                line-height: 1.35;
                font-size: clamp(2rem, 7vw, 3.1rem);
            }

            .progress-label {
                align-items: center;
                display: flex;
                font-weight: 800;
                justify-content: space-between;
                margin: 0.65rem 0 0.35rem;
            }

            .feedback-card {
                font-size: clamp(1.08rem, 3.8vw, 1.35rem);
                font-weight: 850;
                line-height: 1.45;
                text-align: center;
            }

            .feedback-card.success {
                background: linear-gradient(135deg, rgba(31, 191, 117, 0.18), var(--surface)) !important;
                border-color: rgba(31, 191, 117, 0.46);
                animation: happyPop 0.45s ease both;
            }

            .feedback-card.error {
                background: linear-gradient(135deg, rgba(239, 91, 114, 0.16), var(--surface)) !important;
                border-color: rgba(239, 91, 114, 0.42);
                animation: gentleShake 0.42s ease both;
            }

            .answer-note {
                color: var(--text-muted) !important;
                display: block;
                font-size: 0.98rem;
                font-weight: 700;
                margin-top: 0.35rem;
            }

            div.stButton > button {
                align-items: center;
                background: linear-gradient(135deg, #4f8cff, #38c7a5) !important;
                border: 2px solid rgba(36, 48, 68, 0.16) !important;
                border-radius: 18px;
                box-shadow: 0 10px 22px var(--shadow);
                color: #ffffff !important;
                display: flex;
                font-size: 1.02rem;
                font-weight: 850;
                justify-content: center;
                line-height: 1.2;
                min-height: 3.15rem;
                padding: 0.78rem 1rem;
                text-align: center;
                transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease, filter 0.18s ease;
            }

            div.stButton > button:hover {
                border-color: rgba(79, 140, 255, 0.56) !important;
                box-shadow: 0 16px 30px var(--shadow);
                filter: saturate(1.06);
                transform: translateY(-3px);
            }

            div.stButton > button:active {
                box-shadow: 0 6px 14px var(--shadow);
                transform: translateY(0) scale(0.99);
            }

            div.stButton > button *,
            div.stButton > button div,
            div.stButton > button p,
            div.stButton > button span {
                color: #ffffff !important;
                font-weight: 850 !important;
                opacity: 1 !important;
                visibility: visible !important;
            }

            [data-testid="stMetric"] {
                background: var(--surface-strong) !important;
                border: 1px solid var(--border);
                border-radius: 18px;
                box-shadow: 0 10px 24px var(--shadow);
                padding: 0.9rem 1rem;
            }

            [data-testid="stMetric"] label,
            [data-testid="stMetric"] div,
            [data-testid="stMetric"] span {
                color: var(--text-main) !important;
            }

            .stProgress > div > div > div > div {
                background: linear-gradient(90deg, var(--brand), var(--brand-2), var(--brand-3)) !important;
            }

            div[data-baseweb="select"] > div,
            div[data-baseweb="input"],
            div[data-baseweb="input"] input,
            input {
                background-color: var(--input-bg) !important;
                border-color: var(--border) !important;
                color: var(--text-main) !important;
                border-radius: 14px !important;
            }

            div[data-baseweb="select"] span,
            div[data-baseweb="select"] div {
                color: var(--text-main) !important;
            }

            [role="radiogroup"] {
                background: var(--surface);
                border: 1px solid var(--border);
                border-radius: 18px;
                display: flex;
                flex-wrap: wrap;
                gap: 0.55rem;
                padding: 0.75rem;
            }

            [role="radiogroup"] label {
                align-items: center;
                background: var(--option-bg);
                border: 2px solid var(--option-border);
                border-radius: 16px;
                color: var(--text-main) !important;
                cursor: pointer;
                display: flex;
                flex: 1 1 5rem;
                font-weight: 750;
                gap: 0.45rem;
                justify-content: center;
                min-width: 8.5rem;
                padding: 0.65rem 0.75rem;
                text-align: center;
                transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
                white-space: nowrap;
            }

            [role="radiogroup"] label:hover {
                background: var(--option-hover);
                border-color: rgba(79, 140, 255, 0.56);
                box-shadow: 0 8px 18px var(--shadow);
                transform: translateY(-2px);
            }

            [role="radiogroup"] label p,
            [role="radiogroup"] label span,
            [role="radiogroup"] label div {
                color: var(--text-main) !important;
                font-size: 1.08rem;
                font-weight: 850;
                line-height: 1.2;
                margin: 0 !important;
                overflow-wrap: normal;
                white-space: nowrap;
                word-break: keep-all;
            }

            [data-testid="stExpander"] {
                background-color: var(--surface) !important;
                border: 1px solid var(--border) !important;
                border-radius: 18px;
                box-shadow: 0 8px 20px var(--shadow);
            }

            [data-testid="stAlert"] {
                border-radius: 16px;
            }

            [data-testid="stAlert"] p,
            [data-testid="stAlert"] span,
            [data-testid="stAlert"] div {
                color: inherit !important;
            }

            .footer-note {
                color: var(--text-muted) !important;
                font-size: 0.95rem;
                line-height: 1.5;
                margin-top: 1.2rem;
                text-align: center;
            }

            @media (max-width: 640px) {
                .block-container {
                    padding-left: 1rem;
                    padding-right: 1rem;
                }

                .hero {
                    padding-top: 0.8rem;
                }

                .panel,
                .question-panel,
                .feedback-card,
                .result-panel {
                    border-radius: 18px;
                }

                div.stButton > button {
                    min-height: 3rem;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def iniciar_estado():
    dados_iniciais = {
        "pagina": "inicio",
        "operacao": "Todas",
        "nivel": "Fácil",
        "modo_basico": "Números",
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
    }

    for chave, valor in dados_iniciais.items():
        if chave not in st.session_state:
            st.session_state[chave] = valor

    valores_validos = {
        "pagina": ["inicio", "quiz", "resultado"],
        "operacao": ["Todas", "Soma", "Subtração", "Multiplicação", "Divisão"],
        "nivel": ["Básico", "Fácil", "Médio", "Difícil"],
        "modo_basico": ["Números", "Figuras"],
        "modo_resposta": ["alternativas", "digitado"],
        "feedback_tipo": ["", "success", "error"],
    }

    for chave, opcoes in valores_validos.items():
        if st.session_state[chave] not in opcoes:
            st.session_state[chave] = dados_iniciais[chave]


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


def iniciar_quiz(operacao, nivel, modo_basico="Números"):
    st.session_state.pagina = "quiz"
    st.session_state.operacao = operacao
    st.session_state.nivel = nivel
    st.session_state.modo_basico = modo_basico
    st.session_state.questao_atual = 1
    st.session_state.pontuacao = 0
    st.session_state.erros = 0
    limpar_questao()


def escolher_operacao(operacao):
    if st.session_state.nivel == "Básico":
        return random.choice(["Soma", "Subtração"])

    if operacao == "Todas":
        return random.choice(["Soma", "Subtração", "Multiplicação", "Divisão"])

    return operacao


def gerar_valores(operacao, nivel):
    if nivel == "Básico":
        if operacao == "Soma":
            return random.randint(0, 10), random.randint(0, 10)

        a = random.randint(0, 10)
        b = random.randint(0, a)
        return a, b

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
    if st.session_state.nivel == "Básico" and st.session_state.modo_basico == "Figuras":
        fruta = random.choice(FRUTAS)
        grupo_a = fruta * a if a > 0 else "0"
        grupo_b = fruta * b if b > 0 else "0"
        simbolo = "+" if operacao == "Soma" else "-"
        resposta = a + b if operacao == "Soma" else a - b
        return f'<span class="fruit-line">{grupo_a} {simbolo} {grupo_b} = ?</span>', resposta

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

    if st.session_state.nivel in ["Básico", "Fácil"]:
        st.session_state.modo_resposta = "alternativas"
        st.session_state.alternativas = gerar_alternativas(resposta)
    else:
        st.session_state.modo_resposta = "digitado"
        st.session_state.alternativas = []


def verificar_resposta(resposta_usuario):
    if resposta_usuario is None:
        st.warning("Escolha uma resposta antes de continuar. 🙂")
        return

    resposta_usuario = int(resposta_usuario)

    if resposta_usuario == st.session_state.resposta_correta:
        st.session_state.pontuacao += 1
        st.session_state.feedback_tipo = "success"
        st.session_state.feedback_texto = random.choice(MENSAGENS_ACERTO)
    else:
        st.session_state.erros += 1
        st.session_state.feedback_tipo = "error"
        st.session_state.feedback_texto = random.choice(MENSAGENS_ERRO)

    st.session_state.respondido = True


def avancar_questao():
    if st.session_state.questao_atual >= st.session_state.total_questoes:
        st.session_state.pagina = "resultado"
    else:
        st.session_state.questao_atual += 1
        limpar_questao()


def mostrar_cabecalho():
    st.markdown(
        """
        <div class="app-shell">
            <section class="hero">
                <h1 class="main-title">🧮 Pratique Matemática</h1>
                <p class="subtitle">
                    Um quiz colorido para treinar soma, subtração, multiplicação e divisão no seu ritmo.
                </p>
                <div class="badge-row">
                    <span class="soft-badge">🌈 divertido</span>
                    <span class="soft-badge">⭐ progressivo</span>
                    <span class="soft-badge">🎯 com feedback</span>
                </div>
            </section>
        </div>
        """,
        unsafe_allow_html=True,
    )


def mostrar_progresso():
    progresso = st.session_state.questao_atual / st.session_state.total_questoes

    st.markdown(
        f"""
        <div class="progress-label">
            <span>Progresso da rodada</span>
            <span>{st.session_state.questao_atual}/{st.session_state.total_questoes}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(progresso)


def mostrar_feedback():
    classe = "success" if st.session_state.feedback_tipo == "success" else "error"
    complemento = ""

    if st.session_state.feedback_tipo == "error":
        complemento = (
            f'<span class="answer-note">A resposta certa era '
            f'{st.session_state.resposta_correta}.</span>'
        )

    st.markdown(
        f"""
        <div class="feedback-card {classe}">
            {st.session_state.feedback_texto}
            {complemento}
        </div>
        """,
        unsafe_allow_html=True,
    )


def tela_inicio():
    mostrar_cabecalho()

    st.markdown(
        """
        <div class="panel">
            <h3>Olá! Vamos treinar matemática? 👋</h3>
            <p>
                Escolha como quer jogar, responda às perguntas e acompanhe seus acertos.
                A atividade tem 10 questões e foi pensada para aprender de um jeito leve.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="choice-title">1. Escolha a dificuldade</div>', unsafe_allow_html=True)
    nivel = st.selectbox(
        "Escolha o nível:",
        ["Básico", "Fácil", "Médio", "Difícil"],
        label_visibility="collapsed",
    )

    st.markdown('<div class="choice-title">2. Escolha a operação</div>', unsafe_allow_html=True)
    opcoes_operacao = ["Todas", "Soma", "Subtração"]

    if nivel != "Básico":
        opcoes_operacao.extend(["Multiplicação", "Divisão"])

    operacao = st.selectbox(
        "Escolha a operação:",
        opcoes_operacao,
        label_visibility="collapsed",
    )

    modo_basico = "Números"

    if nivel == "Básico":
        st.markdown('<div class="choice-title">3. Escolha o jeito de brincar</div>', unsafe_allow_html=True)
        modo_basico = st.radio(
            "Como deseja jogar no nível Básico?",
            ["Números", "Figuras"],
            horizontal=True,
            label_visibility="collapsed",
        )

    with st.expander("✨ Entenda os níveis"):
        st.write("**Básico:** soma e subtração com números de 0 a 10.")
        st.write("**Fácil:** contas simples com alternativas.")
        st.write("**Médio:** contas maiores com resposta digitada.")
        st.write("**Difícil:** contas mais desafiadoras com resposta digitada.")

    if st.button("Início", use_container_width=True):
        iniciar_quiz(operacao, nivel, modo_basico)
        st.rerun()

    st.markdown(
        '<div class="footer-note">Projeto desenvolvido para apoio ao aprendizado de matemática básica.</div>',
        unsafe_allow_html=True,
    )


def tela_quiz():
    mostrar_cabecalho()

    if st.session_state.enunciado == "":
        gerar_questao()

    mostrar_progresso()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Questão", f"{st.session_state.questao_atual}/{st.session_state.total_questoes}")

    with col2:
        st.metric("Acertos", st.session_state.pontuacao)

    with col3:
        st.metric("Erros", st.session_state.erros)

    st.markdown(
        f"""
        <div class="question-panel">
            <div class="question-kicker">Pergunta atual</div>
            <div class="question-text">{st.session_state.enunciado}</div>
            <div class="instruction-text">Leia com calma e escolha a resposta que combina com a conta.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.respondido:
        if st.session_state.modo_resposta == "alternativas":
            st.markdown('<div class="choice-title">Escolha uma alternativa:</div>', unsafe_allow_html=True)
            colunas = st.columns(len(st.session_state.alternativas))

            for indice, alternativa in enumerate(st.session_state.alternativas):
                with colunas[indice]:
                    if st.button(
                        str(alternativa),
                        key=f"alternativa_{st.session_state.questao_atual}_{indice}_{alternativa}",
                        use_container_width=True,
                    ):
                        verificar_resposta(alternativa)
                        st.rerun()
        else:
            resposta_usuario = st.number_input(
                "Digite sua resposta:",
                step=1,
                format="%d",
                key=f"resposta_digitada_{st.session_state.questao_atual}",
            )

            if st.button("Enviar", use_container_width=True):
                verificar_resposta(resposta_usuario)
                st.rerun()

    else:
        mostrar_feedback()

        if st.button("Continuar", use_container_width=True):
            avancar_questao()
            st.rerun()


def tela_resultado():
    mostrar_cabecalho()

    acertos = st.session_state.pontuacao
    erros = st.session_state.erros
    total = st.session_state.total_questoes
    aproveitamento = int((acertos / total) * 100)

    st.markdown(
        f"""
        <div class="result-panel">
            <h3>Resultado da atividade 🏁</h3>
            <p>
                Você concluiu a rodada com <strong>{acertos}</strong> acertos em
                <strong>{total}</strong> questões. Veja seu desempenho abaixo:
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Acertos", acertos)

    with col2:
        st.metric("Erros", erros)

    with col3:
        st.metric("Aproveitamento", f"{aproveitamento}%")

    if aproveitamento >= 80:
        st.success("Excelente! Você mandou muito bem nas operações praticadas. 🌟")
    elif aproveitamento >= 50:
        st.info("Bom trabalho! Você está evoluindo e pode ficar ainda melhor. 😊")
    else:
        st.warning("Continue praticando! Cada nova tentativa ajuda o aprendizado. 💪")

    col_a, col_b = st.columns(2)

    with col_a:
        if st.button("🔁 Refazer atividade", use_container_width=True):
            iniciar_quiz(
                st.session_state.operacao,
                st.session_state.nivel,
                st.session_state.modo_basico,
            )
            st.rerun()

    with col_b:
        if st.button("🏠 Voltar ao início", use_container_width=True):
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
