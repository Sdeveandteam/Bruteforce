import sys

def generate_wordlist():
    filename = "passwords.txt"
    
    base_words = [
        "admin", "password", "user", "login", "root", "rahasia", "sdev", "skena",
        "creative", "studio", "aesthetic", "gshock", "vans", "vespa", "yaris",
        "kopi", "angkringan", "ronda", "ontel", "pantai", "sore", "senja",
        "bucin", "sayang", "cinta", "kamu", "aku", "ndoro", "mas", "mbak",
        "jakarta", "bandung", "surabaya", "jogja", "malang", "solo", "semarang",
        "qwerty", "asdfghjk", "zxcvbnm", "123456", "12345678", "1234567890",
        "football", "gaming", "online", "hacker", "cyber", "security", "testing"
    ]
    
    suffixes = [
        "", "123", "321", "12345", "77", "99", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",
        "2020", "2021", "2022", "2023", "2024", "2025", "2026", "!", "@", "#", "123!", "123@"
    ]
    
    wordlist = set()
    
    for word in base_words:
        wordlist.add(word)
        wordlist.add(word.lower())
        wordlist.add(word.upper())
        wordlist.add(word.capitalize())
        
    for word in base_words:
        for suffix in suffixes:
            if suffix != "":
                variants = [word, word.lower(), word.upper(), word.capitalize()]
                for v in variants:
                    wordlist.add(f"{v}{suffix}")
                    wordlist.add(f"{suffix}{v}")

    for i in range(100, 1000):
        wordlist.add(str(i))
    for i in range(1980, 2027):
        wordlist.add(str(i))
        
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for password in sorted(wordlist):
                file.write(f"{password}\n")
        print(f"[+] Berhasil membuat {len(wordlist)} wordlist di file: {filename}")
    except Exception as e:
        print(f"[!] Gagal membuat file: {e}")

if __name__ == "__main__":
    generate_wordlist()
