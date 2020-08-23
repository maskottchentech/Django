from django.shortcuts import render
import requests
import bs4

def index(request):
	value = []
	if request.method == 'POST':
		form = request.POST['your_url']
		resp = requests.get(form)
		scrapval = bs4.BeautifulSoup(resp.text,"html.parser")
		for data in scrapval.find_all('img'):
			srcval = data.get('src')
			print(srcval)
			value.append(srcval)

	return render(request,'index.html',{'value':value})


