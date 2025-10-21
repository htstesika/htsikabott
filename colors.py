class Colors:
    # ANSI color codes
    RED = '\033[38;5;196m'
    GREEN = '\033[38;5;46m'
    YELLOW = '\033[38;5;226m'
    BLUE = '\033[38;5;39m'
    CYAN = '\033[38;5;51m'
    MAGENTA = '\033[38;5;201m'
    WHITE = '\033[38;5;255m'
    ORANGE = '\033[38;5;208m'
    PURPLE = '\033[38;5;129m'
    
    # Background colors
    BG_RED = '\033[48;5;196m'
    BG_GREEN = '\033[48;5;46m'
    BG_BLUE = '\033[48;5;39m'
    
    # Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    
    def rainbow_text(self, text):
        """Create rainbow effect for text"""
        colors = [self.RED, self.ORANGE, self.YELLOW, self.GREEN, self.BLUE, self.PURPLE]
        result = ""
        for i, char in enumerate(text):
            result += colors[i % len(colors)] + char
        return result + self.RESET