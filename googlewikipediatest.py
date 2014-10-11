from pygoogle import pygoogle
import wikipedia


searchTarget = raw_input()
g = pygoogle(searchTarget)
g.pages = 1
#g.display_results()
urls = []
urls = g.get_urls()
urlwiki = ""

for url in urls:
 	if url.find("wikipedia") == -1:
 			continue
 	else:
     		urlwiki = url
     		break

if(urlwiki != ""):
 	urlparse = urlwiki.rstrip().split("/")
 	wikipage = wikipedia.page(urlparse[-1])
 	print(wikipedia.summary(wikipage.title, sentences=1))
