import time
import sys

class Animator:
    def __init__(self):
        self.colors = __import__('utils.colors', fromlist=['Colors']).Colors()
    
    def loading_animation(self, text="Loading", duration=2):
        """Fast loading animation"""
        frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        start_time = time.time()
        
        while time.time() - start_time < duration:
            for frame in frames:
                sys.stdout.write(f"\r{self.colors.CYAN}[{frame}] {text}{self.colors.RESET}")
                sys.stdout.flush()
                time.sleep(0.1)
        
        sys.stdout.write(f"\r{self.colors.GREEN}[✓] {text} Complete!{self.colors.RESET}\n")
    
    def animate_exit(self):
        """Cool exit animation"""
        messages = [
            "Cleaning traces...",
            "Securing session...", 
            "Goodbye! 👋",
            "CYBER ARMADA - Stay Secure!"
        ]
        
        for msg in messages:
            print(f"{self.colors.BLUE}[→] {msg}{self.colors.RESET}")
            time.sleep(0.5)