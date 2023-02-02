print("Фільмотека:")

class Filmlist:
    def __init__(self, title, released_year, genre, count_views):
        self.title = title
        self.released_year = released_year
        self.genre = genre   
        self.count_views = count_views    


# Метод play, який збільшує кількість переглядів певної назви на 1.
    def play(self, views=1):
        self.count_views +=views

# Після відображення фільму, як string, показується назва та рік випуску
    def __str__(self):
        return f"{self.title} {self.released_year}"

# Функція, що виводить список фільмів
    def get_movies():
         for movie in Filmlist:
          print (movie)    

    def search():
        movie_title = input("ВВедіть назву фільму: ")
        for movie in Filmlist:
            if movie_title == movie.title:
             print(movie)   
       
movie_1 = Filmlist(title="Avatar: The Way of Water", released_year="2022", genre="Fantasy", count_views="120000")
movie_2 = Filmlist(title="The Batman", released_year="2022", genre="Action", count_views="80000")
movie_3 = Filmlist(title="Bullet Train", released_year="2022", genre="Action", count_views="99000")
movie_4 = Filmlist(title="Watcher", released_year="2022", genre="Drama", count_views="60000")
movie_5 = Filmlist(title="House of Gucci", released_year="2021", genre="Drama", count_views="200000")

class Serials(Filmlist):
    def __init__(self, series_number, season_number, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.series_number = series_number
        self.season_number = season_number

# інформація про серію відображається у вигляді рядка, S:номер сезону, E - номер серії
    def __str__(self):
     return f"{self.title} S: {self.season_number}, E - {self.series_number}"

# Функція, що виводить список серіалів
    def get_series():
     for serial in Serials():
        print(serial)
     
serial_1 = Serials(title="Wednesday", released_year="2022", genre="Mysteries", series_number="05", season_number="01", count_views="350000")
serial_2 = Serials(title="House of the Dragon", released_year="2022", genre="Drama", series_number="01", season_number="01", count_views="250000")
serial_3 = Serials(title="Better Call Soul", released_year="2015", genre="Drama", series_number="06", season_number="04", count_views="120000")
serial_4 = Serials(title="Money Heist", released_year="2017", genre="Thriller", series_number="03", season_number="02", count_views="300000")
serial_5 = Serials(title="The Black List", released_year="2013", genre="Detective", series_number="08", season_number="06", count_views="200000")


def generate_views(type:str):

 type = input("Оберіть, що бажаєте переглянути :\n1. Фільм\n2. Серіал\n")
 
 film_list = []
 
 for i in range(10):
    if type == "1": 
       object = Filmlist(i)
    
    elif type == "2":
      object = Serials(i)

 film_list.append(object)
 
 generate_views()
 print(generate_views)



