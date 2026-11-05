@echo off
TITLE ANPU // Local Intelligence Node
COLOR 0A

echo ========================================================
echo   ANPU // MULTI-DOMAIN & ICS ANOMALY INTELLIGENCE ENGINE
echo   Operational Node: Active [Local Windows Execution]
echo ========================================================
echo.

echo [+] Step 1: Executing multi-domain ingestion pipeline...
py anpu_ingest.py

if errorlevel 1 (
    echo [-] ERROR: Ingestion script failed. Check Python environment.
    goto END
)

echo.
echo [+] Step 2: Polling passive ICS registers (Modbus simulation)...
py anpu_ics_sim.py

echo.
echo [+] Step 3: Running ANPU Evolution Engine (Model Retraining)...
py evolution_engine.py

echo.
echo [+] Step 4: Running Isolation Forest anomaly scoring engine...
py anpu_anomaly_engine.py

echo.
echo [+] Step 5: Launching Active Honey-PLC Proxy Listener (Port 502)...
echo [+] Press CTRL+C to terminate the active tripwire listener.
echo ========================================================

:: Spin up the active proxy trap in the foreground
py honey_proxy.py

:END
echo.
echo ========================================================
echo   CYCLE COMPLETE. AWAITING OPERATOR INPUT OR NEXT SCHEDULE.
echo ========================================================
pause