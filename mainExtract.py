import PyPDF2
import sys
from FileMerger import fileMerge


def textExtractor():
    i = 0

    inputfileName = input("Enter the name of input file: ")
    outFileName = input("Enter the name of output file: ")

    print('Extracting....')

    pdfFile = open(inputfileName, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFile)

    print("Pages in PDF: " + str(pdfReader.numPages) + "\n")

    with open(outFileName, 'w') as f:
        while i < pdfReader.numPages:
            pages = pdfReader.getPage(i)
            print(pages.extractText(), file=f)

            i += 1


textExtractor()

again = input("Complete! Would you like to input another file? ")

if again == 'yes':
    textExtractor()
if again == 'no':

    cont = input('Extraction completed! Would you like to merge files? ')

    if cont == 'yes':
        fileMerge()
    if cont == 'no':
        sys.exit()
