from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

def perform_kmeans(transactions):
    transactions_str = [" ".join(items) for items in transactions]
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(transactions_str)
    kmeans = KMeans(n_clusters=2, random_state=42).fit(X)
    clustered = {}
    for idx, label in enumerate(kmeans.labels_):
        clustered.setdefault(label, []).append(transactions[idx])
    return clustered