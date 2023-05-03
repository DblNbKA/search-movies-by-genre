import tmdbsimple as tmdb

# Установка ключа API
tmdb.API_KEY = '00a12344e199220710a3a77050374a14'

# Список жанров фильмов для поиска
g = input("Введите жарн через запятую: ")

genres = g.split(", ")
print(genres)

# Поиск фильмов
for i in range(1,2):
    response = tmdb.Discover().movie(page=i, include_adult=False, with_genres=','.join(str(tmdb.Genres().movie_list()['genres'][g]['id']) for g in range(len(genres)) if tmdb.Genres().movie_list()['genres'][g]['name'].lower() in genres))
    results = response['results']
    for result in results:
        title = result['title']
        title = title.replace("'", "")
        overview = result['overview']
        trailer_url = 'https://www.youtube.com/results?search_query=' + '+'.join(title.split()) + '+trailer'
        print('Название:', title)
        print('Описание:', overview)
        print('Ссылка на трейлер:', trailer_url)
        print('Ссылка на просмотр на Netflix:', 'https://www.netflix.com/search?q=' + '+'.join(title.split()))
        print('Ссылка на просмотр на Amazon Prime Video:', 'https://www.amazon.com/s?k=' + '+'.join(title.split()) + '&ref=nb_sb_noss_2')
        print('Ссылка на просмотр на Hulu:', 'https://www.hulu.com/search?q=' + '+'.join(title.split()))
        print('Ссылка на просмотр на HBO:', 'https://www.hbo.com/search?q=' + '+'.join(title.split()))
        print('-------------------------------------')


