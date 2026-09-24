from flask import Flask, render_template, redirect, url_for
from tester.runner import run_suite
from tester.storage import save_run, get_all_runs, get_latest_run

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/run')
def trigger_run():
    # Déclenche les tests métier et sauvegarde le bilan en base
    run_data = run_suite()
    save_run(run_data)
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    # Récupère l'historique et le détail du dernier test pour l'interface
    history = get_all_runs()
    latest = get_latest_run()
    return render_template('dashboard.html', history=history, latest=latest)