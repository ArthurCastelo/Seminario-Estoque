
# 📦 Sistema de Estoque com Django REST + Docker + Monitoramento Kuma + Telegram


Este projeto é um sistema de estoque construído com Django REST Framework, containerizado com Docker, com monitoramento integrado via Kuma e notificações via bot do Telegram.

---

## 🚀 Como iniciar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Suba os containers com Docker Compose:**
   ```bash
   docker-compose up -d
   ```

3. **Serviços que serão iniciados:**
   - `web`: servidor Django (API REST).
   - `db`: banco de dados MySQL.
   - `kuma`: sistema de monitoramento.

---

## 🌐 Endpoints disponíveis

| Recurso          | URL Padrão                            | Descrição                                      |
|------------------|----------------------------------------|------------------------------------------------|
| API DRF          | `http://localhost:8000/api/`           | Acesso à API REST principal                    |
| Swagger UI       | `http://localhost:8000/swagger/`       | Documentação interativa da API                |
| Monitoramento    | `http://localhost:3001`                | Interface do Kuma para monitoramento           |

---

## 📂 Endpoints da API

- `/clientes/` - Gerenciamento de clientes
- `/fornecedores/` - Gerenciamento de fornecedores
- `/produtos/` - Gerenciamento de produtos
- `/pedidos/` - Gerenciamento de pedidos

Todos os endpoints estão implementados no arquivo `views.py`.

---

## 📲 Integração com Telegram

O sistema permite o envio de notificações via **bot do Telegram**, incluindo eventos de monitoramento.

### Como configurar:

1. Crie um bot no Telegram com [@BotFather](https://t.me/BotFather).
2. Pegue o **token do bot**.
3. Pegue o **chat ID** do usuário ou grupo que receberá os alertas.
4. Adicione essas variáveis no código ou arquivo `.env` (dependendo da sua estrutura):
   ```env
   TELEGRAM_TOKEN=seu_token_aqui
   TELEGRAM_CHAT_ID=seu_chat_id_aqui
   ```

> **Importante:** Todos os eventos do sistema, incluindo falhas monitoradas pelo Kuma, serão enviados para o Telegram configurado.

---

## 🔐 Acesso ao Monitoramento Kuma

- URL: `http://localhost:3001`
- Usuário: `root`
- Senha: `root123`

Use essas credenciais para acessar o painel web e configurar os monitoramentos desejados.

---

## 🧪 Testando a API

Você pode testar os endpoints usando ferramentas como:
- [Postman](https://www.postman.com/)
- [Insomnia](https://insomnia.rest/)
- Ou diretamente via Swagger: `http://localhost:8000/swagger/`

---

## 🐳 Requisitos

- Docker
- Docker Compose

---

## 🛠️ Futuras Melhorias

- Autenticação com JWT
- Painel frontend em React ou Vue
- Exportação de relatórios
- Testes automatizados

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou _pull request_.
