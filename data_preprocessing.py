import os
import spacy
from spacy.cli import download

download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")

def read_reviews(folder_path):
    reviews = {}

    for filename in os.listdir(folder_path): # Retrieves all reviews files in directory
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

                # Extract star rating from filename (id_star.txt format)
                star_rating = int(filename.split('_')[-1].split('.')[0])
                # Assign labels given extracted star rating
                label = 1 if star_rating >= 7 else 0

                # Apply preprocessing on review content
                tokens = preprocess_review(content)

                # Assign each review a dictionary of label and preprocessed content
                reviews[filename] = {'label': label, 'content': tokens}

    return reviews

def preprocess_review(content):
    # Process content using Spacy NLP pipeline
    # Includes tokenization, stopwords flag, lemmatized token
    doc = nlp(content)

    # Apply tokenization, remove stopwords, lemmatization
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    
    return tokens

# Read positive and negative reviews
pos_reviews = read_reviews('../data/pos') 
neg_reviews = read_reviews('../data/neg')  

# Print a specific review
print(f"{len(pos_reviews)} positive reviews in total")
print(pos_reviews['13_7.txt'])

# Generate 3 sets of features 
# 1: stopwords, lemmatization, TFIDF
# 2: stopwords, stemming, TFIDF
# 3: stopwords, lemmatiazation
# 4: CONSIDER OTHER SETS OF FEATURES (e.g. no stopwords, no punctuation)