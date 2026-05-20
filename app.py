from flask import Flask, render_template, request, redirect, url_for
import os
from engine import MonitoringEngine
from readers import CSVLogReader
from writers import CSVLogWriter
from strategies import DurationCalculator

app = Flask(__name__)

# Configuration
DATA_FOLDER = 'data'
LOG_FILE = os.path.join(DATA_FOLDER, 'logs.csv')
os.makedirs(DATA_FOLDER, exist_ok=True)

# Dependency Injection
reader = CSVLogReader()
writer = CSVLogWriter()
strategy = DurationCalculator()
engine = MonitoringEngine(reader, writer, strategy)


@app.route('/')
def index():
    # Get data for dashboard
    active_visitors = engine.get_active_visitors(LOG_FILE)
    all_logs = engine.get_all_logs(LOG_FILE)

    # Calculate duration for finished logs (for display)
    processed_logs = []
    for log in all_logs:
        duration = engine.get_calculated_duration(log)
        processed_logs.append({
            'data': log,
            'duration': duration
        })

    return render_template('index.html', active=active_visitors, logs=processed_logs)


@app.route('/checkin', methods=['POST'])
def check_in():
    name = request.form['name']
    purpose = request.form['purpose']
    contact = request.form['contact']

    engine.check_in(LOG_FILE, name, purpose, contact)
    return redirect(url_for('index'))


@app.route('/checkout/<entry_id>')
def check_out(entry_id):
    engine.check_out(LOG_FILE, entry_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)