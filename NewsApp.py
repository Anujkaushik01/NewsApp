# A CLI app to extract news from NewsAPI and then save the news to news.txt file.

import requests


def everynews(url: str) -> str:

    print('\nYou must give atleast one of the keyword or domain filter to get news.')
    print('Leave blank if you don\'t want to apply any specific filter.\n')

    while True: # To loop until atleast one of keyword or domain filter is given.

        # Filter news by keyword.
        print('Keywords or a phrase to search for.')
        if keyword:= input('> '):
            url += f'q={keyword}&' # Adds 'keyword' parameter to url.

            # Filter news by keyword in title, description, or content.
            print('\nSearch for keyword in (leave blank to search in all):')
            print('1: title, 2:description, or 3:content')
            searchin: dict[str, str] = {'1': 'title', '2': 'description', '3': 'content'}
            while (keyword_search := input('> ')) and keyword_search not in ['1', '2', '3']:
                print('\nInvalid option! Choose between 1, 2, or 3, or leave empty.\n')
            if keyword_search:
                url += f'searchIn={searchin[keyword_search]}&' # Adds 'searchIn' parameter to url.

        # Filter news by domain.
        print('Which domain(s) you want to search from? (Leave empty for all.)')
        if domain:= input('> '):
            url += f'domains={domain}&' # Adds 'domain' parameter to url.
        
        # Breaks loop if atleast one of keyword or domain parameter is given.
        if keyword or domain:
            break
        else:
            print('\nError: You must provide at least one of the keyword filter or the domain filter.\n')

    # Filter news starting from date.
    print('\nFrom which date/time you want to search articles from? ')
    print('Enter Date in YYYY-MM-DD format or including time YYYY-MM-DDTHH-MM-SS format.')
    if from_time:= input('> '):
        url += f'from={from_time}&' # Adds 'from' parameter to url.
        
    # Filter news till date.
    print('\nTo which date/time you want to search articles? ')
    print('Enter Date in YYYY-MM-DD format or including time YYYY-MM-DDTHH:MM:SS format.')
    if to_time:= input('> '):
        url += f'to={to_time}&' # Adds 'to' parameter to url

    # Sort news articles.
    print('\nSort articles by: (default sorted by publishedAt)')
    print('1: relevancy, 2: popularity, 3: publishedAt')
    sortby: dict[str, str] = {'1': 'relevancy', '2': 'popularity', '3': 'publishedAt'}
    while (sort := input('> ')) and sort not in ['1', '2', '3']:
        print('Inavlid option. Choose between 1, 2, or 3, or leave empty.')
    if sort:
        url += f'sortBy={sortby[sort]}&' # Adds 'sortBy' parameter to url.

    # Filter to return specified no. of results per page. 
    print('\nNo. of results to return per page. (by default 100, Maximum 100)')
    while True:
        page_size_: str = input('> ')
        if not page_size_:
            break
        try:
            page_size: int = int(page_size_)
            if (page_size < 1) or (page_size > 100): # Ensures pageSize is between 1 and 100.
                raise ValueError
            else:
                url += f'pageSize={page_size}&' # Adds 'pageSize' parameter to url.
                break
        except ValueError:
            print('\nOnly enter value between 1 and 100 or leave empty.')

    # Filter to see desired page.
    print('\nEnter page number:')
    while True:
        page_: str = input('> ')
        if not page_:
            break
        try: 
            page: int = int(page_)
            if page < 1: # Ensures page no. is greater than 1.
                raise ValueError
            else:
                url += f'page={page}&' # Adds 'page' parameter to url.
                break
        except ValueError:
            print('Only enter values gretaer than 1 or leave empty.')
    
    return url


def top_headlines(url:str) -> str:

    # Checks if user want to filter news.
    print('\nDo you want to apply filters? (By default you will get all english news.)')
    while (apply_filter := input('> ').lower()) not in {'y', 'yes', 'n', 'no'}:
        print('\nChoose between yes/y or no/n only.')
    
    # If user don't want to filter news.
    if apply_filter in {'n', 'no'}:
        url += 'language=en&' # Adds 'language' parameter as english to url.

    else: # If user want to filter news.
        
        # Filter news by country.
        print('\nSelect country: (Leave blank for global news)')
        print('ae,ar,at,au,be,bg,br,ca,ch,cn,co,cu,cz,de,eg,fr,gb,gr,'
            'hk,hu,id,ie,il,in,it,jp,kr,lt,lv,ma,mx,my,ng,nl,no,nz,'
            'ph,pl,pt,ro,rs,ru,sa,se,sg,si,sk,th,tr,tw,ua,us,ve,za')
        while (country := input('> ').lower()) and country not in ['ae','ar','at','au',
                'be','bg','br','ca','ch','cn','co','cu','cz','de','eg','fr','gb','gr',
                'hk','hu','id','ie','il','in','it','jp','kr','lt','lv','ma','mx','my',
                'ng','nl','no','nz','ph','pl','pt','ro','rs','ru','sa','se','sg','si','sk',
                'th','tr','tw','ua','us','ve','za']:
            print('\nInvalid selection!')
        if country:
            url += f'country={country}&' # Adds 'country' parameter to url.

        # Filter news by category.
        print('\nSelect category: (Leave blank for every catergory news)')
        print('business,entertainment,general,health,science,sports,technology')
        while (category := input('> ').lower()) and category not in ['business','entertainment','general','health','science','sports','technology']:
            print('Invalid category!')
        if category:
            url += f'category={category}&' # Adds 'category' parameter to url.

        # Filter news by keyword.
        print('\nKeywords or a phrase to search for.')
        if keyword:= input('> '):
            url += f'q={keyword}&' # Add 'q' parameter to url.
    
            # Filter news by keyword in title, description, or content.
            print('\nSearch for keyword in (leave blank to search in all):')
            print('1: title, 2:description, or 3:content')
            searchin: dict[str, str] = {'1': 'title', '2': 'description', '3': 'content'}
            while (keyword_search := input('> ')) and keyword_search not in ['1', '2', '3']:
                print('\nInvalid option! Choose between 1, 2, or 3, or leave empty.\n')
            if keyword_search:
                url += f'searchIn={searchin[keyword_search]}&' # Adds 'searchIn' parameter to url.

        # Filter to return specified no. of results per page. 
        print('\nNo. of results to return per page. (by default 100, Maximum 100)')
        while True:
            page_size_: str = input('> ')
            if not page_size_:
                break
            try:
                page_size: int = int(page_size_)
                if (page_size < 1) or (page_size > 100): # Ensures pageSize is between 1 and 100.
                    raise ValueError
                else:
                    url += f'pageSize={page_size}&' # Adds 'pageSize' parameter to url.
                    break
            except ValueError:
                print('\nOnly enter value between 1 and 100')

        # Filter to see desired page.
        print('\nEnter page number:')
        while True:
            page_: str = input('> ')
            if not page_:
                break
            try: 
                page = int(page_)
                if page < 1: # Ensures page no. is greater than 1.
                    raise ValueError
                else:
                    url += f'page={page}&' # Adds 'page' parameter to url.
                    break
            except ValueError:
                print('Only enter values gretaer than 1!')

    return url
  
  
def get_news() -> None:

    url: str = 'https://newsapi.org/v2/'
    print('\nWelcome\n')
    print('Which type of news you want to see?')
    print('1 for Everything')
    print('2 for Top Headlines')
    
    while (news_type := input('> ')) not in {'1', '2'}: # Ensures user enter 1 or 2 only.
        print('Choose between 1 or 2 only.')

    if news_type == '1':
        url += 'everything?'
        url = everynews(url)
    else:
        url += 'top-headlines?'
        url = top_headlines(url)

    api: str = 'apiKey=50c04ca450184a58a10bd81ddaf69150'

    url += api
    response = requests.get(url)

    data = response.json() # Response from NewsAPI.

    article_titles = [article.get('title','') for article in data.get('articles', [])]
    article_urls = [article.get('url','') for article in data.get('articles', [])]
    article_author = [article.get('author','') for article in data.get('articles', [])]
    published_at = [article.get('publishedAt','') for article in data.get('articles', [])]
    
    # Write data to file 'news.txt'.
    with open('news.txt', 'wt') as f:
        f.write(f'Status: {data['status']}\n')

        if data['status'] == 'error': # If API responded with error.
            f.write(f'Error code: {data.get('code')}\n')
            f.write(f'Error message: {data.get('message')}\n')
        else:
            f.write(f'Total results: {data.get('totalResults','0')}\n\n')
            for title,article_url,author,published_at_ in zip(article_titles,article_urls,article_author,published_at):
                f.write(f'{title} \n')
                f.write(f'by {author}, Published at: {published_at_}\n')
                f.write(f'url: {article_url}\n\n')

    print(f'\nurl is: {url}') 

if __name__ == '__main__':
    get_news()
