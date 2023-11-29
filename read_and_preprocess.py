import os
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from bs4 import BeautifulSoup # used for HTML parsing
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

def read_reviews(folder_path):
    """Reads the reviews in the folder path, storing label (derived from star rating) and content in a dictionary."""
    reviews = {}

    # Retrieve all review files in directory
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Verify file path is valid before reading
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Remove HTML tags (e.g. <br></br>)
                soup = BeautifulSoup(content, "html.parser")
                content = soup.get_text()

                # Extract star rating from filename (id_star.txt format)
                star_rating = int(filename.split('_')[-1].split('.')[0])
                # Assign labels given extracted star rating
                label = 1 if star_rating >= 7 else 0

                # Assign each review a dictionary of label and content
                reviews[filename] = {'content': content, 'label': label}

    return reviews

def get_wordnet_pos(treebank_tag):
    """Converts the POS naming scheme from the Penn Treebank tag to a WordNet tag."""
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        # Wordnet lemmatize function will default to NOUN anyways
        return wordnet.NOUN

stoplist = set(stopwords.words('english'))

def verify_stopwords_punctuation(token, a_stopwords, a_punctuation):
    """Verifies whether a token is a stopword or part of punctuation given filtering criteria."""
    return (not a_stopwords or not token in stoplist) and (not a_punctuation or not token in string.punctuation)

def preprocess_reviews(contents, a_stopwords = False, a_punctuation = False, a_stemming = False, a_lemmatization = False):
    """Applies tokenization, n-gram generation, and further preprocessing based on supplied criteria."""
    # Initialisation
    stemmer = LancasterStemmer()
    lemmatizer = WordNetLemmatizer()
    n_gram_size = 2 # not in parameters as not part of feature selection
    
    preprocessed_contents = []

    for content in contents:
        # Apply tokenization
        tokens = nltk.word_tokenize(content)

        # Apply preprocessing based on criteria supplied
        if a_stemming:
            preprocessed_tokens = [stemmer.stem(token.lower()) for token in tokens if verify_stopwords_punctuation(token, a_stopwords, a_punctuation)]
        elif a_lemmatization:
            pos_tags = nltk.pos_tag(tokens)
            preprocessed_tokens = [lemmatizer.lemmatize(token, get_wordnet_pos(pos)).lower() for token, pos in pos_tags if verify_stopwords_punctuation(token, a_stopwords, a_punctuation)]
        else:
            preprocessed_tokens = [token.lower() for token in tokens if verify_stopwords_punctuation(token, a_stopwords, a_punctuation)]

        # Generate n-grams (treating them as units due to _)
        preprocessed_n_grams = []

        for i in range(1, n_gram_size + 1):
            n_grams = list(ngrams(preprocessed_tokens, i))

            for n_gram in n_grams:
                preprocessed_n_grams.append('_'.join(n_gram))

        preprocessed_contents.append(' '.join(preprocessed_n_grams))
    
    return preprocessed_contents 