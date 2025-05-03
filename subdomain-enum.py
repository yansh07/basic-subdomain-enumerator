import socket
import datetime
from concurrent.futures import ThreadPoolExecutor
import re
from colorama import Fore, init, Back, Style
init()

def check_domain(subdomain):
    try:
        ip = socket.gethostbyname(subdomain)
        print(f"{Fore.GREEN}[+] Found: {subdomain} -> {Fore.GREEN}{ip}")
    except socket.gaierror:
        pass


domain = input("Enter domain (e.g., example.com or example.edu/ac.com): ").strip().lower()
if not re.match(r"^(?!www\.)([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$", domain):
    print(Fore.RED + "Invalid domain format!!")
    exit()
try:
    with open("subdomain-list.txt", "r") as file:
        subdomains = [f"{line.strip()}.{domain}" for line in file]
        start = datetime.datetime.now()
except FileNotFoundError:
    print(Fore.RED + "subdomain-list.txt not found!!!")
    exit()

print(Fore.CYAN + f"\n[*] Scanning subdomains for: {domain}\n")

with ThreadPoolExecutor(max_workers=30) as executor:
    for sub in subdomains:
        executor.submit(check_domain, sub)
        
            
end = datetime.datetime.now()
duration = end - start
print(" ")
print(Fore.MAGENTA + "[*] Scan complete\n")
print(Fore.MAGENTA + f"Time taken: {duration}")
print("")