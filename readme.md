# Sentiment Analysis NLP Pipeline

This project presents a Sentiment Analysis pipeline built on a dataset of 4000 movie reviews. It encompasses a variety of models including a Naive Bayes Classifier, SGD Logistic Regression, SVMs, and BERT.

## File Structure Overview

- **`entire_pipeline.ipynb`**: 
  - This Jupyter notebook encapsulates the complete pipeline for evaluating various models, excluding BERT. 
  - It includes the process for hyperparameter optimization of the SVMs model using grid search.

- **`bert.ipynb`**: 
  - Focused on the BERT model, this notebook employs both the base uncased and cased versions of BERT for the analysis.

- **`read_and_preprocess.py`**: 
  - A Python script for reading `.txt` files and assigning labels based on extracted ratings from filenames. 
  - It implements preprocessing steps such as the removal of stopwords and punctuation, and the application of stemming and lemmatization techniques.

- **`tfidf.py`**: 
  - Features a custom implementation of the Term Frequency-Inverse Document Frequency (TF-IDF) algorithm.

- **`naive_bayes.py`**: 
  - Contains a custom implementation of the Naive Bayes Classifier.

