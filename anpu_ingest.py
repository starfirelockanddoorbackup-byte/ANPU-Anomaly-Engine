import os
import sqlite3
from datetime import datetime

# Define database path ensuring the 'data' directory is automatically created
DB_DIR = "data"
DB_NAME = os.path.join(DB_DIR, "anpu_telemetry.db")

def init_multidomain_db():
    """Initializes the SQLite database and creates tables for all intelligence pillars."""
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # 1. Maritime Logistics Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS maritime_metrics (
            timestamp TEXT,
            chokepoint_id TEXT,
            congestion_index REAL,
            dark_vessel_count INTEGER
        )
    ''')
    
    # 2. Cyber Telemetry & Perimeter Probing Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cyber_events (
            timestamp TEXT,
            sector TEXT,
            scan_velocity REAL,
            exploit_chatter_score REAL
        )
    ''')
    
    # 3. Macro-Financial Signals Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS macro_finance (
            timestamp TEXT,
            indicator_name TEXT,
            spread_value REAL,
            liquidity_index REAL
        )
    ''')
    
    # 4. Underground / Dark Web Chatter Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS underground_signals (
            timestamp TEXT,
            topic_vector TEXT,
            mention_velocity REAL,
            credential_dumps INTEGER
        )
    ''')
    
    # 5. Media Narrative & Ground Reporting Divergence Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS media_bias_signals (
            timestamp TEXT,
            headline_topic TEXT,
            left_slant_volume INTEGER,
            right_slant_volume INTEGER,
            independent_ground_reports INTEGER,
            narrative_divergence_score REAL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("[+] ANPU Multi-Domain Database schema initialized successfully.")

def ingest_telemetry_cycle():
    """Ingests a synchronized multi-domain telemetry snapshot across all pillars."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    now = datetime.utcnow().isoformat()
    
    # Insert synchronized vectors
    cursor.execute("INSERT INTO maritime_metrics VALUES (?, ?, ?, ?)", 
                   (now, "CHOKEPOINT_ALPHA", 84.5, 12))
                   
    cursor.execute("INSERT INTO cyber_events VALUES (?, ?, ?, ?)", 
                   (now, "ENERGY_GRID", 92.1, 78.4))
                   
    cursor.execute("INSERT INTO macro_finance VALUES (?, ?, ?, ?)", 
                   (now, "SOVEREIGN_SPREAD", 4.25, -1.8))
                   
    cursor.execute("INSERT INTO underground_signals VALUES (?, ?, ?, ?)", 
                   (now, "ICS_EXPLOIT_STAGING", 88.0, 5))
                   
    cursor.execute("INSERT INTO media_bias_signals VALUES (?, ?, ?, ?, ?, ?)",
                   (now, "GLOBAL_SUPPLY_DISRUPTION", 450, 420, 85, 85.0))
                   
    conn.commit()
    conn.close()
    print(f"[+] Synchronized multi-domain telemetry cycle ingested at {now}")

if __name__ == "__main__":
    init_multidomain_db()
    ingest_telemetry_cycle()