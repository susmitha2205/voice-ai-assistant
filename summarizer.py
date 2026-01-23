# summarizer.py

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict


def summarize_text(text: str, max_sentences: int = 2) -> str:
    if not text:
        return text

    stop_words = set(stopwords.words("english"))

    words = word_tokenize(text.lower())
    freq_table = defaultdict(int)

    for word in words:
        if word.isalnum() and word not in stop_words:
            freq_table[word] += 1

    sentences = sent_tokenize(text)
    sentence_scores = defaultdict(int)

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_table:
                sentence_scores[sentence] += freq_table[word]

    # Pick top N sentences
    ranked_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )

    summary = " ".join(ranked_sentences[:max_sentences])
    return summary
