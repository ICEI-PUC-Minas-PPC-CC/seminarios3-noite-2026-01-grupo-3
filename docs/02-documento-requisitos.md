# 02 — Documento de Requisitos do Software

> **Grupo:** **Grupo 3**  
> **Aplicação:** **Sistema para prática de operações matemáticas básicas**  
> **Comunidade:** **Centro Municipal de Educação Dr. Tarso de Coimbra**

---

## 1. Visão Geral

A aplicação consiste em um sistema educacional simples, desenvolvido para auxiliar na prática de operações matemáticas básicas. O software será destinado a estudantes atendidos no contexto da comunidade parceira vinculada ao Centro Municipal de Educação Dr. Tarso de Coimbra.

A proposta busca resolver a necessidade de uma ferramenta acessível, visual e de baixa complexidade para reforço de conteúdos de matemática básica, permitindo que o usuário resolva exercícios, receba correção automática e acompanhe seu desempenho ao final da atividade.

---

## 2. Público-Alvo

| Campo | Informação |
| ------- | ----------- |
| Perfil dos usuários | Estudantes em fase de aprendizagem e reforço de operações matemáticas básicas |
| Faixa etária | Público em idade escolar |
| Necessidades de acessibilidade | Interface visual, intuitiva, com pouco texto, botões bem identificados e sem dependência de áudio |
| Nível de familiaridade com tecnologia | Básico |

> **Lembrete (Tarso de Coimbra):** Os usuários podem ter deficiência auditiva/surdez. A interface deve ser **visual, intuitiva e de baixa complexidade**. Priorize elementos visuais (imagens, ícones, cores) sobre texto extenso.

## 3. Requisitos Funcionais

| ID | Requisito | Prioridade | Origem da demanda |
| ---- | ---------- | :----------: | ------------------ |
| RF01 | O sistema deve apresentar uma tela inicial com instruções visuais simples de uso | Alta | Contato inicial com a comunidade em 06/03/2026 |
| RF02 | O sistema deve apresentar exercícios de soma, subtração, multiplicação e divisão | Alta | Contato inicial com a comunidade em 06/03/2026 |
| RF03 | O sistema deve permitir que o usuário digite ou informe sua resposta para cada exercício | Alta | Contato inicial com a comunidade em 06/03/2026 |
| RF04 | O sistema deve corrigir automaticamente as respostas e informar acerto ou erro | Alta | Contato inicial com a comunidade em 06/03/2026 |
| RF05 | O sistema deve exibir o resultado final da atividade, mostrando quantidade de acertos e erros | Alta | Contato inicial com a comunidade em 06/03/2026 |

## 4. Requisitos Não Funcionais

| ID | Requisito | Categoria |
| ---- | ---------- | ----------- |
| RNF01 | A aplicação deve ser acessível via navegador web | Acessibilidade |
| RNF02 | A interface deve ser simples e intuitiva | Usabilidade |
| RNF03 | A aplicação deve funcionar em dispositivos móveis | Compatibilidade |
| RNF04 | A aplicação deve utilizar elementos visuais claros, com pouco texto e navegação objetiva | Acessibilidade |
| RNF05 | A aplicação não deve depender de áudio para execução das funcionalidades principais | Acessibilidade |

## 5. Requisitos de Acessibilidade

- [x] Interface predominantemente visual (ícones, cores, imagens)
- [x] Textos curtos e objetivos
- [x] Botões grandes e identificáveis
- [x] Contraste adequado de cores
- [ ] Compatível com Libras (se aplicável: vídeos, sinais, glossário)
- [x] Sem dependência de áudio para funcionalidades essenciais
- [x] Outro: feedback visual de acerto e erro

## 6. Tecnologias Escolhidas

| Componente | Tecnologia |
| ----------- | ----------- |
| Front-end | Streamlit |
| Back-end (se houver) | Python |
| Banco de dados (se houver) | Não se aplica nesta versão inicial |
| Hospedagem | Streamlit Community Cloud |
| Outras ferramentas | Git e GitHub |

## 7. Protótipo / Wireframes

O protótipo da aplicação será composto, inicialmente, por três telas principais:

1. **Tela inicial**: apresentação da aplicação e botão para iniciar a atividade.  
2. **Tela de exercícios**: exibição da operação matemática, campo de resposta e retorno visual de acerto ou erro.  
3. **Tela de resultado**: exibição da quantidade de acertos, erros e opção de reiniciar a atividade.

Os wireframes serão salvos em `evidencias/prints/`.

## 8. Escopo Mínimo Viável (MVP)

As funcionalidades mínimas para entrega da aplicação são:

- [x] Tela inicial simples com instruções básicas
- [x] Exercícios de soma, subtração, multiplicação e divisão com correção automática
- [x] Tela final com resultado da atividade

## 9. Funcionalidades Desejáveis (se houver tempo)

- Seleção de nível de dificuldade
- Feedback visual mais detalhado para o usuário
