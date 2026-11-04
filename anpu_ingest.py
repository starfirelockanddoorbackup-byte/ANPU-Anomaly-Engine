import sqlite3
import os
from datetime import datetime

DB_PATH = "data/anpu_telemetry.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Expanded Multi-Domain Telemetry Table covering all intelligence pillars
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS telemetry_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            maritime_dark_transits INTEGER,
            cyber_scada_probes INTEGER,
            bgp_route_anomalies INTEGER,
            grid_frequency_deviation REAL,
            gps_jamming_index REAL,
            macro_volatility_index REAL,
            media_divergence_score REAL,
            information_vacuum_flag INTEGER,
            hti_score REAL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("[+] ANPU Multi-Domain Extended Schema initialized successfully.")

def ingest_recon_cycle():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    timestamp = datetime.utcnow().isoformat()
    
    # Simulated incoming telemetry across all recon vectors
    maritime_dark = 4
    cyber_probes = 55
    bgp_anomalies = 2          # BGP Route leaks / prefix shifts
    grid_dev = 0.04            # Frequency deviation from stable baseline (Hz)
    gps_jamming = 1.2          # GNSS degradation index
    macro_volatility = 49.2    # Financial stress indicator
    media_divergence = 88.5    # Spin vs. ground reality delta
    info_vacuum = 1            # 1 if physical anomalies precede mainstream reporting
    
    # Calculate Hybrid Threat Index (HTI) across weighted multi-domain pillars
    hti_score = (
        (maritime_dark * 1.5) + 
        (cyber_probes * 0.5) + 
        (bgp_anomalies * 3.0) + 
        (grid_dev * 20.0) + 
        (gps_jamming * 4.0) + 
        (media_divergence * 0.8)
    ) / 10.0

    cursor.execute('''
        INSERT INTO telemetry_logs (
            timestamp, maritime_dark_transits, cyber_scada_probes, 
            bgp_route_anomalies, grid_frequency_deviation, gps_jamming_index, 
            macro_volatility_index, media_divergence_score, information_vacuum_flag, hti_score
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (timestamp, maritime_dark, cyber_probes, bgp_anomalies, grid_dev, 
          gps_jamming, macro_volatility, media_divergence, info_vacuum, hti_score))
    
    conn.commit()
    conn.close()
    print(f"[+] Recon cycle ingested at {timestamp} // Calculated HTI Score: {hti_score:.2f}")

if __name__ == "__main__":
    init_db()
    ingest_recon_cycle()