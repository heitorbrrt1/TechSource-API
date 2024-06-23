# TechSource-API
**TechSource-API** é o backend para o e-commerce [TechSource](https://github.com/heitorbrrt1/TechSource-UI)

<!-- 
. Ele foi desenvolvido utilizando as seguintes tecnologias:
- **Docker**: Uma plataforma para desenvolvimento, envio e execução de aplicativos em contêineres.
- **Django**: Um framework web em Python que facilita a criação de aplicativos robustos e escaláveis.
- **Django Rest Framework**: Uma extensão do Django que simplifica a criação de APIs RESTful.
- **Nginx**: Um servidor web e proxy reverso que melhora o desempenho e a segurança.
- **Postgres**: Um sistema de gerenciamento de banco de dados relacional.
-->

<div style="display: inline-block; padding: 20px;">
   <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original-wordmark.svg" width="60" height="60"/>
   <img src="https://static.djangoproject.com/img/logos/django-logo-negative.svg" width="70" height="70"/>
   <img src="https://www.django-rest-framework.org/img/logo.png" width="100" height="50"/>
   <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nginx/nginx-original.svg" width="60" height="60"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" width="50" height="50"/>
</div>


## Configuração do Ambiente

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
