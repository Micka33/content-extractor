content-extractor
=================

Content-extractor is python based project. The only reason to this is the availability of the librairies. (The best ones are in python IMO)
Currently, this project parse pdf and psd file to extract meaningful content, such as texts and images both linked into a json string


Dependencies
=================

Content-extractor is build upon the followings:

- [psd-tools](https://pypi.python.org/pypi/psd-tools/) To extract images and text from psd files
- [pdfminer](http://www.unixuser.org/~euske/python/pdfminer/#intro) To extract text from pdf files
- [pdfimages](http://ubuntugenius.wordpress.com/2012/02/04/how-to-extract-images-from-pdf-documents-in-ubuntulinux/) To extract images from pdf files as image.ppm
- [ImageMagick](http://www.imagemagick.org/script/index.php) To convert the ppm images to png

How to use it
=================

From psd files:
Images:
This command will extract the images into the `./images/` folder (note that the folder should already exist)
Because of the psd-tools library, layers into the psd files can't contain "Fx" effect, if so, they should be converted into "Smart Object".
Text:
Because of the psd-tools library, you can't know the font, bold, italic, underline attribute. The text without any other information of this kind.

    ./parser.py psdtools/work.psd './images/'

From pdf files:
Images:
This command will extract the images into the `./images/` folder (note that the folder should alreadyd exist)
Images are extracted in a two step process, first we extract them as ppm with a temporary name, them we convert them into png files with their final name.
Text:
Because of the pdfminer library, you can't have many fonts in the same paragraph. It is also not possible to extract the underlines. However the bold and italic attribute are extracted as html and directly integrated into the string.

    ./parser.py pdfreader/book.pdf './images/'

JSON Format
=================

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
