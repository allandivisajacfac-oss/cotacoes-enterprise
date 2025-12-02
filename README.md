```markdown
# Projeto de Exemplo Conteinerizado com Banco de Dados (PostgreSQL)

Este projeto demonstra como configurar um aplicativo Python (Flask) com um banco de dados PostgreSQL, ambos executados de forma consistente em ambientes locais (Docker Desktop) e remotos (Render), utilizando a orquestração do Docker Compose.

## 🚀 1. Configuração Local (Docker Desktop)

Certifique-se de ter o [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e em execução.

### 💻 Como Rodar (Usando o Script de Automação)

1. **Torne o script executável:**

   ```bash
   chmod +x setup.sh
   ```

2. **Execute o script de setup:**
   Este comando irá construir a imagem, subir os contêineres e inicializar o banco de dados automaticamente.

   ```bash
   ./setup.sh
   ```

3. **Acesse o Aplicativo:**
   O aplicativo estará acessível em:

   ```
   http://localhost:5000
   ```

4. **Parar o Serviço e Persistência de Dados:**
   Pressione `Ctrl+C` no terminal e depois execute:

   ```bash
   docker-compose down
   ```
   *Para apagar os dados persistidos no volume, use `docker-compose down -v`.*

### 🔍 Processo Manual (Alternativa)

Se preferir fazer manualmente, siga os passos:

1.  **Construir e Subir:** `docker-compose up --build -d`
2.  **Aguardar:** Espere cerca de 10-15 segundos para o banco de dados iniciar.
3.  **Inicializar BD:** `curl -X POST http://localhost:5000/setup`

## 🌐 2. Preparação para Implantação Remota (GitHub)

Siga os passos abaixo para preparar seu repositório:

1. **Crie o Repositório:** Crie um novo repositório vazio no GitHub.
2. **Inicialize e Adicione Arquivos:** Na pasta do projeto local:
   ```bash
   git init
   git add .
   git commit -m "Commit inicial do projeto Flask/Docker/PostgreSQL"
   git branch -M main
   ```
3. **Conecte e Envie:** Conecte o repositório local ao GitHub (substitua `[URL_DO_SEU_REPOSITORIO]`):
   ```bash
   git remote add origin [URL_DO_SEU_REPOSITORIO]
   git push -u origin main