# Step 1: Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Step 2: Sample dataset (user-item ratings)
# Columns: 'User', 'Item', 'Rating'
data = {
    'User': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Bob', 'Charlie', 'Charlie', 'Charlie'],
    'Item': ['Item1', 'Item2', 'Item3', 'Item1', 'Item2', 'Item3', 'Item1', 'Item2', 'Item3'],
    'Rating': [5, 3, 2, 4, 5, 1, 2, 3, 5]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 3: Pivot the data to create a User-Item matrix
user_item_matrix = df.pivot(index='User', columns='Item', values='Rating').fillna(0)

# Step 4: Calculate cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)

# Convert similarity matrix to a DataFrame for better readability
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Step 5: Function to recommend items for a given user
def recommend_items(user, num_recommendations=3):
    # Get the similar users to the input user
    similar_users = user_similarity_df[user].sort_values(ascending=False)
    
    # Exclude the input user from the similar users
    similar_users = similar_users[similar_users.index != user]
    
    # Get the ratings of items by similar users
    similar_user_ratings = user_item_matrix.loc[similar_users.index]
    
    # Calculate a weighted average of ratings by the similar users
    weighted_ratings = similar_user_ratings.T.dot(similar_users)
    
    # Normalize the weighted ratings (to avoid bias towards users with higher similarity)
    recommendations = weighted_ratings / similar_users.sum()
    
    # Sort the recommendations and return the top N items
    recommended_items = recommendations.sort_values(ascending=False).head(num_recommendations)
    
    return recommended_items

# Step 6: Example of recommending items for 'Alice'
recommended_for_alice = recommend_items('Alice')
print("Recommendations for Alice:")
print(recommended_for_alice)

