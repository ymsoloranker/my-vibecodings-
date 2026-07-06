def analyze_sentence(sentence: str) -> dict:
    """Analyze a sentence and return word count, char count, and reversal."""
    words = sentence.strip().split()
    word_count = len(words)
    char_count = len(sentence.replace(" ", ""))
    reversed_sentence = " ".join(reversed(words))
    return {
        "word_count": word_count,
        "char_count": char_count,
        "reversed": reversed_sentence
    }


if __name__ == "__main__":
    result = analyze_sentence("Claude makes coding fun")
    print(result)
