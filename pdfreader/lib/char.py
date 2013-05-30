class char(object):

    _size = 0
    _width = 0
    _height = 0
    _x = 0
    _y = 0
    _font = None
    _isBold = False
    _isItalic = False
    _char = ''

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

    def __init__(self, xml_char):
        self._font = xml_char.get('font').split('+')[1] if xml_char.get('font') != None else None
        if self._font is not None:
            (left, top, self._width, self._height) = xml_char.get('bbox').split(',')
            self._width = int(float(self._width))
            self._height = int(float(self._height))
            self._x = int(float(left)) - self._width
            self._y = int(float(top)) - self._height
            self._size = int(float(xml_char.get('size')))
            self._isBold = True if len(self._font.split('-')) == 2 and 'Bold' in self._font.split('-')[1] else False
            self._isItalic = True if len(self._font.split('-')) == 2 and 'Italic' in self._font.split('-')[1] else False
            self._font = self._font.split('-')[0]
            #
            self._char = xml_char.string

    def isBold(self):
        return self._isBold

    def isItalic(self):
        return self._isItalic

    def __str__(self):
        if self._font is None:
            return ""
        try:
            char = str(self._char)
            return char
        except UnicodeEncodeError:
            return ""
