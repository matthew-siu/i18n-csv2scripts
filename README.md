### Guide for build-script.py

This is a guide for generating EN, TC and CN scripts for .xml (Android) and .strings (iOS) on Terminal.

1. Edit the spreadsheet and follow this patterns:

| Android     |       |       |       | iOS         |       |       |       |
| ------------| ----- | ----- | ----- | ----------- | ----- | ----- | ----- |
| id          | en    | tc    | cn    | id          | en    | tc    | cn    |
| lable_hello | Hello | 你好！ | 你好！ | lable_hello | Hello | 你好！ | 你好！ |

2. Export to .csv

3. Make sure python2.7 has installed on your OS. (python -V)

4a. For Android:
	python build-script.py [.csv path] -a

4b. For iOS
	python build-script.py [.csv path] -i
	
5. Paste the texts to your project file.	
