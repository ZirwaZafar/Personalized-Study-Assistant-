import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
import random

# Sample dataset with user progress, topics, and progress tracking
data = {
    'User': ['User1', 'User2', 'User3', 'User4'],
    'Math': [80, 60, 90, 50],
    'Science': [70, 50, 80, 60],
    'History': [60, 40, 70, 80],
    'English': [85, 70, 75, 55],
    'Physics': [78, 65, 88, 40],
    'Progress': [0.85, 0.65, 0.90, 0.70]  # User's overall progress score
}

df = pd.DataFrame(data)
df.set_index('User', inplace=True)

# Normalizing the data to improve recommendation accuracy
df_normalized = (df.drop('Progress', axis=1) - df.drop('Progress', axis=1).mean()) / df.drop('Progress', axis=1).std()

# Using KNN to recommend study topics based on similarity
knn = NearestNeighbors(n_neighbors=2, metric='cosine')
knn.fit(df_normalized)

# Function to recommend study topics for a new user based on their progress
def recommend_study(user_progress):
    user_progress_normalized = (user_progress - np.mean(user_progress)) / np.std(user_progress)
    distances, indices = knn.kneighbors([user_progress_normalized])

    # Identify the most similar user
    similar_user = df.index[indices[0][0]]
    print(f"Recommended study topics for new user based on {similar_user}'s progress:")

    # Display topics based on the most similar user
    user_data = df.loc[similar_user].drop('Progress')  # Ignore the Progress column
    for topic, score in user_data.items():
        print(f"Study {topic}: Current Progress: {score}")

    # Recommend improvements based on similarity
    print("\nSuggested improvements based on similarity:")
    if df.loc[similar_user, 'Progress'] < 0.7:
        print("Focus more on improving Physics and History for better performance.")
    else:
        print("Great progress! Keep maintaining this focus and track your progress.")

# Function to generate random new user profile for recommendations
def generate_new_user_profile():
    math_score = random.randint(50, 100)
    science_score = random.randint(50, 100)
    history_score = random.randint(50, 100)
    english_score = random.randint(50, 100)
    physics_score = random.randint(50, 100)
    return [math_score, science_score, history_score, english_score, physics_score]

# Example: Recommend study topics for a randomly generated new user based on their progress
new_user_progress = generate_new_user_profile()  # Random scores for Math, Science, History, English, Physics
print(f"\nNew User's Progress: {new_user_progress}")
recommend_study(new_user_progress)
