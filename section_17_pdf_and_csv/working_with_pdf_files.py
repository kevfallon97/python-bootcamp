
import PyPDF2

# read the pdf
f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(f"Number of pages {pdf_reader.numPages}")

# get the first page
page_one = pdf_reader.getPage(0)
# convert text to python string
page_one_text = page_one.extractText()
f.close()

# Writing a new pdf file
# read the file
f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
# get specific page object
first_page = pdf_reader.getPage(0)

# in order to write to a new file, created pdf_writer
pdf_writer = PyPDF2.PdfFileWriter()
# add pages to this writer object
pdf_writer.addPage(first_page)

# open a new file
pdf_output = open('Some_BrandNew_Doc.pdf', 'wb')
# use pdf writer to write to the new file
pdf_writer.write(pdf_output)

# close files
f.close()
pdf_output.close()

# grab all the text within a pdf file
f = open('Working_Business_Proposal.pdf', 'rb')
pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):
	page = pdf_reader.getPage(num)
	pdf_text.append(page.extractText())
