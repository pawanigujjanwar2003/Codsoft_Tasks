class MovieRecommendationSystem:
    def _init_(self):
        self.movie_features = {1: ['Action', 4.5], 2: ['Comedy', 3.8], 3: ['Drama', 4.2],
                               4: ['Action', 3.5], 5: ['Comedy', 4.0]}
        self.user_preferences = {}

    def add_user_preference(self, user_id, movie_id, rating):
        self.user_preferences.setdefault(user_id, {})[movie_id] = rating

    def recommend_movies(self, user_id, top_n=2):
        user_preference = self.user_preferences.get(user_id, {})
        if not user_preference:
            return "No user preferences found. Please rate some movies."

        recommendations = {}
        for movie_id, (genre, _) in self.movie_features.items():
            if movie_id not in user_preference:
                weight = user_preference.get(movie_id, 0)
                if genre not in recommendations:
                    recommendations[genre] = []
                recommendations[genre].append((movie_id, weight))

        sorted_recommendations = {genre: sorted(movies, key=lambda x: x[1], reverse=True)[:top_n]
                                  for genre, movies in recommendations.items()}

        return sorted_recommendations

# Example usage:
recommendation_system = MovieRecommendationSystem()
recommendation_system.add_user_preference(user_id=1, movie_id=2, rating=4.0)
recommendation_system.add_user_preference(user_id=1, movie_id=3, rating=5.0)

user_id = 1
recommendations = recommendation_system.recommend_movies(user_id=user_id, top_n=2)
print(f"Recommended movies for User {user_id}:")
for genre, movies in recommendations.items():
    for movie_id, rating in movies:
        print(f"Movie ID: {movie_id}, Genre: {genre}, User Rating: {rating}")