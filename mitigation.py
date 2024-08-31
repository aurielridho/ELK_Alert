#!/usr/bin/env python3

import requests

# Konfigurasi Gemini API
gemini_api_key = 'AIzaSyCE1AGLlCHoC3T4zC69osT4-xGZng8XAEM'  # API Key Gemini
gemini_url = 'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent'  # URL Gemini API

def fetch_mitigation_from_gemini(rule_name):
    # Fungsi untuk mengambil mitigasi dari Gemini API
    headers = {'Content-Type': 'application/json'}  # Header untuk request
    data = {
        'contents': [
            {
                'role': 'user',  # Menetapkan peran sebagai user
                'parts': [
                    {
                        'text': (f"Provide mitigation steps and details for the following rule:\n"
                                 f"Rule Name: {rule_name}\n"
                                 f"Please include a detailed explanation of the attack and steps to mitigate it.")  # Konten permintaan
                    }
                ]
            }
        ]
    }
    params = {'key': gemini_api_key}  # Parameter API key
    response = requests.post(gemini_url, headers=headers, json=data, params=params)  # Melakukan request POST ke API
    
    if response.status_code == 200:
        json_response = response.json()  # Parse respons JSON
        if 'candidates' in json_response and len(json_response['candidates']) > 0:
            candidate = json_response['candidates'][0]  # Mengambil kandidat pertama
            if 'content' in candidate and 'parts' in candidate['content'] and len(candidate['content']['parts']) > 0:
                return candidate['content']['parts'][0]['text']  # Mengambil teks mitigasi
            else:
                return "Tidak ada detail mitigasi yang ditemukan dalam respons."  # Tidak ada mitigasi yang ditemukan
        else:
            return "Tidak ada kandidat yang ditemukan dalam respons."  # Tidak ada kandidat yang ditemukan
    else:
        return f"Error: {response.status_code}"  # Mengembalikan pesan error jika status code tidak 200
