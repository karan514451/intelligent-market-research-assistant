def analyze_sentiment(text):

    positive_words = ["good", "great", "excellent", "best"]

    score = sum(word in text.lower() for word in positive_words)

    if score > 0:
        return "Positive"

    return "Neutral"