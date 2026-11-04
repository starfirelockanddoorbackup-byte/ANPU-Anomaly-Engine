@echo off
TITLE ANPU // Local Intelligence Node
COLOR 0A

echo ========================================================
echo   ANPU // MULTI-DOMAIN ANOMALY INTELLIGENCE ENGINE
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
echo [+] Step 2: Running Isolation Forest anomaly scoring engine...
py anpu_anomaly_engine.py

:END
echo.
echo ========================================================
echo   CYCLE COMPLETE. AWAITING OPERATOR INPUT OR NEXT SCHEDULE.
echo ========================================================
pause