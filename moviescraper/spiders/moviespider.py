from gc import callbacks
from tracemalloc import start
import scrapy



class MovieSpider(scrapy.Spider):
    name='movie'
    # user_name = input("Enter the username of a user whose diary data you want: ")
    # print(user_name)martyk0015mp
    start_urls = ['https://letterboxd.com/martyk0015mp/films/diary/']
    # print(start_urls)
    # custom_settings = {
        # 'CONCURRENT_REQUESTS': 1,
        # 'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        # 'DOWNLOAD_DELAY': 0
    # }
    

    def getDetails(self, response):
        movie = response.meta.get('movie')
    
        directors = []
        if isinstance(response.xpath('//*[@id="featured-film-header"]/p/a/span/text()'),list):
            for director in response.xpath(
                '//*[@id="featured-film-header"]/p/a/span/text()'):
                directors.append(director.get())
        else:
            directors.append(response.xpath(
                '//*[@id="featured-film-header"]/p/a/span/text()').get('data'))
        
        genres_themes = response.xpath('//*[@id="tab-genres"]/div')
        genres = []
        themes = []
        if len(genres_themes) == 2:
            
            for theme in response.xpath('//*[@id="tab-genres"]/div[2]/p/a/text()'):
                themes.append(theme.get())
        
            
            if isinstance(response.xpath('//*[@id="tab-genres"]/div[1]/p/a/text()'),list):
                for genre in response.xpath('//*[@id="tab-genres"]/div[1]/p/a/text()'):
                    genres.append(genre.get())
            else:
                genres.append(response.xpath(
                    '//*[@id="tab-genres"]/div[1]/p/a/text()').get('data'))
        else:
            if isinstance(response.xpath('//*[@id="tab-genres"]/div/p/a/text()'), list):
                for genre in response.xpath('//*[@id="tab-genres"]/div/p/a/text()'):
                    genres.append(genre.get())
            else:
                genres.append(response.xpath(
                    '//*[@id="tab-genres"]/div/p/a/text()').get('data'))
        cast = []
        if isinstance(response.xpath('//*[@id="tab-cast"]/div/p/a/text()'), list):
            for actor in response.xpath('//*[@id="tab-cast"]/div/p/a/text()'):
                cast.append(actor.get())
        else:
            cast.append(response.xpath('//*[@id="tab-cast"]/div/p/a/text()').get('data'))
        
        writers = []
        if isinstance(response.xpath('//*[@id="tab-crew"]/div[3]/p/a/text()'),list):
            for writer in response.xpath('//*[@id="tab-crew"]/div[3]/p/a/text()'):
                writers.append(writer.get())
        else:
            writers.append(response.xpath(
                '//*[@id="tab-crew"]/div[3]/p/a/text()').get('data'))
        
        cinematographers = []
        if isinstance(response.xpath('//*[@id="tab-crew"]/div[5]/p/a/text()'),list):
            for cinematographer in response.xpath('//*[@id="tab-crew"]/div[5]/p/a/text()'):
                cinematographers.append(cinematographer.get())
        else:
            cinematographers.append(response.xpath(
                '//*[@id="tab-crew"]/div[5]/p/a/text()').get('data'))
        
        composers = []
        if isinstance(response.xpath('//*[@id="tab-crew"]/div[10]/p/a/text()'),list):
            for composer in response.xpath('//*[@id="tab-crew"]/div[10]/p/a/text()'):
                composers.append(composer.get())
        else:
            composers.append(response.xpath(
                '//*[@id="tab-crew"]/div[10]/p/a/text()').get('data'))
            
            
        duration = ''
        duration_full = response.xpath(
            '//*[@id="film-page-wrapper"]/div[2]/section[2]/p/text()')[0].get()
        duration_full = duration_full.replace('\t','').replace('\n','').replace('\xa0','')
        for i in duration_full:
            if i.isdigit():
                duration += i
        duration = int(duration)
            
        countries = []
        if isinstance(response.xpath('//*[@id="tab-details"]/div[2]/p/a/text()'),list):
            for country in response.xpath('//*[@id="tab-details"]/div[2]/p/a/text()'):
                countries.append(country.get())
        else:
            countries.append(response.xpath(
                '//*[@id="tab-details"]/div[2]/p/a/text()').get('data'))
            
        languages = []
        if isinstance(response.xpath('//*[@id="tab-details"]/div[3]/p/a/text()'),list):
            for language in response.xpath('//*[@id="tab-details"]/div[3]/p/a/text()'):
                languages.append(language.get())
        else:
            languages.append(response.xpath(
                '//*[@id="tab-details"]/div[3]/p/a/text()').get('data'))
        
        rating = movie.css('td.td-rating').css('span::text').get()
        print("RATINGGGGGGGGGGGGGGG",rating)
        # rating = self.get_rating(" ½ ")
        rating = self.get_rating(rating)

        
        yield {
            'title':  movie.css('h3.headline-3').css('a::text').get(),
            'link': "https://letterboxd.com"+movie.css('h3.headline-3').css('a').attrib['href'][14:],
            'rating': rating,
            'release_date': movie.css('td.td-released').css('span::text').get(),
            'duration': duration,
            'genres': genres,
            'themes': themes,
            'director': directors,
            'cinematographer': cinematographers,
            'writers': writers,
            'cast': cast,
            'composer': composers,
            'country': countries,
            'language': languages
        }
    
    def parse(self, response):
        
        for movie in response.css('tr.diary-entry-row'):
        
            # genres, duration, director, cinematographer, writers, cast, composer, country, language = yield response.follow("https://letterboxd.com"+movie.css('h3.headline-3').css('a').attrib['href'][14:], callback=self.getDetails)
            # yield response.follow("https://letterboxd.com"+movie.css('h3.headline-3').css('a').attrib['href'][14:], callback=self.getDetails)
            yield scrapy.Request(
                url="https://letterboxd.com/" + movie.css('h3.headline-3').css('a').attrib['href'][14:],
                callback=self.getDetails,
                meta={'movie':movie}
            )
        
        if response.css('a.next'):
            next_page_link = response.css('a.next').attrib['href']
            next_page = "https://letterboxd.com"+next_page_link
            if next_page_link is not None:
                yield response.follow(next_page, callback=self.parse)
        
        
    def get_rating(self, rating):
        if rating == ' ':
            return 0
        elif rating == ' ½ ':
            return 1
        elif rating == ' ★ ':
            return 2
        elif rating == ' ★½ ':
            return 3
        elif rating == ' ★★ ':
            return 4
        elif rating == ' ★★½ ':
            return 5
        elif rating == ' ★★★ ':
            return 6
        elif rating == ' ★★★½ ':
            return 7
        elif rating == ' ★★★★ ':
            return 8
        elif rating == ' ★★★★½ ':
            return 9
        elif rating == ' ★★★★★ ':
            return 10
        else:
            return 'FALSE INPUT'
        
        
        
        ## Letterboxd.comfilm ?????? wheree