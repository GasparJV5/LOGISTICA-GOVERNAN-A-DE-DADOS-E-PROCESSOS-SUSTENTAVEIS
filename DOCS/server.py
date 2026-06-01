from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__)
CORS(app)

# ✅ CAMINHO DO BANCO
DB = 'mdr.db'

# ✅ CRIAR BANCO
def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT
        )
    ''')

    conn.commit()
    conn.close()

# ✅ ROTA PRINCIPAL (abre teu HTML)
@app.route('/')
def home():
    return send_from_directory('DOCS', 'testemvp.html')

# ✅ SERVE OUTROS ARQUIVOS DA PASTA DOCS
@app.route('/DOCS/<path:filename>')
def docs_files(filename):
    return send_from_directory('DOCS', filename)

# ✅ SALVAR
@app.route('/save', methods=['POST'])
def save():
    data = request.json

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM data")
    cursor.execute("INSERT INTO data (content) VALUES (?)", [json.dumps(data)])

    conn.commit()
    conn.close()

    print("✅ SALVO NO BANCO")
    return jsonify({'status': 'ok'})

# ✅ CARREGAR
@app.route('/load', methods=['GET'])
def load():
    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()

        cursor.execute("SELECT content FROM data ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()

        conn.close()

        if row:
            return jsonify(json.loads(row[0]))
        else:
            return jsonify({"blocks": []})

    except Exception as e:
        print("❌ ERRO AO CARREGAR:", e)
        return jsonify({"blocks": []})

# ✅ BACKUP
@app.route('/backup', methods=['POST'])
def backup():
    data = request.json

    with open('backup_mdr.json', 'w') as f:
        json.dump(data, f)

    print("📁 BACKUP FEITO")
    return jsonify({'status': 'ok'})

# ✅ START DO SERVIDOR (IMPORTANTE)
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
