# Projeto Ouvidoria

Este repositório contém um sistema de **Ouvidoria** desenvolvido em Python, integrando operações de CRUD com um banco de dados MySQL. O projeto permite registrar, listar, pesquisar, atualizar e deletar manifestações dos usuários.

## 📁 Estrutura do Projeto

```
├── main.py
├── operacoesbd.py
├── funcoes_ouvidoria.py
└── README.md
```

## 🗄️ Banco de Dados

O banco utilizado se chama **`locadora_guylherme`**, contendo as seguintes tabelas:

### **Tabela: ouvidoria**
| Coluna     | Tipo        | Descrição |
|------------|-------------|-----------|
| codigo     | INT (PK)    | Identificador único |
| problema   | VARCHAR     | Descrição da manifestação |
| status     | VARCHAR     | Status atual da manifestação |

Exemplo visual:

```
ouvidoria
 ├── codigo
 ├── problema
 └── status
```

## 🧩 Funcionalidades

### ✔ Listagem de manifestações  
Mostra todas as manifestações cadastradas.

### ✔ Criar nova manifestação  
Registra um novo texto no banco de dados.

### ✔ Contagem de manifestações  
Exibe quantas manifestações existem no sistema.

### ✔ Pesquisar por código  
Busca uma manifestação específica pelo ID.

### ✔ Deletar manifestação  
Remove uma manifestação existente mediante confirmação.

### ✔ Atualizar status  
Possibilita alterar o status da manifestação para:
- fechado  
- encerrado  
- resolvido  
- em andamento  
- pendente  

## 🧪 Tecnologias Utilizadas
- Python 3  
- MySQL Connector  
- Banco de Dados MySQL  
- Paradigma estruturado  

## 🚀 Como Executar o Projeto

### 1️⃣ Instale o MySQL Connector:
```bash
pip install mysql-connector-python
```

### 2️⃣ Ajuste as credenciais de conexão em `main.py`:
```python
conexao = criarConexao('localhost', 'seu_usuario', 'sua_senha', 'nome_do_banco')
```

### 3️⃣ Execute o sistema:
```bash
python main.py
```

## 📌 Observações Importantes
- O sistema utiliza *prepared statements* para evitar SQL Injection.  
- Todas as operações com o banco possuem tratamento de exceções.  
- O menu é totalmente interativo via terminal.

---

## 👨‍💻 Autor
Projeto desenvolvido por **Jonathas Barbosa de Oliveira** como parte da atividade acadêmica de Banco de Dados e Programação.

---
