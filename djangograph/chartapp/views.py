from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


def homepage(request):
	return render(request,'index.html')

class GraphData(APIView):

	def get(self,request,format=None):
		labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
		DefaultData = [12, 19, 3, 5, 2, 3]
		data = {
		"labels":labels,
		"DefaultData":DefaultData,
		}
		return Response(data)



