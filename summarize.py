def summarize_fir(text):
    sentences = text.split('.')
    return '. '.join(sentences[:2]) + ('.' if len(sentences) > 1 else '')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

past_firs = [
    "A mobile phone was stolen near the park on May 10th.",
    "An individual was assaulted in the marketplace last night.",
    "A robbery occurred in the local bank on April 3rd."
]

def find_similar_firs(fir_text):
    docs = past_firs + [fir_text]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(docs)
    scores = cosine_similarity(vectors[-1], vectors[:-1]).flatten()
    similar = sorted(zip(past_firs, scores), key=lambda x: x[1], reverse=True)
    return [{"text": s[0], "score": s[1]} for s in similar[:3]]