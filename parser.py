#!/usr/bin/env python2

def file_exist(file_path):
    import os.path
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return True
    return False

def get_4b_magic_number(file_path):
    try:
        binaryFile = open(file_path, 'rb')
        magicNumber = binaryFile.read(4)
    except(IOError), e:
        print "%s: unable to open/read.\n%s" % (file_path, e)
    else:
        return magicNumber
    return False

def parse(file_path, image_folder):
    if file_exist(file_path):
        magicNumber = get_4b_magic_number(file_path)
        if magicNumber is not False:
            if magicNumber == "8BPS": #PSD file
                from psdtools import main
            elif magicNumber == "%PDF": #PDF file
                from pdfreader import main
            json = main.run(file_path, image_folder)
            """ We write the json into a file called metadata.json """
            target = open("metadata.json", 'w+') ## a will append, w will over-write
            target.write(json)
            target.close()
        else:
            print "%s: not a psd nor a pdf (Magic Number unknown)" % file_path
    else:
        print "%s: file not found." % file_path

if __name__ == '__main__':
    import sys
    if len(sys.argv) is 3:
        parse(sys.argv[1], sys.argv[2])
    else:
        print "usage: %s pdf_or_psd_file_path generated_images_path/ (eg: python %s book.pdf/.psd './images/')" % (sys.argv[0], sys.argv[0])
