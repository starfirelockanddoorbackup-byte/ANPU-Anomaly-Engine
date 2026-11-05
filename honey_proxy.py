import socket
import datetime
import os

# --- ANPU NODE CONTROL: HONEY-PLC PROXY ---
LOG_DIR = "./logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "honeypot_probes.log")

def log_probe(source_ip, port, payload):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ALERT: Unauthorized probe from {source_ip}:{port} | Payload: {payload}\n"
    print(log_entry.strip())
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

def run_honeypot(host="0.0.0.0", port=502):
    """
    Simulates a standard Modbus/TCP industrial control port (502).
    Acts as Phase I tripwire: Captures reconnaissance and unauthorized scans.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((host, port))
        server.listen(5)
        print(f"[+] ANPU Honey-PLC Proxy active on {host}:{port} [TRIPWIRE SET]")
    except PermissionError:
        print(f"[!] ERROR: Binding to port {port} requires elevated permissions (Run as Administrator).")
        return
    except Exception as e:
        print(f"[!] Error starting proxy: {e}")
        return

    while True:
        try:
            client_sock, address = server.accept()
            source_ip, source_port = address
            
            # Read initial incoming probe payload
            payload = client_sock.recv(1024)
            log_probe(source_ip, source_port, payload)
            
            # Send dummy response to trap/hold the connection briefly
            client_sock.sendall(b"\x00\x01\x00\x00\x00\x06\x01\x03\x00\x00\x00\x01")
            client_sock.close()
        except KeyboardInterrupt:
            print("\n[!] Shutting down Honey-PLC Proxy...")
            break
        except Exception as e:
            print(f"[!] Connection handling error: {e}")

if __name__ == "__main__":
    run_honeypot()