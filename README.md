# Sistema de Cadastro de Usuários

Projeto desenvolvido em Python com SQLite para gerenciamento de usuários através do terminal.

## Funcionalidades

✅ Cadastrar usuários

✅ Listar todos os usuários

✅ Buscar usuário por ID

✅ Atualizar nome, telefone ou e-mail

✅ Remover usuários

✅ Validação de e-mail único

✅ Armazenamento permanente utilizando SQLite

---

## Tecnologias Utilizadas

- Python 3
- SQLite3
- SQL
- Git
- GitHub

---

## Estrutura do Projeto

```text
├── biblioteca/
│   ├── interface/
│   └── data_base/
├── main.py
├── banco.db
└── README.md
```

---

## Banco de Dados

Tabela: `usuario`

| Campo | Tipo |
|---------|---------|
| id | INTEGER |
| nome | TEXT |
| tel | TEXT |
| email | TEXT |

### Características

- ID gerado automaticamente
- Nome obrigatório
- Telefone obrigatório
- E-mail obrigatório e único

---

## Operações SQL Utilizadas

```sql
CREATE TABLE
INSERT INTO
SELECT
UPDATE
DELETE
```

---

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Entre na pasta:

```bash
cd seu-repositorio
```

Execute o programa:

```bash
python main.py
```

---

## Objetivo do Projeto

Este projeto foi desenvolvido para praticar:

- Programação em Python
- Modularização
- Manipulação de Banco de Dados
- SQL
- CRUD (Create, Read, Update e Delete)
- Organização de projetos

---

## Melhorias Futuras

- Busca por nome
- Ordenação de registros
- Exportação para CSV
- Interface gráfica
- Validação avançada de dados

---

## Autor

Helio de Oliveira Santos Neto