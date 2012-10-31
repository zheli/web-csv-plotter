web-csv-plotter
===============

A simple tool I made at work, plot data from local csv file onto an interactive HTML5 chart.

![Screenshot](https://raw.github.com/zheli/web-csv-plotter/master/screenshot.PNG "Screenshot")

Introduction
===============
It is still very simple, but it works for me. I don't have to manually plot csv data into Excel anymore. It will save you a lot of time if you have hundreds of csv files need to be checked in charts. You can also compare two csv files. Just need to put them into different folders. As for me, I put the new generated CSV files into one folder and the reference files into another.

Prerequisites
===============
* Python
* Django



How to run it
===============
Create a new file called config.py in the project folder (where README.md is) and add this:

	DATA_FOLDER = "path to one folder"
	REF_FOLDER  = "path to another folder"

Here is mine:

	import os
	SRC_PATH = os.path.join("C:\\", "dev", "PS_GMA")
	DATA_FOLDER = os.path.join(SRC_PATH, "Logfiles")
	REF_FOLDER = os.path.join(SRC_PATH, "ReferenceLogs")

Then launch it using:

    python manage.py runserver

and visit localhost:8000 in your browser.

Now it only has two functions:
* localhost:8000			for comparing two csv files
* localhost:8000/log_view	for checking single csv file