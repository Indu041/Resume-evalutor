
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_text, job_description):
    corpus = [resume_text, job_description]
    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform(corpus)
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(similarity[0][0] * 100, 2)
