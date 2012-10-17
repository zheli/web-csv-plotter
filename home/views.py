# Create your views here.
import json
import logging
import os
from django.http import HttpResponse
from django.template  import RequestContext
from django.shortcuts import render_to_response

def home(request):
	filename_option = None
	if request.method == 'GET':
		filename = request.GET.get('filename', '')
		if not filename:
			filename = 'log_WPS__SYSTEM__GOUGING__Change_Voltage_While_Welding.csv'
	elif request.method == 'POST':
		filename = request.POST.get('filename', '')
		filename_option = request.POST.get('filename_option', '')

	if filename[-3:] != 'csv':
		filename = filename + '.csv'

	dir_list = os.listdir("C:\\")
	file_list = []
	for fname in dir_list:
		if fname[-3:] == 'csv':
			file_list.append(fname)

	if filename_option:
		filename = filename_option

	params = { 
		'filename': filename,
		'file_list': file_list
		}
	return render_to_response('home.html', params, context_instance = RequestContext(request))

def csv_data(request):
	filename = request.GET.get('filename', '')
	response_data = { 'data' : '' }

	with open('C:\\'+filename) as f:
		logging.debug('getting csv file content')
		while True:
			line = f.readline()
			if not line:
				break
			line = line.replace(' ms,', ',')
			response_data['data'] = response_data['data'] + line
		return HttpResponse(json.dumps(response_data), mimetype='application/json')

	return HttpResponse('Something wrong!')

def csv_data_WPS(request):
	response_data = { 'data' : '' }

	with open('C:\\log_PS1__SYSTEM__GMA__ArcOut.csv') as f:
		logging.debug('getting csv file content')
		while True:
			line = f.readline()
			if not line:
				break
			line = line.replace(' ms,', ',')
			response_data['data'] = response_data['data'] + line
		return HttpResponse(json.dumps(response_data), mimetype='application/json')

	return HttpResponse('Something wrong!')