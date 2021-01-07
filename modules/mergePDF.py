# Merge PDF
from PyPDF2 import PdfFileMerger, PdfFileReader


def mergePdf(inputs, output):
    merger = PdfFileMerger()

    # Editing the List
    organizedInputs = []
    for i in inputs:
        organizedInputs += i.split()

    # Main Cycle
    for name in organizedInputs:
        merger.append(PdfFileReader(name, 'rb'))

    # Save Operation
    merger.write(output)
