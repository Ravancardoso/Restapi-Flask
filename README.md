🐍 Repositório RestAPI-Flask
Repositório voltado ao treinamento sobre as práticas Devops, utilizando uma aplicação RestAPI em Flask.

🌟 Tecnologias Utilizadas
Este projeto utiliza as seguintes tecnologias-chave:

Python 3.x: Linguagem principal para o desenvolvimento da API Flask.

Flask: Micro-framework Python para construir a RestAPI.

Docker: Para conteinerização da aplicação, garantindo um ambiente de execução isolado e consistente.

Docker Compose: Para orquestrar e gerenciar a aplicação e seus serviços (ex: banco de dados, se houver).

Makefile: Utilizado para automatizar tarefas comuns de desenvolvimento e deploy (build, run, testes, etc.).

🛠️ Pré-requisitos
Para rodar este projeto, você precisará ter instalado em sua máquina:

Docker: Necessário para construir e rodar os contêineres.

Docker Compose: Necessário para orquestrar os serviços.

Make: Necessário para executar os comandos de automação.

⚙️ Como Executar
Este projeto foi configurado para ser executado de forma rápida e eficiente usando o Makefile.

1. Clonar o Repositório
2. Executar a Aplicação (Comando Mágico!)
Para construir a imagem Docker e iniciar os contêineres em modo detached (segundo plano), execute:

Este comando fará o seguinte:

Construirá a imagem Docker do projeto (Dockerfile).

Iniciará o contêiner da aplicação e quaisquer serviços dependentes (definidos no docker-compose.yml).

3. Acessar a API
A API estará disponível em: http://localhost:[PORTA_DA_APLICAÇÃO]

Exemplo de Teste Rápido: Tente acessar o endpoint de saúde: http://localhost:[PORTA]/health para confirmar que a aplicação está rodando.

🧹 Comandos Úteis do Makefile
Utilize estes comandos para automatizar tarefas comuns de desenvolvimento e manutenção:

🧪 Rodando Testes
Para executar os testes unitários e de integração, use o comando dedicado:

💡 Contribuição
Sinta-se à vontade para contribuir! Por favor, siga as diretrizes abaixo:

Faça um Fork do projeto.

Crie uma Branch para sua feature (git checkout -b feature/minha-feature).

Faça Commit de suas alterações (git commit -m 'feat: Adiciona nova feature X').

Faça Push para a Branch (git push origin feature/minha-feature).

Abra um Pull Request.

📄 Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo para detalhes.