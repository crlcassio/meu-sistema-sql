import os
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "chave_secreta_online"

# URL DE CONEXÃO DO SUPABASE (Cole a sua aqui)
DATABASE_URL = "postgresql://postgres:[SQLSucumbencias]@db.xvcvnxbhwdovvulwudgz.supabase.co:5432/postgres"

def get_db_connection():
    try:
        # O psycopg2 consegue conectar direto usando a URI
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"Erro: {e}")
        return None

# ... (Mantenha as rotas @app.route iguaizinhas às anteriores) ...

if __name__ == '__main__':
    # Na nuvem, o servidor define a porta automaticamente
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)