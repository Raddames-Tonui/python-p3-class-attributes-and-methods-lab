class Song:
    count = []
    genre_count = {}
    artist_count ={}
    GENRES = ["Hip-Hop","Pop", "Trap", "Bongo", "Rap", "Afrobeats", "Rhumba", "House", "Country", "Riddim", "Taarab", "Zilizopendwa", "RnB", "Rock"]
   
    def __init__(self, name, artist, genre):
        if self.check_genre(genre):
            self.name = name
            self.artist = artist
            self.genre = genre
            Song.add_song_to_count(self)
            Song.update_genre_count(genre)  # Update genre count

    # Class methods
    @classmethod
    def check_genre(cls, genre):
        return genre in cls.GENRES

    @classmethod
    def add_song_to_count(cls, song):
        cls.count.append(song)

    @classmethod
    def update_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
        
    @classmethod
    def print_name_of_all_genres(cls):
        genres_with_songs = {song.genre for song in cls.count}
        print(genres_with_songs)
        
    @classmethod
    def print_no_of_songs(cls):
        print([song.artist for song in cls.count])
        print(len(cls.count))

    


big_boys_problem = Song("Big Boys Problem", "Bob", "Bongo")
big_thriller = Song("Big Thriller", "Johnny", "RnB")
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")


# Print the number of songs and their artists
Song.print_no_of_songs()

# Print the names of genres that have associated songs
Song.print_name_of_all_genres()

# Print the genre count
print(Song.genre_count)
