"# ELK_Alert" 

Memantau Alert Keamanan:

Skrip ini dirancang untuk memantau dan memeriksa alert keamanan dari Elasticsearch yang berkaitan dengan potensi ancaman atau masalah dalam sistem yang dipantau. Alert ini diperiksa setiap menit untuk memastikan tidak ada ancaman yang terlewat.
Menampilkan Notifikasi dan Detail:

Ketika ada alert yang ditemukan, skrip akan menampilkan pop-up notifikasi yang berisi ringkasan jumlah rule yang terpicu dan detail terkait dari setiap alert. Pop-up ini menggunakan antarmuka grafis Tkinter untuk menampilkan informasi secara visual, memungkinkan pengguna untuk dengan mudah memahami dan menangani alert.
Mengambil Mitigasi dari API Eksternal:

Untuk setiap rule yang terpicu, skrip akan menggunakan Gemini API untuk mengambil langkah mitigasi atau penjelasan lebih lanjut mengenai cara menangani masalah yang terdeteksi. Ini memberikan panduan tambahan kepada pengguna tentang bagaimana menanggapi setiap alert.
Target Pengguna
