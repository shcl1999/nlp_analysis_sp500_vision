from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def vectorization(df_vision, df_meta):
        # Vectorize the vision data
    vision_vectorizer = TfidfVectorizer(stop_words='english')
    vision_tfidf = vision_vectorizer.fit_transform(df_vision['Processed'])

    # Vectorize the meta words
    meta_vectorizer = TfidfVectorizer(stop_words='english', vocabulary=vision_vectorizer.vocabulary_)
    meta_tfidf = meta_vectorizer.fit_transform(df_meta['[UNK]'])

    # Compute cosine similarity
    similarity_matrix = cosine_similarity(vision_tfidf, meta_tfidf)

    # Calculate percentage similarity for each vision statement
    similarity_percentages = similarity_matrix.max(axis=1) * 100

    # Add the similarity percentages to the vision data
    df_vision['Similarity Percentage'] = similarity_percentages

    return df_vision