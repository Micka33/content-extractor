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
 - If you don't have [apt-get](http://doc.ubuntu-fr.org/apt-get) then you should have [brew](http://mxcl.github.io/homebrew/).
 - You have [curl](http://pwet.fr/man/linux/commandes/curl) installed (the shell executable, not the php module).

When you launch the script it is installing [pip](https://pypi.python.org/pypi/pip) and [easy_install](http://pythonhosted.org/distribute/easy_install.html) if they are not already present on your system.

    cd install
    sh install.sh

How to use it
=================

 - From psd files:
   - Images: This command will extract the images into the `./images/` folder (note that the folder should already exist).
Because of the psd-tools library, layers into the psd files can't contain "Fx" effect, if so, they should be converted into "Smart Object".
   - Text: Because of the psd-tools library, you can't know the font, bold, italic, underline attribute. The text without any other information of this kind.
    
    `./parser.py psdtools/work.psd './images/'`

 - From pdf files:
   - Images: This command will extract the images into the `./images/` folder (note that the folder should alreadyd exist).
Images are extracted in a two step process, first we extract them as ppm with a temporary name, then we convert them into png files with their final name.

   - Text: Because of the pdfminer library, you can't have many fonts in the same paragraph. It is also not possible to extract the underlines. However the bold and italic attribute are extracted as html and directly integrated into the string.

    `./parser.py pdfreader/book.pdf './images/'`


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

 - Make the difference between a pdf a psd we should check the extension not just look for pdf or psd into the name of the file
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
