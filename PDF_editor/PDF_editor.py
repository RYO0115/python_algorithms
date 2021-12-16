# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# You need to pip install pypdf2
import PyPDF2

import os,sys
import glob

cur_dir = os.getcwd()

input_pdf_filenames = glob.glob(cur_dir + "/pdf_files/input/*.pdf")
input_pdf_filenames.sort()
output_pdf_filename = cur_dir + "/pdf_files/output/merged.pdf"


# %%
input_pdf_filenames


# %%

# Import PDF Files and merge into one file

pdf_writer = PyPDF2.PdfFileWriter()
for file in input_pdf_filenames:
    pdf_reader = PyPDF2.PdfFileReader(file)
    for page_id in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page_id))


# %%
# Output Merged PDF File

with open(output_pdf_filename, "wb") as f:
    pdf_writer.write(f)


# %%



