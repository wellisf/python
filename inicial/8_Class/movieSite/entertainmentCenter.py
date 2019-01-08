import fresh_tomatoes
import movie

toy_story = movie.Movie('Toy Story', 'Toys come to life',
                  'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                  'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = movie.Movie("Avatar", "A marine on an alien planet", 
               "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
               "https://www.youtube.com/watch?v=5PSNL1qE6VY")

interview_vampire = movie.Movie("Interview with the Vampire","The narrative is framed by a present-day interview",
                 "https://upload.wikimedia.org/wikipedia/en/f/fe/InterviewwithaVampireMoviePoste.JPG",
                 "https://www.youtube.com/watch?v=qmFYu8x46VY")

movies = [toy_story, avatar, interview_vampire]

fresh_tomatoes.open_movies_page(movies)
