import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# PDF Page 22 - raw_skills.csv dataset
def load_dataset():
    return pd.read_csv("raw_skills.csv")


# PDF Pages 7, 17, 18, 19 - IPO and 4-step ranking pipeline
def get_recommendations(user_skills, top_n=3):
    # PDF Page 18 - Ingestion Step minimum 3 skills validation
    if not isinstance(user_skills, list) or len(user_skills) < 3:
        raise ValueError("Minimum 3 skills required")

    # PDF Pages 7, 18 - PHASE 1 INPUT: user profile ingestion
    cleaned_user_skills = [str(skill).strip().lower() for skill in user_skills if str(skill).strip()]
    if len(cleaned_user_skills) < 3:
        raise ValueError("Minimum 3 skills required")
    user_profile = " ".join(cleaned_user_skills)

    # PDF Page 22 - dataset loading for item features
    df = load_dataset()

    # PDF Pages 9, 11, 13, 18 - PHASE 2 PROCESS: shared vocabulary + TF-IDF weighting
    documents = df["skills"].fillna("").astype(str).str.lower().tolist() + [user_profile]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # PDF Pages 15, 16 - cosine similarity scoring (0 to 1 range)
    job_vectors = tfidf_matrix[:-1]
    user_vector = tfidf_matrix[-1]
    similarity_scores = cosine_similarity(user_vector, job_vectors).flatten()

    # PDF Page 20 - Cold Start detection if max score is 0
    if len(similarity_scores) == 0 or similarity_scores.max() == 0:
        return {
            "recommendations": [],
            "cold_start": True,
            "user_skills": cleaned_user_skills,
            "total_jobs_scored": int(len(df)),
            "algorithm": "TF-IDF + Cosine Similarity",
            "method": "Content-Based Filtering",
        }

    # PDF Page 19 - Step 3 Sorting: descending by score
    sorted_indices = similarity_scores.argsort()[::-1]

    # PDF Page 19 - Step 4 Filtering: Top-N only
    top_indices = sorted_indices[:top_n]

    # PDF Pages 7, 19 - PHASE 3 OUTPUT: Top results formatting
    recommendations = []
    for rank, idx in enumerate(top_indices, start=1):
        match_score = float(similarity_scores[idx])
        recommendations.append(
            {
                "rank": rank,
                "job_role": str(df.iloc[idx]["job_role"]),
                "match_score": match_score,
                "match_percent": round(match_score * 100, 1),
                "skills": str(df.iloc[idx]["skills"]),
            }
        )

    return {
        "recommendations": recommendations,
        "cold_start": False,
        "user_skills": cleaned_user_skills,
        "total_jobs_scored": int(len(df)),
        "algorithm": "TF-IDF + Cosine Similarity",
        "method": "Content-Based Filtering",
    }
