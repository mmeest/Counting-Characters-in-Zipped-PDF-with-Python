from PyPDF2 import PdfFileReader    # for unzipped (.pdf)content
import re                           # regular expression
import zlib                         # zlib - for zipped (.pdf)content
import clipboard                    # for copying text to clipboard


""" 
                    To create Windows executable with Heart icon:
                        pip install pyinstaller
                        pyinstaller -F -i "heart.ico" reader.py
"""


# file(.pdf) name to count characters
pdf_document = input("Insert file(.pdf) name without extension: ") + ".pdf"
""" pdf_document = "test.pdf" """

pdf = open(pdf_document, "rb").read()
stream = re.compile(b'.*?FlateDecode.*?stream(.*?)endstream', re.S)
pdf_raw = ""

# content of compressed file(.pdf)
for s in re.findall(stream,pdf):
    s = s.strip(b'\r\n')
    string_slice = ""
    try:
        string_slice = zlib.decompress(s).decode('UTF-8')
        """ print(string_slice)
        print("") """
        pdf_raw += string_slice
    except:
        pass

cleantext = ""

""" clean = re.compile("<.*?>")
cleantext = re.sub(clean, '', pdf_raw) """

# removing line breakes
pdf_raw = pdf_raw.replace('\r','').replace('\n','')
# removing <> - tags
cleantext = re.sub('<.*?>', '', pdf_raw)
""" print(pdf_raw) """

""" print(type(pdf_raw)) """
# cleantext - compressed(.pdf) content in uncompressed form
""" print(cleantext) """

# uncompressed (.pdf) content
with open(pdf_document, "rb") as filehandle:
    pdf = PdfFileReader(filehandle)
    info = pdf.getDocumentInfo()
    pages = pdf.getNumPages()

    # info about the (.pdf) file
    """ print (info)
    print ("number of pages: %i" % pages) """

    page1 = pdf.getPage(0)
    """ print(page1)
    print(page1.extractText()) """
    print("")

    charachter_count = str(len(page1.extractText()))

    whole_string = page1.extractText()

    charachter_count_clean = 0
    for i in whole_string:
        if i != ' ':
            charachter_count_clean += 1


start = cleantext.find("Please choose your language:Detailed Medical Report")
end = cleantext.find("CompletionDoctor's Signature1") + 30

# (.pdf) form cut out from string
real_value = cleantext[start:end]
real_character_count = 0

# counting symbols without spaces
for i in real_value:
    if i != ' ':
        real_character_count += 1

""" print(pdf_raw) """

# remove the end of string
user_input_end = pdf_raw.find("</date><docSignature/></subform_12_2></Page12></Formular1>")
clear_input = pdf_raw[:user_input_end]

# remove the start of the string
""" if "LanguageDropdown/><subform_1_2><IDNumber>" in pdf_raw:
    user_input_start = pdf_raw.rfind("LanguageDropdown/><subform_1_2><IDNumber>")
else:
    user_input_start = pdf_raw.rfind("LanguageDropdown/><subform_1_2><IDNumber/>") """
user_input_start = pdf_raw.rfind("<subform_1_2><IDNumber") + 13
# clear_input - actual text inserted on form fields
clear_input = clear_input[user_input_start:]
""" print(clear_input) """

# removing >0< - symbols
clear_input = clear_input.replace('>0<', '><')
""" print(clear_input) """

# removing <> - tags
clear_input_without_tags = re.sub('<.*?>', '', clear_input)
""" print(clear_input_without_tags) """


input_character_count = 0
# counting symbols without spaces
for i in clear_input_without_tags:
    if i != ' ':
        input_character_count += 1

# clear_input - UI with <> -tags
""" print(clear_input) """
print("")
print("       Form:")
print("")
print(real_value)                   # real_value - actual content of file(UI)
print("")
print("")
print("       User input text:")
print("")
print(clear_input_without_tags)     # text inserted into form
print("")
print("")
print("1. String length(unzipped content) with spaces: " + str(charachter_count) + " characters.")
print("2. String length(unzipped content) without spaces: " + str(charachter_count_clean) + " characters.")
print("")
print("3. String length(zipped content with <> - tags): " + str(len(pdf_raw)) + " characters.")
print("4. String length(zipped content without <> - tags): " + str(len(cleantext)) + " characters.")
print("")
print("5. String length - actual length of form with spaces: " + str(len(real_value)) + " characters.")
print("6. String length - actual length of form without spaces: " + str(real_character_count) + " characters")
print("")
print("7. String length - user input text with spaces: " + str(len(clear_input_without_tags)) + " characters")
print("8. String length - user input text without spaces: " + str(input_character_count) + " characters")
""" input("Press enter to exit.") """
print("")
clipboard_copy = input("Copy text to clipboard? \n   A - PDF form \n   B - user input \n   C - PDF form and user input \n choice: ").upper()
if clipboard_copy == "A":
    clipboard.copy(real_value)
elif clipboard_copy == "B":
    clipboard.copy(clear_input_without_tags)
elif clipboard_copy == "C":
    clipboard.copy(real_value + clear_input_without_tags)



