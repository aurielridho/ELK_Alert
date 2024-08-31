#!/usr/bin/env python3

import tkinter as tk

def show_popup(summary):
    # Fungsi untuk menampilkan pop-up notifikasi dengan scrolling
    window = tk.Tk()  # Membuat instance jendela Tkinter
    window.title("Notifikasi Alert")  # Menetapkan judul jendela
    window.geometry("900x600")  # Menetapkan ukuran jendela
    window.configure(bg="#f0f0f0")  # Menetapkan warna latar belakang

    total_alerts = summary.get("total", 0)  # Mendapatkan total alert
    rule_details = summary.get("rules", {})  # Mendapatkan detail rule

    header = tk.Label(window, text=f"Jumlah Rule Terpicu: {total_alerts}", font=('Helvetica', 14, 'bold'), bg="#f0f0f0")
    header.pack(pady=10)

    canvas = tk.Canvas(window, bg="#ffffff")
    scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)  # Scrollbar vertikal
    scrollable_frame = tk.Frame(canvas, bg="#ffffff")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))  # Mengatur area yang bisa discroll
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")  # Membuat window di canvas
    canvas.pack(side="left", fill="both", expand=True)  # Mengatur penempatan canvas
    scrollbar.pack(side="right", fill="y")  # Mengatur penempatan scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)  # Mengatur scrollbar agar sinkron dengan canvas

    def toggle_details(rule_name):
        if rule_name in details_frames:
            detail_frame = details_frames[rule_name]  # Mendapatkan frame detail berdasarkan nama rule
            if detail_frame.winfo_ismapped():
                detail_frame.pack_forget()  # Sembunyikan frame jika sedang terlihat
                toggle_buttons.get(rule_name, tk.Button()).config(text="Detail")  # Ubah teks tombol menjadi "Detail"
            else:
                detail_frame.pack(fill=tk.X, padx=10, pady=5)  # Tampilkan frame jika tersembunyi
                toggle_buttons.get(rule_name, tk.Button()).config(text="Tutup")  # Ubah teks tombol menjadi "Tutup"

    toggle_buttons = {}  # Dictionary untuk menyimpan tombol toggle
    details_frames = {}  # Dictionary untuk menyimpan frame detail

    for rule_name, details in rule_details.items():
        rule_frame = tk.Frame(scrollable_frame, bg="#ffffff", bd=1, relief=tk.RAISED)  # Membuat frame untuk setiap rule
        rule_frame.pack(pady=5, padx=10, fill=tk.X)

        rule_label = tk.Label(rule_frame, text=rule_name, font=('Helvetica', 12, 'bold'), bg="#ffffff")  # Label untuk nama rule
        rule_label.pack(side=tk.LEFT, padx=5)

        toggle_button = tk.Button(rule_frame, text="Detail", command=lambda r=rule_name: toggle_details(r))  # Tombol untuk toggle detail
        toggle_button.pack(side=tk.RIGHT)
        toggle_buttons[rule_name] = toggle_button  # Simpan tombol ke dictionary

        detail_frame = tk.Frame(scrollable_frame, bg="#ffffff")  # Frame untuk detail rule
        detail_frame.pack(pady=5, padx=10, fill=tk.X)
        detail_frame.pack_forget()  # Sembunyikan frame detail secara default
        details_frames[rule_name] = detail_frame  # Simpan frame detail ke dictionary

        ids_and_ips = []  # List untuk menyimpan ID dan IP dari detail rule
        for detail in details:
            doc_id = detail['id']  # Mengambil ID dokumen
            ip = detail.get('ip', 'No IP')  # Mengambil IP, jika tidak ada akan diisi dengan "No IP"
            ids_and_ips.append(f"ID: {doc_id}\nIP: {ip}")  # Tambahkan ID dan IP ke list

        detail_text = "\n".join(ids_and_ips)  # Gabungkan ID dan IP
        detail_label = tk.Label(detail_frame, text=detail_text, justify=tk.LEFT, bg="#ffffff", wraplength=850)  # Label untuk menampilkan detail
        detail_label.pack(anchor="w")

    window.mainloop()  # Menjalankan loop utama Tkinter
