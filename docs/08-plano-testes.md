# 08 - Plano de Testes

## 1. Objetivo

Este documento apresenta o plano de testes do MVP desenvolvido para a Etapa 3 do projeto de Seminários III.

O objetivo dos testes é verificar se a aplicação educacional de matemática básica está funcionando corretamente, considerando o fluxo principal previsto no wireframe e as funcionalidades implementadas no código em Python com Streamlit.

A aplicação possui tela inicial, tela de resolução de exercícios e tela de resultado final, conforme previsto no wireframe do projeto.

Os testes foram realizados de forma manual, utilizando a aplicação em ambiente local e também por meio do link público de acesso disponibilizado na Internet.

---

## 2. Escopo dos Testes

Os testes foram realizados sobre o MVP da aplicação educacional desenvolvida em Python com Streamlit.

Foram testadas as seguintes funcionalidades:

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
- Visualização em tema claro e tema escuro;
- Acesso à aplicação publicada na Internet.

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
| Ambiente | Local e aplicação publicada na Internet |

---

## 4. Critérios de Aceitação

A aplicação foi considerada aprovada porque:

- A tela inicial foi carregada corretamente;
- O usuário conseguiu escolher a operação matemática;
- O usuário conseguiu escolher o nível de dificuldade;
- O botão "Como usar" apresentou orientações de uso;
- O botão "Iniciar atividade" iniciou o quiz;
- As questões foram exibidas corretamente;
- No nível Fácil, as alternativas foram exibidas;
- Nos níveis Médio e Difícil, o campo de resposta digitada foi exibido;
- O sistema corrigiu automaticamente as respostas;
- O sistema apresentou feedback visual após cada resposta;
- O sistema contabilizou corretamente acertos e erros;
- O sistema avançou corretamente entre as questões;
- Após 10 questões, o sistema exibiu a tela de resultado;
- A tela final apresentou acertos, erros e aproveitamento;
- O botão "Refazer atividade" reiniciou o quiz;
- O botão "Voltar ao início" retornou para a tela inicial;
- A interface permaneceu legível em tema claro e tema escuro;
- A aplicação pôde ser acessada publicamente pela Internet.

---

## 5. Casos de Teste

| Código | Funcionalidade testada | Procedimento | Resultado esperado | Status |
|---|---|---|---|---|
| T01 | Abertura da aplicação | Acessar a aplicação pelo navegador | A tela inicial deve ser exibida corretamente | Aprovado |
| T02 | Título da aplicação | Verificar o cabeçalho da página | Deve aparecer o título "Pratique Matemática Básica" | Aprovado |
| T03 | Seleção de operação | Abrir o campo de operação | Devem aparecer as opções Todas, Soma, Subtração, Multiplicação e Divisão | Aprovado |
| T04 | Seleção de nível | Abrir o campo de nível | Devem aparecer as opções de dificuldade disponíveis na aplicação | Aprovado |
| T05 | Botão Como usar | Clicar no botão "Como usar" | O sistema deve exibir as instruções de uso | Aprovado |
| T06 | Início da atividade | Selecionar uma operação, um nível e clicar em "Iniciar atividade" | O sistema deve abrir a tela do quiz | Aprovado |
| T07 | Contador de questões | Iniciar uma atividade | O sistema deve exibir "Questão 1/10" | Aprovado |
| T08 | Exibição da questão | Verificar a conta matemática exibida | A questão deve aparecer de forma clara e legível | Aprovado |
| T09 | Nível Fácil | Iniciar atividade no nível Fácil | O sistema deve exibir alternativas para seleção | Aprovado |
| T10 | Nível Médio | Iniciar atividade no nível Médio | O sistema deve exibir campo para digitar a resposta | Aprovado |
| T11 | Nível Difícil | Iniciar atividade no nível Difícil | O sistema deve exibir campo para digitar a resposta | Aprovado |
| T12 | Responder sem alternativa | No nível Fácil, clicar em "Responder" sem escolher alternativa | O sistema deve alertar para selecionar uma alternativa | Aprovado |
| T13 | Resposta correta | Inserir ou selecionar uma resposta correta | O sistema deve exibir mensagem de resposta correta | Aprovado |
| T14 | Resposta incorreta | Inserir ou selecionar uma resposta incorreta | O sistema deve exibir mensagem de resposta incorreta e informar a resposta certa | Aprovado |
| T15 | Contagem de acertos | Responder corretamente uma questão | O número de acertos deve aumentar em 1 | Aprovado |
| T16 | Contagem de erros | Responder incorretamente uma questão | O número de erros deve aumentar em 1 | Aprovado |
| T17 | Avançar questão | Após responder, clicar em "Próxima" | O sistema deve exibir uma nova questão | Aprovado |
| T18 | Voltar durante o quiz | Clicar em "Voltar" ou "Voltar ao início" | O sistema deve retornar para a tela inicial | Aprovado |
| T19 | Finalização da atividade | Responder as 10 questões | O sistema deve abrir a tela de resultado final | Aprovado |
| T20 | Resultado final | Verificar a tela final | Devem aparecer acertos, erros e aproveitamento | Aprovado |
| T21 | Cálculo do aproveitamento | Comparar acertos com a porcentagem exibida | O aproveitamento deve estar correto | Aprovado |
| T22 | Mensagem por desempenho | Finalizar atividade com diferentes pontuações | O sistema deve exibir mensagem adequada ao desempenho | Aprovado |
| T23 | Refazer atividade | Clicar em "Refazer atividade" | O sistema deve iniciar uma nova rodada de exercícios | Aprovado |
| T24 | Voltar ao início no resultado | Clicar em "Voltar ao início" | O sistema deve retornar para a tela inicial | Aprovado |
| T25 | Operação Soma | Selecionar Soma e iniciar a atividade | As questões devem apresentar contas de adição | Aprovado |
| T26 | Operação Subtração | Selecionar Subtração e iniciar a atividade | As questões devem apresentar contas de subtração | Aprovado |
| T27 | Operação Multiplicação | Selecionar Multiplicação e iniciar a atividade | As questões devem apresentar contas de multiplicação | Aprovado |
| T28 | Operação Divisão | Selecionar Divisão e iniciar a atividade | As questões devem apresentar divisões com resultado inteiro | Aprovado |
| T29 | Operação Todas | Selecionar Todas e iniciar a atividade | O sistema deve variar entre soma, subtração, multiplicação e divisão | Aprovado |
| T30 | Acesso pela Internet | Acessar o link público da aplicação publicada | A aplicação deve abrir normalmente no navegador | Aprovado |
| T31 | Evidências da aplicação | Verificar os prints registrados no repositório | Os prints devem comprovar o funcionamento da aplicação | Aprovado |

---

## 6. Resultado Geral dos Testes

Após a execução dos testes manuais, o MVP foi considerado aprovado.

As principais funcionalidades previstas para a Etapa 3 foram validadas:

- A aplicação abre corretamente;
- O usuário consegue iniciar a atividade;
- O sistema gera questões de matemática básica;
- O sistema corrige automaticamente as respostas;
- O sistema apresenta feedback visual;
- O sistema contabiliza acertos e erros;
- O sistema exibe o resultado final;
- O usuário consegue refazer a atividade;
- O usuário consegue voltar para a tela inicial;
- A interface permanece legível em tema claro e tema escuro;
- A aplicação está acessível por meio de link público na Internet.

---

## 7. Conclusão

Com base nos testes realizados, conclui-se que o MVP da aplicação "Pratique Matemática Básica" está funcional e atende aos requisitos definidos para esta etapa do projeto.

O sistema apresentou comportamento adequado durante os testes manuais, permitindo que o usuário pratique operações matemáticas básicas de forma simples, acessível e interativa.

Dessa forma, o MVP encontra-se aprovado para apresentação e validação da Etapa 3.
