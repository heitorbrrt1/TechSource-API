# TechSource-API

TechSource-API é o backend de um e-commerce chamado TechSource, construído utilizando Django Rest Framework para fornecer uma plataforma de serviços de tecnologia. Ele utiliza Docker para a facilitação do ambiente de desenvolvimento e implementação, Nginx como servidor web e Postgres como banco de dados.

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
