from PyPDF2 import PdfWriter,PdfReader
num=int(input("enter the number of pages:"))
pdf1=open('1JS21CS013.pdf','rb')
pdf2=open('DAA.pdf','rb')

pdf_writer=PdfWriter()

pdf1_reader=PdfReader(pdf1)
page=pdf1_reader.pages[num-1]
pdf_writer.add_page(page)

pdf2_reader=PdfReader(pdf2)
page=pdf2_reader.pages[num-1]
pdf_writer.add_page(page)

with open('output.pdf','wb') as output:
    pdf_writer.write(output)