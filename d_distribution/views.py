from django.shortcuts import render
import json
import requests as request
import sys
from django.http import JsonResponse

#math libraries
import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

# Create your views here.
def main_page(request):
	return render(request, 'main_page.html',{})

def post(request):
	result = {}

	try:
		if request.is_ajax():

			numElements = int(request.GET.get('numElements'))
			mean1 = float(request.GET.get('mean1'))
			deviation1 = float(request.GET.get('deviation1'))
			mean2 = float(request.GET.get('mean2'))
			deviation2 = float(request.GET.get('deviation2'))

			#calculations for x
			x = np.random.normal(mean1,deviation1,size=numElements)
			x_mean = sum(x)/numElements			
			x_std = np.std(x)
			x_loweralt = x_mean -(3*x_std) 
			x_higheralt = x_mean+(3*x_std)
			bins = np.linspace(x_loweralt, x_higheralt, 30)
			histogram, bins = np.histogram(x, bins=bins, normed=True) 
			bin_centers = 0.5*(bins[1:] + bins[:-1])
			x_pdf = ss.norm.pdf(bin_centers)


			#calculations for j
			j = np.random.normal(mean2,deviation2,size=numElements)
			j_mean = sum(j)/numElements			
			j_std = np.std(j)
			j_loweralt = j_mean -(3*j_std) 
			j_higheralt = j_mean+(3*j_std)
			bins = np.linspace(j_loweralt, j_higheralt, 30)
			histogram, bins = np.histogram(j, bins=bins, normed=True) 
			bin_centers = 0.5*(bins[1:] + bins[:-1])
			j_pdf = ss.norm.pdf(bin_centers)

			#num_list calculations
			num_list = j_pdf + x_pdf
			average_of_num_list = sum(num_list)/len(num_list)
			#standard deviation
			sdNum = stat.stdev(num_list)
			#pvalue
			pval = list(ss.f_oneway(j_pdf, x_pdf))[1]


			print(pval)

			result = {
				"pval":pval,
				"mean1":x_mean,
				"distribution1":list(x_pdf),
				"mean2":j_mean,
				"distribution2":list(j_pdf),
			}

		else:
			result = {}
	except:
		result = {}

	#result = {"pval":1}

	return JsonResponse(result)
			


