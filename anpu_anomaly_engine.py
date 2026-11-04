import sqlite3
import pandas as pd
from sklearn.ensemble import IsolationForest
import sys

DB_PATH = "data/anpu_telemetry.db"

def load_telemetry():
    """Load all historical telemetry logs from SQLite into a pandas DataFrame."""
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM telemetry_logs", conn)
        conn.close()
        return df
    except Exception as e:
        print(f"[-] Error opening telemetry database: {e}")
        print("[-] Run anpu_ingest.py first to initialize the database.")
        sys.exit(1)

def run_anomaly_detection():
    df = load_telemetry()
    
    if df.empty or len(df) < 2:
        print("[!] Insufficient telemetry rows in database to train model. Ingest more cycles first.")
        return

    # Select numerical features for the Isolation Forest feature matrix
    feature_columns = [
        'maritime_dark_transits',
        'cyber_scada_probes',
        'bgp_route_anomalies',
        'grid_frequency_deviation',
        'gps_jamming_index',
        'macro_volatility_index',
        'media_divergence_score',
        'information_vacuum_flag',
        'hti_score'
    ]
    
    X = df[feature_columns]

    # Initialize and fit the Isolation Forest model
    model = IsolationForest(contamination='auto', random_state=42)
    model.fit(X)
    
    # Predict anomalies: 1 = normal (inlier), -1 = anomaly (outlier)
    df['anomaly_prediction'] = model.predict(X)
    df['anomaly_score'] = model.decision_function(X) # Lower score = more anomalous

    # Filter for the most recent cycle
    latest_row = df.iloc[-1]
    is_outlier = latest_row['anomaly_prediction'] == -1

    print("\n" + "="*60)
    print("ANPU // ANOMALY ENGINE EVALUATION READOUT")
    print("="*60)
    print(f"Timestamp: {latest_row['timestamp']}")
    print(f"Hybrid Threat Index (HTI): {latest_row['hti_score']:.2f}")
    print(f"Model Status: {'[!] ANOMALY DETECTED' if is_outlier else '[V] Baseline Nominal'}")
    print(f"Anomaly Path Score: {latest_row['anomaly_score']:.4f}")
    print("-"*60)

    # Operator Feedback Loop (The Closed-Loop Triage Gate)
    if is_outlier or latest_row['hti_score'] > 5.0:
        print("[GATE] High threat threshold breached or structural anomaly flagged.")
        feedback = input("[GATE] Classify event: (t)rue positive, (f)alse alarm, or (s)kip? [t/f/s]: ").strip().lower()
        
        if feedback == 't':
            print("[+] Marked as TRUE POSITIVE. Logging vector signature to local threat memory.")
        elif feedback == 'f':
            print("[+] Marked as FALSE ALARM. Adjusting local model sensitivity thresholds.")
        else:
            print("[+] Skipped operator validation. Maintaining current operating posture.")
    else:
        print("[+] All multi-domain vectors operating within normal statistical variance. No action required.")
    print("="*60 + "\n")

if __name__ == "__main__":
    run_anomaly_detection()