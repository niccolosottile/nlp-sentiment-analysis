A Sentiment Analysis NLP pipeline built on a dataset of 4000 movie reviews. Includes Naive Bayes Classifier, SGD Logistic Regression, SVM, and BERT models.

Below is an overview of the file structure and the purpose of each file:

entire_pipeline.ipynb: This Jupyter notebook contains the complete pipeline for evaluating various models (excluding BERT). It also includes the process for hyperparameter optimization of the SVM model using grid search.

bert.ipynb: Dedicated to the BERT model, this notebook implements the pipeline using both the base uncased and cased versions of BERT.

read_and_preprocess.py: A Python script responsible for reading .txt files, assigning labels based on extracted ratings from file names, and applying various preprocessing steps. These steps may include the removal of stopwords and punctuation, as well as the application of stemming and lemmatization techniques.

tfidf.py: Contains a custom implementation of the Term Frequency-Inverse Document Frequency (TF-IDF) algorithm.

naive_bayes.py: Contains a custom implementation of the Naive Bayes Classifier.
