<p align="center">
<img src="heart.ico" width="60" height="60">
</p>

# Counting-Characters-in-Zipped-PDF-with-Python
Counting text symbols inside Zipped PDF files with Python script (+ Python script to Windows Executable with icon)

## Features:
* GNU licence notice:\
  https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
* Command line application that count charachters in zipped .pdf
* Feature to copy output values to clipboard
* Both source code and executable

## Output:
1. String length(unzipped content) with spaces:           *(If this message is not eventually replaced by the proper contents...*
2. String length(unzipped content) without spaces:        Same as above but without white spaces
3. String length(zipped content with <> - tags):          All zippe PDF content with <> tags(E.g. <Form>)
4. String length(zipped content without <> - tags):       Same as above but <> tags removed
5. String length - actual length of form with spaces:     All visible content of form(Form text and user input)
6. String length - actual length of form without spaces:  Same as above but spaces removed
7. String length - user input text with spaces:           Only user input text
8. String length - user input text without spaces:        Same as above but spaces removed

## To create executable with heart icon('heart.ico'):
* pip install pyinstaller
* pyinstaller -F -i "heart.ico" reader.py

## Version history

### ver. 2020.12.22
* Fixed auth. of file
* Input file name can be entered with or without '.pdf' extention

### ver. 2020.08.28
* Input PDF files without extention
* Count zipped and unzipped content of PDF file


