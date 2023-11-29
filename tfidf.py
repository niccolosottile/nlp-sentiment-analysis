import math
import numpy as np
from collections import defaultdict

def calcualate_tfs(contents):
    """Calculates each n-gram's frequency in each review."""
    doc_terms = defaultdict(dict)
    doc_count = defaultdict(int)  # To store document count for each term
    
    # Assuming 'contents' is a list of review contents
    for i, content in enumerate(contents):
        terms = defaultdict(int)
        seen_terms = set()  # Keep track of terms seen in this document

        # Assuming 'content' is a string containing n-grams separated by white space
        for term in content.split():
            terms[term] += 1

            if term not in seen_terms:
                doc_count[term] += 1
                seen_terms.add(term)
    
        doc_terms[i] = terms

    return doc_terms, doc_count

def calculate_idfs(doc_count, num_docs):
    """Calculates idf for each n-gram."""
    idfs = {}

    for term, count in doc_count.items():
        # Calculate the idf for the given n-gram
        idfs[term] = math.log(num_docs / (1 + count), 10) # Logarithm with base 10

    return idfs


def calculate_tfidfs(contents, idfs, term_to_index):
    """Calculates tf-idf scores for each review."""
    # Initialize an empty array for storing tf-idf scores
    num_docs = len(contents)
    tfidf = np.zeros((num_docs, len(idfs)))

    # Assuming 'contents' is a list of review contents
    for i, content in enumerate(contents):
        terms = defaultdict(int)

        # Count tf for each term if it is in fitted feature space
        for term in content.split():
            if term in term_to_index:
                terms[term] += 1

        # Calculate tfidfs using fitted idfs
        for term, freq in terms.items():
            col_index = term_to_index[term]
            tfidf[i, col_index] = freq * idfs[term]

    return tfidf