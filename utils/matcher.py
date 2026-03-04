from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_match_score(resume_text, jd_text):

    resume_emb, jd_emb = model.encode([resume_text, jd_text])

    score = cosine_similarity([resume_emb], [jd_emb])[0][0]

    return round(score * 100, 2)