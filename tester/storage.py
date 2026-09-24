import sqlite3
import json
import os

# La base sera créée à la racine du projet
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'runs.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS runs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  passed INTEGER,
                  failed INTEGER,
                  error_rate REAL,
                  latency_avg REAL,
                  latency_p95 REAL,
                  full_json TEXT)''')
    conn.commit()
    conn.close()

def save_run(run_data):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    summary = run_data['summary']
    c.execute('''INSERT INTO runs (timestamp, passed, failed, error_rate, latency_avg, latency_p95, full_json)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''',
              (run_data['timestamp'], summary['passed'], summary['failed'],
               summary['error_rate'], summary['latency_ms_avg'], summary['latency_ms_p95'],
               json.dumps(run_data)))
    conn.commit()
    conn.close()

def get_all_runs():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM runs ORDER BY id DESC LIMIT 50')
    rows = c.fetchall()
    conn.close()
    return rows

def get_latest_run():
    runs = get_all_runs()
    if runs:
        return json.loads(runs[0]['full_json'])
    return None