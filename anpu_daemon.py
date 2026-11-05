import time
import subprocess
from datetime import datetime

# Define how often ANPU should poll and evaluate telemetry (e.g., every 30 minutes)
POLL_INTERVAL_SECONDS = 1800 

def run_pipeline_cycle():
    print(f"\n[ANPU DAEMON] Starting automated intelligence cycle at {datetime.now().isoformat()}")
    try:
        # 1. Run multi-domain ingestion
        subprocess.run(["py", "anpu_ingest.py"], check=True)
        
        # 2. Run passive ICS simulation poll
        subprocess.run(["py", "anpu_ics_sim.py"], check=True)
        
        # 3. Run Isolation Forest anomaly scoring engine
        subprocess.run(["py", "anpu_anomaly_engine.py"], check=True)
        
        print("[ANPU DAEMON] Cycle completed successfully. Baseline updated.")
    except subprocess.CalledProcessError as e:
        print(f"[-] ERROR during daemon cycle execution: {e}")

if __name__ == "__main__":
    print("="*60)
    print(" ANPU // AUTONOMOUS INTELLIGENCE DAEMON ACTIVE")
    print(f" Polling frequency: Every {POLL_INTERVAL_SECONDS // 60} minutes.")
    print("="*60)
    
    # Run immediately on launch
    run_pipeline_cycle()
    
    # Keep running in a continuous background loop while your office workstation is active
    while True:
        try:
            time.sleep(POLL_INTERVAL_SECONDS)
            run_pipeline_cycle()
        except KeyboardInterrupt:
            print("\n[!] Daemon paused by operator. Exiting safely.")
            break