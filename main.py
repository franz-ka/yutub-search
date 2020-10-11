# uso: python3 main.py buscar pala bras (con venv activado)

#lib: https://github.com/joetats/youtube_search
#alternativa no probada: https://github.com/alexmercerind/youtube-search-python
#from pprint import pprint
import sys
from youtube_search import YoutubeSearch

#to_json() es la otra función que tiene, devuelve string con json
results = YoutubeSearch(' '.join(sys.argv[1:]), max_results=20).to_dict()

if not results:
	print('Sin resultados')
else:
	print(f'{len(results)} resultados')
	#pprint(results)
	for i, r in enumerate(results):
		title, views, url = r['title'], r['views'], r['url_suffix']
		print(f'{i+1:>2}) {views:>18} | {title}')
