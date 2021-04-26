If you want to convert the table in the Google Sheets directly, I highly recommend you to check out this method:
https://github.com/matthew-siu/i18n-googlesheet-translator

### Guide for build-script.py

This is a guide for generating EN, TC and CN scripts for .xml (Android) and .strings (iOS) on Terminal.

1. Edit the spreadsheet and follow this patterns:

| Android     |       |       |       | iOS         |       |       |       |
| ------------| ----- | ----- | ----- | ----------- | ----- | ----- | ----- |
| id          | en    | tc    | cn    | id          | en    | tc    | cn    |
| lable_hello | Hello | 你好！ | 你好！ | lable_hello | Hello | 你好！ | 你好！ |

2. Export to .csv

3. Make sure python2.7 has installed on your OS. (python -V)

4. Run the commands:
	a. For Android i18n:
	`python build-script.py [.csv path] -a`

	b. For iOS i18n:
	`python build-script.py [.csv path] -i`
	
5. Paste the texts to your project file.	
