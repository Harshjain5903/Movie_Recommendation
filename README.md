# Project: Movie Recommender System Using Machine Learning

**By Harsh Jain**

<img src="demo/6.jpeg" alt="workflow" width="70%">

Recommendation systems are becoming increasingly important in today’s extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, recommendation systems help them make the right choices without having to expend excessive cognitive resources.

The purpose of a recommendation system is to search for content that would be interesting to an individual. It uses multiple factors to create personalized lists of useful and interesting content specific to each user. These systems rely on Artificial Intelligence–based algorithms that analyze all possible options and create customized lists based on user profiles, browsing history, and behavioral patterns. The results are generated through predictive modeling and heuristics with available data.

---

## Types of Recommendation Systems

### 1) Content-Based

* Uses item attributes and user preferences to recommend similar items.
* Common examples: **YouTube**, **Twitter**, **Spotify**.
* Works by analyzing item features (e.g., genre, artist, keywords) and user actions.
* Creates item vectors using embeddings and recommends items with similar vectors.
* Limitation: Over-specialization — users may receive repetitive recommendations within limited categories.

### 2) Collaborative Filtering

* Based on **user-item interactions** and similarities between users or items.
* Example: **Book or movie recommendations** based on user ratings.
* Principle: If User A and User B have similar tastes, items liked by User B can be recommended to User A.
* Challenges:

  * Large **user-item matrix** → computationally expensive.
  * Bias towards popular items.
  * Difficulty recommending **new/unrated** items.

### 3) Hybrid Systems

* Combine **content-based** and **collaborative** methods to overcome their limitations.
* Widely used in modern platforms (Netflix, Amazon).
* Often utilize **embeddings**, **Word2Vec**, or other feature-combination models.

---

## About This Project

This is a **Streamlit web application** that recommends movies similar to the one selected by the user.

👉 [**Click here to try the live demo**](https://movie-recommeder-system.herokuapp.com/)

---

## Demo

<img src="demo/1.png" alt="workflow" width="70%">  
<img src="demo/2.png" alt="workflow" width="70%">  
<img src="demo/3.png" alt="workflow" width="70%">  

---

## Dataset Used

🎬 [TMDB 5000 Movie Dataset (Kaggle)](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

---

## Core Concept: Cosine Similarity

1. **Cosine Similarity** measures the angle between two vectors to determine how similar they are.
2. Each movie is represented as a vector of features (genre, description, etc.).
3. Cosine similarity produces values between **0 (different)** and **1 (identical)**.
4. This allows us to recommend movies that are mathematically “close” to the user’s choice.

📘 Reference: [Learn Data Sci – Cosine Similarity](https://www.learndatasci.com/glossary/cosine-similarity/)

---

## How to Run

### Step 1 — Clone the repository

```bash
git clone https://github.com/harshjain5903/Movie-Recommender-System.git
cd Movie-Recommender-System
```

### Step 2 — Create a Conda environment

```bash
conda create -n movie python=3.7.10 -y
conda activate movie
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Generate models

```bash
# Run this notebook to preprocess data and build the model
Movie Recommender System Data Analysis.ipynb
```

### Step 5 — Launch the app

```bash
streamlit run app.py
```

---

## Author

**Harsh Jain**
Master’s in Computer Science, University of Illinois Chicago
📧 [harshsjain9@gmail.com](mailto:harshsjain9@gmail.com)
🌐 [harshjain.us](https://harshjain.us)
💻 [GitHub: harshjain5903](https://github.com/harshjain5903)
