class newQuote:
    """
    The newQuote class is used to form quotes for main.py
    """
    def __init__(self, quote, speaker, date, tags):
        self.quote = quote
        self.speaker = speaker
        self.date = date
        self.tags = tags
    
    def toDict(self): # Convert the newQuote object to a dictionar
        return {"quote": self.quote, "speaker": self.speaker, "date": self.date, "tags": self.tags}