from psd_tools import PSDImage
from psd_tools.constants import BlendMode
import psd_tools.user_api.psd_image
import json
import uuid

"""
{"pages":[{"images":[], "paragraphs":[{"size":0, "width":0, "string":"", "x":0, "y":0, "font":"", "height":0}]}]}
or
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
        }
    ]
}
"""
class ImportPSD(object):

    """ Will Parse a PSD and store its data """
    data = {'pages':[]}
    imagePath = './'
    psd = None
    PSDFilePath = None

    @classmethod
    def __init__(self, PSDFilePath, imagePath):
        self.PSDFilePath = PSDFilePath
        self.imagePath = imagePath
        self.psd = PSDImage.load(PSDFilePath)

    @classmethod
    def parse(self):
        self.data['pages'].append(self.browseSheets(sheets=self.psd.layers, parentName="root"))

    @classmethod
    def browseSheets(self, sheets, parentName, page_num=1):
        array = {}
        for sheet in sheets:
            if isinstance(sheet, psd_tools.user_api.psd_image.Layer):
                """ this sheet is a layer, it may be an image or some text """
                if sheet.text_data is not None:
                    """ If it's a text """
                    dic = dict({    'name': sheet.name,
                                    'x': sheet.bbox.x1,
                                    'y': sheet.bbox.y2,
                                    'width': sheet.bbox.width,
                                    'height': sheet.bbox.height,
                                    'string': sheet.text_data.text,
                                    'font': None
                                })
                    if 'paragraphs' not in array:
                        array['paragraphs'] = []
                    array['paragraphs'].append(dic)
                else:
                    """ If it's an image """
                    imageName = str(uuid.uuid1())+'_'+sheet.name+'_'+parentName+'.png'
                    if sheet is not None and sheet.as_PIL() is not None:
                        sheet.as_PIL().save(self.imagePath+imageName)
                    else:
                        imageName = None
                    if 'images' not in array:
                        array['images'] = []
                    array['images'].append(imageName)
            elif isinstance(sheet, psd_tools.user_api.psd_image.Group):
                """ this sheet is a group and may contains many layers """
                if sheet.visible_global:
                    arr = self.browseSheets(sheets=sheet.layers, parentName=sheet.name, page_num=page_num+1)
                    self.data['pages'].append(arr)
        return array

    @classmethod
    def toJson(self):
        """ Will convert the parsed data array into json """
        return json.dumps(self.data)



def run(pdf_file, image_folder):
    importedPSD = ImportPSD(PSDFilePath=pdf_file, imagePath=image_folder)
    importedPSD.parse()
    jsonString = importedPSD.toJson()
    return jsonString




if __name__ == '__main__':
    import sys
    if len(sys.argv) is 3:
        run(sys.argv[1], sys.argv[2])
    else:
        print "usage: %s pdf_file_path generated_images_path/ (eg: python %s book.pdf './images/')" % (sys.argv[0], sys.argv[0])
