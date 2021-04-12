### Guide for build-script.py

This is a guide for generating EN, TC and CN scripts for .xml (Android) and .strings (iOS) on Terminal.

Edit the spreadsheet and follow this patterns:

| Android  | | | | iOS| | | |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| id  | en  | tc | cn | id  | en  | tc | cn |
| lable_hello | Hello | 你好！| 你好！| lable_hello | Hello | 你好！| 你好！|

Export to .csv

Make sure python2.7 has installed on your OS. (python -V)

For Android:
	python build-script.py [.csv path] -a

For iOS
	python build-script.py [.csv path] -i
