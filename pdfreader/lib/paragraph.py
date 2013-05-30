from line import line
from cStringIO import StringIO

class paragraph(object):

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

    def __init__(self, xml_paragraph):
        (left, top, self._width, self._height) = xml_paragraph.get('bbox').split(',')
        self._width = int(float(self._width))
        self._height = int(float(self._height))
        self._x = int(float(left)) - self._width
        self._y = int(float(top)) - self._height
        #
        xml = xml_paragraph.find_all('textline')
        self._lines = []
        for l in xml:
            self._lines.append(line(l))
        #
        self._font = self._lines[0].font if len(self._lines) > 0 else None
        self._size = self._lines[0].size if len(self._lines) > 0 else None

    def toDict(self):
        dico = dict({  'font': self._font,
                        'size': self._size,
                        'x': self._x,
                        'y': self._y,
                        'width': self._width,
                        'height': self._height
                        })
        string = StringIO()
        count = 0
        for l in self._lines:
            if count != 0:
                string.write("\n")
            string.write(str(l))
            count = 1
        dico.update({'string': string.getvalue()})
        return dico

    def __str__(self):
        string = StringIO()
        count = 0
        for l in self._lines:
            if count != 0:
                string.write("\n")
            string.write(str(l))
            count = 1
        return string.getvalue()






















if __name__ == '__main__':
    import sys
    import json
    from bs4 import BeautifulSoup
    file="""<?xml version="1.0" encoding="utf-8" ?>
<pages>
<page id="1" bbox="0.000,0.000,1024.000,748.000" rotate="0">
<textbox id="2" bbox="50.000,40.406,489.850,269.078">
<textline bbox="50.000,236.006,485.115,269.078">
<text font="OWDOPW+Georgia-Bold" bbox="263.163,702.557,271.263,721.036" size="18.479">L</text>
<text font="OWDOPW+Georgia-Bold" bbox="271.927,702.557,281.904,721.036" size="18.479">O</text>
<text font="OWDOPW+Georgia-BoldItalic" bbox="282.582,702.557,291.996,721.036" size="18.479">R</text>
<text font="OWDOPW+Georgia-BoldItalic" bbox="292.659,702.557,301.416,721.036" size="18.479">E</text>
<text font="OWDOPW+Georgia-Italic" bbox="302.094,702.557,314.525,721.036" size="18.479">M</text>
<text font="OWDOPW+Georgia" bbox="315.202,702.557,318.434,721.036" size="18.479"> </text>
<text font="OWDOPW+Georgia" bbox="319.111,702.557,324.341,721.036" size="18.479">I</text>
<text font="OWDOPW+Georgia" bbox="325.005,702.557,333.186,721.036" size="18.479">P</text>
<text font="OWDOPW+Georgia" bbox="333.849,702.557,341.373,721.036" size="18.479">S</text>
<text font="OWDOPW+Georgia" bbox="342.050,702.557,352.188,721.036" size="18.479">U</text>
<text font="OWDOPW+Georgia" bbox="352.865,702.557,365.297,721.036" size="18.479">M</text>
<text font="OWDOPW+Georgia" bbox="191.847,236.006,197.631,269.078" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="197.636,236.006,211.412,269.078" size="33.072">d</text>
<text font="OWDOPW+Georgia" bbox="211.417,236.006,224.353,269.078" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="224.355,236.006,231.219,269.078" size="33.072">l</text>
<text font="OWDOPW+Georgia" bbox="231.222,236.006,244.158,269.078" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="244.160,236.006,254.000,269.078" size="33.072">r</text>
<text font="OWDOPW+Georgia" bbox="253.993,236.006,259.777,269.078" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="259.782,236.006,270.150,269.078" size="33.072">s</text>
<text font="OWDOPW+Georgia" bbox="270.152,236.006,277.184,269.078" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="277.184,236.006,285.464,269.078" size="33.072">t</text>
<text font="OWDOPW+Georgia" bbox="285.469,236.006,291.253,269.078" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="291.258,236.006,303.354,269.078" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="303.351,236.006,324.495,269.078" size="33.072">m</text>
<text font="OWDOPW+Georgia" bbox="324.493,236.006,336.085,269.078" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="336.094,236.006,344.374,269.078" size="33.072">t</text>
<text font="OWDOPW+Georgia" bbox="344.379,236.006,350.859,269.078" size="33.072">,</text>
<text font="OWDOPW+Georgia" bbox="350.847,236.006,356.631,269.078" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="356.636,236.006,367.532,269.078" size="33.072">c</text>
<text font="OWDOPW+Georgia" bbox="367.534,236.006,380.470,269.078" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="380.473,236.006,394.657,269.078" size="33.072">n</text>
<text font="OWDOPW+Georgia" bbox="394.652,236.006,405.020,269.078" size="33.072">s</text>
<text font="OWDOPW+Georgia" bbox="405.022,236.006,416.614,269.078" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="416.624,236.006,427.520,269.078" size="33.072">c</text>
<text font="OWDOPW+Georgia" bbox="427.522,236.006,435.802,269.078" size="33.072">t</text>
<text font="OWDOPW+Georgia" bbox="435.807,236.006,447.399,269.078" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="447.409,236.006,455.689,269.078" size="33.072">t</text>
<text font="OWDOPW+Georgia" bbox="455.694,236.006,469.494,269.078" size="33.072">u</text>
<text font="OWDOPW+Georgia" bbox="469.498,236.006,479.338,269.078" size="33.072">r</text>
<text font="OWDOPW+Georgia" bbox="479.331,236.006,485.115,269.078" size="33.072"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,203.606,420.075,237.278">
<text font="OTOBVA+Georgia-Italic" bbox="50.000,203.606,63.752,236.654" size="33.048">a</text>
<text font="OTOBVA+Georgia-Italic" bbox="63.747,203.606,77.547,236.654" size="33.048">d</text>
<text font="OTOBVA+Georgia-Italic" bbox="77.542,203.606,84.670,236.654" size="33.048">i</text>
<text font="OTOBVA+Georgia-Italic" bbox="84.690,203.606,98.562,236.654" size="33.048">p</text>
<text font="OTOBVA+Georgia-Italic" bbox="98.557,203.606,105.685,236.654" size="33.048">i</text>
<text font="OTOBVA+Georgia-Italic" bbox="105.704,203.606,116.048,236.654" size="33.048">s</text>
<text font="OTOBVA+Georgia-Italic" bbox="116.043,203.606,123.171,236.654" size="33.048">i</text>
<text font="OTOBVA+Georgia-Italic" bbox="123.190,203.606,134.086,236.654" size="33.048">c</text>
<text font="OTOBVA+Georgia-Italic" bbox="134.082,203.606,141.210,236.654" size="33.048">i</text>
<text font="OTOBVA+Georgia-Italic" bbox="141.229,203.606,155.389,236.654" size="33.048">n</text>
<text font="OTOBVA+Georgia-Italic" bbox="155.384,203.606,169.136,236.654" size="33.048">g</text>
<text font="OWDOPW+Georgia" bbox="169.109,203.606,174.893,236.678" size="33.072"> </text>
<text font="YFNXOA+Georgia-Bold" bbox="174.898,203.606,188.626,237.278" size="33.672">e</text>
<text font="YFNXOA+Georgia-Bold" bbox="188.622,203.606,196.878,237.278" size="33.672">l</text>
<text font="YFNXOA+Georgia-Bold" bbox="196.873,203.606,205.369,237.278" size="33.672">i</text>
<text font="YFNXOA+Georgia-Bold" bbox="205.364,203.606,214.892,237.278" size="33.672">t</text>
<text font="YFNXOA+Georgia-Bold" bbox="214.911,203.606,222.783,237.278" size="33.672">,</text>
<text font="YFNXOA+Georgia-Bold" bbox="222.778,203.606,228.874,237.278" size="33.672"> </text>
<text font="YFNXOA+Georgia-Bold" bbox="228.870,203.606,241.182,237.278" size="33.672">s</text>
<text font="YFNXOA+Georgia-Bold" bbox="241.177,203.606,254.905,237.278" size="33.672">e</text>
<text font="YFNXOA+Georgia-Bold" bbox="254.900,203.606,270.812,237.278" size="33.672">d</text>
<text font="OWDOPW+Georgia" bbox="270.816,203.606,276.600,236.678" size="33.072"> </text>
<text font="UXGHCH+Georgia-BoldItalic" bbox="276.606,203.606,292.517,237.062" size="33.456">d</text>
<text font="UXGHCH+Georgia-BoldItalic" bbox="292.508,203.606,307.772,237.062" size="33.456">o</text>
<text font="UXGHCH+Georgia-BoldItalic" bbox="307.765,203.606,313.861,237.062" size="33.456"> </text>
<text font="UXGHCH+Georgia-BoldItalic" bbox="313.858,203.606,327.226,237.062" size="33.456">e</text>
<text font="UXGHCH+Georgia-BoldItalic" bbox="327.229,203.606,336.013,237.062" size="33.456">i</text>
<text font="UXGHCH+Georgia-BoldItalic" bbox="336.005,203.606,352.445,237.062" size="33.456">u</text>
<text font="UXGHCH+Georgia-BoldItalic" bbox="352.448,203.606,364.856,237.062" size="33.456">s</text>
<text font="UXGHCH+Georgia-BoldItalic" bbox="364.858,203.606,388.906,237.062" size="33.456">m</text>
<text font="UXGHCH+Georgia-BoldItalic" bbox="388.906,203.606,404.170,237.062" size="33.456">o</text>
<text font="UXGHCH+Georgia-BoldItalic" bbox="404.163,203.606,420.075,237.062" size="33.456">d</text>
<text>
</text>
</textline>
<textline bbox="50.000,170.206,452.162,204.656">
<text font="OWDOPW+Georgia" bbox="50.000,170.206,58.625,204.656" size="34.450">t</text>
<text font="OWDOPW+Georgia" bbox="58.630,170.206,70.705,204.656" size="34.450">e</text>
<text font="OWDOPW+Georgia" bbox="70.710,170.206,92.735,204.656" size="34.450">m</text>
<text font="OWDOPW+Georgia" bbox="92.740,170.206,107.015,204.656" size="34.450">p</text>
<text font="OWDOPW+Georgia" bbox="107.020,170.206,120.495,204.656" size="34.450">o</text>
<text font="OWDOPW+Georgia" bbox="120.500,170.206,130.750,204.656" size="34.450">r</text>
<text font="OWDOPW+Georgia" bbox="130.737,170.425,136.521,203.497" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="136.526,170.425,143.558,203.497" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="143.558,170.425,157.742,203.497" size="33.072">n</text>
<text font="OWDOPW+Georgia" bbox="157.738,170.425,168.634,203.497" size="33.072">c</text>
<text font="OWDOPW+Georgia" bbox="168.636,170.425,175.668,203.497" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="175.668,170.425,189.444,203.497" size="33.072">d</text>
<text font="OWDOPW+Georgia" bbox="189.449,170.425,196.481,203.497" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="196.481,170.425,210.257,203.497" size="33.072">d</text>
<text font="OWDOPW+Georgia" bbox="210.262,170.425,224.062,203.497" size="33.072">u</text>
<text font="OWDOPW+Georgia" bbox="224.066,170.425,238.250,203.497" size="33.072">n</text>
<text font="OWDOPW+Georgia" bbox="238.246,170.425,246.526,203.497" size="33.072">t</text>
<text font="OWDOPW+Georgia" bbox="246.530,170.425,252.314,203.497" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="252.319,170.425,266.119,203.497" size="33.072">u</text>
<text font="OWDOPW+Georgia" bbox="266.124,170.425,274.404,203.497" size="33.072">t</text>
<text font="OWDOPW+Georgia" bbox="274.409,170.425,280.193,203.497" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="280.197,170.425,287.061,203.497" size="33.072">l</text>
<text font="OWDOPW+Georgia" bbox="287.066,170.425,299.162,203.497" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="299.167,170.425,312.607,203.497" size="33.072">b</text>
<text font="OWDOPW+Georgia" bbox="312.612,170.425,325.548,203.497" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="325.553,170.425,335.393,203.497" size="33.072">r</text>
<text font="OWDOPW+Georgia" bbox="335.374,170.425,346.966,203.497" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="346.970,170.425,352.754,203.497" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="352.759,170.425,364.351,203.497" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="364.356,170.425,372.636,203.497" size="33.072">t</text>
<text font="OWDOPW+Georgia" bbox="372.641,170.425,378.425,203.497" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="378.430,170.425,392.206,203.497" size="33.072">d</text>
<text font="OWDOPW+Georgia" bbox="392.210,170.425,405.146,203.497" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="405.151,170.425,412.015,203.497" size="33.072">l</text>
<text font="OWDOPW+Georgia" bbox="412.020,170.425,424.956,203.497" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="424.961,170.425,434.801,203.497" size="33.072">r</text>
<text font="OWDOPW+Georgia" bbox="434.782,170.425,446.374,203.497" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="446.378,170.425,452.162,203.497" size="33.072"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,137.606,489.490,170.678">
<text font="OWDOPW+Georgia" bbox="50.000,137.606,71.144,170.678" size="33.072">m</text>
<text font="OWDOPW+Georgia" bbox="71.142,137.606,83.238,170.678" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="83.235,137.606,95.451,170.678" size="33.072">g</text>
<text font="OWDOPW+Georgia" bbox="95.458,137.606,109.642,170.678" size="33.072">n</text>
<text font="OWDOPW+Georgia" bbox="109.638,137.606,121.734,170.678" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="121.731,137.606,127.515,170.678" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="127.520,137.606,139.616,170.678" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="139.614,137.606,146.478,170.678" size="33.072">l</text>
<text font="OWDOPW+Georgia" bbox="146.480,137.606,153.512,170.678" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="153.512,137.606,166.952,170.678" size="33.072">q</text>
<text font="OWDOPW+Georgia" bbox="166.942,137.606,180.742,170.678" size="33.072">u</text>
<text font="OWDOPW+Georgia" bbox="180.747,137.606,192.843,170.678" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="192.841,137.606,199.321,170.678" size="33.072">.</text>
<text font="OWDOPW+Georgia" bbox="199.309,137.606,205.093,170.678" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="205.098,137.606,223.242,170.678" size="33.072">U</text>
<text font="OWDOPW+Georgia" bbox="223.249,137.606,231.529,170.678" size="33.072">t</text>
<text font="OWDOPW+Georgia" bbox="231.534,137.606,237.318,170.678" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="237.322,137.606,248.914,170.678" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="248.924,137.606,263.108,170.678" size="33.072">n</text>
<text font="OWDOPW+Georgia" bbox="263.103,137.606,270.135,170.678" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="270.135,137.606,291.279,170.678" size="33.072">m</text>
<text font="OWDOPW+Georgia" bbox="291.277,137.606,297.061,170.678" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="297.066,137.606,309.162,170.678" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="309.159,137.606,322.935,170.678" size="33.072">d</text>
<text font="OWDOPW+Georgia" bbox="322.940,137.606,328.724,170.678" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="328.729,137.606,349.873,170.678" size="33.072">m</text>
<text font="OWDOPW+Georgia" bbox="349.870,137.606,356.902,170.678" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="356.902,137.606,371.086,170.678" size="33.072">n</text>
<text font="OWDOPW+Georgia" bbox="371.082,137.606,378.114,170.678" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="378.114,137.606,399.258,170.678" size="33.072">m</text>
<text font="OWDOPW+Georgia" bbox="399.255,137.606,405.039,170.678" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="405.044,137.606,416.972,170.678" size="33.072">v</text>
<text font="OWDOPW+Georgia" bbox="416.962,137.606,428.554,170.678" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="428.564,137.606,442.748,170.678" size="33.072">n</text>
<text font="OWDOPW+Georgia" bbox="442.743,137.606,449.775,170.678" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="449.775,137.606,461.871,170.678" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="461.869,137.606,483.013,170.678" size="33.072">m</text>
<text font="OWDOPW+Georgia" bbox="483.010,137.606,489.490,170.678" size="33.072">,</text>
<text>
</text>
</textline>
<textline bbox="50.000,105.206,489.850,138.278">
<text font="OWDOPW+Georgia" bbox="50.000,105.206,63.440,138.278" size="33.072">q</text>
<text font="OWDOPW+Georgia" bbox="63.430,105.206,77.230,138.278" size="33.072">u</text>
<text font="OWDOPW+Georgia" bbox="77.235,105.206,84.267,138.278" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="84.267,105.206,94.635,138.278" size="33.072">s</text>
<text font="OWDOPW+Georgia" bbox="94.638,105.206,100.422,138.278" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="100.426,105.206,114.610,138.278" size="33.072">n</text>
<text font="OWDOPW+Georgia" bbox="114.606,105.206,127.542,138.278" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="127.544,105.206,137.912,138.278" size="33.072">s</text>
<text font="OWDOPW+Georgia" bbox="137.914,105.206,146.194,138.278" size="33.072">t</text>
<text font="OWDOPW+Georgia" bbox="146.199,105.206,156.039,138.278" size="33.072">r</text>
<text font="OWDOPW+Georgia" bbox="156.032,105.206,169.832,138.278" size="33.072">u</text>
<text font="OWDOPW+Georgia" bbox="169.837,105.206,183.613,138.278" size="33.072">d</text>
<text font="OWDOPW+Georgia" bbox="183.618,105.206,189.402,138.278" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="189.406,105.206,200.998,138.278" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="201.008,105.206,213.128,138.278" size="33.072">x</text>
<text font="OWDOPW+Georgia" bbox="213.126,105.206,224.718,138.278" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="224.727,105.206,234.567,138.278" size="33.072">r</text>
<text font="OWDOPW+Georgia" bbox="234.560,105.206,245.456,138.278" size="33.072">c</text>
<text font="OWDOPW+Georgia" bbox="245.458,105.206,252.490,138.278" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="252.490,105.206,260.770,138.278" size="33.072">t</text>
<text font="OWDOPW+Georgia" bbox="260.775,105.206,272.871,138.278" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="272.869,105.206,281.149,138.278" size="33.072">t</text>
<text font="OWDOPW+Georgia" bbox="281.154,105.206,288.186,138.278" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="288.186,105.206,301.122,138.278" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="301.124,105.206,315.308,138.278" size="33.072">n</text>
<text font="OWDOPW+Georgia" bbox="315.303,105.206,321.087,138.278" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="321.092,105.206,334.892,138.278" size="33.072">u</text>
<text font="OWDOPW+Georgia" bbox="334.897,105.206,341.761,138.278" size="33.072">l</text>
<text font="OWDOPW+Georgia" bbox="341.763,105.206,348.627,138.278" size="33.072">l</text>
<text font="OWDOPW+Georgia" bbox="348.630,105.206,360.726,138.278" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="360.723,105.206,381.867,138.278" size="33.072">m</text>
<text font="OWDOPW+Georgia" bbox="381.865,105.206,392.761,138.278" size="33.072">c</text>
<text font="OWDOPW+Georgia" bbox="392.763,105.206,405.699,138.278" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="405.702,105.206,411.486,138.278" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="411.490,105.206,418.354,138.278" size="33.072">l</text>
<text font="OWDOPW+Georgia" bbox="418.357,105.206,430.453,138.278" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="430.450,105.206,443.890,138.278" size="33.072">b</text>
<text font="OWDOPW+Georgia" bbox="443.893,105.206,456.829,138.278" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="456.831,105.206,466.671,138.278" size="33.072">r</text>
<text font="OWDOPW+Georgia" bbox="466.664,105.206,473.696,138.278" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="473.696,105.206,484.064,138.278" size="33.072">s</text>
<text font="OWDOPW+Georgia" bbox="484.066,105.206,489.850,138.278" size="33.072"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,72.806,366.807,105.878">
<text font="OWDOPW+Georgia" bbox="50.000,72.806,64.184,105.878" size="33.072">n</text>
<text font="OWDOPW+Georgia" bbox="64.179,72.806,71.211,105.878" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="71.211,72.806,81.579,105.878" size="33.072">s</text>
<text font="OWDOPW+Georgia" bbox="81.582,72.806,88.614,105.878" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="88.614,72.806,94.398,105.878" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="94.402,72.806,108.202,105.878" size="33.072">u</text>
<text font="OWDOPW+Georgia" bbox="108.207,72.806,116.487,105.878" size="33.072">t</text>
<text font="OWDOPW+Georgia" bbox="116.492,72.806,122.276,105.878" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="122.281,72.806,134.377,105.878" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="134.374,72.806,141.238,105.878" size="33.072">l</text>
<text font="OWDOPW+Georgia" bbox="141.241,72.806,148.273,105.878" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="148.273,72.806,161.713,105.878" size="33.072">q</text>
<text font="OWDOPW+Georgia" bbox="161.703,72.806,175.503,105.878" size="33.072">u</text>
<text font="OWDOPW+Georgia" bbox="175.508,72.806,182.540,105.878" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="182.540,72.806,196.244,105.878" size="33.072">p</text>
<text font="OWDOPW+Georgia" bbox="196.251,72.806,202.035,105.878" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="202.040,72.806,213.632,105.878" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="213.642,72.806,225.762,105.878" size="33.072">x</text>
<text font="OWDOPW+Georgia" bbox="225.759,72.806,231.543,105.878" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="231.548,72.806,243.140,105.878" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="243.150,72.806,255.246,105.878" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="255.243,72.806,261.027,105.878" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="261.032,72.806,271.928,105.878" size="33.072">c</text>
<text font="OWDOPW+Georgia" bbox="271.930,72.806,284.866,105.878" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="284.869,72.806,306.013,105.878" size="33.072">m</text>
<text font="OWDOPW+Georgia" bbox="306.010,72.806,327.154,105.878" size="33.072">m</text>
<text font="OWDOPW+Georgia" bbox="327.152,72.806,340.088,105.878" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="340.090,72.806,353.866,105.878" size="33.072">d</text>
<text font="OWDOPW+Georgia" bbox="353.871,72.806,366.807,105.878" size="33.072">o</text>
<text>
</text>
</textline>
<textline bbox="50.000,40.406,164.070,73.478">
<text font="OWDOPW+Georgia" bbox="50.000,40.406,60.896,73.478" size="33.072">c</text>
<text font="OWDOPW+Georgia" bbox="60.898,40.406,73.834,73.478" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="73.837,40.406,88.021,73.478" size="33.072">n</text>
<text font="OWDOPW+Georgia" bbox="88.023,40.406,98.391,73.478" size="33.072">s</text>
<text font="OWDOPW+Georgia" bbox="98.394,40.406,109.986,73.478" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="109.988,40.406,123.428,73.478" size="33.072">q</text>
<text font="OWDOPW+Georgia" bbox="123.406,40.406,137.206,73.478" size="33.072">u</text>
<text font="OWDOPW+Georgia" bbox="137.209,40.406,149.305,73.478" size="33.072">a</text>
<text font="OWDOPW+Georgia" bbox="149.307,40.406,157.587,73.478" size="33.072">t</text>
<text font="OWDOPW+Georgia" bbox="157.590,40.406,164.070,73.478" size="33.072">.</text>
<text>
</text>
</textline>
</textbox>
</page>
</pages>
    """
    soup = BeautifulSoup(file)
    p = paragraph(soup.pages.page.textbox)
    print ("[%s] font[%s] json[%s]" % (p, p.font, p.toDict()))
