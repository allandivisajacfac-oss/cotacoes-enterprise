```python
# app.py
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# --- Configuração do Banco de Dados ---
# Pega as credenciais das variáveis de ambiente
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DB_NAME = os.environ.get('POSTGRES_DB')
# Para ambiente local, DB_HOST é 'db'.
DB_HOST = os.environ.get('DB_HOST', 'db') 

# Configuração da URI de conexão. 
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Modelo do Banco de Dados ---
class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

# --- Rotas da Aplicação ---

@app.route('/')
def list_items():
    items = Item.query.all()
    if not items:
        # Mensagem que sugere a rota de setup se a lista estiver vazia
        return jsonify({
            "status": "online",
            "message": "Bem-vindo! O banco de dados está conectado. Tente enviar um POST para /setup para criar a tabela e adicionar dados de exemplo.",
            "items": []
        })
    return jsonify([item.to_dict() for item in items])

@app.route('/setup', methods=['POST'])
def setup_db():
    """Cria as tabelas do BD e popula com dados de exemplo."""
    try:
        # Cria todas as tabelas definidas nos modelos
        db.create_all()
        
        # Adiciona dados de exemplo se a tabela estiver vazia
        if Item.query.count() == 0:
            item1 = Item(name="Laptop Dev", description="Maquina para desenvolvimento conteinerizado.")
            item2 = Item(name="Monitor Ultra", description="Monitor ultrawide para melhor produtividade.")
            db.session.add_all([item1, item2])
            db.session.commit()
            return jsonify({"message": "Banco de dados e tabela 'items' criados e populados com sucesso!"}), 201
        
        return jsonify({"message": "Banco de dados e tabela 'items' criados e populados com sucesso!"}), 201
    except Exception as e:
        # Garante que a sessão seja revertida em caso de erro
        db.session.rollback()
        return jsonify({"error": f"Erro ao configurar o banco de dados: {e}"}), 500

@app.route('/health')
def health_check():
    """Verifica se a aplicação e a conexão com o BD estão funcionando."""
    try:
        # Testa a conexão executando uma consulta simples no BD
        db.session.execute(db.text('SELECT 1'))
        return "OK", 200
    except Exception as e:
        print(f"Database Connection Failed: {e}")
        return "Database Connection Failed", 503

if __name__ == '__main__':
    # O Flask rodará na porta 8080 dentro do contêiner
    app.run(debug=True, host='0.0.0.0', port=8080)
```