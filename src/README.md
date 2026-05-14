# 📂 Código-Fonte da Aplicação

> Este diretório contém o código-fonte do software desenvolvido pelo Grupo 3 para a disciplina de Seminários III.

---

## Informações do Projeto

| Campo | Informação |
|-------|-----------|
| Nome da aplicação | Pratique Matemática Básica |
| Tecnologias utilizadas | Python e Streamlit |
| URL em produção | A definir / inserir link do deploy após hospedagem |

## Como Executar Localmente

Para executar a aplicação em seu computador, é necessário ter o **Python** instalado.

A aplicação pode ser executada em computadores com **Windows, Linux ou macOS**.

---

### Passo a passo

### 1. Baixar o projeto

Você pode baixar o projeto de duas formas:

#### Opção 1 — Pelo Git

Abra o terminal na pasta onde deseja salvar o projeto e execute:

```bash
git clone https://github.com/ICEI-PUC-Minas-PPC-CC/seminarios3-noite-2026-01-grupo-3
```

Depois, entre na pasta do projeto:

```bash
cd seminarios3-noite-2026-01-grupo-3
```

#### Opção 2 — Baixar como ZIP

1. Acesse o repositório no GitHub.
2. Clique no botão **Code**.
3. Clique em **Download ZIP**.
4. Extraia o arquivo baixado.
5. Abra a pasta extraída no computador.

---

### 2. Abrir o terminal na pasta do projeto

Abra o terminal dentro da pasta principal do projeto.

No Windows, pode ser usado:

- Prompt de Comando;
- PowerShell;
- Terminal do Windows.

No Linux ou macOS, use o Terminal.

---

### 3. Instalar as dependências

Com o terminal aberto na pasta principal do projeto, execute:

```bash
python -m pip install streamlit
```

Caso o comando `python` não funcione, tente:

```bash
py -m pip install streamlit
```

ou:

```bash
python3 -m pip install streamlit
```

---

### 4. Executar a aplicação

Ainda na pasta principal do projeto, execute:

```bash
python -m streamlit run src/app.py
```

Caso o comando `python` não funcione, tente:

```bash
py -m streamlit run src/app.py
```

ou:

```bash
python3 -m streamlit run src/app.py
```

---

### 5. Abrir no navegador

Após executar o comando, a aplicação deverá abrir automaticamente no navegador.

Caso isso não aconteça, copie o endereço exibido no terminal, parecido com este:

```text
http://localhost:8501
```

Depois, cole esse endereço no navegador.

---

## Observação

Para executar localmente, é necessário usar um computador com Python instalado.

Após o deploy em nuvem, a aplicação poderá ser acessada pela internet em qualquer dispositivo com navegador, como computador, notebook, tablet ou celular.
