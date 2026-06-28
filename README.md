# 💻 Seminários III — Projeto Extensionista

> **Grupo:** Grupo 3
> **Aplicação:** Pratique Matemática Básica
> **Comunidade parceira:** Centro Municipal de Educação Dr. Tarso de Coimbra
> **Disciplina:** Seminários III — PUC Minas
> **Professor responsável:** Harison Herman Silva
> **Status:** Projeto concluído

---

## 👥 Integrantes

| Integrante                   | Participação principal                                                                                                      |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Luciano Expedito Franco      | Organização do projeto, documentação, atualização do repositório, apoio no desenvolvimento, validações e entrega presencial |
| João Vitor Geraldo Parussolo | Requisitos, prototipação, desenvolvimento, validações e apresentação do projeto                                             |
| Brian Giaccon Vilela         | Desenvolvimento da aplicação, testes, ajustes e demonstração prática do sistema                                             |
| Todos                        | Planejamento, decisões, contatos, validações, organização das evidências e relatórios                                       |

**E-mail de contato:** [lefranco@sga.pucminas.br](mailto:lefranco@sga.pucminas.br)

---

## 🎯 Sobre o Projeto

O **Pratique Matemática Básica** é uma aplicação educacional desenvolvida para auxiliar estudantes na prática das quatro operações matemáticas básicas:

* soma;
* subtração;
* multiplicação;
* divisão.

A aplicação possui interface simples, visual e intuitiva, permitindo que o usuário escolha uma operação e um nível de dificuldade, resolva exercícios, receba correção automática e visualize seu desempenho ao final da atividade.

O projeto foi desenvolvido para atender estudantes vinculados ao Centro Municipal de Educação Dr. Tarso de Coimbra, considerando também usuários com deficiência auditiva ou surdez.

Por esse motivo, a aplicação utiliza textos curtos, botões identificáveis, imagens, elementos visuais e não depende de áudio para suas funcionalidades principais.

---

## 🌐 Aplicação Publicada

A aplicação está disponível pela Internet por meio do Streamlit Community Cloud:

[**Acessar Pratique Matemática Básica**](https://pratique-matematica-basica-5gyr4nnmabpmxhmhnmyaap.streamlit.app/)

---

## ✅ Funcionalidades

* [x] Tela inicial com instruções;
* [x] seleção da operação matemática;
* [x] opção de utilizar todas as operações;
* [x] exercícios de soma;
* [x] exercícios de subtração;
* [x] exercícios de multiplicação;
* [x] exercícios de divisão;
* [x] níveis Básico, Fácil, Médio e Difícil;
* [x] questões com alternativas;
* [x] questões com respostas digitadas;
* [x] exercícios utilizando figuras;
* [x] exercícios utilizando imagens de cédulas;
* [x] atividades relacionadas a valores monetários;
* [x] correção automática;
* [x] feedback visual de acerto ou erro;
* [x] apresentação da resposta correta;
* [x] contagem de acertos e erros;
* [x] cálculo do percentual de aproveitamento;
* [x] tela de resultado final;
* [x] opção de refazer a atividade;
* [x] opção de retornar à tela inicial;
* [x] acesso por navegador;
* [x] hospedagem na Internet.

---

## 🎚️ Níveis de Dificuldade

### Básico

O nível Básico utiliza números menores, alternativas e maior presença de elementos visuais. Também possui atividades utilizando figuras e imagens de cédulas.

### Fácil

O nível Fácil apresenta operações simples, com valores um pouco maiores e respostas por alternativas.

### Médio

O nível Médio apresenta operações com maior dificuldade e questões com respostas digitadas.

### Difícil

O nível Difícil utiliza valores maiores e operações mais complexas, mantendo o foco nas quatro operações matemáticas básicas.

---

## ♿ Acessibilidade

A aplicação foi planejada considerando as necessidades do público atendido.

Foram adotadas as seguintes medidas:

* interface visual e intuitiva;
* textos curtos e objetivos;
* botões grandes e identificáveis;
* contraste adequado entre os elementos;
* feedback visual de acerto e erro;
* utilização de imagens;
* navegação de baixa complexidade;
* ausência de dependência de áudio;
* funcionamento diretamente pelo navegador.

Durante a entrega presencial, a apresentação também contou com o apoio de uma intérprete de Libras.

---

## 🛠️ Tecnologias Utilizadas

| Componente               | Tecnologia                    |
| ------------------------ | ----------------------------- |
| Linguagem de programação | Python                        |
| Interface web            | Streamlit                     |
| Editor de código         | Visual Studio Code            |
| Versionamento            | Git                           |
| Repositório              | GitHub                        |
| Hospedagem               | Streamlit Community Cloud     |
| Prototipação             | PowerPoint e Canva            |
| Comunicação do grupo     | WhatsApp, ligações e reuniões |
| Participação remota      | Google Meet                   |

---

## 📁 Estrutura do Repositório

```text
├── README.md
├── requirements.txt
├── docs/
│   ├── 01-termo-autorizacao.md
│   ├── 02-documento-requisitos.md
│   ├── 03-plano-desenvolvimento.md
│   ├── 04-checklist-logistica.md
│   ├── 05-diario-bordo.md
│   ├── 06-registro-contatos.md
│   ├── 08-plano-testes.md
│   ├── 09-relatorio-testes.md
│   ├── Wireframes - Grupo3.pdf
│   └── Registro-monitoramento-praticas-extensao-Grupo3.pdf
├── src/
│   ├── app.py
│   ├── README.md
│   └── Imagens&Gifs/
│       └── Notas/
├── evidencias/
│   ├── fotos/
│   └── prints/
└── relatorios/
    └── 07-relatorio-atividades.md
```

---

## ▶️ Como Executar Localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/ICEI-PUC-Minas-PPC-CC/seminarios3-noite-2026-01-grupo-3.git
```

### 2. Acessar a pasta do projeto

```bash
cd seminarios3-noite-2026-01-grupo-3
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
streamlit run src/app.py
```

Após a execução, a aplicação deverá abrir automaticamente no navegador.

Caso isso não aconteça, acesse:

```text
http://localhost:8501
```

---

## 🧪 Testes

Foram realizados testes manuais para verificar:

* abertura da aplicação;
* funcionamento da tela inicial;
* seleção das operações;
* seleção dos níveis;
* geração das questões;
* funcionamento das alternativas;
* funcionamento das respostas digitadas;
* respostas corretas e incorretas;
* atualização dos acertos e erros;
* cálculo do aproveitamento;
* carregamento das imagens;
* atividades com figuras;
* atividades com cédulas;
* reinício da atividade;
* retorno à tela inicial;
* funcionamento pelo navegador;
* acesso pelo link público.

Os documentos de testes estão disponíveis abaixo:

* [Plano de testes](docs/08-plano-testes.md)
* [Relatório de testes](docs/09-relatorio-testes.md)

---

## 📄 Documentação do Projeto

### Planejamento e desenvolvimento

* [Termo e informações iniciais](docs/01-termo-autorizacao.md)
* [Documento de requisitos](docs/02-documento-requisitos.md)
* [Plano e cronograma de desenvolvimento](docs/03-plano-desenvolvimento.md)
* [Checklist de preparação e logística](docs/04-checklist-logistica.md)
* [Diário de bordo](docs/05-diario-bordo.md)
* [Registro de contatos](docs/06-registro-contatos.md)

### Protótipo

* [Wireframes do Grupo 3](docs/Wireframes%20-%20Grupo3.pdf)

### Relatório da prática extensionista

* [Registro e monitoramento das práticas de extensão](docs/Registro-monitoramento-praticas-extensao-Grupo3.pdf)

### Relatório APC

* [Base para o relatório de atividades](relatorios/07-relatorio-atividades.md)

### Código-fonte

* [Documentação do código](src/README.md)
* [Código principal da aplicação](src/app.py)

---

## 📷 Evidências

As evidências do projeto estão organizadas nas seguintes pastas:

* [Fotos da entrega presencial](evidencias/fotos/)
* [Prints da aplicação](evidencias/prints/)

As fotos registram a apresentação realizada para a comunidade parceira, enquanto os prints demonstram as principais telas e funcionalidades do sistema.

---

## 🤝 Validações Realizadas

### Validação do wireframe

O wireframe foi apresentado ao professor Harison, que considerou adequada a proposta de manter a aplicação simples.

Como sugestão, o professor orientou a criação de níveis de dificuldade, iniciando com contas simples e alternativas e aumentando gradualmente a complexidade.

### Validação intermediária do MVP

Em 13/05/2026, foi enviado ao professor um vídeo demonstrando a primeira versão funcional da aplicação.

### Validação com a comunidade

Em 18/05/2026, o MVP foi apresentado no Centro Municipal de Educação Dr. Tarso de Coimbra.

Durante a apresentação, foram sugeridos:

* criação de um nível mais básico;
* utilização de números menores;
* maior uso de figuras;
* atividades utilizando cédulas;
* maior presença de elementos visuais.

Essas sugestões foram incorporadas à versão final.

---

## 🎓 Entrega Presencial

A entrega presencial foi realizada em:

| Campo      | Informação                                                       |
| ---------- | ---------------------------------------------------------------- |
| Data       | 18/06/2026                                                       |
| Horário    | 14h20                                                            |
| Local      | Laboratório de Informática 6 — PUC Minas, campus Poços de Caldas |
| Comunidade | Centro Municipal de Educação Dr. Tarso de Coimbra                |

Luciano Expedito Franco e Brian Giaccon Vilela participaram presencialmente.

João Vitor Geraldo Parussolo participou remotamente por meio do Google Meet.

Durante a apresentação:

* João Vitor explicou o projeto e seu processo de desenvolvimento;
* Luciano auxiliou nas explicações e na contextualização;
* Brian realizou a demonstração prática da aplicação no notebook.

A atividade contou com participantes da Tarso de Coimbra e com o apoio de uma intérprete de Libras.

---

## 📊 Resultados

O projeto resultou em uma aplicação web funcional que:

* atende ao escopo definido;
* permite praticar as quatro operações básicas;
* apresenta diferentes níveis de dificuldade;
* utiliza elementos visuais;
* oferece correção imediata;
* mostra acertos, erros e aproveitamento;
* funciona pelo navegador;
* está disponível pela Internet;
* foi validada pelo professor;
* recebeu sugestões da comunidade;
* foi ajustada após as validações;
* foi apresentada e entregue presencialmente.

---

## 🔗 Links Principais

* **Aplicação:** [Pratique Matemática Básica](https://pratique-matematica-basica-5gyr4nnmabpmxhmhnmyaap.streamlit.app/)
* **Repositório:** [GitHub do Grupo 3](https://github.com/ICEI-PUC-Minas-PPC-CC/seminarios3-noite-2026-01-grupo-3)
* **Wireframe:** [Wireframes - Grupo3.pdf](docs/Wireframes%20-%20Grupo3.pdf)
* **Relatório da extensão:** [Registro-monitoramento-praticas-extensao-Grupo3.pdf](docs/Registro-monitoramento-praticas-extensao-Grupo3.pdf)

---

## ✅ Situação Final

* [x] Grupo formado;
* [x] comunidade parceira definida;
* [x] demandas levantadas;
* [x] requisitos documentados;
* [x] protótipo elaborado;
* [x] protótipo validado;
* [x] tecnologias definidas;
* [x] MVP desenvolvido;
* [x] testes realizados;
* [x] validação intermediária concluída;
* [x] sugestões da comunidade implementadas;
* [x] deploy realizado;
* [x] aplicação publicada;
* [x] entrega presencial realizada;
* [x] fotos e prints organizados;
* [x] relatório da prática extensionista preenchido;
* [x] relatório de atividades preenchido;
* [x] autoavaliações individuais preenchidas;
* [x] projeto concluído.

---

## ✅ Conclusão

O Grupo 3 concluiu o desenvolvimento da aplicação **Pratique Matemática Básica**, cumprindo as etapas de planejamento, levantamento de demandas, prototipação, desenvolvimento, testes, validações, deploy, entrega presencial e elaboração dos relatórios.

A escolha de manter um escopo simples e funcional permitiu desenvolver uma solução compatível com as necessidades da comunidade e com o prazo da disciplina.

A aplicação está concluída, documentada e disponível para utilização pela Internet.
