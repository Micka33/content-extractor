from util.convert import converter
from lib.book import book

def text_to_dict(fileinput):
    """
    extracting the text into a xml string
    """
    convert = converter()
    xml = convert.as_xml().add_input_file(fileinput).run()
    """
    Parsing the xml string to transform it into a dictionary
    """
    b = book(xml)
    return b.toDict()


"""
Extracting the images out of the pdf file
images are named respecting the following convention: tempppm-[pageNumber]-[imageNumber].ppm (eg: tempppm-001-000.ppm)
"""
import subprocess
import sys

def extract_images(file, AS="jpeg"):
    if "jpeg" in AS:
        subprocess.call('/usr/local/bin/pdfimages -p -j '+file+' tempimg', shell=True, stderr=sys.stdout)
    elif "ppm" in AS:
        subprocess.call('/usr/local/bin/pdfimages -p '+file+' tempimg', shell=True, stderr=sys.stdout)



"""
Matching ppm images with pattern to convert them in png images
At the same time, dict_book is updated with the path of the png images
"""
import glob
import json
import uuid
import re
import os

def get_img_names_by_page_number():
    image_list = {}
    ppm_images = glob.glob('./tempimg*.*')
    for image in ppm_images:
        match = re.match( r'\./tempimg\-(\d+)\-(\d+)\.[jpg|ppm|pbm]', image, re.M|re.I)
        if match:
            page_num = int(match.group(1)) - 1
            image_num = int(match.group(2))
            if page_num not in image_list:
                image_list[page_num] = {}
            image_list[page_num].update({image_num:image})
    return image_list

def rename_imgs__update_dict(image_list, dict_book, image_folder, AS="jpeg"):
    for page in image_list.iterkeys():
        for image in image_list[page].iterkeys():
            if 'images' not in dict_book['pages'][page]:
                dict_book['pages'][page].update({'images':[]})
            if "jpeg" in AS:
                image_name = "%s_p%d.jpg" % (uuid.uuid1(), page)
                dict_book['pages'][page]['images'].append(image_name)
                subprocess.call('mv %s %s'%(image_list[page][image], image_folder+image_name), shell=True, stderr=sys.stdout)
            elif "ppm" in AS:
                image_name = "%s_p%d.png" % (uuid.uuid1(), page)
                dict_book['pages'][page]['images'].append(image_name)
                subprocess.call('/usr/local/bin/convert %s %s'%(image_list[page][image], image_folder+image_name), shell=True, stderr=sys.stdout)
                os.remove(image_list[page][image])
    return dict_book

def get_images_update_dict(dict_book, image_folder, AS="jpeg"):
    image_list = get_img_names_by_page_number()
    dict_book = rename_imgs__update_dict(image_list, dict_book, image_folder, AS)
    return dict_book


def run(pdf_file, image_folder, AS="jpeg"):
    dict_book = text_to_dict(pdf_file)
    extract_images(pdf_file, AS)
    dict_book = get_images_update_dict(dict_book, image_folder, AS)
    return json.dumps(dict_book)


if __name__ == '__main__':
    import sys
    if len(sys.argv) is 3:
        print run(sys.argv[1], sys.argv[2])
    else:
        print "usage: %s pdf_file_path generated_images_path/ (eg: python %s book.pdf './images/')" % (sys.argv[0], sys.argv[0])



"""
# here is an example of how look the dict_book
print json.dumps(dict_book)
{
    "pages": [
        {
            "images": [
                "961dfcc0-c1eb-11e2-92af-040ccedc7e34_p0.png"
            ],
            "paragraphs": [
                {
                    "size": 98,
                    "width": 587,
                    "string": "Book Title",
                    "y": -98,
                    "x": -324,
                    "font": "Georgia",
                    "height": 705
                }
            ]
        },
        {
            "images": [
                "96f4e9ee-c1eb-11e2-ad2b-040ccedc7e34_p1.png"
            ],
            "paragraphs": [
                {
                    "size": 24,
                    "width": 138,
                    "string": "CHAPTER 1",
                    "y": -24,
                    "x": -88,
                    "font": "Georgia",
                    "height": 711
                },
                {
                    "size": 33,
                    "width": 489,
                    "string": "Lorem ipsum dolor sit amet, consectetur \n<i>adipisicing</i> <b>elit, sed</b> <i><b>do eiusmod</i></b>\ntempor incididunt ut labore et dolore \nmagna aliqua. Ut enim ad minim veniam,\nquis nostrud exercitation ullamco laboris \nnisi ut aliquip ex ea commodo\nconsequat.",
                    "y": -229,
                    "x": -439,
                    "font": "Georgia",
                    "height": 269
                }
            ]
        },
        {
            "paragraphs": [
                {
                    "size": 24,
                    "width": 133,
                    "string": "SECTION 1",
                    "y": -24,
                    "x": -83,
                    "font": "Georgia",
                    "height": 711
                }
            ]
        }
    ]
}
"""