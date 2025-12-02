```bash
#!/bin/bash
# setup.sh - Script de automação para iniciar o ambiente Docker e configurar o BD.

# Função para verificar o status de um serviço (web)
check_service_status() {
    local max_retries=15
    local retries=0
    local url="http://localhost:5000/health"

    echo "Aguardando o serviço web iniciar e se conectar ao banco de dados..."

    while [ $retries -lt $max_retries ]; do
        # O comando curl tenta se conectar e verifica se a resposta é "OK" (status 200)
        response=$(curl -s -o /dev/null -w "%{http_code}" $url)
        
        if [ "$response" -eq 200 ]; then
            echo "Serviço web iniciado e BD conectado (Status 200)."
            return 0
        fi

        echo "Tentativa $((retries + 1)) de $max_retries falhou. Aguardando 2 segundos..."
        sleep 2
        retries=$((retries + 1))
    done

    echo "ERRO: O serviço web não iniciou a tempo ou a conexão com o BD falhou."
    exit 1
}

# 1. Construir as imagens e subir os contêineres
echo "Construindo e iniciando os serviços (web e db) com docker-compose..."
docker-compose up --build -d

# 2. Esperar o serviço web estar pronto (Health Check)
check_service_status

# 3. Inicializar o banco de dados (criar tabelas e dados de exemplo)
echo "Executando a configuração inicial do banco de dados (/setup)..."
curl -X POST http://localhost:5000/setup

echo ""
echo "========================================================"
echo "✅ SETUP CONCLUÍDO!"
echo "O aplicativo está rodando em http://localhost:5000"
echo "Para parar os serviços, execute: docker-compose down"
echo "========================================================"
```
