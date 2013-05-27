#!/usr/bin/env python2

def parse(file_path, image_folder):
    if 'psd' in file_path:
        from psdtools import main
    elif 'pdf' in file_path:
        from pdfreader import main
    json = main.run(file_path, image_folder)
    """ We write the json into a file called metadata.json """
    target = open("metadata.json", 'w+') ## a will append, w will over-write
    target.write(json)
    target.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) is 3:
        parse(sys.argv[1], sys.argv[2])
    else:
        print "usage: %s pdf_or_psd_file_path generated_images_path/ (eg: python %s book.pdf/.psd './images/')" % (sys.argv[0], sys.argv[0])
