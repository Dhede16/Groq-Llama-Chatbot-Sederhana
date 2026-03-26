# 🦙 Groq Llama Chatbot

Chatbot berbasis terminal yang menggunakan **Groq API** dengan model **Llama 3.3 70B**. Mendukung streaming real-time, riwayat percakapan, dan pergantian model secara langsung.

---

## ✨ Fitur

- 💬 **Streaming real-time** — respons muncul bertahap seperti ChatGPT
- 🧠 **Memori percakapan** — bot mengingat konteks selama sesi berlangsung
- 🔄 **Ganti model** — pilih model Llama/Mixtral/Gemma saat runtime
- 🎨 **Tampilan berwarna** — antarmuka terminal yang nyaman dibaca
- 🔐 **Aman** — API key dibaca dari file `.env`, tidak hardcode di script

---

## 🚀 Cara Instalasi

### 1. Clone repository ini
```bash
git clone https://github.com/username/groq-llama-chatbot.git
cd groq-llama-chatbot
```

### 2. Install dependensi
```bash
pip install -r requirements.txt
```

### 3. Buat file `.env`
```bash
# Windows
copy .env.example .env

# Mac / Linux
cp .env.example .env
```

Lalu buka `.env` dan isi dengan API key kamu:
```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxx
```

> Dapatkan API Key **gratis** di: [https://console.groq.com](https://console.groq.com)

### 4. Jalankan chatbot
```bash
python groq_chatbot.py
```

---

## 💡 Perintah yang Tersedia

| Perintah | Fungsi |
|---|---|
| `/help` | Tampilkan daftar perintah |
| `/model` | Ganti model AI |
| `/history` | Lihat riwayat percakapan |
| `/clear` | Hapus riwayat percakapan |
| `/quit` | Keluar dari chatbot |

---

## 🤖 Model yang Didukung

| Model | Kecepatan | Kualitas |
|---|---|---|
| `llama-3.3-70b-versatile` | ⚡⚡ | ⭐⭐⭐⭐⭐ |
| `llama-3.1-8b-instant` | ⚡⚡⚡ | ⭐⭐⭐ |
| `llama3-70b-8192` | ⚡⚡ | ⭐⭐⭐⭐ |
| `mixtral-8x7b-32768` | ⚡⚡ | ⭐⭐⭐⭐ |
| `gemma2-9b-it` | ⚡⚡⚡ | ⭐⭐⭐ |

---

## 📁 Struktur Project

```
groq-llama-chatbot/
├── groq_chatbot.py     # Script utama
├── requirements.txt    # Dependensi Python
├── .env.example        # Template konfigurasi (aman di-commit)
├── .gitignore          # File yang diabaikan Git
└── README.md           # Dokumentasi ini
```

---

## 🛠 Teknologi

- [Python 3.8+](https://www.python.org/)
- [Groq API](https://console.groq.com)
- [Llama 3.3 by Meta](https://ai.meta.com/llama/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📄 Lisensi

MIT License — bebas digunakan dan dimodifikasi.
