# Create your views here.
import json
import logging
import os
from django.http import HttpResponse
from django.template  import RequestContext
from django.shortcuts import render_to_response

try:
	from config import *
except:
	SRC_PATH = os.path.join("C:\\")
	DATA_FOLDER = os.path.join(SRC_PATH, "Logfiles")
	REF_FOLDER = os.path.join(SRC_PATH, "ReferenceLogs")

def get_csv_filelist_in_dir(dir_path):
	dir_path = os.listdir(dir_path) #get all the item in that folder
	file_list = []
	for fname in dir_path:
		if fname[-3:] == 'csv':
			file_list.append(fname)

	return file_list

def get_selected_html(file_list, filename):
	if file_list and filename in file_list:
		file_list.remove(filename)
		selected = '<option selected="selected" value="%s">%s</option>' % (filename, filename)
	else:
		selected = None
	return selected

def home(request):
	filename_option = None
	if request.method == 'GET':
		filename = request.GET.get('filename', '')
		filename_ref = request.GET.get('filename_ref', '')
		if not filename:
			filename = 'log_WPS__SYSTEM__GOUGING__Change_Voltage_While_Welding.csv'
	elif request.method == 'POST':
		#filename = request.POST.get('filename', '')
		filename = request.POST.get('filename_option', '')
		filename_ref = request.POST.get('filename_ref_option', '')

	if filename[-3:] != 'csv':
		filename = filename + '.csv'

	file_list  		= get_csv_filelist_in_dir(DATA_FOLDER)
	file_list_ref  	= get_csv_filelist_in_dir(REF_FOLDER)
	selected  		= get_selected_html(file_list, filename)
	selected_ref 	= get_selected_html(file_list_ref, filename_ref)

	params = { 
		'filename'		: filename,
		'filename_ref'  : filename_ref,
		'file_list'		: file_list,
		'file_list_ref' : file_list_ref,
		'compare_log' 	: True,
		'selected' 		: selected,
		'selected_ref' 	: selected_ref
		}
	return render_to_response('home.html', params, context_instance = RequestContext(request))

def log_view(request):
	filename_option = None
	if request.method == 'GET':
		filename = request.GET.get('filename', '')
		if not filename:
			filename = 'log_PS1__SYSTEM__GOUGING__Change_Voltage_While_Welding.csv'
	elif request.method == 'POST':
		filename = request.POST.get('filename', '')
		filename_option = request.POST.get('filename_option', '')

	if filename[-3:] != 'csv':
		filename = filename + '.csv'

	file_list = get_csv_filelist_in_dir(DATA_FOLDER)

	if filename_option:
		filename = filename_option

	selected = get_selected_html(file_list, filename)

	params = { 
		'filename': filename,
		'file_list': file_list,
		'compare_log': False,
		'selected': selected
		}
	return render_to_response('home.html', params, context_instance = RequestContext(request))

def csv_data(request):
	filename = request.GET.get('filename', '')
	response_data = { 'data' : '' }
	print("getting file [%s]" % os.path.join(DATA_FOLDER, filename))

	with open(os.path.join(DATA_FOLDER, filename)) as f:
		while True:
			line = f.readline()
			if not line:
				break
			line = line.replace(' ms,', ',')
			response_data['data'] = response_data['data'] + line
		return HttpResponse(json.dumps(response_data), mimetype='application/json')

	return HttpResponse('Something wrong!')

def csv_data_WPS(request):
	filename = request.GET.get('filename', '')
	response_data = { 'data' : '' }

	print("getting file [%s]" % os.path.join(REF_FOLDER, filename))

	try:
		with open(os.path.join(REF_FOLDER, filename)) as f:
			while True:
				line = f.readline()
				if not line:
					break
				line = line.replace(' ms,', ',')
				response_data['data'] = response_data['data'] + line
			return HttpResponse(json.dumps(response_data), mimetype='application/json')
	except:
		return HttpResponse('Something wrong!')