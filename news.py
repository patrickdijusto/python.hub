from GoogleNews import GoogleNews

googlenews = GoogleNews()

googlenews = GoogleNews(period='7d')

googlenews.search('USA')

result =  googlenews.result()

for x in result:
	print("-x"*50)
	print("Title:", x['title'])