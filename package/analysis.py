from collections import Counter
import matplotlib.pyplot as plt
import os


stopwords = [
    "the",
    "and",
    "of",
    "in",
    "to",
    "for",
    "with",
    "have",
    "are",
    "is",
    "as",
    "this",
    "that",
    "from",
    "by",
    "a",
    "an",
    "their",
    "however,",
    "also",
    "be",
    "range",
    "high",
    "on",
    "we",
    "has",
    "can",
    "here",
    "as",
    "or",
    "various",
    "at",
    "into",
    "these",
    "such",
    "which",
    "used",
    "been",
    "it",
    "use",
    "using",
    "discuss",
    "review",
    "methods",
    "recent",
    "low",
    "2",
]


def word_frequency(abstract_text):

    words = abstract_text.split()
    words = [word.lower() for word in words if word.lower() not in stopwords]

    word_counts = Counter(words)

    return word_counts


def plot_frequency(total_counts, top_n=30):
    common_words = total_counts.most_common(top_n)
    words, counts = zip(*common_words)

    print("Top 30 Most Common Professional Terms:")
    word_count_dict = dict(zip(words, counts))
    print(word_count_dict)

    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.title(
        f"Top {top_n} Most Common Professional Terms in Abstracts (Excluding Stopwords)"
    )
    plt.xlabel("Professional Terms")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    # plt.show()
    if "PYTEST_CURRENT_TEST" in os.environ:
        plt.savefig("/tmp/test_plot.png")  # 在测试环境中保存图形
    else:
        plt.show()
