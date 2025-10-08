# 🛒 E-commerce Django

Exemplo de e-commerce simples desenvolvido para a disciplina de **Programação Web** com Django.  

---

## 🚀 Como executar

### Pré-requisitos
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

### Passos
1. Clone o repositório:
    ```bash
    git clone <https://github.com/Guxtavoc/ExemploProgWeb>
    cd <nome-da-pasta>
    ```
2. Execute a aplicação usando Docker Compose:
    ```bash
    docker-compose up
    ```
3. Acesse a aplicação no navegador:
    ```
    http://localhost:8000
    ```
4. Acesse o painel admin:
    ```
    http://localhost:8000/admin
    ```

### Comandos úteis
```bash
# Executar em segundo plano
docker-compose up -d

# Parar a aplicação
docker-compose down

# Ver logs
docker-compose logs

# Criar usuário admin
docker-compose exec web python manage.py createsuperuser
---
```
> 🧠 Este README foi elaborado com o auxílio de uma inteligência artificial (ChatGPT) para facilitar a organização e apresentação das informações.
