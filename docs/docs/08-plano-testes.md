# 08 - Plano de Testes

## 1. Objetivo

Este documento apresenta o plano de testes do MVP desenvolvido para a Etapa 3 do projeto de Seminários III.

O objetivo dos testes é verificar se a aplicação educacional de matemática básica está funcionando corretamente, considerando o fluxo principal previsto no wireframe e as funcionalidades implementadas no código em Python com Streamlit.

A aplicação possui tela inicial, tela de resolução de exercícios e tela de resultado final, conforme previsto no wireframe do projeto.

---

## 2. Escopo dos Testes

Os testes serão realizados sobre o MVP da aplicação educacional desenvolvida em Python com Streamlit.

Serão testadas as seguintes funcionalidades:

- Abertura da aplicação;
- Exibição da tela inicial;
- Seleção da operação matemática;
- Seleção do nível de dificuldade;
- Exibição das instruções de uso;
- Início da atividade;
- Geração das questões;
- Resposta por alternativas no nível Fácil;
- Resposta digitada nos níveis Médio e Difícil;
- Correção automática das respostas;
- Exibição de feedback para acerto e erro;
- Contagem de acertos;
- Contagem de erros;
- Avanço entre questões;
- Finalização após 10 questões;
- Exibição do resultado final;
- Cálculo do aproveitamento;
- Botão para refazer atividade;
- Botão para voltar ao início;
- Visualização em tema claro e tema escuro.

---

## 3. Ambiente de Testes

| Item | Descrição |
|---|---|
| Linguagem | Python |
| Framework | Streamlit |
| Navegador | Google Chrome ou Microsoft Edge |
| Sistema Operacional | Windows |
| Tipo de teste | Teste manual funcional |
| Responsáveis | Integrantes do Grupo 3 |
| Quantidade de questões | 10 questões por rodada |

---

## 4. Critérios de Aceitação

A aplicação será considerada aprovada se:

- A tela inicial for carregada corretamente;
- O usuário conseguir escolher a operação matemática;
- O usuário conseguir escolher o nível de dificuldade;
- O botão "Como usar" apresentar orientações de uso;
- O botão "Iniciar atividade" iniciar o quiz;
- As questões forem exibidas corretamente;
- No nível Fácil, as alternativas forem exibidas;
- Nos níveis Médio e Difícil, o campo de resposta digitada for exibido;
- O sistema corrigir automaticamente as respostas;
- O sistema apresentar feedback visual após cada resposta;
- O sistema contabilizar corretamente acertos e erros;
- O sistema avançar corretamente entre as questões;
- Após 10 questões, o sistema exibir a tela de resultado;
- A tela final apresentar acertos, erros e aproveitamento;
- O botão "Refazer atividade" reiniciar o quiz;
- O botão "Voltar ao início" retornar para a tela inicial;
- A interface continuar legível em tema claro e tema escuro.

---

## 5. Casos de Teste

| Código | Funcionalidade testada | Procedimento | Resultado esperado | Status |
|---|---|---|---|---|
| T01 | Abertura da aplicação | Acessar a aplicação pelo navegador | A tela inicial deve ser exibida corretamente | Pendente |
| T02 | Título da aplicação | Verificar o cabeçalho da página | Deve aparecer o título "Pratique Matemática Básica" | Pendente |
| T03 | Seleção de operação | Abrir o campo de operação | Devem aparecer as opções Todas, Soma, Subtração, Multiplicação e Divisão | Pendente |
| T04 | Seleção de nível | Abrir o campo de nível | Devem aparecer as opções Fácil, Médio e Difícil | Pendente |
| T05 | Botão Como usar | Clicar no botão "Como usar" | O sistema deve exibir as instruções de uso | Pendente |
| T06 | Início da atividade | Selecionar uma operação, um nível e clicar em "Iniciar atividade" | O sistema deve abrir a tela do quiz | Pendente |
| T07 | Contador de questões | Iniciar uma atividade | O sistema deve exibir "Questão 1/10" | Pendente |
| T08 | Exibição da questão | Verificar a conta matemática exibida | A questão deve aparecer de forma clara e legível | Pendente |
| T09 | Nível Fácil | Iniciar atividade no nível Fácil | O sistema deve exibir alternativas para seleção | Pendente |
| T10 | Nível Médio | Iniciar atividade no nível Médio | O sistema deve exibir campo para digitar a resposta | Pendente |
| T11 | Nível Difícil | Iniciar atividade no nível Difícil | O sistema deve exibir campo para digitar a resposta | Pendente |
| T12 | Responder sem alternativa | No nível Fácil, clicar em "Responder" sem escolher alternativa | O sistema deve alertar para selecionar uma alternativa | Pendente |
| T13 | Resposta correta | Inserir ou selecionar uma resposta correta | O sistema deve exibir mensagem de resposta correta | Pendente |
| T14 | Resposta incorreta | Inserir ou selecionar uma resposta incorreta | O sistema deve exibir mensagem de resposta incorreta e informar a resposta certa | Pendente |
| T15 | Contagem de acertos | Responder corretamente uma questão | O número de acertos deve aumentar em 1 | Pendente |
| T16 | Contagem de erros | Responder incorretamente uma questão | O número de erros deve aumentar em 1 | Pendente |
| T17 | Avançar questão | Após responder, clicar em "Próxima" | O sistema deve exibir uma nova questão | Pendente |
| T18 | Voltar durante o quiz | Clicar em "Voltar" ou "Voltar ao início" | O sistema deve retornar para a tela inicial | Pendente |
| T19 | Finalização da atividade | Responder as 10 questões | O sistema deve abrir a tela de resultado final | Pendente |
| T20 | Resultado final | Verificar a tela final | Devem aparecer acertos, erros e aproveitamento | Pendente |
| T21 | Cálculo do aproveitamento | Comparar acertos com a porcentagem exibida | O aproveitamento deve estar correto | Pendente |
| T22 | Mensagem por desempenho | Finalizar atividade com diferentes pontuações | O sistema deve exibir mensagem adequada ao desempenho | Pendente |
| T23 | Refazer atividade | Clicar em "Refazer atividade" | O sistema deve iniciar uma nova rodada de exercícios | Pendente |
| T24 | Voltar ao início no resultado | Clicar em "Voltar ao início" | O sistema deve retornar para a tela inicial | Pendente |
| T25 | Tema claro | Abrir a aplicação com o sistema em tema claro | Todos os textos e botões devem permanecer legíveis | Pendente |
| T26 | Tema escuro | Abrir a aplicação com o sistema em tema escuro | Todos os textos e botões devem permanecer legíveis | Pendente |
| T27 | Operação Soma | Selecionar Soma e iniciar a atividade | As questões devem apresentar contas de adição | Pendente |
| T28 | Operação Subtração | Selecionar Subtração e iniciar a atividade | As questões devem apresentar contas de subtração | Pendente |
| T29 | Operação Multiplicação | Selecionar Multiplicação e iniciar a atividade | As questões devem apresentar contas de multiplicação | Pendente |
| T30 | Operação Divisão | Selecionar Divisão e iniciar a atividade | As questões devem apresentar divisões com resultado inteiro | Pendente |
| T31 | Operação Todas | Selecionar Todas e iniciar a atividade | O sistema deve variar entre soma, subtração, multiplicação e divisão | Pendente |

---
