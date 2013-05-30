from paragraph import paragraph
from cStringIO import StringIO

class page(object):

    _paragraphs = []

    @property
    def paragraphs(self):
        return self._paragraphs


    def __init__(self, xml_page):
        xml = xml_page.find_all('textbox')
        self._paragraphs = []
        for p in xml:
            self._paragraphs.append(paragraph(p))

    def toDict(self):
        array = {'paragraphs': []}
        for p in self._paragraphs:
            array['paragraphs'].append(p.toDict())
        return array


    def __str__(self):
        string = StringIO()
        count = 0
        for p in self._paragraphs:
            if count != 0:
                string.write("\n\n")
            string.write(str(p))
            count = 1
        return string.getvalue()






























if __name__ == '__main__':
    import sys
    from bs4 import BeautifulSoup
    file="""<?xml version="1.0" encoding="utf-8" ?>
<pages>
<page id="1" bbox="0.000,0.000,1024.000,748.000" rotate="0">
<textbox id="0" bbox="50.000,40.406,489.850,269.078">
<textline bbox="50.000,236.006,485.115,269.078">
<text font="OWDOPW+Georgia" bbox="263.163,702.557,271.263,721.036" size="18.479">L</text>
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
</textbox>
</textbox>
<textbox id="1" bbox="50.000,598.517,314.528,697.733">
<textline bbox="50.000,598.517,314.528,697.733">
<text font="OWDOPW+Georgia" bbox="50.000,598.517,104.432,697.733" size="99.216">U</text>
<text font="OWDOPW+Georgia" bbox="104.454,598.517,147.006,697.733" size="99.216">n</text>
<text font="OWDOPW+Georgia" bbox="146.991,598.517,171.831,697.733" size="99.216">t</text>
<text font="OWDOPW+Georgia" bbox="171.846,598.517,192.942,697.733" size="99.216">i</text>
<text font="OWDOPW+Georgia" bbox="192.942,598.517,217.782,697.733" size="99.216">t</text>
<text font="OWDOPW+Georgia" bbox="217.796,598.517,238.388,697.733" size="99.216">l</text>
<text font="OWDOPW+Georgia" bbox="238.395,598.517,273.171,697.733" size="99.216">e</text>
<text font="OWDOPW+Georgia" bbox="273.200,598.517,314.528,697.733" size="99.216">d</text>
<text>
</text>
</textline>
</textbox>
<textbox id="2" bbox="66.250,478.004,181.273,502.808">
<textline bbox="66.250,478.004,181.273,502.808">
<text font="OWDOPW+Georgia" bbox="66.250,478.004,77.122,502.808" size="24.804">L</text>
<text font="OWDOPW+Georgia" bbox="78.013,478.793,88.727,498.636" size="19.843">O</text>
<text font="OWDOPW+Georgia" bbox="89.628,478.793,99.737,498.636" size="19.843">R</text>
<text font="OWDOPW+Georgia" bbox="100.639,478.793,110.042,498.636" size="19.843">E</text>
<text font="OWDOPW+Georgia" bbox="110.943,478.793,124.292,498.636" size="19.843">M</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="125.193,478.793,128.664,498.636" size="19.843"> </text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="129.566,478.004,136.586,502.808" size="24.804">I</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="137.480,478.793,146.264,498.636" size="19.843">P</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="147.163,478.793,155.241,498.636" size="19.843">S</text>
<text font="OWDOPW+Georgia" bbox="156.140,478.793,167.026,498.636" size="19.843">U</text>
<text font="OWDOPW+Georgia" bbox="167.925,478.793,181.273,498.636" size="19.843">M</text>
<text>
</text>
</textline>
</textbox>
</page>
</pages>
    """
    soup = BeautifulSoup(file)
    p = page(soup.pages.page)
    print ("[%s] json[%s]" % (p, p.toDict()))
