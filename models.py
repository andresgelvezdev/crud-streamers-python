class Streamer:
    def __init__(self, name, followers, subs):
        self.name = name
        self.followers = followers
        self.subs = subs

class Colors:
    GREEN = "\033[32m"
    RED = "\033[31m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"