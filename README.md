Guide for build-script.py

This is a guide for generating EN, TC and CN scripts on Terminal

1. Open and edit spreadsheet with the following patterns:

| Android  | | | | iOS| | | |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| id  | en  | tc | cn | id  | en  | tc | cn |
| lable_hello | Hello | 你好！| 你好！| lable_hello | Hello | 你好！| 你好！|

2. Export to .csv

3. Make sure python2.7 has installed on your OS. (python -V)

4a. for Android:
	python build-script.py [.csv path] -a

4b. for iOS
	python build-script.py [.csv path] -i
