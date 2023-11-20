#%%
import os
import spacy
from spacy.cli import download
from nltk.stem.lancaster import LancasterStemmer

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

                # Assign each review a dictionary of label and content
                reviews[filename] = {'label': label, 'content': content}

    return reviews

# Read positive and negative reviews
pos_reviews = read_reviews('../data/pos') 
neg_reviews = read_reviews('../data/neg') 

#%%
def preprocess_reviews(reviews, stopwords = False, punctuation = False, stemming = False, lemmatization = False):
    preprocessed_reviews = {}

    for filename in reviews.keys():
        content = reviews[filename]['content']

        # Process content using Spacy NLP pipeline
        doc = nlp(content)

        if stemming:
            # Lemmatization not available in Spacy, using NLTK's LancasterStemmer
            st = LancasterStemmer()
            # Applying stemming
            tokens = [st.stem(token.text.lower()) for token in doc if (stopwords and not token.is_stop) and (punctuation and not token.is_punct)]
        elif lemmatization:
            # Applying lemmatization
            tokens = [token.lemma_.lower() for token in doc if (stopwords and not token.is_stop) and (punctuation and not token.is_punct)]
        else:
            tokens = [token.text.lower() for token in doc if (stopwords and not token.is_stop) and (punctuation and not token.is_punct)]

        preprocessed_reviews[filename] = {'label': reviews[filename]['label'], 'content': tokens}
    
    return preprocessed_reviews 

# Preprocess data
preprocessed_pos = preprocess_reviews(pos_reviews, True, True, False, True)
preprocessed_neg = preprocess_reviews(neg_reviews, True, True, False, True)

# Print a specific review
print(f"{len(preprocessed_pos)} positive reviews in total")
print(preprocessed_pos['13_7.txt'])

# Generate 3 sets of features 
# 1: stopwords, lemmatization, TFIDF
# 2: stopwords, stemming, TFIDF
# 3: stopwords, lemmatization
# 4: stopwords, punctuation, lemmatization

# Apply n-gram after on features set