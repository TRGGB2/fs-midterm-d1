import pandas as pd
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
link = "https://future-sphere-lecture-assets.s3-us-west-2.amazonaws.com/python-400-10/notes/midterm.xlsx"
pf = pd.read_excel(link)

print(pf)
print("\n")

sorted_list = pf.sort_values(["Score"], ascending=False)
print(sorted_list)


pdf = PdfFileReader("pdf/midterm.pdf")
pw = PdfFileWriter()

grabfirst = pdf.getPage(0)
grablast = pdf.getPage(3)

pw.addPage(grabfirst)
pw.addPage(grablast)


with Path("pdf/midtermclone.pdf").open(mode="wb") as output:
  pw.write(output)