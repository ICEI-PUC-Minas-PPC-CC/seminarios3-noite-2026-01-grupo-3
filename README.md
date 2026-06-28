# 📂 Código-Fonte — Pratique Matemática Básica

> **Grupo:** Grupo 3
> **Disciplina:** Seminários III
> **Comunidade parceira:** Centro Municipal de Educação Dr. Tarso de Coimbra
> **Tecnologias:** Python e Streamlit
> **Status:** Aplicação concluída e publicada

---

## 💻 Sobre a Aplicação

O **Pratique Matemática Básica** é uma aplicação educacional desenvolvida para auxiliar estudantes na prática das quatro operações matemáticas básicas:

* soma;
* subtração;
* multiplicação;
* divisão.

A aplicação possui interface simples, visual e intuitiva, com diferentes níveis de dificuldade, correção automática, feedback imediato e apresentação do desempenho final.

O sistema foi desenvolvido considerando as necessidades do público atendido pelo Centro Municipal de Educação Dr. Tarso de Coimbra, incluindo usuários com deficiência auditiva ou surdez.

Por esse motivo, as funcionalidades principais não dependem de áudio e utilizam textos curtos, botões identificáveis, imagens e elementos visuais.

---

## 🌐 Aplicação Publicada

A aplicação está disponível pela Internet por meio do Streamlit Community Cloud:

[**Acessar Pratique Matemática Básica**](https://pratique-matematica-basica-5gyr4nnmabpmxhmhnmyaap.streamlit.app/)

---

## 🛠️ Tecnologias Utilizadas

| Componente               | Tecnologia                |
| ------------------------ | ------------------------- |
| Linguagem de programação | Python                    |
| Interface web            | Streamlit                 |
| Editor de código         | Visual Studio Code        |
| Versionamento            | Git                       |
| Repositório              | GitHub                    |
| Hospedagem               | Streamlit Community Cloud |
| Prototipação             | PowerPoint e Canva        |

---

## 📁 Estrutura do Diretório

```text
src/
├── app.py
├── README.md
└── Imagens&Gifs/
    └── Notas/
        ├── nota-2.png
        ├── nota-5.png
        ├── nota-10.png
        ├── nota-20.png
        ├── nota-50.png
        ├── nota-100.png
        └── nota-200.png
```

> Os nomes dos arquivos de imagem podem variar conforme a organização atual da pasta.

---

## ✅ Funcionalidades

A aplicação possui as seguintes funcionalidades:

* [x] Tela inicial com orientações;
* [x] seleção da operação matemática;
* [x] opção de utilizar todas as operações;
* [x] exercícios de soma;
* [x] exercícios de subtração;
* [x] exercícios de multiplicação;
* [x] exercícios de divisão;
* [x] nível Básico;
* [x] nível Fácil;
* [x] nível Médio;
* [x] nível Difícil;
* [x] questões com alternativas;
* [x] questões com respostas digitadas;
* [x] atividades utilizando figuras;
* [x] atividades utilizando imagens de cédulas;
* [x] atividades relacionadas a valores monetários;
* [x] correção automática;
* [x] feedback visual de acerto ou erro;
* [x] apresentação da resposta correta;
* [x] contagem de acertos e erros;
* [x] cálculo do percentual de aproveitamento;
* [x] tela de resultado final;
* [x] opção de refazer a atividade;
* [x] opção de retornar à tela inicial;
* [x] funcionamento em navegador;
* [x] acesso pela Internet.

---

## 🎯 Níveis de Dificuldade

### Básico

O nível Básico foi desenvolvido após o contato com a comunidade parceira.

Ele utiliza:

* números menores;
* operações simples;
* alternativas para seleção;
* maior presença de elementos visuais;
* atividades com figuras e cédulas.

### Fácil

O nível Fácil apresenta contas simples, com valores um pouco maiores e respostas por alternativas.

### Médio

O nível Médio apresenta operações com maior dificuldade e pode exigir que o usuário digite a resposta.

### Difícil

O nível Difícil utiliza valores maiores e operações mais complexas, mantendo o foco nas quatro operações matemáticas básicas.

---

## ♿ Acessibilidade

A aplicação foi planejada considerando as características do público atendido.

Foram adotadas as seguintes medidas:

* interface visual e intuitiva;
* textos curtos e objetivos;
* botões grandes e identificáveis;
* contraste entre os elementos;
* feedback visual de acerto e erro;
* uso de imagens;
* navegação de baixa complexidade;
* ausência de dependência de áudio;
* funcionamento diretamente pelo navegador.

---

## ▶️ Como Executar Localmente

### 1. Clonar o repositório

```bash
git clone <URL-DO-REPOSITORIO>
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

Após executar o comando, a aplicação será aberta automaticamente no navegador.

Caso não abra, acesse:

```text
http://localhost:8501
```

---

## 📦 Dependências

As dependências necessárias estão registradas no arquivo `requirements.txt`, localizado na pasta principal do repositório.

Dependência principal:

```text
streamlit
```

---

## 🧪 Testes Realizados

Foram realizados testes manuais para verificar:

* abertura da aplicação;
* carregamento das imagens;
* funcionamento da tela inicial;
* seleção das operações;
* seleção dos níveis;
* geração das questões;
* funcionamento das alternativas;
* funcionamento das respostas digitadas;
* respostas corretas;
* respostas incorretas;
* atualização dos acertos e erros;
* cálculo do aproveitamento;
* exibição do resultado final;
* reinício da atividade;
* retorno à tela inicial;
* atividades com figuras;
* atividades com cédulas;
* funcionamento pelo navegador;
* acesso pelo link público.

Os testes foram concluídos e as funcionalidades principais foram consideradas operacionais.

---

## ☁️ Deploy

O deploy foi realizado no **Streamlit Community Cloud**, utilizando o repositório do GitHub.

Configuração principal:

```text
Arquivo principal: src/app.py
Arquivo de dependências: requirements.txt
```

Link da versão publicada:

https://pratique-matematica-basica-5gyr4nnmabpmxhmhnmyaap.streamlit.app/

---

## 👥 Integrantes

| Integrante                   | Participação principal                                                                       |
| ---------------------------- | -------------------------------------------------------------------------------------------- |
| Luciano Expedito Franco      | Organização, documentação, atualização do repositório, apoio no desenvolvimento e validações |
| João Vitor Geraldo Parussolo | Requisitos, prototipação, desenvolvimento, validação e apresentação do projeto               |
| Brian Giaccon Vilela         | Desenvolvimento, testes, ajustes e demonstração prática da aplicação                         |
| Todos                        | Planejamento, decisões, validações, entrega presencial e relatórios                          |

---

## 📌 Observações

O projeto foi desenvolvido com foco em simplicidade e utilidade.

Durante o desenvolvimento, o professor sugeriu a inclusão de níveis de dificuldade. Posteriormente, a comunidade parceira indicou a necessidade de um nível ainda mais básico e de maior uso de recursos visuais.

A partir desses retornos, foram implementados:

* nível Básico;
* atividades com números menores;
* questões com figuras;
* atividades com imagens de cédulas;
* maior variedade de exercícios visuais.

---

## ✅ Situação Final

* [x] Código-fonte concluído;
* [x] funcionalidades implementadas;
* [x] imagens adicionadas;
* [x] testes realizados;
* [x] aplicação publicada;
* [x] link público funcionando;
* [x] validação realizada;
* [x] entrega presencial concluída;
* [x] documentação atualizada.

A aplicação **Pratique Matemática Básica** está concluída e disponível para utilização.
