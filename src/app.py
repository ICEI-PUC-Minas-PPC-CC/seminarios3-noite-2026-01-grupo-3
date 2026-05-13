import streamlit as st
        ['Fácil', 'Médio', 'Difícil']
    )

    if st.button("Iniciar atividade"):
        st.session_state.operacao = operacao
        st.session_state.nivel = nivel
        st.session_state.pagina = 'quiz'
        st.rerun()


# =========================
# QUIZ
# =========================

elif st.session_state.pagina == 'quiz':

    st.title("✏️ Resolva a questão")

    pergunta, resposta_correta = gerar_conta(st.session_state.operacao)

    st.write(
        f"Questão {st.session_state.questao_atual} de {st.session_state.total_questoes}"
    )

    st.subheader(pergunta)

    resposta_usuario = st.number_input(
        "Digite sua resposta:",
        step=1,
        format="%d"
    )

    if st.button("Confirmar resposta"):

        if resposta_usuario == resposta_correta:
            st.success("✅ Resposta correta!")
            st.session_state.pontuacao += 1
        else:
            st.error(
                f"❌ Resposta incorreta! A resposta correta era {resposta_correta}"
            )

        st.session_state.questao_atual += 1

        if st.session_state.questao_atual > st.session_state.total_questoes:
            st.session_state.pagina = 'resultado'

        st.rerun()


# =========================
# RESULTADO FINAL
# =========================

elif st.session_state.pagina == 'resultado':

    st.title("🏆 Resultado Final")

    acertos = st.session_state.pontuacao
    total = st.session_state.total_questoes

    porcentagem = (acertos / total) * 100

    st.write(f"### Você acertou {acertos} de {total} questões")
    st.write(f"### Aproveitamento: {porcentagem:.0f}%")

    if porcentagem >= 70:
        st.success("Parabéns! Excelente resultado!")
    else:
        st.warning("Continue praticando para melhorar!")

    if st.button("Reiniciar atividade"):

        st.session_state.pontuacao = 0
        st.session_state.questao_atual = 1
        st.session_state.pagina = 'inicio'

        st.rerun()
