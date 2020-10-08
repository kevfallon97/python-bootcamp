
import csv
import PyPDF2
import re

# task one: grab the google drive link from .csv file
data = open("find_the_link.csv", encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

link_to_pdf = ''
for index, line in enumerate(data_lines):
	link_to_pdf += line[index]

# task two: download the PDF from the Google Drive link and fine the phone number
pattern = r'\d{3}.\d{3}.\d{4}'

f = open('Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):
	page = pdf_reader.getPage(num)
	page_text = page.extractText()
	match = re.search(pattern, page_text)
	if match:
		print(match.group())