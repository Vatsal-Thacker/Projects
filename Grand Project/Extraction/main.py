# Importing Dependencies

import docx2txt
from PyPDF3 import PdfFileReader


# Extracting text from DOCX
def doctotext(m):
    temp = docx2txt.process(m)
    resume_text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
    text = ' '.join(resume_text)
    return (text)


## Extracting text from PDF
def pdftotext(m):
    # pdf file object
    # you can find find the pdf file with complete code in below
    pdfFileObj = open(m, 'rb')

    # pdf reader object
    pdfFileReader = PdfFileReader(pdfFileObj)

    # number of pages in pdf
    num_pages = pdfFileReader.numPages

    currentPageNumber = 0
    text = ''

    # Loop in all the pdf pages.
    while (currentPageNumber < num_pages):
        # Get the specified pdf page object.
        pdfPage = pdfFileReader.getPage(currentPageNumber)

        # Get pdf page text.
        text = text + pdfPage.extractText()

        # Process next page.
        currentPageNumber += 1
    return (text)


if __name__ == '__main__':

    FilePath = r"C:\Users\Vatsa\PycharmProjects\Converter\Sample Resume\Docx\Abhishek Sharma.docx"
    FilePath.lower().endswith(('.png', '.docx'))
    if FilePath.endswith('.docx'):
        textinput = doctotext(FilePath)
    elif FilePath.endswith('.pdf'):
        textinput = pdftotext(FilePath)
    else:
        print("File not support")
