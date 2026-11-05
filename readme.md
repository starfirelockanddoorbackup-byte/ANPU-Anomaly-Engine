# ANPU // Anomaly Engine & Edge Defense Suite
**Matthews Operations Lab · Open-Source Infrastructure Security**

ANPU is a lightweight, zero-cloud anomaly detection and edge telemetry monitoring suite engineered to protect local industrial controls, personal servers, and municipal nodes against unauthorized reconnaissance and cyber-attacks. 

Designed for air-gapped and austere environments, ANPU runs entirely on local hardware without relying on external cloud telemetry servers or proprietary third-party APIs.

---

### The Problem We Are Solving
Modern cyber threats target critical infrastructure, small business networks, and home labs with automated low-and-slow probing campaigns. Centralized security tools often fail when wide-area network (WAN) connections drop or when cloud-hosted SIEM platforms are severed. ANPU provides sovereign, autonomous edge protection.

### How ANPU Works (The 3-Step Protection Process)
1. **Trap & Monitor:** Deceptive proxy listeners (such as Honey-PLC Modbus wrappers) monitor network ports and capture foreign packet signatures in real time.
2. **Score Locally:** Unsupervised Isolation Forest algorithms process telemetry logs locally via SQLite, flagging behavioral anomalies in under 15 milliseconds.
3. **Quarantine & Evolve:** Rogue IP addresses and suspicious probe vectors are automatically isolated, while the local evolution engine retrains its baseline threat parameters without leaking data externally.

---

### Core Stack & Architecture
* **Language:** Python 3.10+
* **Database:** Zero-dependency SQLite local event logging
* **Machine Learning:** Scikit-learn Isolation Forest anomaly scoring
* **Architecture:** Modular, single-file or lightweight multi-script layout designed for seamless deployment on low-power hardware (Raspberry Pi, industrial gateways, or local workstations).

> **Note on Local AI (Ollama / LLMs):** ANPU's core anomaly detection engine operates entirely independently. While our primary command desk utilizes local instances of Ollama for advanced log summarization and natural language telemetry parsing, **Ollama is an optional companion tier and is not required or bundled within this repository.**

---

### Quick Start Installation

```bash
# Clone the repository
git clone https://github.com/starfirelockanddoorbackup-byte/ANPU-Anomaly-Engine.git
cd ANPU-Anomaly-Engine

# Install lightweight dependencies
pip install -r requirements.txt

# Launch the telemetry daemon
python anpu_core.py
```

---

### Beta Testing & Contribution
ANPU is currently in active beta testing under the **Matthews Operations Lab** open-source initiative. We welcome security researchers, engineers, and resilience advocates to review the codebase, open issues, and help harden sovereign edge infrastructure.

### License
Distributed under the MIT License. See `LICENSE` for details.

*Powered by Matthews Operations Lab*