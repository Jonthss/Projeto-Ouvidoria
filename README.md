📢 Projeto Ouvidoria

Este projeto é um sistema de Ouvidoria desenvolvido em Python com integração a um banco de dados MySQL. A aplicação permite que usuários registrem reclamações, sugestões ou elogios (manifestações), além de permitir a gestão administrativa desses registros (pesquisa, exclusão e atualização de status).

Desenvolvido como parte da avaliação da disciplina, focado na manipulação de dados via CRUD (Create, Read, Update, Delete).

🚀 Funcionalidades

O sistema opera via terminal (CLI) e oferece as seguintes opções:

Listar Manifestações: Exibe todas as ocorrências registradas no banco.

Criar Nova Manifestação: Insere um novo problema ou sugestão.

Contador: Exibe o número total de registros no sistema.

Pesquisar por Código: Busca detalhes de uma manifestação específica pelo ID.

Atualizar Status: Altera o estado da manifestação (Ex: De Pendente para Resolvido ou Fechado).

Deletar Manifestação: Remove um registro do banco de dados (com confirmação de segurança).

🛠️ Tecnologias Utilizadas

Python 3

MySQL (Banco de Dados)

MySQL Connector (Driver de conexão)

🗂️ Estrutura do Projeto

main.py: Arquivo principal que executa o menu e o loop do sistema.

funcoes_ouvidoria.py: Contém a lógica de negócios (funções para listar, criar, deletar, etc.).

operacoesbd.py: Módulo responsável pela conexão e execução de comandos SQL no banco (wrapper).

📝 Pré-requisitos e Configuração do Banco de Dados

Antes de executar, é necessário preparar o banco de dados.

Certifique-se de ter o MySQL instalado.

Crie o banco de dados e a tabela conforme a estrutura abaixo:

-- Criação da Tabela 'ouvidoria'
CREATE TABLE ouvidoria (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    problema VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'Pendente'
);


Nota: O código atual está configurado para conectar no banco locadora_guylherme (conforme linha 5 do main.py). Você pode alterar esse nome no código ou criar o banco com esse nome.

⚙️ Instalação e Execução

Clone o repositório:

git clone [https://github.com/seu-usuario/projeto-ouvidoria.git](https://github.com/seu-usuario/projeto-ouvidoria.git)
cd projeto-ouvidoria


Instale a dependência do MySQL:

pip install mysql-connector-python


Configure a Conexão:
Abra o arquivo main.py e verifique a linha de conexão. Altere os parâmetros 'localhost', 'root', 'SENHA', 'NOME_DO_BANCO' para corresponderem ao seu ambiente local:

# Exemplo em main.py
conexao = criarConexao('localhost', 'root', 'sua_senha_aqui', 'seu_banco_aqui')


Execute o projeto:

python main.py


👤 Autor

Jonathas Barbosa de Oliveira

Projeto Ouvidoria - Etapa 2

Curso: Análise e Desenvolvimento de Sistemas