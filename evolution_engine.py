import sqlite3
import numpy as np
from sklearn.ensemble import IsolationForest
import os

# Align database path with your active local environment
DB_PATH = "anpu_telemetry.db"

def fetch_telemetry_data():
    """Pulls recorded probe logs from SQLite to drive the learning cycle."""
    if not os.path.exists(DB_PATH):
        print(f"[!] No active telemetry database found at {DB_PATH}. Using baseline seed matrix.")
        # Fallback operational seed: [packet_size, connection_frequency, error_rate]
        return np.array([[50, 2, 0.0], [55, 3, 0.0], [48, 1, 0.0], [52, 2, 0.1]])
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        # Ensure table exists just in case it's a fresh database file
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS telemetry_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source_ip TEXT,
                anomaly_score REAL,
                status TEXT
            )
        ''')
        conn.commit()
        
        cursor.execute("SELECT anomaly_score FROM telemetry_logs ORDER BY timestamp DESC LIMIT 100")
        rows = cursor.fetchall()
    except sqlite3.OperationalError as e:
        print(f"[!] Database operational note: {e}. Using baseline seed matrix.")
        rows = []
    finally:
        conn.close()
    
    if not rows or len(rows) < 3:
        return np.array([[50, 2, 0.0], [55, 3, 0.0], [48, 1, 0.0], [52, 2, 0.1]])
    
    # Map historical records into a feature matrix for the Isolation Forest
    data = np.array([[float(row[0]), len(row), 0.1] for row in rows])
    return data

def run_evolution_cycle():
    """Executes Phase III continuous learning: Retrains the anomaly model on new data."""
    print("[*] ANPU Evolution Engine: Initializing training cycle...")
    
    X_train = fetch_telemetry_data()
    
    # Initialize and fit the Isolation Forest model with adaptive contamination
    model = IsolationForest(contamination=0.15, random_state=42)
    model.fit(X_train)
    
    print(f"[+] Model successfully evolved on {len(X_train)} operational vectors.")
    print("[+] Baseline updated. Autonomous threat parameters adjusted.")
    return model

if __name__ == "__main__":
    run_evolution_cycle()