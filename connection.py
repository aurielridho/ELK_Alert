#!/usr/bin/env python3

from elasticsearch import Elasticsearch

# Konfigurasi Elasticsearch
es = Elasticsearch(
    ['https://localhost:9200'],  # URL Elasticsearch
    basic_auth=('elastic', 'tm*8I=B32rkMM7qiSTFN'),  # Otentikasi dasar
    verify_certs=True,  # Verifikasi sertifikat SSL
    ca_certs='/root/elkalert/certs/http_ca.crt'  # Lokasi sertifikat CA
)

def search_alerts():
    # Fungsi untuk mencari alert di Elasticsearch
    query = {
        "size": 10,
        "query": {
            "bool": {
                "filter": [
                    {"range": {"@timestamp": {"gte": "now-1m"}}}  # Filter waktu 1 menit terakhir
                ]
            }
        },
        "_source": ["kibana.alert.rule.name", "@timestamp", "source.ip"],  # Sumber field yang ingin diambil
        "sort": [{"@timestamp": {"order": "desc"}}]  # Urutkan berdasarkan timestamp terbaru
    }

    response = es.search(index=".internal.alerts-security.alerts-default-*", body=query)  # Melakukan pencarian di Elasticsearch

    hits = response['hits']['hits']  # Mendapatkan hasil pencarian

    return hits  # Mengembalikan hasil pencarian
