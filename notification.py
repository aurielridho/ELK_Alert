#!/usr/bin/env python3

import time
import threading
from connection import search_alerts
from mitigation import fetch_mitigation_from_gemini
from gui import show_popup

def check_alerts():
    # Fungsi untuk memeriksa alert dari Elasticsearch
    hits = search_alerts()  # Memanggil fungsi untuk mencari alert

    rule_details = {}
    for hit in hits:
        alert = hit['_source']
        rule_name = alert.get("kibana.alert.rule.name", "No name")
        timestamp = alert.get("@timestamp", "No timestamp")
        doc_id = hit['_id']
        ip = alert.get("source", {}).get("ip", "No IP")

        if rule_name not in rule_details:
            rule_details[rule_name] = []

        rule_details[rule_name].append({
            "id": doc_id,
            "timestamp": timestamp,
            "ip": ip
        })

    if rule_details:
        rule_summary = {
            "total": sum(len(details) for details in rule_details.values()),
            "rules": rule_details
        }
        threading.Thread(target=show_popup, args=(rule_summary,), daemon=True).start()  # Menampilkan pop-up di thread terpisah

def monitor_alerts():
    global running
    running = True
    while running:
        try:
            check_alerts()
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(60)  # Jeda selama 60 detik sebelum memeriksa lagi

if __name__ == "__main__":
    monitor_alerts()  # Jalankan fungsi monitoring ketika skrip dijalankan
