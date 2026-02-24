import os
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "sucumbencia_online_2026"

# SUA URL DO SUPABASE (Ajuste a senha abaixo)
DATABASE_URL = "postgresql://postgres:SQLSucumbencias@db.xvcvnxbhwdovvulwudgz.supabase.co:5432/postgres"

def get_db_connection():
    try:
        # Conecta usando a URL completa do Supabase
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"Erro ao conectar no Supabase: {e}")
        return None

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']
    
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute('INSERT INTO usuarios (nome, email) VALUES (%s, %s)', (nome, email))
            conn.commit()
            flash("Registro salvo com sucesso!", "success")
        except Exception as e:
            flash(f"Erro no banco: {e}", "error")
        finally:
            cur.close()
            conn.close()
    return redirect(url_for('ver_usuarios'))

@app.route('/usuarios')
def ver_usuarios():
    conn = get_db_connection()
    users = []
    if conn:
        cur = conn.cursor()
        cur.execute('SELECT id, nome, email FROM usuarios ORDER BY id DESC')
        users = cur.fetchall()
        cur.close()
        conn.close()
    return render_template('usuarios.html', usuarios=users)

if __name__ == '__main__':
    # Porta dinâmica para o Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)