import argparse

from PyPDF2 import PdfFileWriter, PdfFileReader


def get_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-p', '--password', metavar='password', default='pass', help='Password')
    
    parser.add_argument('-f', '--file', help='A crypte file', metavar='FILE', type=argparse.FileType('r'), default=None)
    
    return parser.parse_args()

def add_encryption(input_pdf, output_pdf, password):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, 
                       use_128bit=True)

    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)

if __name__ == '__main__':

    args = get_args()
    file_arg = args.file
    
    #print(file_arg.name, str(args.password))
    
    add_encryption(input_pdf=file_arg.name,
                   output_pdf='1-encrypted.pdf',
                   password=str(args.password))
