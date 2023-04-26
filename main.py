import json
# Python's built-in module for opening and reading URLs
from urllib.request import urlopen


def pprint(book_data):
    already = set()
    book_id = book_data['objectIDs']
    for book_id in book_id:
        url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'+str(book_id)
        response = urlopen(url)
        book = json.load(response)
        
        artist_name = book['artistDisplayName']
        artist_nationality = book['artistNationality']
        artist_begin_date = book['artistBeginDate']
        artist_end_date = book['artistEndDate']
        
        if artist_name and artist_begin_date and artist_end_date and artist_nationality=='Japanese' and artist_name not in already:
            already.add(artist_name)
            print('名前:', artist_name)        
            print('国:', artist_nationality)        
            print('生誕日:', artist_begin_date)        
            print('生没日:', artist_end_date)
            print('=============================================')  

if __name__ == '__main__':
    url = 'https://collectionapi.metmuseum.org/public/collection/v1/search?q=japanese'
    response = urlopen(url)
    book_data = json.load(response)
    pprint(book_data)
