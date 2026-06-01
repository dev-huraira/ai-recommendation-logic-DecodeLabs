# 🎯 AI Recommendation Logic — Tech Stack Recommender
## DecodeLabs Industrial Training | Batch 2026 | Project 3

---

### About
A content-based recommendation system that matches
user skills to the most relevant tech career paths.
Built strictly following the DecodeLabs Project 3
PDF specifications.

You enter 3 or more skills and the AI recommends
your Top 3 matching career paths using TF-IDF
vectorization and Cosine Similarity.

---

### How It Works                                     User enters 3+ skills
↓
Step 1: Ingestion — skills captured as user profile
↓
Step 2: Scoring — TF-IDF + Cosine Similarity applied
↓
Step 3: Sorting — results ranked descending
↓
Step 4: Filtering — Top 3 results returned

---

### PDF Concepts Implemented

| PDF Page | Concept | Status |
|---|---|---|
| Page 7 | IPO Framework Input Process Output | ✅ |
| Page 8 | Content-Based Filtering chosen | ✅ |
| Page 9 | Vector Mapping shared vocabulary | ✅ |
| Page 10 | Binary overlap limitation solved | ✅ |
| Page 11 | TF-IDF Feature Extraction | ✅ |
| Page 12 | TF-IDF Mathematical Formula | ✅ |
| Page 13 | Similarity Engine Process Phase | ✅ |
| Page 14 | Euclidean Distance NOT used | ✅ |
| Page 15 | Cosine Similarity Industry Standard | ✅ |
| Page 16 | Score range 0 to 1 | ✅ |
| Page 17 | 4-Step Ranking Pipeline | ✅ |
| Page 18 | Step 1 Ingestion Step 2 Scoring | ✅ |
| Page 19 | Step 3 Sorting Step 4 Filtering Top-N | ✅ |
| Page 20 | Cold Start Problem detected | ✅ |
| Page 21 | Cold Start bypass implemented | ✅ |
| Page 22 | Tech Stack Recommender assignment | ✅ |
| Page 23 | Full execution pipeline | ✅ |

---

### Tech Stack
- Backend: Python, Flask
- ML Libraries: Scikit-Learn, Pandas
- Algorithm: TF-IDF + Cosine Similarity
- Method: Content-Based Filtering
- Dataset: raw_skills.csv (15 job roles)
- Frontend: HTML, CSS, Vanilla JavaScript
- Theme: Black and White

---

### How to Run on Any System

Step 1 - Install Python 3.8 or higher from python.org

Step 2 - Clone the repository:
git clone https://github.com/dev-huraira/ai-recommendation-logic
cd ai-recommendation-logic

Step 3 - Install dependencies:
pip install flask pandas scikit-learn

Step 4 - Run the web server:
python app.py

Step 5 - Open in browser:
http://localhost:5000

---

### How to Use

1. Open http://localhost:5000
2. Type a skill in the input field
3. Press Enter or comma to add it as a tag
4. Add at least 3 skills
5. Click GET RECOMMENDATIONS
6. See your Top 3 matching career paths

---

### Sample Test Skills

Test 1 - Should recommend Data Scientist and ML roles:
Python, Machine Learning, TensorFlow, SQL, Statistics

Test 2 - Should recommend DevOps and Cloud roles:
AWS, Docker, Kubernetes, Linux, Automation

Test 3 - Should recommend Frontend and Full Stack roles:
JavaScript, React, HTML, CSS, TypeScript

---

### Dataset
15 job roles in raw_skills.csv including:
- Data Scientist
- DevOps Engineer
- Backend Developer
- Frontend Developer
- ML Engineer
- Cloud Architect
- Cybersecurity Analyst
- Data Analyst
- Full Stack Developer
- AI Research Engineer
- Mobile Developer
- Database Administrator
- Network Engineer
- Software Engineer
- Project Manager

---

### Cold Start Problem
If no skills match any job role the system detects
a Cold Start Problem (PDF Page 20) and shows a
warning message asking the user to try different skills.

---

### Project Structure
ai-recommendation-logic/
├── recommender.py        ← Core recommendation logic
├── app.py                ← Flask web server
├── raw_skills.csv        ← Dataset
├── requirements.txt      ← Dependencies
├── .gitignore            ← Git ignore rules
├── README.md             ← This file
└── templates/
└── index.html        ← Web UI

---

### Built By
- Program : DecodeLabs Industrial Training
- Batch   : 2026
- Project : Project 3 - AI Recommendation Logic
- Contact : decodelabs.tech@gmail.com
- Website : www.decodelabs.tech
