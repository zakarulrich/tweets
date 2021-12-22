from datetime import date


class Tweet():
    def __init__(self, text):
        self.text = text
        self.created_at = date.today()
        self.id = None
