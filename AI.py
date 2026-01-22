def recommend_movie(user_interest):

    movies = {
        "Inception": ["sci-fi", "thriller", "mind-bending"],
        "Interstellar": ["sci-fi", "space", "emotional"],
        "Avengers": ["action", "superhero", "fun"],
        "Titanic": ["romance", "emotional", "drama"],
        "Joker": ["psychological", "dark", "drama"]
    }

    user_interest = user_interest.lower()

    
    user_keywords = user_interest.split()

    best_movie = None
    best_score = 0

    
    for movie, tags in movies.items():
        score = 0
        for word in user_keywords:
            if word in tags:
                score += 1

        
        if score > best_score:
            best_score = score
            best_movie = movie

    
    if best_movie:
        return f"🎬 Recommended Movie: {best_movie}"
    else:
        return "Sorry, no recommendation found."



print("🤖 AI Movie Recommendation System")
print("Type 'exit' to stop")

while True:
    interest = input("\nWhat kind of movie do you like? ")

    if interest.lower() == "exit":
        print("Goodbye 👋")
        break

    result = recommend_movie(interest)
    print(result)


    