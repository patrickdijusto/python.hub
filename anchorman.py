import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate',100)



from GoogleNews import GoogleNews

googlenews = GoogleNews()

googlenews = GoogleNews(period='1d')

googlenews.search('Brooklyn')

result =  googlenews.result()




for x in result:
	print("-x"*50)
	print("Title:", x['title'])
	engine.say(x['title']) 
	
	
engine.runAndWait()