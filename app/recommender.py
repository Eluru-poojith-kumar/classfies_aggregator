
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend(user_preferences, all_classifieds):
    documents = [cls["title"] + " " + " ".join(cls.get("tags", [])) for cls in all_classifieds]
    documents.insert(0, " ".join(user_preferences))

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)
    similarity = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    scored = list(zip(all_classifieds, similarity))
    scored.sort(key=lambda x: x[1], reverse=True)
    recommendations = [item[0] for item in scored[:5]]
    return recommendations
