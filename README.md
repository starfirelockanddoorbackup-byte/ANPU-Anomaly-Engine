# ANPU // Cross-Domain Telemetry & Anomaly Engine
**Matthews Operations Lab &bull; Autonomous Edge Resilience Node**

The **ANPU Cross-Domain Telemetry & Anomaly Engine** is a zero-bloat, open-source situational awareness and threat detection tool designed for independent facility operators, regional infrastructure managers, and civil defense units. 

It bridges the blind spot between enterprise IT telemetry, maritime logistics chokepoints, and macroeconomic volatility, running entirely locally (offline-capable) to provide early warning signals ahead of cascading multi-vector disruptions.

---

## Core Architecture

1. **Ingestion Layer (`anpu_ingest.py`):** Pulls hourly RSS intelligence feeds, maritime AIS chokepoint metrics, and macroeconomic bond spreads into a lightweight, self-contained local SQLite database (`anpu_telemetry.db`).
2. **Unsupervised Anomaly Core (`anpu_anomaly_engine.py`):** Utilizes an `IsolationForest` model to evaluate telemetry sequences and calculate a composite **Hybrid Threat Index (HTI)** score without relying on cloud-dependent APIs.
3. **Local Presentation & Feedback Gate (`index.html`):** A high-density, dark-mode web dashboard rendering real-time telemetry with an integrated operator feedback loop (`[True Positive / False Alarm]`) that dynamically adjusts local detection sensitivity weights.

---

## Quick-Start Installation Guide

### Prerequisites
* Python 3.9+
* Git

### Step 1: Clone the Repository
```bash
git clone [https://github.com/your-username/anpu-telemetry-engine.git](https://github.com/your-username/anpu-telemetry-engine.git)
cd anpu-telemetry-engine