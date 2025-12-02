### 3. `Dockerfile` (Receita da Imagem Docker)

```dockerfile
# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de dependências e instale-as
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta na qual o aplicativo Flask irá rodar
EXPOSE 8080

# Defina o comando para rodar o aplicativo quando o contêiner for iniciado
CMD ["python", "app.py"]
```
