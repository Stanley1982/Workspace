#coding:utf-8

import os
import re

def list_files_to_txt(dir_out, wildcard, recursion):
    book_list = []
    exts = wildcard.split(" ")
    files = os.listdir(dir_out)
    for name in files:
        fullname = os.path.join(dir_out, name)
        if os.path.isdir(fullname) & recursion:
            list_files_to_txt(fullname, wildcard, recursion)
        else:
            for ext in exts:
                if (name.endswith(ext)):
                    book_list.append(name)
                    break
    return book_list


def new_book(book_title,dir_out):
    out_file = book_title + ".rst"
    file_out = open(dir_out + out_file, 'w',encoding='utf-8')
    file_out.write(".. _"+out_file+":")
    file_out.write("\n"*2)
    file_out.write((len(book_title)*2+5)*"*")
    file_out.write("\n")
    file_out.write(book_title)
    file_out.write("\n")
    file_out.write((len(book_title)*2+5)* "*")
    file_out.write("\n"*2)
    file_out.close()


dir_input = "F:\\99 Kindle\\Record\\"
dir_out = "F:\\99 Kindle\\Test\\"
wildcard = ".rst"
recursion = 0

book_list = list_files_to_txt(dir_out, wildcard, recursion)

file_name = "My Clippings_a.txt"
fn = open(dir_input+file_name,'r',encoding= 'utf-8')



line = fn.readline().split('\n')[0]

while line:

    r1 = ['？','：',':','\?',' ']
    book_title = line


    for a in r1:
        book_title = re.sub(a,'_',book_title)
    
    
    if (book_title+'.rst') not in book_list:
        new_book(book_title, dir_out)
        book_list.append(book_title)
    else:
        next
              

    record_time = fn.readline().split('\n')[0]
    fn.readline()
    file_out = open(dir_out + book_title + '.rst', 'a',encoding='utf-8')
    file_out.write(fn.readline())  
    file_out.write("\n")
    file_out.write(" " * 20)
    file_out.write("*")
    file_out.write(record_time)
    file_out.write("*")
    file_out.write("\n")
    file_out.write("\n")
    file_out.close()
    
    fn.readline()
    line = fn.readline().split('\n')[0]

fn.close()



file_book_name = open(dir_out + 'name.rst', 'w',encoding='utf-8')

for book_name in book_list:
    file_book_name.write(' '*3)    
    file_book_name.write(book_name)
    file_book_name.write('\n')
    
file_book_name.close()

