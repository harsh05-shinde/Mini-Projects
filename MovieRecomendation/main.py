import numpy as np

#WE ARE BUILDIING THE MOVIE RECOMENDATION SYSTEM

# LABEL GENRE
["Action","Comedy","Drama","Romance","Sci-Fic"]

#MOVIE TITLES 
movie_titles = np.array([
    "The Matrix",
    "Titanic",
    "Avengers",
    "The Notebook",
    "Interstellar",
    "Deadpool",
    "La La Land",
    "Inception",
    "Toy Story",
    "The Godfather"
])

#GENRE VECTOR
movie_genres = np.array([
    [1, 0, 0, 0, 1],  # The Matrix: Action + Sci-Fi
    [0, 0, 1, 1, 0],  # Titanic: Drama + Romance
    [1, 0, 1, 0, 1],  # Avengers: Action + Drama + Sci-Fi
    [0, 0, 1, 1, 0],  # The Notebook: Drama + Romance
    [0, 0, 1, 0, 1],  # Interstellar: Drama + Sci-Fi
    [1, 1, 0, 0, 1],  # Deadpool: Action + Comedy + Sci-Fi
    [0, 1, 1, 1, 0],  # La La Land: Comedy + Drama + Romance
    [1, 0, 1, 0, 1],  # Inception: Action + Drama + Sci-Fi
    [0, 1, 1, 0, 0],  # Toy Story: Comedy + Drama
    [0, 0, 1, 0, 0]   # The Godfather: Drama
])


score_list = []
#Displaying MOvie
for i in enumerate(movie_titles):
    print(i)

#Taking user input
while True:
    try:
        user_input = int(input("Please enter the Index of the Movie:")) 
        if user_input<0 or user_input>9:
            print("Please enter the Numbers in between 0 to 9")
        else:
           break
    except ValueError:
          print("Please enter Numbers Only")
          
          
for i in range(len(movie_genres)):
    dot_product = np.dot(movie_genres[user_input],movie_genres[i])
    Norm_of_movie1 = np.linalg.norm(movie_genres[user_input])
    Norm_of_movie2 = np.linalg.norm(movie_genres[i])

    score = dot_product/(Norm_of_movie1*Norm_of_movie2)
    score_list.append(score)
    
cleaned = [float(i) for i in score_list]

cleaned[user_input] =  -1

sort = np.argsort(cleaned)

reversed_sort = sort[::-1]

Movie_recomendation = movie_titles[reversed_sort[0:3]]
print(Movie_recomendation)















