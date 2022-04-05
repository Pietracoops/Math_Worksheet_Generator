from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
from pylatex.package import Package
from datetime import datetime

# seed the pseudorandom number generator
from random import seed
from random import random
import os
import shutil


def prep_str(str):
    # Check the string length
    empty_spaces_needed = 4 - len(str)

    new_str = ''
    counter = 0
    for i in range(0, 4):
        if empty_spaces_needed != 0:
            new_str = new_str + '&   '
            empty_spaces_needed -= 1
        else:
            new_str = new_str + '& {} '.format(str[counter])
            counter += 1

    return new_str

def generate_value(doc, doc2, difficulty):

    operator = '+ '
    # Get addition/subtraction/multiplication/division depending on difficulty
    if difficulty == 1:
        operator = '+ '

        # First difficulty is singular numbers being added together

        # Get first number
        number1 = int((random() * 11))
        number1_str = prep_str(str(number1)) # Create the first string
        number2 = int((random() * 11))
        number2_str = prep_str(str(number2)) # Create the first string

        number2_str = operator + number2_str # Add operator

        sol_str = prep_str(str(number2 + number1))

        doc.append(NoEscape(number1_str + r'\\'))
        doc.append(NoEscape(number2_str + r'\\'))
        doc.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(number1_str + r'\\'))
        doc2.append(NoEscape(number2_str + r'\\'))
        doc2.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(sol_str + r'\\'))

    if difficulty == 2:
        operator = '- '

        # Second difficulty is subtraction but always positive

        # Get first number
        number1 = int((random() * 50)) + 50
        number1_str = prep_str(str(number1)) # Create the first string
        number2 = int((random() * 50))
        number2_str = prep_str(str(number2)) # Create the first string

        number2_str = operator + number2_str # Add operator

        sol_str = prep_str(str(number1 - number2))

        doc.append(NoEscape(number1_str + r'\\'))
        doc.append(NoEscape(number2_str + r'\\'))
        doc.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(number1_str + r'\\'))
        doc2.append(NoEscape(number2_str + r'\\'))
        doc2.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(sol_str + r'\\'))

    if difficulty == 3:
        operator = '+ '

        # First difficulty is singular numbers being added together

        # Get first number
        number1 = int((random() * 101))
        number1_str = prep_str(str(number1)) # Create the first string
        number2 = int((random() * 101))
        number2_str = prep_str(str(number2)) # Create the first string

        number2_str = operator + number2_str # Add operator

        sol_str = prep_str(str(number1 + number2))

        doc.append(NoEscape(number1_str + r'\\'))
        doc.append(NoEscape(number2_str + r'\\'))
        doc.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(number1_str + r'\\'))
        doc2.append(NoEscape(number2_str + r'\\'))
        doc2.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(sol_str + r'\\'))

    if difficulty == 4:
        operator = '- '

        # Negative numbers

        # Get first number
        number1 = int((random() * 101))
        number1_str = prep_str(str(number1)) # Create the first string
        number2 = int((random() * 101))
        number2_str = prep_str(str(number2)) # Create the first string

        number2_str = operator + number2_str # Add operator

        sol_str = prep_str(str(number1 - number2))

        doc.append(NoEscape(number1_str + r'\\'))
        doc.append(NoEscape(number2_str + r'\\'))
        doc.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(number1_str + r'\\'))
        doc2.append(NoEscape(number2_str + r'\\'))
        doc2.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(sol_str + r'\\'))

    if difficulty == 5:

        # Negative numbers and additions

        # Get first number
        number1 = int((random() * 101))
        number1_str = prep_str(str(number1)) # Create the first string
        number2 = int((random() * 101))
        number2_str = prep_str(str(number2)) # Create the first string

        number3 = int((random() * 100))
        if number3 > 50:
            operator = '- '
            number2_str = operator + number2_str  # Add operator
            sol_str = prep_str(str(number1 - number2))
        else:
            operator = '+ '
            number2_str = operator + number2_str  # Add operator
            sol_str = prep_str(str(number1 + number2))


        doc.append(NoEscape(number1_str + r'\\'))
        doc.append(NoEscape(number2_str + r'\\'))
        doc.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(number1_str + r'\\'))
        doc2.append(NoEscape(number2_str + r'\\'))
        doc2.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(sol_str + r'\\'))

    if difficulty == 6:
        operator = 'x '
        # multiplication

        # Get first number
        number1 = int((random() * 13))
        number1_str = prep_str(str(number1)) # Create the first string
        number2 = int((random() * 13))
        number2_str = prep_str(str(number2)) # Create the first string


        number2_str = operator + number2_str  # Add operator

        sol_str = prep_str(str(number1 * number2))

        doc.append(NoEscape(number1_str + r'\\'))
        doc.append(NoEscape(number2_str + r'\\'))
        doc.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(number1_str + r'\\'))
        doc2.append(NoEscape(number2_str + r'\\'))
        doc2.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(sol_str + r'\\'))


    if difficulty == 7:
        operator = 'x '
        # multiplication

        # Get first number
        number1 = int((random() * 13))
        number1_str = prep_str(str(number1)) # Create the first string
        number2 = int((random() * 101))
        number2_str = prep_str(str(number2)) # Create the first string

        number2_str = operator + number2_str  # Add operator

        sol_str = prep_str(str(number1 * number2))

        doc.append(NoEscape(number1_str + r'\\'))
        doc.append(NoEscape(number2_str + r'\\'))
        doc.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(number1_str + r'\\'))
        doc2.append(NoEscape(number2_str + r'\\'))
        doc2.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(sol_str + r'\\'))

    if difficulty == 8:
        operator = 'x '
        # multiplication

        # Get first number
        number1 = int((random() * 101))
        number1_str = prep_str(str(number1)) # Create the first string
        number2 = int((random() * 101))
        number2_str = prep_str(str(number2)) # Create the first string

        number2_str = operator + number2_str  # Add operator

        sol_str = prep_str(str(number1 * number2))

        doc.append(NoEscape(number1_str + r'\\'))
        doc.append(NoEscape(number2_str + r'\\'))
        doc.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(number1_str + r'\\'))
        doc2.append(NoEscape(number2_str + r'\\'))
        doc2.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(sol_str + r'\\'))


    if difficulty == 9:
        operator = r'÷ '
        # multiplication

        # Get first number
        number1 = int((random() * 101)) + 1 # need the + 1 so no division by 0
        number1_str = prep_str(str(number1)) # Create the first string
        number2 = number1 * int((random() * 11))
        number2_str = prep_str(str(number2)) # Create the first string

        number1_str = operator + number1_str  # Add operator

        sol_str = prep_str(str(number2 / number1))

        doc.append(NoEscape(number2_str + r'\\'))
        doc.append(NoEscape(number1_str + r'\\'))
        doc.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(number2_str + r'\\'))
        doc2.append(NoEscape(number1_str + r'\\'))
        doc2.append(NoEscape(r'\hline'))
        doc2.append(NoEscape(sol_str + r'\\'))


    if difficulty == 10:
        operator = r'÷ '
        # multiplication

        # Get first number
        number3 = int((random() * 100))

        if number3 > 50:
            # multiplication
            operator = r'x '
            number1 = int((random() * 101))
            number1_str = prep_str(str(number1)) # Create the first string
            number2 = int((random() * 101))
            number2_str = prep_str(str(number2)) # Create the first string

            number2_str = operator + number2_str  # Add operator

            sol_str = prep_str(str(number2 * number1))

            doc.append(NoEscape(number1_str + r'\\'))
            doc.append(NoEscape(number2_str + r'\\'))
            doc.append(NoEscape(r'\hline'))
            doc2.append(NoEscape(number1_str + r'\\'))
            doc2.append(NoEscape(number2_str + r'\\'))
            doc2.append(NoEscape(r'\hline'))
            doc2.append(NoEscape(sol_str + r'\\'))
        else:
            # division
            number1 = int((random() * 101)) + 1 # need the +1 so no division by 0
            number1_str = prep_str(str(number1))  # Create the first string
            number2 = number1 * int((random() * 11))
            number2_str = prep_str(str(number2))  # Create the first string

            number1_str = operator + number1_str  # Add operator

            sol_str = prep_str(str(number2 / number1))

            doc.append(NoEscape(number2_str + r'\\'))
            doc.append(NoEscape(number1_str + r'\\'))
            doc.append(NoEscape(r'\hline'))
            doc2.append(NoEscape(number2_str + r'\\'))
            doc2.append(NoEscape(number1_str + r'\\'))
            doc2.append(NoEscape(r'\hline'))
            doc2.append(NoEscape(sol_str + r'\\'))



def generate_table_row(doc, doc2, difficulty):

    #Create table beginning

    doc.append(NoEscape(r'\begin{table}[!htb]'))
    doc.append(NoEscape(r'\begin{adjustwidth}{-4.0cm}{-4.5cm}'))
    doc2.append(NoEscape(r'\begin{table}[!htb]'))
    doc2.append(NoEscape(r'\begin{adjustwidth}{-4.0cm}{-4.5cm}'))

    for i in range(0,10,1):
        doc.append(NoEscape(r'\begin{minipage}{.1\linewidth}'))
        doc.append(NoEscape(r'\centering'))
        doc.append(NoEscape(r'\begin{tabular}{c@{\,}c@{\,}c@{\,}c@{\,}c}'))
        doc2.append(NoEscape(r'\begin{minipage}{.1\linewidth}'))
        doc2.append(NoEscape(r'\centering'))
        doc2.append(NoEscape(r'\begin{tabular}{c@{\,}c@{\,}c@{\,}c@{\,}c}'))
        generate_value(doc, doc2, difficulty)
        doc.append(NoEscape(r'\end{tabular}'))
        doc.append(NoEscape(r'\end{minipage}'))
        doc2.append(NoEscape(r'\end{tabular}'))
        doc2.append(NoEscape(r'\end{minipage}'))


    doc.append(NoEscape(r'\end{adjustwidth}'))
    doc.append(NoEscape(r'\end{table}'))
    doc.append(NoEscape(r'\vspace{1.2em}'))
    doc2.append(NoEscape(r'\end{adjustwidth}'))
    doc2.append(NoEscape(r'\end{table}'))
    doc2.append(NoEscape(r'\vspace{0.5em}'))



def create_document(document_name, pdf_name, difficulty, output_directory):
    doc = Document(document_name)
    doc2 = Document(document_name + '_sols')
    # Add required packages
    doc.preamble.append(NoEscape(r'\usepackage{background}'))
    doc.preamble.append(NoEscape(r'\usepackage{eso-pic}'))
    doc.preamble.append(NoEscape(r'\usepackage{changepage}'))
    doc2.preamble.append(NoEscape(r'\usepackage{background}'))
    doc2.preamble.append(NoEscape(r'\usepackage{eso-pic}'))
    doc2.preamble.append(NoEscape(r'\usepackage{changepage}'))

    doc.preamble.append(NoEscape(r'\setlength{\textheight}{9in}'))
    doc.preamble.append(NoEscape(r'\pagenumbering{gobble}')) # Remove page numbers
    doc2.preamble.append(NoEscape(r'\setlength{\textheight}{9in}'))
    doc2.preamble.append(NoEscape(r'\pagenumbering{gobble}')) # Remove page numbers

    # This is to fix the "no \title available bug"
    doc.preamble.append(NoEscape(r'\renewcommand\maketitle{}'))
    doc2.preamble.append(NoEscape(r'\renewcommand\maketitle{}'))

    # Import the templates
    str = r'\newcommand\BackgroundPic{\put(0,0){\parbox[b][\paperheight]{\paperwidth}{\vfill\centering\includegraphics[width=\paperwidth,height=\paperheight]{' + pdf_name + r'}\vfill}}}'
    doc.preamble.append(NoEscape(str))
    doc2.preamble.append(NoEscape(str))

    doc.append(NoEscape(r'\AddToShipoutPicture*{\BackgroundPic}'))
    doc.append(NoEscape(r'\maketitle'))
    doc2.append(NoEscape(r'\AddToShipoutPicture*{\BackgroundPic}'))
    doc2.append(NoEscape(r'\maketitle'))

    for i in range (0, 10, 1):
        generate_table_row(doc, doc2, difficulty)

    doc.generate_pdf(clean_tex=False, compiler='pdfLaTeX', filepath=output_directory + document_name)
    doc2.generate_pdf(clean_tex=False, compiler='pdfLaTeX', filepath=output_directory + document_name + '_sols')


def remove_tex_files(path):
    dir_list = os.listdir(path)
    for item in dir_list:
        if item.endswith(".tex"):
            os.remove(os.path.join(path, item))

if __name__ == '__main__':
    # Basic document

    seed(datetime.now())

    current_directory = 'C:/Users/massimo/Desktop/flag_project'
    output_directory  = 'C:/Users/massimo/Desktop/flag_project/outputs/'

    number_of_generations = 25
    number_of_templates = 2


    ## NORMAL


    # Make root path
    og_path = output_directory + "Original"
    if os.path.isdir(og_path):
        shutil.rmtree(og_path, ignore_errors=False, onerror=None)

    os.mkdir(og_path)

    page_counter = 1
    for k in range (1, 11, 1):
        difficulty = k
        os.mkdir(og_path + r"/T{}/".format(difficulty))
        for i in range(1, number_of_generations + 1, 1):
            print("Generating Tier {} set {} of {}".format(difficulty, i, number_of_generations - 1))
            document_name = "Tier{}_".format(difficulty) + str(i)
            create_document(document_name, current_directory + '/templates/Page {}.pdf'.format(page_counter), difficulty, og_path + r"/T{}/".format(difficulty))
            remove_tex_files(og_path + r"/T{}/".format(difficulty))
        page_counter += number_of_templates


    ## PIRATE

    # Make root path
    og_path = output_directory + "Pirate"
    if os.path.isdir(og_path):
        shutil.rmtree(og_path, ignore_errors=False, onerror=None)

    os.mkdir(og_path)

    page_counter = 2
    for k in range (1, 11, 1):
        difficulty = k
        os.mkdir(og_path + r"/T{}/".format(difficulty))
        for i in range(1, number_of_generations + 1, 1):
            print("Generating Tier {} set {} of {}".format(difficulty, i, number_of_generations - 1))
            document_name = "Tier{}_".format(difficulty) + str(i)
            create_document(document_name, current_directory + '/templates/Page {}.pdf'.format(page_counter), difficulty, og_path + r"/T{}/".format(difficulty))
            remove_tex_files(og_path + r"/T{}/".format(difficulty))
        page_counter += number_of_templates