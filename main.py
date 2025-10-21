import os
import sys
import time
from modules.dodos_attack import DDoSAttack
from modules.exploit_tool import ExploitFramework
from modules.bypass_system import BypassTools
from modules.page_killer import PageKiller
from modules.link_destroyer import LinkDestroyer
from utils.colors import Colors
from utils.animator import Animator

class CyberArmada:
    def __init__(self):
        self.colors = Colors()
        self.animator = Animator()
        self.modules = {
            '1': {'name': 'DDoS Attack', 'class': DDoSAttack},
            '2': {'name': 'Exploitation', 'class': ExploitFramework},
            '3': {'name': 'Bypass System', 'class': BypassTools},
            '4': {'name': 'Page Killer', 'class': PageKiller},
            '5': {'name': 'Link Destroyer', 'class': LinkDestroyer}
        }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_banner(self):
        self.clear_screen()
        banner = f"""
{self.colors.RED}
╔══════════════════════════════════════════════════════════════╗
║    ██████ ██    ██ ██████  ███████ ██████       █████  ██████  ║  
║   ██      ██    ██ ██   ██ ██      ██   ██     ██   ██ ██   ██ ║
║   ██      ██    ██ ██████  █████   ██████      ███████ ██████  ║
║   ██      ██    ██ ██   ██ ██      ██   ██     ██   ██ ██   ██ ║
║    ██████  ██████  ██████  ███████ ██   ██     ██   ██ ██   ██ ║
║                                                              ║
║    {self.colors.CYAN}C Y B E R   A R M A D A   v2.0{self.colors.RED}                   ║
║         Enterprise Security Testing Framework                ║
╚══════════════════════════════════════════════════════════════╝
{self.colors.RESET}
        """
        print(banner)
    
    def show_menu(self):
        menu = f"""
{self.colors.CYAN}╔══════════════════════════════════════════════════════════════╗
{self.colors.CYAN}║                     {self.colors.YELLOW}⚡ AVAILABLE WEAPONS ⚡{self.colors.CYAN}                    ║
{self.colors.CYAN}╠══════════════════════════════════════════════════════════════╣{self.colors.RESET}

{self.colors.RED}[1] {self.colors.WHITE}DDoS Attack        {self.colors.YELLOW}→ {self.colors.CYAN}Enterprise Grade DDoS
{self.colors.RED}[2] {self.colors.WHITE}Exploitation       {self.colors.YELLOW}→ {self.colors.CYAN}Advanced Exploit Framework  
{self.colors.RED}[3] {self.colors.WHITE}Bypass System      {self.colors.YELLOW}→ {self.colors.CYAN}WAF & Firewall Bypass
{self.colors.RED}[4] {self.colors.WHITE}Page Killer        {self.colors.YELLOW}→ {self.colors.CYAN}Instant Web Page Destroyer
{self.colors.RED}[5] {self.colors.WHITE}Link Destroyer     {self.colors.YELLOW}→ {self.colors.CYAN}Permanent Link Destruction

{self.colors.RED}[0] {self.colors.WHITE}Exit

{self.colors.CYAN}╚══════════════════════════════════════════════════════════════╝{self.colors.RESET}
        """
        print(menu)
    
    def run(self):
        while True:
            self.show_banner()
            self.show_menu()
            
            choice = input(f"\n{self.colors.GREEN}[?] Select weapon: {self.colors.WHITE}").strip()
            
            if choice == '0':
                self.animator.animate_exit()
                break
            
            elif choice in self.modules:
                module_name = self.modules[choice]['name']
                module_class = self.modules[choice]['class']
                
                print(f"\n{self.colors.YELLOW}[!] Loading {module_name}...{self.colors.RESET}")
                self.animator.loading_animation(f"Initializing {module_name}")
                
                # Initialize and run module
                try:
                    module = module_class()
                    module.run()
                except Exception as e:
                    print(f"\n{self.colors.RED}[!] Error: {e}{self.colors.RESET}")
                    input(f"\n{self.colors.CYAN}[+] Press Enter to continue...")
            else:
                print(f"\n{self.colors.RED}[!] Invalid selection!{self.colors.RESET}")
                time.sleep(1)

if __name__ == "__main__":
    try:
        armada = CyberArmada()
        armada.run()
    except KeyboardInterrupt:
        print(f"\n{Colors().RED}[!] Stopped by user{Colors().RESET}")
    except Exception as e:
        print(f"\n{Colors().RED}[!] Fatal error: {e}{Colors().RESET}")