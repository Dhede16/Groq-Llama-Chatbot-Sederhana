# -*- coding: utf-8 -*-
"""
Chatbot menggunakan Groq API dengan model Llama
Cara menjalankan:
  1. pip install -r requirements.txt
  2. Salin .env.example -> .env lalu isi GROQ_API_KEY
  3. python groq_chatbot.py
"""

import os
import sys
from dotenv import load_dotenv

# Load API key dari file .env (aman, tidak ter-upload ke GitHub)
load_dotenv()

# ─────────────────────────────────────────────
#  KONFIGURASI
# ─────────────────────────────────────────────
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
MODEL        = "llama-3.3-70b-versatile"
MAX_TOKENS   = 1024
TEMPERATURE  = 0.7

SYSTEM_PROMPT = """Kamu adalah asisten AI yang cerdas, ramah, dan membantu.
Jawab pertanyaan dengan jelas dan informatif dalam bahasa yang digunakan pengguna.
Jika tidak tahu jawabannya, katakan dengan jujur."""

AVAILABLE_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "llama3-70b-8192",
    "llama3-8b-8192",
    "mixtral-8x7b-32768",
    "gemma2-9b-it",
]

# ─────────────────────────────────────────────
#  WARNA TERMINAL (Windows & Unix)
# ─────────────────────────────────────────────
if sys.platform == "win32":
    os.system("color")
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        pass

class Color:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE    = "\033[94m"
    GRAY    = "\033[90m"


def print_banner():
    print(f"""
{Color.CYAN}{Color.BOLD}
+----------------------------------------------+
|         GROQ LLAMA CHATBOT                   |
|    Powered by Groq API + Llama 3.3 70B       |
+----------------------------------------------+
{Color.RESET}""")
    print(f"{Color.GRAY}  Model   : {Color.YELLOW}{MODEL}")
    print(f"{Color.GRAY}  Perintah: {Color.GREEN}/help{Color.GRAY} untuk bantuan, {Color.RED}/quit{Color.GRAY} untuk keluar{Color.RESET}\n")


def print_help():
    print(f"""
{Color.CYAN}{'─'*46}
  PERINTAH YANG TERSEDIA
{'─'*46}{Color.RESET}
  {Color.GREEN}/help{Color.RESET}         Tampilkan bantuan ini
  {Color.GREEN}/clear{Color.RESET}        Hapus riwayat percakapan
  {Color.GREEN}/model{Color.RESET}        Ganti model Llama
  {Color.GREEN}/history{Color.RESET}      Tampilkan riwayat chat
  {Color.GREEN}/quit{Color.RESET}         Keluar dari chatbot
{Color.CYAN}{'─'*46}{Color.RESET}
""")


def print_model_list():
    print(f"\n{Color.CYAN}Model yang tersedia:{Color.RESET}")
    for i, m in enumerate(AVAILABLE_MODELS, 1):
        marker = f"{Color.GREEN} <- aktif{Color.RESET}" if m == MODEL else ""
        print(f"  {Color.YELLOW}{i}.{Color.RESET} {m}{marker}")
    print()


# ─────────────────────────────────────────────
#  KELAS CHATBOT
# ─────────────────────────────────────────────
class GroqChatbot:
    def __init__(self, api_key: str):
        if not api_key:
            print(f"""
{Color.RED}[ERROR] GROQ_API_KEY tidak ditemukan!

Langkah perbaikan:
  1. Salin file template  : cp .env.example .env
  2. Buka file .env       : notepad .env
  3. Isi API key kamu     : GROQ_API_KEY=gsk_xxx...

Dapatkan API Key gratis di: https://console.groq.com
{Color.RESET}""")
            sys.exit(1)

        try:
            from groq import Groq
            self.client = Groq(api_key=api_key)
        except ImportError:
            print(f"""
{Color.RED}[ERROR] Library 'groq' belum terinstall!

Jalankan: pip install -r requirements.txt
{Color.RESET}""")
            sys.exit(1)

        self.model   = MODEL
        self.history = []

    def chat(self, user_message: str) -> str:
        self.history.append({"role": "user", "content": user_message})
        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + self.history

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE,
                stream=True,
            )

            full_response = ""
            print(f"\n{Color.MAGENTA}Asisten:{Color.RESET} ", end="", flush=True)

            for chunk in response:
                delta = chunk.choices[0].delta.content
                if delta:
                    print(delta, end="", flush=True)
                    full_response += delta

            print("\n")
            self.history.append({"role": "assistant", "content": full_response})
            return full_response

        except Exception as e:
            print(f"\n{Color.RED}[ERROR] {str(e)}{Color.RESET}\n")
            if self.history and self.history[-1]["role"] == "user":
                self.history.pop()
            return ""

    def clear_history(self):
        self.history = []
        print(f"{Color.GREEN}Riwayat percakapan dihapus.{Color.RESET}\n")

    def show_history(self):
        if not self.history:
            print(f"{Color.YELLOW}  (Belum ada percakapan){Color.RESET}\n")
            return
        print(f"\n{Color.CYAN}{'─'*46}\n  RIWAYAT PERCAKAPAN\n{'─'*46}{Color.RESET}")
        for msg in self.history:
            role  = "Anda   " if msg["role"] == "user" else "Asisten"
            color = Color.BLUE if msg["role"] == "user" else Color.MAGENTA
            content = msg["content"]
            if len(content) > 100:
                content = content[:100] + "..."
            print(f"  {color}{role}:{Color.RESET} {content}")
        print(f"{Color.CYAN}{'─'*46}{Color.RESET}\n")

    def change_model(self):
        global MODEL
        print_model_list()
        try:
            choice = int(input(f"{Color.YELLOW}Pilih nomor model (1-{len(AVAILABLE_MODELS)}): {Color.RESET}"))
            if 1 <= choice <= len(AVAILABLE_MODELS):
                self.model = AVAILABLE_MODELS[choice - 1]
                MODEL = self.model
                print(f"{Color.GREEN}Model diganti ke: {self.model}{Color.RESET}\n")
            else:
                print(f"{Color.RED}Pilihan tidak valid.{Color.RESET}\n")
        except ValueError:
            print(f"{Color.RED}Masukkan angka yang valid.{Color.RESET}\n")


# ─────────────────────────────────────────────
#  FUNGSI UTAMA
# ─────────────────────────────────────────────
def main():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    print_banner()
    bot = GroqChatbot(api_key=GROQ_API_KEY)
    print(f"{Color.GREEN}Chatbot siap! Ketik pesan Anda di bawah.{Color.RESET}\n")

    while True:
        try:
            user_input = input(f"{Color.BLUE}Anda: {Color.RESET}").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Color.YELLOW}Sampai jumpa!{Color.RESET}\n")
            break

        if not user_input:
            continue

        cmd = user_input.lower()
        if cmd in ("/quit", "/exit", "/q"):
            print(f"\n{Color.YELLOW}Sampai jumpa!{Color.RESET}\n")
            break
        elif cmd == "/help":
            print_help()
        elif cmd == "/clear":
            bot.clear_history()
        elif cmd == "/history":
            bot.show_history()
        elif cmd == "/model":
            bot.change_model()
        else:
            bot.chat(user_input)


if __name__ == "__main__":
    main()
