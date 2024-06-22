# TechSource-API

**TechSource-API** é o backend para o e-commerce [TechSource](https://github.com/heitorbrrt1/TechSource-UI). Ele foi desenvolvido utilizando as seguintes tecnologias:

- **Docker**: Uma plataforma para desenvolvimento, envio e execução de aplicativos em contêineres.
- **Django**: Um framework web em Python que facilita a criação de aplicativos robustos e escaláveis.
- **Django Rest Framework**: Uma extensão do Django que simplifica a criação de APIs RESTful.
- **Nginx**: Um servidor web e proxy reverso que melhora o desempenho e a segurança.
- **Postgres**: Um sistema de gerenciamento de banco de dados relacional.

## Configuração do Ambiente

### Requisitos
- Docker
- Docker Compose

### Configuração Inicial
   Clone o repositório: `git clone https://github.com/seu-usuario/TechSource-API.git`
   Navegue até o diretório do projeto: `cd TechSource-API`

### Configuração do Banco de Dados
   1. Crie o arquivo `.env` utilizando o arquivo `.env-example` como base.
   2. Configure as variáveis de ambiente no arquivo `.env` para conexão com o banco de dados Postgres conforme necessário. 
   3. Certifique-se de alterar os campos `SECRET_KEY`, `POSTGRES_USER` e `POSTGRES_PASSWORD`.

 
### Executando o Servidor
   Execute o comando  `docker compose up` para iniciar o servidor

### Acessando a API
Após a execução dos passos anteriores, a API estará disponível em `http://localhost:8000/`.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
