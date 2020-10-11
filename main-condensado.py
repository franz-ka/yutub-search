# uso: python3 main-condensado.py (con venv activado)
from youtube_search import YoutubeSearch
results = YoutubeSearch('térmiso búsqueda', max_results=20).to_dict()
for r in results:
	title, views, url = r['title'], r['views'], r['url_suffix']
	print(f'{url} {views:>18} {title}')
