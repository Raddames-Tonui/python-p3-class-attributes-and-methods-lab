class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()  # Increment count
        Song.update_artist_count(artist)  # Update artist count
        Song.add_to_genre(genre)  # Add genre to list
        Song.add_to_artist(artist)  # Add artist to list
        Song.add_to_genre_count(genre)  # Update genre count

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def update_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    @classmethod
    def print_name_of_all_genres(cls):
        print(cls.genre_count.keys())
        print(f"{cls.genres} Total: {len(cls.genres)} ")
    
    @classmethod
    def print_name_of_all_artists(cls):
        print(f"Artists: {sorted(cls.artists)}  Total: {len(cls.artists)}")

    @classmethod
    def print_no_of_songs(cls):
        print(cls.count)

    @classmethod
    def print_artist_count(cls):
        print(cls.artist_count)

# Create instances of Song
big_boys_problem = Song("Big Boys Problem", "Bob", "Bongo")
big_thriller = Song("Big Thriller", "Johnny", "RnB")
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")

# Print the number of songs
Song.print_no_of_songs()
Song.print_artist_count()
Song.print_name_of_all_genres()
Song.print_name_of_all_artists()


