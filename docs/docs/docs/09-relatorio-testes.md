# 09 - Relatório de Testes

## 1. Objetivo

Este documento apresenta o relatório dos testes realizados no MVP da aplicação educacional desenvolvida para a Etapa 3 do projeto de Seminários III.

O objetivo dos testes foi verificar se a aplicação está funcionando corretamente, de acordo com o fluxo previsto no wireframe e com as funcionalidades implementadas no sistema.

---

## 2. Descrição da Aplicação Testada

A aplicação testada é um sistema educacional simples para prática de operações matemáticas básicas.

O sistema permite que o usuário:

- Escolha a operação matemática desejada;
- Escolha o nível de dificuldade;
- Responda a uma sequência de 10 questões;
- Receba feedback imediato de acerto ou erro;
- Visualize a quantidade de acertos;
- Visualize a quantidade de erros;
- Visualize o aproveitamento final;
- Refaça a atividade;
- Retorne à tela inicial.

As operações disponíveis são:

- Todas;
- Soma;
- Subtração;
- Multiplicação;
- Divisão.

Os níveis disponíveis são:

- Fácil;
- Médio;
- Difícil.

---

## 3. Ambiente de Testes

| Item | Descrição |
|---|---|
| Linguagem | Python |
| Framework | Streamlit |
| Navegador utilizado | Google Chrome / Microsoft Edge |
| Sistema Operacional | Windows |
| Tipo de teste | Teste manual funcional |
| Responsáveis | Integrantes do Grupo 3 |
| Quantidade de questões por rodada | 10 questões |

---

## 4. Resultado dos Testes

| Código | Funcionalidade testada | Resultado esperado | Resultado obtido | Status |
|---|---|---|---|---|
| T01 | Abertura da aplicação | A tela inicial deve ser exibida corretamente | Tela inicial exibida corretamente | Aprovado |
| T02 | Título da aplicação | Deve aparecer o título "Pratique Matemática Básica" | Título exibido corretamente | Aprovado |
| T03 | Seleção de operação | Devem aparecer as opções Todas, Soma, Subtração, Multiplicação e Divisão | Opções exibidas corretamente | Aprovado |
| T04 | Seleção de nível | Devem aparecer as opções Fácil, Médio e Difícil | Opções exibidas corretamente | Aprovado |
| T05 | Botão Como usar | O sistema deve exibir instruções de uso | Instruções exibidas corretamente | Aprovado |
| T06 | Início da atividade | O sistema deve abrir a tela do quiz | Tela do quiz aberta corretamente | Aprovado |
| T07 | Contador de questões | O sistema deve exibir a questão atual e o total | Contador exibido corretamente | Aprovado |
| T08 | Exibição da questão | A questão deve aparecer de forma clara e legível | Questão exibida corretamente | Aprovado |
| T09 | Nível Fácil | O sistema deve exibir alternativas para seleção | Alternativas exibidas corretamente | Aprovado |
| T10 | Nível Médio | O sistema deve exibir campo para digitar a resposta | Campo de resposta exibido corretamente | Aprovado |
| T11 | Nível Difícil | O sistema deve exibir campo para digitar a resposta | Campo de resposta exibido corretamente | Aprovado |
| T12 | Responder sem alternativa | O sistema deve alertar para selecionar uma alternativa | Alerta exibido corretamente | Aprovado |
| T13 | Resposta correta | O sistema deve exibir mensagem de acerto | Mensagem de acerto exibida corretamente | Aprovado |
| T14 | Resposta incorreta | O sistema deve exibir mensagem de erro e mostrar a resposta correta | Mensagem de erro exibida corretamente | Aprovado |
| T15 | Contagem de acertos | O número de acertos deve aumentar após uma resposta correta | Contagem atualizada corretamente | Aprovado |
| T16 | Contagem de erros | O número de erros deve aumentar após uma resposta incorreta | Contagem atualizada corretamente | Aprovado |
| T17 | Avançar questão | O sistema deve apresentar uma nova questão | Nova questão exibida corretamente | Aprovado |
| T18 | Voltar durante o quiz | O sistema deve retornar para a tela inicial | Retorno realizado corretamente | Aprovado |
| T19 | Finalização da atividade | Após 10 questões, o sistema deve abrir a tela de resultado | Tela de resultado exibida corretamente | Aprovado |
| T20 | Resultado final | Devem aparecer acertos, erros e aproveitamento | Métricas exibidas corretamente | Aprovado |
| T21 | Cálculo do aproveitamento | O aproveitamento deve ser calculado corretamente | Porcentagem calculada corretamente | Aprovado |
| T22 | Mensagem por desempenho | O sistema deve exibir mensagem conforme a pontuação | Mensagem exibida corretamente | Aprovado |
| T23 | Refazer atividade | O sistema deve iniciar uma nova rodada de exercícios | Nova rodada iniciada corretamente | Aprovado |
| T24 | Voltar ao início no resultado | O sistema deve retornar para a tela inicial | Retorno realizado corretamente | Aprovado |
| T25 | Tema claro | Textos e botões devem permanecer legíveis | Interface legível em tema claro | Aprovado |
| T26 | Tema escuro | Textos e botões devem permanecer legíveis | Interface legível em tema escuro | Aprovado |
| T27 | Operação Soma | As questões devem apresentar contas de adição | Questões de soma exibidas corretamente | Aprovado |
| T28 | Operação Subtração | As questões devem apresentar contas de subtração | Questões de subtração exibidas corretamente | Aprovado |
| T29 | Operação Multiplicação | As questões devem apresentar contas de multiplicação | Questões de multiplicação exibidas corretamente | Aprovado |
| T30 | Operação Divisão | As questões devem apresentar divisões com resultado inteiro | Questões de divisão exibidas corretamente | Aprovado |
| T31 | Operação Todas | O sistema deve variar entre as quatro operações | Operações variadas corretamente | Aprovado |

---
