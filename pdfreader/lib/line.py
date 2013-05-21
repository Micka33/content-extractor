from cStringIO import StringIO
from char import char

class line(object):

    _width = 0
    _height = 0
    _x = 0
    _y = 0
    _font = None
    _lines = []

    @property
    def font(self):
        return self._font

    @property
    def size(self):
        return self._size

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


    def __init__(self, xml_line):
        (left, top, self._width, self._height) = xml_line.get('bbox').split(',')
        self._width = int(float(self._width))
        self._height = int(float(self._height))
        self._x = int(float(left)) - self._width
        self._y = int(float(top)) - self._height
        #
        xml_string = xml_line.find_all('text')
        self._chars = []
        for c in xml_string:
            self._chars.append(char(c))
        #
        self._font = self._chars[0].font if len(self._chars) > 0 else None
        self._size = self._chars[0].size if len(self._chars) > 0 else None

    _italic_on = False
    def handle_italic(self, c, string):
        if self._italic_on is False and c.isItalic() is True:
            string.write('<i>')
            self._italic_on = True
        if self._italic_on is True and c.isItalic() is False:
            string.write('</i>')
            self._italic_on = False

    _bold_on = False
    def handle_bold(self, c, string):
        if self._bold_on is False and c.isBold() is True:
            string.write('<b>')
            self._bold_on = True
        if self._bold_on is True and c.isBold() is False:
            string.write('</b>')
            self._bold_on = False


    def __str__(self):
        string = StringIO()
        for c in self._chars:
            self.handle_italic(c, string)
            self.handle_bold(c, string)
            string.write(str(c))
        return string.getvalue()








if __name__ == '__main__':
    import sys
    from bs4 import BeautifulSoup
    file="""<?xml version="1.0" encoding="utf-8" ?>
<pages>
<page id="1" bbox="0.000,0.000,1024.000,748.000" rotate="0">
<textbox id="0" bbox="263.163,702.557,365.297,721.036">
<textline bbox="263.163,702.557,365.297,721.036">
<text font="OWDOPW+Georgia" bbox="263.163,702.557,271.263,721.036" size="18.479">L</text>
<text font="OWDOPW+Georgia-Bold" bbox="271.927,702.557,281.904,721.036" size="18.479">O</text>
<text font="OWDOPW+Georgia-BoldItalic" bbox="282.582,702.557,291.996,721.036" size="18.479">R</text>
<text font="OWDOPW+Georgia-BoldItalic" bbox="292.659,702.557,301.416,721.036" size="18.479">E</text>
<text font="OWDOPW+Georgia-Italic" bbox="302.094,702.557,314.525,721.036" size="18.479">M</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="315.202,702.557,318.434,721.036" size="18.479"> </text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="319.111,702.557,324.341,721.036" size="18.479">I</text>
<text font="OWDOPW+Georgia" bbox="325.005,702.557,333.186,721.036" size="18.479">P</text>
<text font="OWDOPW+Georgia" bbox="333.849,702.557,341.373,721.036" size="18.479">S</text>
<text font="OWDOPW+Georgia" bbox="342.050,702.557,352.188,721.036" size="18.479">U</text>
<text font="OWDOPW+Georgia" bbox="352.865,702.557,365.297,721.036" size="18.479">M</text>
<text>
</text>
</textline>
</textbox>
</page>
</pages>
    """
    soup = BeautifulSoup(file)
    l = line(soup.pages.page.textbox.textline)
    print ("[%s] font[%s]" % (l, l.font))
