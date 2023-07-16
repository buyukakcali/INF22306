import docx


def read_docx(file_path):
    document = docx.Document(file_path)
    text = []
    for paragraph in document.paragraphs:
        text.append(paragraph.text)
        j = ""
        for i in text:
            j += i.strip('\n')
    print(j)
    # return 'n'.join(text)
    with open(output_file, 'w') as ex1output:
        # finally, write the result list to the file (be careful, 'writelines()' is used)
        ex1output.writelines(j)
    return 'Check the output file'  # this is for information. actually it isn't necessary. We can return "True" or "1"


if __name__ == '__main__':
    output_file = 'C:\\Users\\user\\Desktop\\QUIZ4.txt'
    print(read_docx('C:\\Users\\user\\Desktop\\QUIZ3.docx'))
