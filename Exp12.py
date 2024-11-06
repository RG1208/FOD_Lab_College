import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'User': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Bob', 'Charlie', 'Charlie', 'Charlie'],
    'Item': ['Item1', 'Item2', 'Item3', 'Item1', 'Item2', 'Item3', 'Item1', 'Item2', 'Item3'],
    'Rating': [5, 3, 2, 4, 5, 1, 2, 3, 5]
}

df = pd.DataFrame(data)

user_item_matrix = df.pivot(index='User', columns='Item', values='Rating').fillna(0)

user_similarity = cosine_similarity(user_item_matrix)

user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

def recommend_items(user, num_recommendations=3):

    similar_users = user_similarity_df[user].sort_values(ascending=False)

    similar_users = similar_users[similar_users.index != user]

    similar_user_ratings = user_item_matrix.loc[similar_users.index]

    weighted_ratings = similar_user_ratings.T.dot(similar_users)
 
    recommendations = weighted_ratings / similar_users.sum()

    recommended_items = recommendations.sort_values(ascending=False).head(num_recommendations)
    
    return recommended_items

recommended_for_alice = recommend_items('Alice')
print("Recommendations for Alice:")
print(recommended_for_alice)

