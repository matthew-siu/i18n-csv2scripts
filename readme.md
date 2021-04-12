Guide for build-script.py

This is a guide for generating EN, TC and CN scripts on Terminal

1. Open and edit the google spreadsheet on:
	https://docs.google.com/spreadsheets/d/1ldBZ_sXtI7Pdm_Ozx1nN4Klu3Gh8ms4fMsso0LKZXtA/edit#gid=0

2. File -> Download -> csv

3. Make sure python2.7 has installed on your OS. (python -V)

4a. for Android:
	python build-script.py [.csv path] -a

4b. for iOS
	python build-script.py [.csv path] -i
