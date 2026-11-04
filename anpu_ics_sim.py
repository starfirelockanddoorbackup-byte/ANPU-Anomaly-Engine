import sqlite3
import random
from datetime import datetime

DB_PATH = "data/anpu_telemetry.db"

def simulate_ics_poll():
    """Simulates passive polling of industrial control registers (Modbus/TCP style)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    timestamp = datetime.utcnow().isoformat()
    
    # Simulated ICS telemetry metrics
    # Normal operation: stable register reads, low unauthorized function codes
    holding_register_variance = round(random.uniform(0.01, 0.05), 3)
    unauthorized_function_codes = random.choice([0, 0, 0, 1]) # Rare rogue command code attempt
    plc_heartbeat_jitter_ms = random.randint(2, 12)
    unexpected_station_connection = random.choice([0, 0, 0, 0, 1]) # Unauthorized IP probe on Level 1
    
    # Calculate an industrial threat score contribution
    ics_threat_index = (
        (holding_register_variance * 10.0) + 
        (unauthorized_function_codes * 5.0) + 
        (plc_heartbeat_jitter_ms * 0.2) + 
        (unexpected_station_connection * 4.0)
    )

    print("\n" + "="*50)
    print("ANPU // ICS PASSIVE SENSOR TELEMETRY POLL")
    print("="*50)
    print(f"Timestamp: {timestamp}")
    print(f"Register Variance: {holding_register_variance}")
    print(f"Unauthorized Function Codes: {unauthorized_function_codes}")
    print(f"PLC Heartbeat Jitter: {plc_heartbeat_jitter_ms}ms")
    print(f"Unexpected Station Connection: {unexpected_station_connection}")
    print(f"Calculated ICS Threat Index: {ics_threat_index:.2f}")
    print("="*50)

    # In a full deployment, this appends or updates an ICS telemetry table in SQLite
    conn.commit()
    conn.close()

if __name__ == "__main__":
    simulate_ics_poll()