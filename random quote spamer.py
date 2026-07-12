
import random
from datetime import datetime
 
QUOTES = [
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "Don't watch the clock; do what it does. Keep going.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "It always seems impossible until it's done.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Sometimes we're tested not to show our weaknesses, but to discover our strengths.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "Little things make big days.",
    "It's going to be hard, but hard does not mean impossible.",
    "Don't wait for opportunity. Create it.",
    "Sometimes later becomes never. Do it now.",
    "The key to success is to focus on goals, not obstacles.",
    "Dream bigger. Do bigger.",
]
 
OUTPUT_FILE = "quote.txt"
 
 
def get_random_quote():
    return random.choice(QUOTES)
 
 
def save_quote_to_file(quote, filename=OUTPUT_FILE):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f'"{quote}"\n\nGenerated on: {timestamp}\n')
 
 
def main():
    quote = get_random_quote()
    save_quote_to_file(quote)
    print(f"Quote saved to {OUTPUT_FILE}:")
    print(f'"{quote}"')
 
 
if __name__ == "__main__":
    main()
 