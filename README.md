#  Exercícios Práticos & Mini-Sistemas em Python

> **Este Repositorio contem a continuação de alguns exercicios praticos de python!!**

Este repositório foi criado para documentar a minha evolução na linguagem **Python**, reunindo desde a consolidação de sintaxes essenciais até o desenvolvimento de **sistemas orientados a objetos (POO)** com manipulação de arquivos e regras de negócio em linha de comando (CLI)[cite: 2, 6].

---

##  Projetos Integradores em Destaque

### 1.  Sistema Bancário CLI (`ex31.py`)
Aplicação interativa de operações bancárias desenvolvida em **Orientação a Objetos**
* **Destaques Técnicos:**
  * Implementação da classe `Conta` encapsulando atributos (`id`, `nome`, `saldo`) e métodos de movimentação
  * Método `to_dict()` para conversão de objetos em dicionários legíveis para JSON
  * Persistência de dados automática com `json.dump()` e `json.load()` para manter o estado dos dados ao fechar o programa
  * Tratamento de exceções com `try/except FileNotFoundError` para prevenção de falhas no carregamento de arquivos

### 2.  Sistema de Gerenciamento de Biblioteca (`ex32.py`)
Projeto final integrador com múltiplas entidades e controle de acervo.
* **Destaques Técnicos:**
  * Relacionamento entre diferentes classes: `Livro`, `Usuario` e `Biblioteca`
  * Controle de disponibilidade, empréstimos e devoluções de livros
  * Manipulação avançada de listas, dicionários e persistência em disco
Sistema ainda não se encontra versionado pois ainda se encontra incompleto.

### 3.  Sistema de Cadastro de Alunos (`ex30.py`)
Mini-sistema CRUD para gerenciamento de alunos, notas e relatórios de média
* **Destaques Técnicos:**
  * Funções bem divididas para busca, remoção, listagem e adição.
  * Leitura e escrita de estruturas de dados compostas.

---

## Conceitos e Ferramentas Aplicados

* **Paradigma de Programação:** Orientação a Objetos (Classes, Atributos, Métodos, Instanciação)
* **Persistência de Dados:** Arquivos `.json` (com tratamento de caracteres em UTF-8 e formatação limpa)
* **Tratamento de Exceções:** Blocos `try / except` para manipulação segura de cenários de erro
* **Estruturas de Dados:** Listas, Dicionários e List Comprehensions
* **Interface:** Menus interativos via Terminal CLI
---
