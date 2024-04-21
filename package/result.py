
from .openalex_api import openalex_search, convert_text
from .analysis import word_frequency, plot_frequency
from collections import Counter

def project(query, start_year, end_year):
    top_cited = openalex_search(query, start_year, end_year)
    total_counts = Counter()

    for paper in top_cited:
        abstract_inverted_index = paper.get("abstract_inverted_index")
        if abstract_inverted_index:
            abstract_text = convert_text(abstract_inverted_index)
            word_counts = word_frequency(abstract_text)
            total_counts += word_counts

    
    plot_frequency(total_counts, top_n=30)
