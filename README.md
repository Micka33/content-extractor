content-extractor
=================

Content-extractor is python based project. The only reason to this is the availability of the librairies. (The best ones are in python IMO)
Currently, this project parse pdf and psd file to extract meaningful content, such as texts and images both linked under a common json string


Dependencies
=================

Content-extractor is build upon the followings:

- [psd-tools](https://pypi.python.org/pypi/psd-tools/) To extract images and text from psd files
- [pdfminer](http://www.unixuser.org/~euske/python/pdfminer/#intro) To extract text from pdf files as xml
- [beautiful soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) To convert the extracted xml as json
- [pdfimages](http://ubuntugenius.wordpress.com/2012/02/04/how-to-extract-images-from-pdf-documents-in-ubuntulinux/) To extract images from pdf files as image.ppm
- [ImageMagick](http://www.imagemagick.org/script/index.php) To convert the ppm images to png


Installation
=================

Since there is a lot of dependencies and most of them also have their own dependencies, I have made a shellscript to simplify the installation process.

The script assume the following:

 - Mac users already have installed [XQuartz](http://xquartz.macosforge.org/landing/).
 - If you don't have [apt-get](http://doc.ubuntu-fr.org/apt-get), then you should have [brew](http://mxcl.github.io/homebrew/).
 - You have [curl](http://pwet.fr/man/linux/commandes/curl) installed (the shell executable, not the php module).
 - You have [python 2.7.x](http://www.python.org/download/) installed on your system.
 - You have [unzip](http://www.info-zip.org/mans/unzip.html) installed on your system.

When you launch the script, it's installing [pip](https://pypi.python.org/pypi/pip), if it isn't already present on your system.

    cd install
    sh install.sh

How to use it
=================

For any extension (currently pdf/psd) you can use `parser.py [file_path] [image_path]` it will automaticaly do the job.

    #Will write a metada.json and extract the images into the folder images
    ./parser.py psdtools/work.psd './images/'
    ./parser.py pdfreader/book.pdf './images/'

You can also import parser.py into your own python project and use it the folowing way:

    #will return a string containing the json and extract the images into the folder images
    from parser import parser
    json = parser.parse("psdtools/work.psd", "./images/")
    json = parser.parse("pdfreader/book.pdf", "./images/")


You can also use the pdfreader and psdtools script independently doing so:

    Shell:

    ./psdtools/main.py psdtools/work.psd './images/'
    ./pdfreader/main.py pdfreader/book.pdf './images/'


    Python:

    from psdtools import main
    json = main.run("psdtools/work.psd", "./images/")

    from pdfreader import main
    json = main.run("pdfreader/book.pdf", "./images/")
    json = main.run("pdfreader/book.pdf", "./images/", "ppm") #will extract the images as ppm/pbm ad then convert them as png
    json = main.run("pdfreader/book.pdf", "./images/", "jpeg") #default: will extract the images directly as jpg


./pdfreader/main.py is just a simplified interface to the very powerful pdfreader/util/convert.py, I have rewrite convert.py to be a class, but this is originally [pdf2txt.py](http://www.unixuser.org/~euske/python/pdfminer/#pdf2txt) from [pdfminer](http://www.unixuser.org/~euske/python/pdfminer/index.html).
However, you can still use convert.py as if it was the originial [pdf2txt.py](http://www.unixuser.org/~euske/python/pdfminer/index.html#pdf2txt) tool, [here is the documentation](http://www.unixuser.org/~euske/python/pdfminer/index.html#pdf2txt).

    $ pdfreader/util/convert.py -o output.html samples/naacl06-shinyama.pdf
    (extract text as an HTML file whose filename is output.html)

    $ pdfreader/util/convert.py -V -c euc-jp -o output.html samples/jo.pdf
    (extract a Japanese HTML file in vertical writing, CMap is required)

    $ pdfreader/util/convert.py -P mypassword -o output.txt secret.pdf
    (extract a text from an encrypted PDF file)

convert.py can also be imported in a python project (but less options are available due to my lack of implementation)

    # @see pdfreader/main.py:text_to_dict as example
    from util.convert import converter
    convert = converter()
    xml = convert.as_xml().add_input_file(fileinput).run()


How does it work
=================

The information are extracted having in mind to keep the parent-child relations.

 - For a pdf file:
    - A pdf file can have many pages, and so the json string goes. each page has many images and many paragraphs.
    - Each paragraph has a width, height, a content(string), a y and x position, a font, and a font size.
    - For a pdf file the original image name can't be extracted so the images are name like the followong [uniqId]_p[pageNumber].png. uniqId is a unique Id, pageNumber is the page in which the images is contained. you shouldn't need to use this information since the json string contains it.

 - For a psd file:
    - A psd file can have many groups which are translated in pages into the json string. each group in a psd file can have many layers, a layer can be either text(paragraphs) or an image(images).
    - Each text layer has a width, height, a content(string), a y and x position. The font and font size are currenlty not extracted (because psd-tools doesn't do it).
    - For a psd file the image is name with the layer name it come from, but since many layers can have the same name the following is applied to be sure we have a unique name. [uniqId]_[layerName]_[groupName].png.

 - PSD files:
   - Text: Because of the psd-tools library, you can't know the font, bold, italic, underline attribute.

 - PDF files:
   - Text: Because of the pdfminer library, you can't have many fonts in the same paragraph. It is also not possible to extract the underlines. However the bold and italic attribute are extracted as html and directly integrated into the string.

You can see under a simplified example taken out from book.pdf of how look the json string.

JSON Format (from pdfreader/book.pdf 'simplified')
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


How to improve it
=================

 - The psd-tools library should be improved to be able to take out the font, bold italic underline attribute
 - The pdfminer library should be improved to be able to take out the underline attribute
 - Matching the pep8?
 - Checking if the proposed image folder exist if not we create it if we can't fire an error and stop
 - Adding support for more file format
 - Speed is not an issue but why not improving it ?
 - The psd-tools library should be improved to be able to extract layers containing fx effect (is this even possible?)
 - Depending of the platform or a parameter the `\n` into the string attribute in JSON should become `<br/>` or `\r\n`
 - Reduce the number of dependencies ?
 - What else ?

Contributing
=================

You're welcome to contribute to this project in any way you can. If you don't know how to code, don't have time, don't worry, you still can post issue, I will be happy to answer you and correct it as fast as possible.
Want to code ? fork it and submit pull request! Also, pull request comming with an example of what has been improved will be merge in priority.
