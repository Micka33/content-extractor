from cStringIO import StringIO
from bs4 import BeautifulSoup
from page import page
import json

class book(object):

    _pages = []

    @property
    def pages(self):
        return self._pages

    def __init__(self, file):
        soup = BeautifulSoup(file)
        #
        xml = soup.find_all('page')
        self._pages = []
        for p in xml:
            self._pages.append(page(p))

    def toDict(self):
        array = {'pages': []}
        for p in self._pages:
            array['pages'].append(p.toDict())
        return array

    def toJson(self):
        return json.dumps(self.toDict())

    def __str__(self):
        string = StringIO()
        count = 0
        for p in self._pages:
            if count != 0:
                string.write('NEW PAGE')
            string.write(str(p))
            count = 1
        return string.getvalue()























if __name__ == '__main__':
    import sys
    file="""<?xml version="1.0" encoding="utf-8" ?>
<pages>
<page id="1" bbox="0.000,0.000,1024.000,748.000" rotate="0">
<textbox id="0" bbox="263.163,702.557,365.297,721.036">
<textline bbox="263.163,702.557,365.297,721.036">
<text font="OWDOPW+Georgia" bbox="263.163,702.557,271.263,721.036" size="18.479">L</text>
<text font="OWDOPW+Georgia" bbox="271.927,702.557,281.904,721.036" size="18.479">O</text>
<text font="OWDOPW+Georgia" bbox="282.582,702.557,291.996,721.036" size="18.479">R</text>
<text font="OWDOPW+Georgia" bbox="292.659,702.557,301.416,721.036" size="18.479">E</text>
<text font="OWDOPW+Georgia" bbox="302.094,702.557,314.525,721.036" size="18.479">M</text>
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
<textbox id="1" bbox="263.163,607.208,587.501,705.765">
<textline bbox="263.163,607.208,587.501,705.765">
<text font="OWDOPW+Georgia" bbox="263.163,607.208,309.939,705.765" size="98.557">B</text>
<text font="OWDOPW+Georgia" bbox="309.924,607.208,348.475,705.765" size="98.557">o</text>
<text font="OWDOPW+Georgia" bbox="348.482,607.208,387.032,705.765" size="98.557">o</text>
<text font="OWDOPW+Georgia" bbox="387.039,607.208,425.375,705.765" size="98.557">k</text>
<text font="OWDOPW+Georgia" bbox="425.346,607.208,442.583,705.765" size="98.557"> </text>
<text font="OWDOPW+Georgia" bbox="442.598,607.208,486.870,705.765" size="98.557">T</text>
<text font="OWDOPW+Georgia" bbox="486.848,607.208,507.804,705.765" size="98.557">i</text>
<text font="OWDOPW+Georgia" bbox="507.804,607.208,532.479,705.765" size="98.557">t</text>
<text font="OWDOPW+Georgia" bbox="532.493,607.208,552.949,705.765" size="98.557">l</text>
<text font="OWDOPW+Georgia" bbox="552.956,607.208,587.501,705.765" size="98.557">e</text>
<text>
</text>
</textline>
</textbox>
<textbox id="2" bbox="263.163,20.863,360.968,35.236">
<textline bbox="263.163,20.863,360.968,35.236">
<text font="OWDOPW+Georgia" bbox="263.163,20.863,270.976,35.236" size="14.373">D</text>
<text font="OWDOPW+Georgia" bbox="271.497,20.863,279.257,35.236" size="14.373">O</text>
<text font="OWDOPW+Georgia" bbox="279.779,20.863,286.079,35.236" size="14.373">L</text>
<text font="OWDOPW+Georgia" bbox="286.590,20.863,294.350,35.236" size="14.373">O</text>
<text font="OWDOPW+Georgia" bbox="294.871,20.863,302.194,35.236" size="14.373">R</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="302.715,20.863,305.229,35.236" size="14.373"> </text>
<text font="OWDOPW+Georgia" bbox="305.750,20.863,311.602,35.236" size="14.373">S</text>
<text font="OWDOPW+Georgia" bbox="312.123,20.863,318.934,35.236" size="14.373">E</text>
<text font="OWDOPW+Georgia" bbox="319.456,20.863,325.912,35.236" size="14.373">T</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="326.433,20.863,328.947,35.236" size="14.373"> </text>
<text font="OWDOPW+Georgia" bbox="329.469,20.863,336.467,35.236" size="14.373">A</text>
<text font="OWDOPW+Georgia" bbox="336.989,20.863,346.658,35.236" size="14.373">M</text>
<text font="OWDOPW+Georgia" bbox="347.179,20.863,353.990,35.236" size="14.373">E</text>
<text font="OWDOPW+Georgia" bbox="354.512,20.863,360.968,35.236" size="14.373">T</text>
<text>
</text>
</textline>
</textbox>
<rect linewidth="0" bbox="225.912,-0.000,798.912,748.000" />
<rect linewidth="0" bbox="225.912,-0.000,798.088,748.000" />
<figure name="Im1" bbox="237.000,59.000,788.000,506.000">
<image width="551" height="447" />
</figure>
<line linewidth="0" bbox="263.163,698.084,762.327,698.084" />
<layout>
<textgroup bbox="263.163,20.863,587.501,721.036">
<textgroup bbox="263.163,607.208,587.501,721.036">
<textbox id="0" bbox="263.163,702.557,365.297,721.036" />
<textbox id="1" bbox="263.163,607.208,587.501,705.765" />
</textgroup>
<textbox id="2" bbox="263.163,20.863,360.968,35.236" />
</textgroup>
</layout>
</page>
<page id="2" bbox="0.000,0.000,1024.000,748.000" rotate="0">
<textbox id="0" bbox="50.000,687.004,138.569,711.808">
<textline bbox="50.000,687.004,138.569,711.808">
<text font="OWDOPW+Georgia" bbox="50.000,687.004,61.556,711.808" size="24.804">C</text>
<text font="OWDOPW+Georgia" bbox="62.458,687.793,74.194,707.636" size="19.843">H</text>
<text font="OWDOPW+Georgia" bbox="75.092,687.793,84.755,707.636" size="19.843">A</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="85.653,687.793,94.437,707.636" size="19.843">P</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="95.336,687.793,104.249,707.636" size="19.843">T</text>
<text font="OWDOPW+Georgia" bbox="105.148,687.793,114.551,707.636" size="19.843">E</text>
<text font="OWDOPW+Georgia" bbox="115.450,687.793,125.558,707.636" size="19.843">R</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="126.457,687.793,129.927,707.636" size="19.843"> </text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="130.829,687.004,138.569,711.808" size="24.804">1</text>
<text>
</text>
</textline>
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
<textbox id="2" bbox="50.000,40.406,489.850,269.078">
<textline bbox="50.000,236.006,485.115,269.078">
<text font="OWDOPW+Georgia" bbox="50.000,236.006,64.496,269.078" size="33.072">L</text>
<text font="OWDOPW+Georgia" bbox="64.484,236.006,77.420,269.078" size="33.072">o</text>
<text font="OWDOPW+Georgia" bbox="77.422,236.006,87.262,269.078" size="33.072">r</text>
<text font="OWDOPW+Georgia" bbox="87.255,236.006,98.847,269.078" size="33.072">e</text>
<text font="OWDOPW+Georgia" bbox="98.857,236.006,120.001,269.078" size="33.072">m</text>
<text font="OWDOPW+Georgia" bbox="119.998,236.006,125.782,269.078" size="33.072"> </text>
<text font="OWDOPW+Georgia" bbox="125.787,236.006,132.819,269.078" size="33.072">i</text>
<text font="OWDOPW+Georgia" bbox="132.819,236.006,146.523,269.078" size="33.072">p</text>
<text font="OWDOPW+Georgia" bbox="146.530,236.006,156.898,269.078" size="33.072">s</text>
<text font="OWDOPW+Georgia" bbox="156.901,236.006,170.701,269.078" size="33.072">u</text>
<text font="OWDOPW+Georgia" bbox="170.706,236.006,191.850,269.078" size="33.072">m</text>
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
<rect linewidth="0" bbox="0.000,0.000,1024.000,748.000" />
<rect linewidth="0" bbox="0.000,0.000,1024.000,748.000" />
<line linewidth="0" bbox="512.000,40.000,512.000,708.000" />
<figure name="Im1" bbox="332.000,40.000,1178.000,708.000">
<image width="846" height="668" />
</figure>
<line linewidth="0" bbox="50.000,680.750,490.000,680.750" />
<line linewidth="1" bbox="276.606,205.638,420.066,205.638" />
<layout>
<textgroup bbox="50.000,40.406,489.850,711.808">
<textgroup bbox="50.000,598.517,314.528,711.808">
<textbox id="0" bbox="50.000,687.004,138.569,711.808" />
<textbox id="1" bbox="50.000,598.517,314.528,697.733" />
</textgroup>
<textbox id="2" bbox="50.000,40.406,489.850,269.078" />
</textgroup>
</layout>
</page>
<page id="3" bbox="0.000,0.000,1024.000,748.000" rotate="0">
<textbox id="0" bbox="50.000,687.004,133.447,711.808">
<textline bbox="50.000,687.004,133.447,711.808">
<text font="OWDOPW+Georgia" bbox="50.000,687.004,60.098,711.808" size="24.804">S</text>
<text font="OWDOPW+Georgia" bbox="60.999,687.793,70.402,707.636" size="19.843">E</text>
<text font="OWDOPW+Georgia" bbox="71.306,687.793,80.551,707.636" size="19.843">C</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="81.455,687.793,90.369,707.636" size="19.843">T</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="91.259,687.793,96.875,707.636" size="19.843">I</text>
<text font="OWDOPW+Georgia" bbox="97.765,687.793,108.478,707.636" size="19.843">O</text>
<text font="OWDOPW+Georgia" bbox="109.383,687.793,120.427,707.636" size="19.843">N</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="121.332,687.793,124.802,707.636" size="19.843"> </text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="125.707,687.004,133.447,711.808" size="24.804">1</text>
<text>
</text>
</textline>
</textbox>
<textbox id="1" bbox="50.000,639.509,182.264,689.117">
<textline bbox="50.000,639.509,182.264,689.117">
<text font="OWDOPW+Georgia" bbox="50.000,639.509,77.216,689.117" size="49.608">U</text>
<text font="OWDOPW+Georgia" bbox="77.227,639.509,98.503,689.117" size="49.608">n</text>
<text font="OWDOPW+Georgia" bbox="98.496,639.509,110.916,689.117" size="49.608">t</text>
<text font="OWDOPW+Georgia" bbox="110.923,639.509,121.471,689.117" size="49.608">i</text>
<text font="OWDOPW+Georgia" bbox="121.471,639.509,133.891,689.117" size="49.608">t</text>
<text font="OWDOPW+Georgia" bbox="133.898,639.509,144.194,689.117" size="49.608">l</text>
<text font="OWDOPW+Georgia" bbox="144.198,639.509,161.586,689.117" size="49.608">e</text>
<text font="OWDOPW+Georgia" bbox="161.600,639.509,182.264,689.117" size="49.608">d</text>
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
<textbox id="3" bbox="66.250,354.404,453.354,464.808">
<textline bbox="66.250,440.004,316.781,464.808">
<text font="OWDOPW+Georgia" bbox="66.250,440.004,73.990,464.808" size="24.804">1</text>
<text font="OWDOPW+Georgia" bbox="73.985,440.004,78.845,464.808" size="24.804">.</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="96.000,440.004,106.872,464.808" size="24.804">L</text>
<text font="OWDOPW+Georgia" bbox="106.863,440.004,116.565,464.808" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="116.567,440.004,123.947,464.808" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="123.941,440.004,132.635,464.808" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="132.643,440.004,148.501,464.808" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="148.499,440.004,152.837,464.808" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="152.840,440.004,158.114,464.808" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="158.114,440.004,168.392,464.808" size="24.804">p</text>
<text font="OWDOPW+Georgia" bbox="168.398,440.004,176.174,464.808" size="24.804">s</text>
<text font="OWDOPW+Georgia" bbox="176.176,440.004,186.526,464.808" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="186.529,440.004,202.387,464.808" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="202.385,440.004,206.723,464.808" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="206.727,440.004,217.059,464.808" size="24.804">d</text>
<text font="OWDOPW+Georgia" bbox="217.063,440.004,226.765,464.808" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="226.766,440.004,231.914,464.808" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="231.916,440.004,241.618,464.808" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="241.620,440.004,249.000,464.808" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="248.995,440.004,253.333,464.808" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="253.336,440.004,261.112,464.808" size="24.804">s</text>
<text font="OWDOPW+Georgia" bbox="261.114,440.004,266.388,464.808" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="266.388,440.004,272.598,464.808" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="272.602,440.004,276.940,464.808" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="276.943,440.004,286.015,464.808" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="286.013,440.004,301.871,464.808" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="301.870,440.004,310.564,464.808" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="310.571,440.004,316.781,464.808" size="24.804">t</text>
<text>
</text>
</textline>
<textline bbox="66.250,404.804,449.036,429.608">
<text font="OWDOPW+Georgia" bbox="66.250,404.804,76.312,429.608" size="24.804">2</text>
<text font="OWDOPW+Georgia" bbox="76.305,404.804,81.165,429.608" size="24.804">.</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="96.000,404.804,107.556,429.608" size="24.804">C</text>
<text font="OWDOPW+Georgia" bbox="107.558,404.804,117.260,429.608" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="117.262,404.804,127.900,429.608" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="127.896,404.804,135.672,429.608" size="24.804">s</text>
<text font="OWDOPW+Georgia" bbox="135.674,404.804,144.368,429.608" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="144.375,404.804,152.547,429.608" size="24.804">c</text>
<text font="OWDOPW+Georgia" bbox="152.549,404.804,158.759,429.608" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="158.762,404.804,167.456,429.608" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="167.464,404.804,173.674,429.608" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="173.677,404.804,184.027,429.608" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="184.031,404.804,191.411,429.608" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="191.405,404.804,195.743,429.608" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="195.747,404.804,204.819,429.608" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="204.817,404.804,215.149,429.608" size="24.804">d</text>
<text font="OWDOPW+Georgia" bbox="215.153,404.804,220.427,429.608" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="220.427,404.804,230.705,429.608" size="24.804">p</text>
<text font="OWDOPW+Georgia" bbox="230.710,404.804,235.984,429.608" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="235.984,404.804,243.760,429.608" size="24.804">s</text>
<text font="OWDOPW+Georgia" bbox="243.762,404.804,249.036,429.608" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="249.036,404.804,257.208,429.608" size="24.804">c</text>
<text font="OWDOPW+Georgia" bbox="257.210,404.804,262.484,429.608" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="262.484,404.804,273.122,429.608" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="273.118,404.804,282.280,429.608" size="24.804">g</text>
<text font="OWDOPW+Georgia" bbox="282.286,404.804,286.624,429.608" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="286.627,404.804,295.321,429.608" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="295.328,404.804,300.476,429.608" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="300.478,404.804,305.752,429.608" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="305.752,404.804,311.962,429.608" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="311.966,404.804,316.826,429.608" size="24.804">,</text>
<text font="OWDOPW+Georgia" bbox="316.817,404.804,321.155,429.608" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="321.158,404.804,328.934,429.608" size="24.804">s</text>
<text font="OWDOPW+Georgia" bbox="328.936,404.804,337.630,429.608" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="337.637,404.804,347.969,429.608" size="24.804">d</text>
<text font="OWDOPW+Georgia" bbox="347.973,404.804,352.311,429.608" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="352.315,404.804,362.647,429.608" size="24.804">d</text>
<text font="OWDOPW+Georgia" bbox="362.650,404.804,372.352,429.608" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="372.354,404.804,376.692,429.608" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="376.696,404.804,385.390,429.608" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="385.397,404.804,390.671,429.608" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="390.671,404.804,401.021,429.608" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="401.024,404.804,408.800,429.608" size="24.804">s</text>
<text font="OWDOPW+Georgia" bbox="408.802,404.804,424.660,429.608" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="424.658,404.804,434.360,429.608" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="434.362,404.804,444.694,429.608" size="24.804">d</text>
<text font="OWDOPW+Georgia" bbox="444.698,404.804,449.036,429.608" size="24.804"> </text>
<text>
</text>
</textline>
<textline bbox="96.000,379.604,453.354,404.408">
<text font="OWDOPW+Georgia" bbox="96.000,379.604,102.210,404.408" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="102.214,379.604,110.908,404.408" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="110.915,379.604,126.773,404.408" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="126.771,379.604,137.049,404.408" size="24.804">p</text>
<text font="OWDOPW+Georgia" bbox="137.054,379.604,146.756,404.408" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="146.758,379.604,154.138,404.408" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="154.133,379.604,158.471,404.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="158.474,379.604,163.748,404.408" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="163.748,379.604,174.386,404.408" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="174.383,379.604,182.555,404.408" size="24.804">c</text>
<text font="OWDOPW+Georgia" bbox="182.557,379.604,187.831,404.408" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="187.831,379.604,198.163,404.408" size="24.804">d</text>
<text font="OWDOPW+Georgia" bbox="198.166,379.604,203.440,404.408" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="203.440,379.604,213.772,404.408" size="24.804">d</text>
<text font="OWDOPW+Georgia" bbox="213.776,379.604,224.126,404.408" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="224.129,379.604,234.767,404.408" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="234.764,379.604,240.974,404.408" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="240.977,379.604,245.315,404.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="245.319,379.604,255.669,404.408" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="255.673,379.604,261.883,404.408" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="261.886,379.604,266.224,404.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="266.228,379.604,271.376,404.408" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="271.378,379.604,280.450,404.408" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="280.448,379.604,290.528,404.408" size="24.804">b</text>
<text font="OWDOPW+Georgia" bbox="290.530,379.604,300.232,404.408" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="300.233,379.604,307.613,404.408" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="307.608,379.604,316.302,404.408" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="316.309,379.604,320.647,404.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="320.651,379.604,329.345,404.408" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="329.352,379.604,335.562,404.408" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="335.566,379.604,339.904,404.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="339.907,379.604,350.239,404.408" size="24.804">d</text>
<text font="OWDOPW+Georgia" bbox="350.243,379.604,359.945,404.408" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="359.947,379.604,365.095,404.408" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="365.096,379.604,374.798,404.408" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="374.800,379.604,382.180,404.408" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="382.175,379.604,390.869,404.408" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="390.876,379.604,395.214,404.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="395.218,379.604,411.076,404.408" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="411.074,379.604,420.146,404.408" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="420.144,379.604,429.306,404.408" size="24.804">g</text>
<text font="OWDOPW+Georgia" bbox="429.311,379.604,439.949,404.408" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="439.946,379.604,449.018,404.408" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="449.016,379.604,453.354,404.408" size="24.804"> </text>
<text>
</text>
</textline>
<textline bbox="96.000,354.404,154.180,379.208">
<text font="OWDOPW+Georgia" bbox="96.000,354.404,105.072,379.208" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="105.070,354.404,110.218,379.208" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="110.220,354.404,115.494,379.208" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="115.494,354.404,125.574,379.208" size="24.804">q</text>
<text font="OWDOPW+Georgia" bbox="125.567,354.404,135.917,379.208" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="135.920,354.404,144.992,379.208" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="144.991,354.404,149.851,379.208" size="24.804">.</text>
<text font="OWDOPW+Georgia" bbox="149.842,354.404,154.180,379.208" size="24.804"> </text>
<text>
</text>
</textline>
</textbox>
<textbox id="4" bbox="66.250,268.804,450.208,344.008">
<textline bbox="66.250,319.204,450.208,344.008">
<text font="OWDOPW+Georgia" bbox="66.250,319.204,76.186,344.008" size="24.804">3</text>
<text font="OWDOPW+Georgia" bbox="76.182,319.204,81.042,344.008" size="24.804">.</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="96.000,319.204,109.608,344.008" size="24.804">U</text>
<text font="OWDOPW+Georgia" bbox="109.613,319.204,115.823,344.008" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="115.827,319.204,120.165,344.008" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="120.169,319.204,128.863,344.008" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="128.870,319.204,139.508,344.008" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="139.504,319.204,144.778,344.008" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="144.778,319.204,160.636,344.008" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="160.634,319.204,164.972,344.008" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="164.976,319.204,174.048,344.008" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="174.046,319.204,184.378,344.008" size="24.804">d</text>
<text font="OWDOPW+Georgia" bbox="184.382,319.204,188.720,344.008" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="188.723,319.204,204.581,344.008" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="204.580,319.204,209.854,344.008" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="209.854,319.204,220.492,344.008" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="220.488,319.204,225.762,344.008" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="225.762,319.204,241.620,344.008" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="241.618,319.204,245.956,344.008" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="245.960,319.204,254.906,344.008" size="24.804">v</text>
<text font="OWDOPW+Georgia" bbox="254.899,319.204,263.593,344.008" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="263.600,319.204,274.238,344.008" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="274.234,319.204,279.508,344.008" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="279.508,319.204,288.580,344.008" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="288.578,319.204,304.436,344.008" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="304.435,319.204,309.295,344.008" size="24.804">,</text>
<text font="OWDOPW+Georgia" bbox="309.286,319.204,313.624,344.008" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="313.627,319.204,323.707,344.008" size="24.804">q</text>
<text font="OWDOPW+Georgia" bbox="323.700,319.204,334.050,344.008" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="334.054,319.204,339.328,344.008" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="339.328,319.204,347.104,344.008" size="24.804">s</text>
<text font="OWDOPW+Georgia" bbox="347.105,319.204,351.443,344.008" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="351.447,319.204,360.141,344.008" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="360.148,319.204,369.238,344.008" size="24.804">x</text>
<text font="OWDOPW+Georgia" bbox="369.236,319.204,377.930,344.008" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="377.938,319.204,385.318,344.008" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="385.312,319.204,393.484,344.008" size="24.804">c</text>
<text font="OWDOPW+Georgia" bbox="393.486,319.204,398.760,344.008" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="398.760,319.204,404.970,344.008" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="404.974,319.204,414.046,344.008" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="414.044,319.204,420.254,344.008" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="420.257,319.204,425.531,344.008" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="425.531,319.204,435.233,344.008" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="435.235,319.204,445.873,344.008" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="445.870,319.204,450.208,344.008" size="24.804"> </text>
<text>
</text>
</textline>
<textline bbox="96.000,294.004,442.405,318.808">
<text font="OWDOPW+Georgia" bbox="96.000,294.004,106.350,318.808" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="106.354,294.004,111.502,318.808" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="111.503,294.004,116.651,318.808" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="116.653,294.004,125.725,318.808" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="125.723,294.004,141.581,318.808" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="141.580,294.004,149.752,318.808" size="24.804">c</text>
<text font="OWDOPW+Georgia" bbox="149.753,294.004,159.455,318.808" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="159.457,294.004,163.795,318.808" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="163.799,294.004,168.947,318.808" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="168.949,294.004,178.021,318.808" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="178.019,294.004,188.099,318.808" size="24.804">b</text>
<text font="OWDOPW+Georgia" bbox="188.101,294.004,197.803,318.808" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="197.804,294.004,205.184,318.808" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="205.179,294.004,210.453,318.808" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="210.453,294.004,218.229,318.808" size="24.804">s</text>
<text font="OWDOPW+Georgia" bbox="218.231,294.004,222.569,318.808" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="222.572,294.004,233.210,318.808" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="233.207,294.004,238.481,318.808" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="238.481,294.004,246.257,318.808" size="24.804">s</text>
<text font="OWDOPW+Georgia" bbox="246.259,294.004,251.533,318.808" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="251.533,294.004,255.871,318.808" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="255.874,294.004,266.224,318.808" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="266.228,294.004,272.438,318.808" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="272.441,294.004,276.779,318.808" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="276.783,294.004,285.855,318.808" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="285.853,294.004,291.001,318.808" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="291.003,294.004,296.277,318.808" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="296.277,294.004,306.357,318.808" size="24.804">q</text>
<text font="OWDOPW+Georgia" bbox="306.350,294.004,316.700,318.808" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="316.703,294.004,321.977,318.808" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="321.977,294.004,332.255,318.808" size="24.804">p</text>
<text font="OWDOPW+Georgia" bbox="332.261,294.004,336.599,318.808" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="336.602,294.004,345.296,318.808" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="345.304,294.004,354.394,318.808" size="24.804">x</text>
<text font="OWDOPW+Georgia" bbox="354.392,294.004,358.730,318.808" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="358.733,294.004,366.905,318.808" size="24.804">c</text>
<text font="OWDOPW+Georgia" bbox="366.907,294.004,376.609,318.808" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="376.611,294.004,392.469,318.808" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="392.467,294.004,408.325,318.808" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="408.323,294.004,418.025,318.808" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="418.027,294.004,428.359,318.808" size="24.804">d</text>
<text font="OWDOPW+Georgia" bbox="428.363,294.004,438.065,318.808" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="438.067,294.004,442.405,318.808" size="24.804"> </text>
<text>
</text>
</textline>
<textline bbox="96.000,268.804,185.874,293.608">
<text font="OWDOPW+Georgia" bbox="96.000,268.804,104.172,293.608" size="24.804">c</text>
<text font="OWDOPW+Georgia" bbox="104.174,268.804,113.876,293.608" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="113.878,268.804,124.516,293.608" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="124.517,268.804,132.293,293.608" size="24.804">s</text>
<text font="OWDOPW+Georgia" bbox="132.295,268.804,140.989,293.608" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="140.991,268.804,151.071,293.608" size="24.804">q</text>
<text font="OWDOPW+Georgia" bbox="151.055,268.804,161.405,293.608" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="161.407,268.804,170.479,293.608" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="170.480,268.804,176.690,293.608" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="176.692,268.804,181.552,293.608" size="24.804">.</text>
<text font="OWDOPW+Georgia" bbox="181.536,268.804,185.874,293.608" size="24.804"> </text>
<text>
</text>
</textline>
</textbox>
<textbox id="5" bbox="66.250,233.604,461.323,258.408">
<textline bbox="66.250,233.604,461.323,258.408">
<text font="OWDOPW+Georgia" bbox="66.250,233.604,76.420,258.408" size="24.804">4</text>
<text font="OWDOPW+Georgia" bbox="76.418,233.604,81.278,258.408" size="24.804">.</text>
<text> </text>
<text font="OWDOPW+Georgia" bbox="96.000,233.604,109.482,258.408" size="24.804">D</text>
<text font="OWDOPW+Georgia" bbox="109.482,233.604,119.832,258.408" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="119.836,233.604,125.110,258.408" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="125.110,233.604,132.886,258.408" size="24.804">s</text>
<text font="OWDOPW+Georgia" bbox="132.887,233.604,137.225,258.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="137.229,233.604,146.301,258.408" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="146.299,233.604,156.649,258.408" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="156.653,233.604,162.863,258.408" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="162.866,233.604,171.560,258.408" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="171.568,233.604,175.906,258.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="175.909,233.604,181.183,258.408" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="181.183,233.604,188.563,258.408" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="188.558,233.604,198.908,258.408" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="198.911,233.604,206.291,258.408" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="206.286,233.604,214.980,258.408" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="214.987,233.604,219.325,258.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="219.329,233.604,229.661,258.408" size="24.804">d</text>
<text font="OWDOPW+Georgia" bbox="229.664,233.604,239.366,258.408" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="239.368,233.604,244.516,258.408" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="244.518,233.604,254.220,258.408" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="254.222,233.604,261.602,258.408" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="261.596,233.604,265.934,258.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="265.938,233.604,271.212,258.408" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="271.212,233.604,281.850,258.408" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="281.846,233.604,286.184,258.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="286.188,233.604,291.462,258.408" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="291.462,233.604,302.100,258.408" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="302.096,233.604,306.434,258.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="306.438,233.604,315.384,258.408" size="24.804">v</text>
<text font="OWDOPW+Georgia" bbox="315.377,233.604,325.079,258.408" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="325.081,233.604,330.229,258.408" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="330.230,233.604,340.580,258.408" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="340.584,233.604,350.862,258.408" size="24.804">p</text>
<text font="OWDOPW+Georgia" bbox="350.867,233.604,357.077,258.408" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="357.081,233.604,366.153,258.408" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="366.151,233.604,372.361,258.408" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="372.365,233.604,381.059,258.408" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="381.066,233.604,385.404,258.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="385.408,233.604,394.354,258.408" size="24.804">v</text>
<text font="OWDOPW+Georgia" bbox="394.346,233.604,403.040,258.408" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="403.048,233.604,408.196,258.408" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="408.197,233.604,413.471,258.408" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="413.471,233.604,419.681,258.408" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="419.685,233.604,424.023,258.408" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="424.027,233.604,432.721,258.408" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="432.728,233.604,440.504,258.408" size="24.804">s</text>
<text font="OWDOPW+Georgia" bbox="440.506,233.604,448.282,258.408" size="24.804">s</text>
<text font="OWDOPW+Georgia" bbox="448.283,233.604,456.977,258.408" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="456.985,233.604,461.323,258.408" size="24.804"> </text>
<text>
</text>
</textline>
</textbox>
<textbox id="6" bbox="96.000,208.404,398.182,233.208">
<textline bbox="96.000,208.404,398.182,233.208">
<text font="OWDOPW+Georgia" bbox="96.000,208.404,104.172,233.208" size="24.804">c</text>
<text font="OWDOPW+Georgia" bbox="104.174,208.404,109.448,233.208" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="109.448,208.404,114.596,233.208" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="114.598,208.404,119.746,233.208" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="119.747,208.404,130.097,233.208" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="130.101,208.404,145.959,233.208" size="24.804">m</text>
<text font="OWDOPW+Georgia" bbox="145.957,208.404,150.295,233.208" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="150.299,208.404,160.631,233.208" size="24.804">d</text>
<text font="OWDOPW+Georgia" bbox="160.634,208.404,170.336,233.208" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="170.338,208.404,175.486,233.208" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="175.488,208.404,185.190,233.208" size="24.804">o</text>
<text font="OWDOPW+Georgia" bbox="185.192,208.404,192.572,233.208" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="192.566,208.404,201.260,233.208" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="201.268,208.404,205.606,233.208" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="205.609,208.404,214.303,233.208" size="24.804">e</text>
<text font="OWDOPW+Georgia" bbox="214.310,208.404,224.660,233.208" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="224.664,208.404,229.002,233.208" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="229.006,208.404,234.856,233.208" size="24.804">f</text>
<text font="OWDOPW+Georgia" bbox="234.859,208.404,245.209,233.208" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="245.213,208.404,254.375,233.208" size="24.804">g</text>
<text font="OWDOPW+Georgia" bbox="254.380,208.404,259.654,233.208" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="259.654,208.404,268.726,233.208" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="268.724,208.404,274.934,233.208" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="274.938,208.404,279.276,233.208" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="279.280,208.404,289.918,233.208" size="24.804">n</text>
<text font="OWDOPW+Georgia" bbox="289.914,208.404,300.264,233.208" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="300.268,208.404,305.416,233.208" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="305.417,208.404,310.565,233.208" size="24.804">l</text>
<text font="OWDOPW+Georgia" bbox="310.567,208.404,319.639,233.208" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="319.637,208.404,323.975,233.208" size="24.804"> </text>
<text font="OWDOPW+Georgia" bbox="323.979,208.404,334.257,233.208" size="24.804">p</text>
<text font="OWDOPW+Georgia" bbox="334.262,208.404,343.334,233.208" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="343.333,208.404,350.713,233.208" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="350.707,208.404,355.981,233.208" size="24.804">i</text>
<text font="OWDOPW+Georgia" bbox="355.981,208.404,365.053,233.208" size="24.804">a</text>
<text font="OWDOPW+Georgia" bbox="365.051,208.404,371.261,233.208" size="24.804">t</text>
<text font="OWDOPW+Georgia" bbox="371.265,208.404,381.615,233.208" size="24.804">u</text>
<text font="OWDOPW+Georgia" bbox="381.619,208.404,388.999,233.208" size="24.804">r</text>
<text font="OWDOPW+Georgia" bbox="388.993,208.404,393.853,233.208" size="24.804">.</text>
<text font="OWDOPW+Georgia" bbox="393.844,208.404,398.182,233.208" size="24.804"> </text>
<text>
</text>
</textline>
</textbox>
<textbox id="7" bbox="533.000,461.004,974.035,711.052">
<textline bbox="533.000,689.004,974.035,711.052">
<text font="OWDOPW+Georgia" bbox="533.000,689.004,542.664,711.052" size="22.048">L</text>
<text font="OWDOPW+Georgia" bbox="542.656,689.004,551.280,711.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="551.282,689.004,557.842,711.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="557.837,689.004,565.565,711.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="565.571,689.004,579.667,711.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="579.666,689.004,583.522,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="583.525,689.004,588.213,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="588.213,689.004,597.349,711.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="597.354,689.004,604.266,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="604.267,689.004,613.467,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="613.470,689.004,627.566,711.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="627.565,689.004,631.421,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="631.424,689.004,640.608,711.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="640.611,689.004,649.235,711.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="649.237,689.004,653.813,711.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="653.814,689.004,662.438,711.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="662.440,689.004,669.000,711.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="668.995,689.004,672.851,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="672.854,689.004,679.766,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="679.768,689.004,684.456,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="684.456,689.004,689.976,711.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="689.979,689.004,693.835,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="693.838,689.004,701.902,711.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="701.901,689.004,715.997,711.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="715.995,689.004,723.723,711.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="723.730,689.004,729.250,711.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="729.253,689.004,733.573,711.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="733.565,689.004,737.421,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="737.424,689.004,742.000,711.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="742.002,689.004,746.690,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="746.690,689.004,754.834,711.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="754.838,689.004,764.038,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="764.042,689.004,768.618,711.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="768.619,689.004,776.683,711.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="776.682,689.004,780.538,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="780.541,689.004,787.453,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="787.454,689.004,796.654,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="796.658,689.004,803.570,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="803.571,689.004,812.707,711.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="812.712,689.004,820.440,711.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="820.446,689.004,829.902,711.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="829.899,689.004,839.083,711.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="839.086,689.004,843.774,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="843.774,689.004,850.686,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="850.688,689.004,857.600,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="857.602,689.004,865.330,711.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="865.336,689.004,869.192,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="869.195,689.004,878.651,711.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="878.648,689.004,887.848,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="887.851,689.004,892.427,711.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="892.429,689.004,897.005,711.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="897.006,689.004,905.070,711.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="905.069,689.004,908.925,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="908.928,689.004,918.064,711.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="918.069,689.004,924.629,711.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="924.624,689.004,932.352,711.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="932.358,689.004,937.878,711.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="937.882,689.004,942.570,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="942.570,689.004,951.770,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="951.773,689.004,965.869,711.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="965.867,689.004,970.187,711.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="970.179,689.004,974.035,711.052" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,666.204,969.851,688.252">
<text font="OWDOPW+Georgia" bbox="533.000,666.204,539.560,688.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="539.555,666.204,548.867,688.252" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="548.867,666.204,557.491,688.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="557.493,666.204,566.949,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="566.946,666.204,574.210,688.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="574.211,666.204,583.411,688.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="583.414,666.204,590.326,688.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="590.328,666.204,594.184,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="594.187,666.204,599.707,688.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="599.710,666.204,607.438,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="607.445,666.204,621.541,688.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="621.539,666.204,630.675,688.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="630.680,666.204,639.304,688.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="639.306,666.204,645.866,688.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="645.861,666.204,649.717,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="649.720,666.204,658.856,688.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="658.861,666.204,663.437,688.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="663.438,666.204,671.502,688.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="671.501,666.204,678.765,688.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="678.766,666.204,686.494,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="686.501,666.204,693.061,688.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="693.056,666.204,701.120,688.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="701.118,666.204,706.638,688.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="706.642,666.204,710.498,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="710.501,666.204,715.701,688.252" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="715.704,666.204,723.432,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="723.438,666.204,729.998,688.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="729.994,666.204,744.090,688.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="744.088,666.204,751.816,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="751.822,666.204,761.278,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="761.275,666.204,766.795,688.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="766.798,666.204,775.998,688.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="776.002,666.204,790.098,688.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="790.096,666.204,794.416,688.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="794.408,666.204,798.264,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="798.267,666.204,805.995,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="806.002,666.204,815.458,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="815.454,666.204,820.142,688.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="820.142,666.204,834.238,688.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="834.237,666.204,838.093,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="838.096,666.204,842.784,688.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="842.784,666.204,852.240,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="852.237,666.204,857.757,688.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="857.760,666.204,865.488,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="865.494,666.204,873.638,688.252" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="873.643,666.204,881.371,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="881.378,666.204,887.938,688.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="887.933,666.204,891.789,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="891.792,666.204,899.856,688.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="899.854,666.204,909.038,688.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="909.042,666.204,912.898,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="912.901,666.204,920.853,688.252" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="920.846,666.204,928.574,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="928.581,666.204,935.493,688.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="935.494,666.204,941.014,688.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="941.018,666.204,945.706,688.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="945.706,666.204,954.666,688.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="954.667,666.204,963.867,688.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="963.867,666.204,969.851,688.252" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,643.404,940.275,665.452">
<text font="OWDOPW+Georgia" bbox="533.000,643.404,537.576,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="537.578,643.404,546.778,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="546.781,643.404,560.877,665.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="560.875,643.404,564.731,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="564.734,643.404,572.686,665.452" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="572.680,643.404,581.304,665.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="581.306,643.404,585.882,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="585.883,643.404,595.083,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="595.086,643.404,600.606,665.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="600.610,643.404,609.746,665.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="609.750,643.404,617.814,665.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="617.813,643.404,623.333,665.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="623.336,643.404,627.656,665.452" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="627.648,643.404,631.504,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="631.507,643.404,643.779,665.452" size="22.048">N</text>
<text font="OWDOPW+Georgia" bbox="643.781,643.404,648.469,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="648.469,643.404,655.381,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="655.382,643.404,659.958,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="659.960,643.404,663.816,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="663.819,643.404,670.379,665.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="670.374,643.404,679.686,665.452" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="679.686,643.404,688.310,665.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="688.312,643.404,697.768,665.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="697.765,643.404,705.029,665.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="705.030,643.404,714.230,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="714.234,643.404,721.146,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="721.147,643.404,725.003,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="725.006,643.404,730.526,665.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="730.530,643.404,739.730,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="739.733,643.404,746.293,665.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="746.288,643.404,755.424,665.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="755.429,643.404,760.117,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="760.117,643.404,767.029,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="767.030,643.404,770.886,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="770.890,643.404,778.618,665.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="778.624,643.404,785.536,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="785.538,643.404,791.058,665.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="791.061,643.404,795.381,665.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="795.373,643.404,799.229,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="799.232,643.404,807.184,665.452" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="807.178,643.404,814.906,665.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="814.912,643.404,819.488,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="819.490,643.404,823.346,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="823.349,643.404,831.077,665.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="831.083,643.404,835.659,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="835.661,643.404,840.349,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="840.349,643.404,845.869,665.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="845.872,643.404,850.192,665.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="850.184,643.404,854.040,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="854.043,643.404,861.307,665.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="861.309,643.404,869.933,665.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="869.934,643.404,879.390,665.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="879.387,643.404,887.531,665.452" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="887.536,643.404,896.736,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="896.739,643.404,904.467,665.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="904.474,643.404,908.330,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="908.333,643.404,920.125,665.452" size="22.048">w</text>
<text font="OWDOPW+Georgia" bbox="920.130,643.404,924.818,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="924.818,643.404,931.730,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="931.731,643.404,936.419,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="936.419,643.404,940.275,665.452" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,620.604,958.619,642.652">
<text font="OWDOPW+Georgia" bbox="533.000,620.604,540.728,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="540.734,620.604,550.190,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="550.187,620.604,554.875,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="554.875,620.604,568.971,642.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="568.970,620.604,572.826,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="572.829,620.604,582.285,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="582.282,620.604,591.482,642.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="591.485,620.604,600.941,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="600.938,620.604,608.202,642.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="608.203,620.604,612.059,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="612.062,620.604,621.262,642.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="621.266,620.604,625.842,642.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="625.843,620.604,631.363,642.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="631.366,620.604,637.926,642.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="637.922,620.604,642.610,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="642.610,620.604,649.874,642.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="649.875,620.604,654.563,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="654.563,620.604,662.291,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="662.298,620.604,669.210,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="669.211,620.604,673.067,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="673.070,620.604,679.982,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="679.984,620.604,684.672,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="684.672,620.604,690.192,642.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="690.195,620.604,694.515,642.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="694.507,620.604,698.363,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="698.366,620.604,712.462,642.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="712.461,620.604,720.525,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="720.523,620.604,728.667,642.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="728.672,620.604,738.128,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="738.125,620.604,746.189,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="746.187,620.604,750.043,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="750.046,620.604,755.566,642.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="755.570,620.604,760.258,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="760.258,620.604,769.714,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="769.710,620.604,776.974,642.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="776.976,620.604,781.664,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="781.664,620.604,790.848,642.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="790.851,620.604,800.051,642.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="800.054,620.604,809.510,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="809.507,620.604,815.027,642.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="815.030,620.604,819.350,642.652" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="819.342,620.604,823.198,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="823.202,620.604,838.034,642.652" size="22.048">M</text>
<text font="OWDOPW+Georgia" bbox="838.037,620.604,846.101,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="846.099,620.604,853.827,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="853.834,620.604,861.098,642.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="861.099,620.604,868.827,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="868.834,620.604,878.290,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="878.286,620.604,886.350,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="886.349,620.604,893.261,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="893.262,620.604,897.118,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="897.122,620.604,905.186,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="905.184,620.604,909.760,642.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="909.762,620.604,914.450,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="914.450,620.604,923.410,642.652" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="923.403,620.604,932.603,642.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="932.606,620.604,940.670,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="940.669,620.604,954.765,642.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="954.763,620.604,958.619,642.652" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,597.804,970.476,619.852">
<text font="OWDOPW+Georgia" bbox="533.000,597.804,547.096,619.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="547.094,597.804,555.158,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="555.157,597.804,562.885,619.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="562.891,597.804,570.155,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="570.157,597.804,577.885,619.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="577.891,597.804,587.347,619.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="587.344,597.804,595.408,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="595.406,597.804,602.318,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="602.320,597.804,606.176,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="606.179,597.804,610.755,619.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="610.757,597.804,615.445,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="615.445,597.804,623.589,619.852" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="623.594,597.804,632.794,619.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="632.797,597.804,637.373,619.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="637.374,597.804,645.438,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="645.437,597.804,649.293,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="649.296,597.804,658.752,619.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="658.749,597.804,667.373,619.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="667.374,597.804,674.286,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="674.288,597.804,679.808,619.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="679.811,597.804,686.371,619.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="686.366,597.804,694.430,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="694.429,597.804,698.749,619.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="698.741,597.804,702.597,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="702.600,597.804,710.664,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="710.662,597.804,717.926,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="717.928,597.804,725.192,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="725.194,597.804,734.394,619.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="734.397,597.804,748.493,619.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="748.491,597.804,755.403,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="755.405,597.804,763.469,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="763.467,597.804,772.923,619.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="772.920,597.804,776.776,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="776.779,597.804,782.299,619.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="782.302,597.804,790.366,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="790.365,597.804,797.629,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="797.630,597.804,802.318,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="802.318,597.804,807.838,619.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="807.842,597.804,812.530,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="812.530,597.804,816.850,619.852" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="816.842,597.804,820.698,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="820.701,597.804,829.677,619.852" size="22.048">S</text>
<text font="OWDOPW+Georgia" bbox="829.677,597.804,838.301,619.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="838.302,597.804,845.566,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="845.568,597.804,850.256,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="850.256,597.804,854.944,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="854.944,597.804,861.856,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="861.858,597.804,865.714,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="865.717,597.804,879.813,619.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="879.811,597.804,887.875,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="887.874,597.804,897.074,619.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="897.077,597.804,903.637,619.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="903.632,597.804,908.320,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="908.320,597.804,915.232,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="915.234,597.804,919.090,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="919.093,597.804,923.781,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="923.781,597.804,933.237,619.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="933.234,597.804,937.090,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="937.093,597.804,941.781,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="941.781,597.804,951.237,619.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="951.234,597.804,956.754,619.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="956.757,597.804,964.485,619.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="964.492,597.804,970.476,619.852" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,575.004,963.798,597.052">
<text font="OWDOPW+Georgia" bbox="533.000,575.004,541.144,597.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="541.149,575.004,548.877,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="548.883,575.004,555.443,597.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="555.438,575.004,559.758,597.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="559.750,575.004,563.606,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="563.610,575.004,571.674,597.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="571.672,575.004,575.528,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="575.531,575.004,584.715,597.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="584.718,575.004,593.342,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="593.344,575.004,597.920,597.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="597.922,575.004,606.546,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="606.547,575.004,613.107,597.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="613.102,575.004,616.958,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="616.962,575.004,626.418,597.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="626.414,575.004,634.142,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="634.149,575.004,639.669,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="639.672,575.004,648.872,597.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="648.875,575.004,655.787,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="655.789,575.004,659.645,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="659.648,575.004,669.104,597.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="669.101,575.004,677.725,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="677.726,575.004,687.182,597.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="687.179,575.004,691.035,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="691.038,575.004,700.222,597.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="700.226,575.004,709.426,597.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="709.429,575.004,714.117,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="714.117,575.004,717.973,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="717.976,575.004,726.040,597.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="726.038,575.004,730.614,597.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="730.616,575.004,735.304,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="735.304,575.004,744.264,597.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="744.258,575.004,753.458,597.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="753.461,575.004,761.189,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="761.195,575.004,766.715,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="766.718,575.004,771.038,597.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="771.030,575.004,774.886,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="774.890,575.004,781.802,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="781.803,575.004,789.867,597.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="789.866,575.004,798.010,597.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="798.014,575.004,802.702,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="802.702,575.004,808.222,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="808.226,575.004,813.746,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="813.749,575.004,818.437,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="818.437,575.004,825.349,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="825.350,575.004,829.206,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="829.210,575.004,834.410,597.052" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="834.413,575.004,842.141,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="842.147,575.004,846.723,597.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="846.725,575.004,851.413,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="851.413,575.004,858.325,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="858.326,575.004,862.182,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="862.186,575.004,869.098,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="869.099,575.004,877.723,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="877.725,575.004,886.909,597.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="886.912,575.004,894.976,597.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="894.974,575.004,899.550,597.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="899.552,575.004,907.280,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="907.286,575.004,914.198,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="914.200,575.004,918.520,597.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="918.512,575.004,922.368,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="922.371,575.004,931.555,597.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="931.558,575.004,940.182,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="940.184,575.004,944.760,597.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="944.762,575.004,953.386,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="953.387,575.004,959.947,597.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="959.942,575.004,963.798,597.052" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,552.204,950.882,574.252">
<text font="OWDOPW+Georgia" bbox="533.000,552.204,539.912,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="539.914,552.204,548.538,574.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="548.539,552.204,555.803,574.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="555.805,552.204,560.493,574.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="560.493,552.204,565.181,574.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="565.181,552.204,572.093,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="572.094,552.204,575.950,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="575.954,552.204,590.050,574.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="590.048,552.204,598.112,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="598.110,552.204,607.310,574.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="607.314,552.204,613.874,574.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="613.869,552.204,618.557,574.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="618.557,552.204,625.469,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="625.470,552.204,629.790,574.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="629.782,552.204,633.638,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="633.642,552.204,641.594,574.252" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="641.587,552.204,649.315,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="649.322,552.204,653.898,574.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="653.899,552.204,657.755,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="657.758,552.204,665.486,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="665.493,552.204,674.693,574.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="674.696,552.204,678.552,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="678.555,552.204,686.283,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="686.290,552.204,693.202,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="693.203,552.204,698.723,574.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="698.726,552.204,702.582,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="702.586,552.204,707.162,574.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="707.163,552.204,711.851,574.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="711.851,552.204,720.811,574.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="720.813,552.204,728.541,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="728.547,552.204,735.107,574.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="735.102,552.204,743.726,574.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="743.728,552.204,747.584,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="747.587,552.204,754.851,574.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="754.853,552.204,761.413,574.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="761.408,552.204,769.472,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="769.470,552.204,776.382,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="776.384,552.204,780.704,574.252" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="780.696,552.204,784.552,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="784.555,552.204,790.795,574.252" size="22.048">I</text>
<text font="OWDOPW+Georgia" bbox="790.789,552.204,800.245,574.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="800.242,552.204,805.762,574.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="805.765,552.204,813.493,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="813.499,552.204,820.059,574.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="820.054,552.204,829.238,574.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="829.242,552.204,838.442,574.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="838.445,552.204,852.541,574.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="852.539,552.204,856.395,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="856.398,552.204,864.462,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="864.461,552.204,869.981,574.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="869.984,552.204,874.304,574.252" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="874.296,552.204,878.152,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="878.155,552.204,888.603,574.252" size="22.048">E</text>
<text font="OWDOPW+Georgia" bbox="888.608,552.204,896.752,574.252" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="896.757,552.204,904.485,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="904.491,552.204,910.011,574.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="910.014,552.204,913.870,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="913.874,552.204,923.186,574.252" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="923.186,552.204,931.250,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="931.248,552.204,940.208,574.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="940.210,552.204,944.898,574.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="944.898,552.204,950.882,574.252" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,529.404,959.086,551.452">
<text font="OWDOPW+Georgia" bbox="533.000,529.404,538.520,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="538.523,529.404,546.587,551.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="546.586,529.404,553.498,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="553.499,529.404,560.411,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="560.413,529.404,568.141,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="568.147,529.404,572.003,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="572.006,529.404,579.734,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="579.741,529.404,584.317,551.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="584.318,529.404,592.046,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="592.053,529.404,606.149,551.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="606.147,529.404,613.875,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="613.882,529.404,623.338,551.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="623.334,529.404,628.854,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="628.858,529.404,638.058,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="638.061,529.404,652.157,551.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="652.155,529.404,656.011,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="656.014,529.404,663.742,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="663.749,529.404,670.661,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="670.662,529.404,676.182,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="676.186,529.404,680.506,551.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="680.498,529.404,684.354,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="684.357,529.404,689.045,551.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="689.045,529.404,698.181,551.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="698.186,529.404,705.098,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="705.099,529.404,714.299,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="714.302,529.404,728.398,551.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="728.397,529.404,732.253,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="732.256,529.404,741.392,551.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="741.397,529.404,750.597,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="750.600,529.404,757.160,551.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="757.155,529.404,766.355,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="766.358,529.404,773.270,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="773.272,529.404,777.128,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="777.131,529.404,786.267,551.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="786.272,529.404,794.000,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="794.006,529.404,803.190,551.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="803.194,529.404,810.922,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="810.928,529.404,814.784,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="814.787,529.404,823.923,551.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="823.928,529.404,832.552,551.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="832.554,529.404,839.114,551.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="839.109,529.404,844.629,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="844.632,529.404,850.152,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="850.155,529.404,854.843,551.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="854.843,529.404,860.363,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="860.366,529.404,868.990,551.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="868.992,529.404,875.552,551.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="875.547,529.404,879.403,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="879.406,529.404,886.670,551.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="886.672,529.404,891.248,551.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="891.250,529.404,899.314,551.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="899.312,529.404,906.224,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="906.226,529.404,913.138,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="913.139,529.404,917.459,551.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="917.451,529.404,921.307,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="921.310,529.404,930.510,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="930.514,529.404,936.034,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="936.037,529.404,939.893,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="939.896,529.404,944.472,551.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="944.474,529.404,953.098,551.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="953.102,529.404,959.086,551.452" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,506.604,954.680,528.652">
<text font="OWDOPW+Georgia" bbox="533.000,506.604,539.560,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="539.555,506.604,547.283,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="547.290,506.604,561.386,528.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="561.384,506.604,565.240,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="565.243,506.604,573.307,528.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="573.306,506.604,582.490,528.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="582.493,506.604,587.181,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="587.181,506.604,596.317,528.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="596.322,506.604,601.010,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="601.010,506.604,607.922,528.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="607.923,506.604,615.187,528.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="615.189,506.604,619.877,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="619.877,506.604,629.333,528.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="629.330,506.604,637.474,528.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="637.478,506.604,641.798,528.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="641.790,506.604,645.646,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="645.650,506.604,653.714,528.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="653.712,506.604,658.288,528.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="658.290,506.604,662.978,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="662.978,506.604,671.938,528.652" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="671.931,506.604,681.131,528.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="681.134,506.604,688.862,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="688.869,506.604,694.389,528.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="694.392,506.604,698.248,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="698.251,506.604,705.163,528.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="705.165,506.604,712.893,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="712.899,506.604,722.083,528.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="722.086,506.604,725.942,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="725.946,506.604,734.010,528.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="734.008,506.604,743.208,528.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="743.211,506.604,750.475,528.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="750.477,506.604,755.997,528.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="756.000,506.604,764.624,528.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="764.626,506.604,771.186,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="771.181,506.604,775.501,528.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="775.493,506.604,779.349,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="779.352,506.604,784.040,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="784.040,506.604,798.136,528.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="798.134,506.604,807.270,528.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="807.275,506.604,815.003,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="815.010,506.604,821.570,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="821.565,506.604,830.749,528.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="830.752,506.604,835.440,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="835.440,506.604,843.168,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="843.174,506.604,848.694,528.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="848.698,506.604,852.554,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="852.557,506.604,860.621,528.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="860.619,506.604,867.179,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="867.174,506.604,874.438,528.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="874.440,506.604,883.640,528.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="883.643,506.604,887.499,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="887.502,506.604,896.638,528.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="896.643,506.604,904.371,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="904.378,506.604,910.938,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="910.933,506.604,914.789,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="914.792,506.604,923.976,528.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="923.979,506.604,928.667,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="928.667,506.604,936.731,528.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="936.730,506.604,950.826,528.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="950.824,506.604,954.680,528.652" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,483.804,938.820,505.852">
<text font="OWDOPW+Georgia" bbox="533.000,483.804,542.184,505.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="542.187,483.804,550.251,505.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="550.250,483.804,559.386,505.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="559.390,483.804,564.078,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="564.078,483.804,573.038,505.852" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="573.040,483.804,582.240,505.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="582.243,483.804,589.155,505.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="589.157,483.804,593.013,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="593.016,483.804,597.592,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="597.594,483.804,602.282,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="602.282,483.804,611.242,505.852" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="611.243,483.804,618.971,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="618.978,483.804,625.538,505.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="625.533,483.804,634.157,505.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="634.158,483.804,638.014,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="638.018,483.804,647.202,505.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="647.205,483.804,656.405,505.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="656.408,483.804,661.096,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="661.096,483.804,668.008,505.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="668.010,483.804,672.330,505.852" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="672.322,483.804,676.178,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="676.181,483.804,686.629,505.852" size="22.048">E</text>
<text font="OWDOPW+Georgia" bbox="686.634,483.804,696.090,505.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="696.086,483.804,700.774,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="700.774,483.804,714.870,505.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="714.869,483.804,718.725,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="718.728,483.804,726.456,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="726.462,483.804,733.022,505.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="733.018,483.804,741.642,505.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="741.643,483.804,748.555,505.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="748.557,483.804,752.413,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="752.416,483.804,757.104,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="757.104,483.804,766.560,505.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="766.557,483.804,770.413,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="770.416,483.804,778.368,505.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="778.362,483.804,786.090,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="786.096,483.804,790.672,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="790.674,483.804,794.994,505.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="794.986,483.804,798.842,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="798.845,483.804,806.797,505.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="806.790,483.804,815.414,505.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="815.416,483.804,819.992,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="819.994,483.804,829.194,505.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="829.197,483.804,834.717,505.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="834.720,483.804,843.856,505.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="843.861,483.804,851.925,505.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="851.923,483.804,857.443,505.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="857.446,483.804,861.302,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="861.306,483.804,870.762,505.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="870.758,483.804,878.486,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="878.493,483.804,885.757,505.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="885.758,483.804,889.614,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="889.618,483.804,898.754,505.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="898.758,483.804,906.486,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="906.493,483.804,911.069,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="911.070,483.804,915.646,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="915.648,483.804,923.376,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="923.382,483.804,932.838,505.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="932.836,483.804,938.820,505.852" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,461.004,808.235,483.052">
<text font="OWDOPW+Georgia" bbox="533.000,461.004,538.520,483.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="538.523,461.004,546.251,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="546.258,461.004,553.170,483.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="553.171,461.004,562.131,483.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="562.125,461.004,571.325,483.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="571.328,461.004,579.056,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="579.062,461.004,582.918,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="582.922,461.004,587.498,483.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="587.499,461.004,595.227,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="595.234,461.004,603.858,483.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="603.859,461.004,608.179,483.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="608.171,461.004,612.027,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="612.030,461.004,617.550,483.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="617.554,461.004,625.282,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="625.288,461.004,639.384,483.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="639.382,461.004,648.518,483.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="648.523,461.004,657.147,483.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="657.149,461.004,663.709,483.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="663.704,461.004,668.392,483.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="668.392,461.004,677.352,483.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="677.354,461.004,686.554,483.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="686.557,461.004,693.469,483.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="693.470,461.004,697.326,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="697.330,461.004,704.242,483.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="704.243,461.004,711.507,483.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="711.509,461.004,719.237,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="719.243,461.004,723.819,483.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="723.821,461.004,731.549,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="731.555,461.004,738.115,483.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="738.110,461.004,742.798,483.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="742.798,461.004,749.710,483.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="749.712,461.004,758.672,483.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="758.666,461.004,767.866,483.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="767.869,461.004,775.597,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="775.603,461.004,779.459,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="779.462,461.004,788.918,483.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="788.915,461.004,796.643,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="796.650,461.004,803.914,483.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="803.915,461.004,808.235,483.052" size="22.048">.</text>
<text>
</text>
</textline>
</textbox>
<textbox id="8" bbox="533.000,196.204,975.579,446.252">
<textline bbox="533.000,424.204,952.910,446.252">
<text font="OWDOPW+Georgia" bbox="533.000,424.204,543.736,446.252" size="22.048">A</text>
<text font="OWDOPW+Georgia" bbox="543.734,424.204,550.998,446.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="551.000,424.204,554.856,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="554.859,424.204,564.043,446.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="564.046,424.204,572.670,446.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="572.672,424.204,577.248,446.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="577.250,424.204,585.874,446.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="585.875,424.204,592.435,446.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="592.430,424.204,596.286,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="596.290,424.204,604.354,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="604.352,424.204,611.616,446.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="611.618,424.204,615.474,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="615.477,424.204,623.541,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="623.539,424.204,632.723,446.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="632.726,424.204,637.414,446.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="637.414,424.204,646.550,446.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="646.555,424.204,651.243,446.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="651.243,424.204,658.155,446.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="658.157,424.204,665.421,446.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="665.422,424.204,670.110,446.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="670.110,424.204,679.566,446.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="679.563,424.204,687.707,446.252" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="687.712,424.204,691.568,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="691.571,424.204,699.635,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="699.634,424.204,713.730,446.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="713.728,424.204,721.456,446.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="721.462,424.204,726.982,446.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="726.986,424.204,730.842,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="730.845,424.204,739.805,446.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="739.806,424.204,744.494,446.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="744.494,424.204,753.454,446.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="753.456,424.204,761.184,446.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="761.190,424.204,770.646,446.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="770.643,424.204,779.827,446.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="779.830,424.204,789.030,446.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="789.034,424.204,803.130,446.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="803.128,424.204,806.984,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="806.987,424.204,816.443,446.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="816.440,424.204,825.640,446.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="825.643,424.204,830.219,446.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="830.221,424.204,834.797,446.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="834.798,424.204,842.862,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="842.861,424.204,856.957,446.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="856.955,424.204,861.275,446.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="861.267,424.204,865.123,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="865.126,424.204,879.222,446.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="879.221,424.204,887.285,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="887.283,424.204,894.195,446.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="894.197,424.204,901.109,446.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="901.110,424.204,909.174,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="909.173,424.204,913.029,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="913.032,424.204,917.608,446.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="917.610,424.204,925.674,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="925.672,424.204,932.936,446.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="932.938,424.204,942.138,446.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="942.141,424.204,949.053,446.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="949.054,424.204,952.910,446.252" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,401.404,964.691,423.452">
<text font="OWDOPW+Georgia" bbox="533.000,401.404,547.096,423.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="547.094,401.404,555.718,423.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="555.720,401.404,560.296,423.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="560.298,401.404,568.026,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="568.032,401.404,574.944,423.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="574.946,401.404,580.466,423.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="580.469,401.404,585.157,423.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="585.157,401.404,592.885,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="592.891,401.404,596.747,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="596.750,401.404,605.950,423.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="605.954,401.404,611.474,423.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="611.477,401.404,615.333,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="615.336,401.404,619.912,423.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="619.914,401.404,624.602,423.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="624.602,401.404,633.562,423.452" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="633.563,401.404,641.291,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="641.298,401.404,647.858,423.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="647.853,401.404,656.477,423.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="656.478,401.404,660.334,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="660.338,401.404,669.794,423.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="669.790,401.404,677.518,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="677.525,401.404,684.789,423.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="684.790,401.404,689.110,423.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="689.102,401.404,692.958,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="692.962,401.404,702.146,423.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="702.149,401.404,706.837,423.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="706.837,401.404,714.901,423.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="714.899,401.404,728.995,423.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="728.994,401.404,732.850,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="732.853,401.404,740.581,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="740.587,401.404,746.107,423.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="746.110,401.404,750.430,423.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="750.422,401.404,754.278,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="754.282,401.404,763.418,423.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="763.422,401.404,772.734,423.452" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="772.734,401.404,780.798,423.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="780.797,401.404,787.357,423.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="787.352,401.404,795.080,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="795.086,401.404,800.606,423.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="800.610,401.404,807.170,423.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="807.165,401.404,815.229,423.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="815.227,401.404,819.083,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="819.086,401.404,825.998,423.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="826.000,401.404,834.624,423.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="834.626,401.404,843.810,423.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="843.813,401.404,851.877,423.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="851.875,401.404,856.451,423.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="856.453,401.404,864.181,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="864.187,401.404,871.099,423.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="871.101,401.404,874.957,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="874.960,401.404,882.688,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="882.694,401.404,890.838,423.452" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="890.843,401.404,898.571,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="898.578,401.404,904.098,423.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="904.101,401.404,908.421,423.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="908.413,401.404,912.269,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="912.272,401.404,917.472,423.452" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="917.475,401.404,925.203,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="925.210,401.404,934.410,423.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="934.413,401.404,942.557,423.452" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="942.562,401.404,947.250,423.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="947.250,401.404,955.314,423.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="955.312,401.404,960.832,423.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="960.835,401.404,964.691,423.452" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,378.604,937.290,400.652">
<text font="OWDOPW+Georgia" bbox="533.000,378.604,542.200,400.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="542.203,378.604,546.779,400.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="546.781,378.604,551.357,400.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="551.358,378.604,559.422,400.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="559.421,378.604,573.517,400.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="573.515,378.604,580.779,400.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="580.781,378.604,589.405,400.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="589.406,378.604,595.966,400.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="595.962,378.604,605.098,400.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="605.102,378.604,612.830,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="612.837,378.604,619.397,400.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="619.392,378.604,623.248,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="623.251,378.604,627.939,400.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="627.939,378.604,637.123,400.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="637.126,378.604,640.982,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="640.986,378.604,646.506,400.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="646.509,378.604,654.237,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="654.243,378.604,668.339,400.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="668.338,378.604,677.474,400.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="677.478,378.604,686.102,400.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="686.104,378.604,692.664,400.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="692.659,378.604,696.515,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="696.518,378.604,704.246,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="704.253,378.604,712.397,400.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="712.402,378.604,720.130,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="720.136,378.604,725.656,400.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="725.659,378.604,729.515,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="729.518,378.604,734.206,400.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="734.206,378.604,743.390,400.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="743.394,378.604,747.250,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="747.253,378.604,755.205,400.652" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="755.198,378.604,759.886,400.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="759.886,378.604,765.406,400.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="765.410,378.604,773.474,400.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="773.472,378.604,781.200,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="781.206,378.604,785.526,400.652" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="785.518,378.604,789.374,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="789.378,378.604,804.210,400.652" size="22.048">M</text>
<text font="OWDOPW+Georgia" bbox="804.213,378.604,812.277,400.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="812.275,378.604,821.475,400.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="821.478,378.604,828.038,400.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="828.034,378.604,832.722,400.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="832.722,378.604,839.634,400.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="839.635,378.604,843.491,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="843.494,378.604,852.630,400.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="852.635,378.604,859.195,400.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="859.190,378.604,866.918,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="866.925,378.604,872.445,400.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="872.448,378.604,877.136,400.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="877.136,378.604,886.336,400.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="886.339,378.604,900.435,400.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="900.434,378.604,904.290,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="904.293,378.604,912.021,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="912.027,378.604,920.171,400.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="920.176,378.604,927.904,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="927.910,378.604,933.430,400.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="933.434,378.604,937.290,400.652" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,355.804,959.554,377.852">
<text font="OWDOPW+Georgia" bbox="533.000,355.804,541.064,377.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="541.062,355.804,545.638,377.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="545.640,355.804,550.328,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="550.328,355.804,559.288,377.852" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="559.282,355.804,568.482,377.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="568.485,355.804,576.213,377.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="576.219,355.804,581.739,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="581.742,355.804,586.062,377.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="586.054,355.804,589.910,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="589.914,355.804,594.490,377.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="594.491,355.804,602.219,377.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="602.226,355.804,609.490,377.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="609.491,355.804,615.011,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="615.014,355.804,624.214,377.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="624.218,355.804,631.130,377.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="631.131,355.804,634.987,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="634.990,355.804,640.510,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="640.514,355.804,645.202,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="645.202,355.804,654.658,377.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="654.654,355.804,661.918,377.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="661.920,355.804,666.608,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="666.608,355.804,675.792,377.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="675.795,355.804,684.995,377.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="684.998,355.804,694.454,377.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="694.451,355.804,699.971,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="699.974,355.804,704.294,377.852" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="704.286,355.804,708.142,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="708.146,355.804,717.906,377.852" size="22.048">P</text>
<text font="OWDOPW+Georgia" bbox="717.904,355.804,726.528,377.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="726.530,355.804,733.090,377.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="733.085,355.804,738.605,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="738.608,355.804,744.128,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="744.131,355.804,748.819,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="748.819,355.804,754.339,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="754.342,355.804,762.966,377.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="762.968,355.804,769.528,377.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="769.523,355.804,773.379,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="773.382,355.804,787.478,377.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="787.477,355.804,796.101,377.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="796.102,355.804,800.678,377.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="800.680,355.804,805.256,377.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="805.258,355.804,809.946,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="809.946,355.804,816.858,377.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="816.859,355.804,820.715,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="820.718,355.804,825.406,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="825.406,355.804,839.502,377.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="839.501,355.804,848.637,377.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="848.642,355.804,856.370,377.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="856.376,355.804,862.936,377.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="862.931,355.804,872.115,377.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="872.118,355.804,876.806,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="876.806,355.804,884.534,377.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="884.541,355.804,890.061,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="890.064,355.804,893.920,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="893.923,355.804,898.499,377.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="898.501,355.804,903.189,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="903.189,355.804,912.149,377.852" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="912.150,355.804,919.878,377.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="919.885,355.804,926.445,377.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="926.440,355.804,935.064,377.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="935.066,355.804,938.922,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="938.925,355.804,945.837,377.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="945.838,355.804,953.566,377.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="953.570,355.804,959.554,377.852" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,333.004,969.320,355.052">
<text font="OWDOPW+Georgia" bbox="533.000,333.004,542.456,355.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="542.453,333.004,550.181,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="550.187,333.004,557.451,355.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="557.453,333.004,562.973,355.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="562.976,333.004,572.176,355.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="572.179,333.004,579.091,355.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="579.093,333.004,582.949,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="582.952,333.004,592.088,355.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="592.093,333.004,601.293,355.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="601.296,333.004,605.872,355.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="605.874,333.004,613.826,355.052" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="613.819,333.004,618.507,355.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="618.507,333.004,627.963,355.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="627.960,333.004,636.024,355.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="636.022,333.004,642.582,355.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="642.578,333.004,646.898,355.052" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="646.890,333.004,650.746,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="650.749,333.004,661.197,355.052" size="22.048">E</text>
<text font="OWDOPW+Georgia" bbox="661.202,333.004,666.722,355.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="666.725,333.004,671.413,355.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="671.413,333.004,679.477,355.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="679.475,333.004,693.571,355.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="693.570,333.004,697.426,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="697.429,333.004,711.525,355.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="711.523,333.004,720.147,355.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="720.149,333.004,724.725,355.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="724.726,333.004,732.454,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="732.461,333.004,739.373,355.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="739.374,333.004,744.894,355.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="744.898,333.004,749.586,355.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="749.586,333.004,757.314,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="757.320,333.004,761.176,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="761.179,333.004,775.275,355.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="775.274,333.004,783.338,355.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="783.336,333.004,792.536,355.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="792.539,333.004,799.099,355.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="799.094,333.004,803.782,355.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="803.782,333.004,810.694,355.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="810.696,333.004,814.552,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="814.555,333.004,819.131,355.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="819.133,333.004,823.821,355.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="823.821,333.004,831.965,355.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="831.970,333.004,841.170,355.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="841.173,333.004,845.749,355.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="845.750,333.004,853.814,355.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="853.813,333.004,857.669,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="857.672,333.004,865.400,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="865.406,333.004,873.550,355.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="873.555,333.004,881.283,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="881.290,333.004,886.810,355.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="886.813,333.004,890.669,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="890.672,333.004,895.248,355.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="895.250,333.004,903.314,355.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="903.312,333.004,911.936,355.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="911.938,333.004,918.498,355.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="918.493,333.004,926.221,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="926.227,333.004,933.955,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="933.962,333.004,939.482,355.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="939.485,333.004,943.805,355.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="943.797,333.004,947.653,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="947.656,333.004,955.608,355.052" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="955.602,333.004,963.330,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="963.336,333.004,969.320,355.052" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,310.204,956.386,332.252">
<text font="OWDOPW+Georgia" bbox="533.000,310.204,542.312,332.252" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="542.312,310.204,547.000,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="547.000,310.204,554.264,332.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="554.266,310.204,563.466,332.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="563.469,310.204,568.045,332.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="568.046,310.204,576.110,332.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="576.109,310.204,579.965,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="579.968,310.204,587.696,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="587.702,310.204,592.278,332.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="592.280,310.204,600.008,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="600.014,310.204,604.702,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="604.702,310.204,609.902,332.252" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="609.906,310.204,617.634,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="617.640,310.204,627.096,332.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="627.093,310.204,636.277,332.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="636.280,310.204,640.600,332.252" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="640.592,310.204,644.448,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="644.451,310.204,655.683,332.252" size="22.048">R</text>
<text font="OWDOPW+Georgia" bbox="655.678,310.204,663.406,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="663.413,310.204,672.549,332.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="672.554,310.204,680.282,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="680.288,310.204,684.864,332.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="684.866,310.204,689.442,332.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="689.443,310.204,697.507,332.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="697.506,310.204,703.026,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="703.029,310.204,706.885,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="706.888,310.204,715.512,332.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="715.514,310.204,722.074,332.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="722.069,310.204,729.333,332.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="729.334,310.204,734.022,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="734.022,310.204,737.878,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="737.882,310.204,745.610,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="745.616,310.204,753.760,332.252" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="753.765,310.204,761.493,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="761.499,310.204,767.019,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="767.022,310.204,770.878,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="770.882,310.204,778.610,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="778.616,310.204,785.176,332.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="785.171,310.204,793.235,332.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="793.234,310.204,798.754,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="798.757,310.204,802.613,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="802.616,310.204,810.344,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="810.350,310.204,815.870,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="815.874,310.204,820.194,332.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="820.186,310.204,824.042,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="824.045,310.204,830.957,332.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="830.958,310.204,838.686,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="838.693,310.204,852.789,332.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="852.787,310.204,856.643,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="856.646,310.204,863.910,332.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="863.912,310.204,873.112,332.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="873.115,310.204,887.211,332.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="887.210,310.204,891.530,332.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="891.522,310.204,895.378,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="895.381,310.204,904.581,332.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="904.584,310.204,909.160,332.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="909.162,310.204,914.682,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="914.685,310.204,921.245,332.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="921.240,310.204,925.928,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="925.928,310.204,933.192,332.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="933.194,310.204,937.882,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="937.882,310.204,945.610,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="945.616,310.204,952.528,332.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="952.530,310.204,956.386,332.252" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,287.404,975.579,309.452">
<text font="OWDOPW+Georgia" bbox="533.000,287.404,539.912,309.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="539.914,287.404,548.538,309.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="548.539,287.404,553.115,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="553.117,287.404,557.693,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="557.694,287.404,562.382,309.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="562.382,287.404,569.646,309.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="569.648,287.404,574.336,309.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="574.336,287.404,579.856,309.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="579.859,287.404,589.059,309.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="589.062,287.404,598.246,309.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="598.250,287.404,602.938,309.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="602.938,287.404,612.394,309.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="612.390,287.404,616.246,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="616.250,287.404,624.314,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="624.312,287.404,638.408,309.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="638.406,287.404,646.134,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="646.141,287.404,651.661,309.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="651.664,287.404,655.520,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="655.523,287.404,663.251,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="663.258,287.404,667.834,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="667.835,287.404,675.563,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="675.570,287.404,680.258,309.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="680.258,287.404,685.458,309.452" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="685.461,287.404,693.189,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="693.195,287.404,702.651,309.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="702.648,287.404,711.832,309.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="711.835,287.404,715.691,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="715.694,287.404,724.878,309.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="724.882,287.404,733.506,309.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="733.507,287.404,738.083,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="738.085,287.404,746.709,309.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="746.710,287.404,753.270,309.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="753.266,287.404,757.122,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="757.125,287.404,766.581,309.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="766.578,287.404,775.778,309.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="775.781,287.404,780.357,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="780.358,287.404,784.934,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="784.936,287.404,793.000,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="792.998,287.404,807.094,309.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="807.093,287.404,810.949,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="810.952,287.404,818.680,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="818.686,287.404,825.246,309.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="825.242,287.404,833.306,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="833.304,287.404,838.824,309.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="838.827,287.404,843.147,309.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="843.139,287.404,846.995,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="846.998,287.404,861.094,309.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="861.093,287.404,869.157,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="869.155,287.404,873.731,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="873.733,287.404,881.461,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="881.467,287.404,888.379,309.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="888.381,287.404,897.581,309.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="897.584,287.404,905.648,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="905.646,287.404,914.830,309.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="914.834,287.404,922.898,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="922.896,287.404,926.752,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="926.755,287.404,934.483,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="934.490,287.404,941.402,309.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="941.403,287.404,946.923,309.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="946.926,287.404,950.782,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="950.786,287.404,955.362,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="955.363,287.404,963.091,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="963.098,287.404,971.722,309.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="971.723,287.404,975.579,309.452" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,264.604,965.642,286.652">
<text font="OWDOPW+Georgia" bbox="533.000,264.604,541.064,286.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="541.062,264.604,548.326,286.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="548.328,264.604,552.648,286.652" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="552.640,264.604,556.496,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="556.499,264.604,567.171,286.652" size="22.048">V</text>
<text font="OWDOPW+Georgia" bbox="567.163,264.604,575.227,286.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="575.226,264.604,581.786,286.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="581.781,264.604,586.469,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="586.469,264.604,595.669,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="595.672,264.604,602.584,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="602.586,264.604,606.442,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="606.445,264.604,615.901,286.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="615.898,264.604,623.962,286.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="623.960,264.604,629.480,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="629.483,264.604,638.107,286.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="638.109,264.604,647.069,286.652" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="647.062,264.604,656.262,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="656.266,264.604,663.994,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="664.000,264.604,667.856,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="667.859,264.604,673.379,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="673.382,264.604,682.582,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="682.586,264.604,689.146,286.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="689.141,264.604,698.277,286.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="698.282,264.604,702.970,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="702.970,264.604,709.882,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="709.883,264.604,713.739,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="713.742,264.604,721.470,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="721.477,264.604,726.053,286.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="726.054,264.604,733.782,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="733.789,264.604,747.885,286.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="747.883,264.604,755.611,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="755.618,264.604,765.074,286.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="765.070,264.604,770.590,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="770.594,264.604,779.794,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="779.797,264.604,793.893,286.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="793.891,264.604,797.747,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="797.750,264.604,805.478,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="805.485,264.604,812.397,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="812.398,264.604,817.918,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="817.922,264.604,822.242,286.652" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="822.234,264.604,826.090,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="826.093,264.604,838.077,286.652" size="22.048">D</text>
<text font="OWDOPW+Georgia" bbox="838.077,264.604,847.277,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="847.280,264.604,851.968,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="851.968,264.604,858.880,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="858.882,264.604,862.738,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="862.741,264.604,876.837,286.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="876.835,264.604,885.459,286.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="885.461,264.604,894.917,286.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="894.914,264.604,900.434,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="900.437,264.604,908.165,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="908.171,264.604,915.083,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="915.085,264.604,919.405,286.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="919.397,264.604,923.253,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="923.256,264.604,928.776,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="928.779,264.604,936.507,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="936.514,264.604,941.090,286.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="941.091,264.604,945.667,286.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="945.669,264.604,954.869,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="954.872,264.604,961.784,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="961.786,264.604,965.642,286.652" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,241.804,949.056,263.852">
<text font="OWDOPW+Georgia" bbox="533.000,241.804,537.576,263.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="537.578,241.804,546.202,263.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="546.203,241.804,555.163,263.852" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="555.165,241.804,563.789,263.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="563.790,241.804,570.350,263.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="570.346,241.804,575.866,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="575.869,241.804,580.557,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="580.557,241.804,587.469,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="587.470,241.804,591.326,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="591.330,241.804,595.906,263.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="595.907,241.804,603.971,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="603.970,241.804,611.234,263.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="611.235,241.804,620.435,263.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="620.438,241.804,627.350,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="627.352,241.804,631.208,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="631.211,241.804,639.275,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="639.274,241.804,653.370,263.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="653.368,241.804,661.096,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="661.102,241.804,666.622,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="666.626,241.804,670.482,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="670.485,241.804,678.549,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="678.547,241.804,685.107,263.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="685.102,241.804,692.366,263.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="692.368,241.804,701.568,263.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="701.571,241.804,705.427,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="705.430,241.804,713.158,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="713.165,241.804,718.685,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="718.688,241.804,723.008,263.852" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="723.000,241.804,726.856,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="726.859,241.804,733.099,263.852" size="22.048">I</text>
<text font="OWDOPW+Georgia" bbox="733.093,241.804,742.549,263.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="742.546,241.804,746.402,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="746.405,241.804,754.357,263.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="754.350,241.804,759.038,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="759.038,241.804,764.558,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="764.562,241.804,772.626,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="772.624,241.804,780.352,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="780.358,241.804,784.214,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="784.218,241.804,792.170,263.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="792.163,241.804,799.891,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="799.898,241.804,804.474,263.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="804.475,241.804,808.795,263.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="808.787,241.804,812.643,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="812.646,241.804,824.438,263.852" size="22.048">w</text>
<text font="OWDOPW+Georgia" bbox="824.443,241.804,829.131,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="829.131,241.804,836.043,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="836.045,241.804,840.733,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="840.733,241.804,844.589,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="844.592,241.804,852.656,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="852.654,241.804,858.174,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="858.178,241.804,862.498,263.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="862.490,241.804,866.346,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="866.349,241.804,871.037,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="871.037,241.804,880.221,263.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="880.224,241.804,884.080,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="884.083,241.804,893.219,263.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="893.224,241.804,899.784,263.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="899.779,241.804,907.843,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="907.842,241.804,915.570,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="915.576,241.804,922.488,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="922.490,241.804,930.218,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="930.224,241.804,939.680,263.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="939.677,241.804,945.197,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="945.200,241.804,949.056,263.852" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,219.004,962.765,241.052">
<text font="OWDOPW+Georgia" bbox="533.000,219.004,541.960,241.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="541.962,219.004,546.650,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="546.650,219.004,555.610,241.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="555.611,219.004,563.339,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="563.346,219.004,572.802,241.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="572.798,219.004,581.982,241.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="581.986,219.004,591.186,241.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="591.189,219.004,605.285,241.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="605.283,219.004,609.139,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="609.142,219.004,613.718,241.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="613.720,219.004,618.408,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="618.408,219.004,627.368,241.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="627.370,219.004,635.098,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="635.104,219.004,641.664,241.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="641.659,219.004,650.283,241.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="650.285,219.004,654.141,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="654.144,219.004,659.344,241.052" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="659.347,219.004,667.411,241.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="667.410,219.004,676.610,241.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="676.613,219.004,683.877,241.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="683.878,219.004,688.566,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="688.566,219.004,697.526,241.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="697.528,219.004,706.728,241.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="706.731,219.004,713.643,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="713.645,219.004,717.501,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="717.504,219.004,726.640,241.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="726.645,219.004,735.269,241.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="735.270,219.004,741.830,241.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="741.826,219.004,747.346,241.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="747.349,219.004,755.413,241.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="755.411,219.004,759.267,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="759.270,219.004,766.998,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="767.005,219.004,775.149,241.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="775.154,219.004,782.882,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="782.888,219.004,789.800,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="789.802,219.004,795.322,241.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="795.325,219.004,803.389,241.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="803.387,219.004,810.299,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="810.301,219.004,814.621,241.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="814.613,219.004,818.469,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="818.472,219.004,827.432,241.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="827.426,219.004,836.626,241.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="836.629,219.004,841.317,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="841.317,219.004,848.229,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="848.230,219.004,857.190,241.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="857.184,219.004,866.384,241.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="866.387,219.004,874.115,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="874.122,219.004,877.978,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="877.981,219.004,887.117,241.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="887.122,219.004,893.682,241.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="893.677,219.004,901.741,241.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="901.739,219.004,909.467,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="909.474,219.004,916.386,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="916.387,219.004,924.115,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="924.122,219.004,933.578,241.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="933.574,219.004,939.094,241.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="939.098,219.004,942.954,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="942.957,219.004,947.645,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="947.645,219.004,956.781,241.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="956.781,219.004,962.765,241.052" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,196.204,771.144,218.252">
<text font="OWDOPW+Georgia" bbox="533.000,196.204,539.912,218.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="539.914,196.204,549.114,218.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="549.115,196.204,563.211,218.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="563.213,196.204,567.069,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="567.070,196.204,572.270,218.252" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="572.272,196.204,580.000,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="580.002,196.204,586.562,218.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="586.563,196.204,600.659,218.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="600.661,196.204,608.389,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="608.390,196.204,617.846,218.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="617.848,196.204,623.368,218.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="623.370,196.204,632.570,218.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="632.571,196.204,646.667,218.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="646.669,196.204,650.525,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="650.526,196.204,659.662,218.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="659.664,196.204,664.240,218.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="664.242,196.204,672.306,218.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="672.307,196.204,679.571,218.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="679.573,196.204,687.301,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="687.302,196.204,693.862,218.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="693.864,196.204,701.928,218.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="701.930,196.204,707.450,218.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="707.451,196.204,711.307,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="711.309,196.204,716.829,218.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="716.830,196.204,724.558,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="724.560,196.204,738.656,218.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="738.658,196.204,747.794,218.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="747.795,196.204,756.419,218.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="756.421,196.204,762.981,218.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="762.982,196.204,767.302,218.252" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="767.288,196.204,771.144,218.252" size="22.048"> </text>
<text>
</text>
</textline>
</textbox>
<textbox id="9" bbox="533.000,45.404,962.675,181.452">
<textline bbox="533.000,159.404,958.187,181.452">
<text font="OWDOPW+Georgia" bbox="533.000,159.404,543.272,181.452" size="22.048">C</text>
<text font="OWDOPW+Georgia" bbox="543.274,159.404,552.474,181.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="552.477,159.404,559.037,181.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="559.032,159.404,567.096,181.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="567.094,159.404,576.054,181.452" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="576.056,159.404,580.744,181.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="580.744,159.404,586.264,181.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="586.267,159.404,595.467,181.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="595.470,159.404,602.030,181.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="602.026,159.404,605.882,181.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="605.885,159.404,613.949,181.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="613.947,159.404,623.147,181.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="623.150,159.404,630.414,181.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="630.416,159.404,635.936,181.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="635.939,159.404,644.563,181.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="644.565,159.404,651.125,181.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="651.120,159.404,655.440,181.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="655.432,159.404,659.288,181.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="659.291,159.404,667.019,181.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="667.026,159.404,673.586,181.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="673.581,159.404,681.645,181.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="681.643,159.404,687.163,181.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="687.166,159.404,691.022,181.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="691.026,159.404,705.122,181.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="705.120,159.404,713.744,181.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="713.746,159.404,718.322,181.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="718.323,159.404,722.899,181.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="722.901,159.404,727.589,181.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="727.589,159.404,734.501,181.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="734.502,159.404,738.358,181.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="738.362,159.404,745.274,181.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="745.275,159.404,753.003,181.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="753.010,159.404,762.194,181.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="762.197,159.404,766.053,181.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="766.056,159.404,771.256,181.452" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="771.259,159.404,780.459,181.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="780.462,159.404,787.374,181.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="787.376,159.404,794.640,181.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="794.642,159.404,802.370,181.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="802.376,159.404,806.696,181.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="806.688,159.404,810.544,181.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="810.547,159.404,816.067,181.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="816.070,159.404,825.270,181.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="825.274,159.404,831.834,181.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="831.829,159.404,840.965,181.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="840.970,159.404,845.658,181.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="845.658,159.404,852.570,181.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="852.571,159.404,856.427,181.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="856.430,159.404,864.382,181.452" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="864.376,159.404,869.064,181.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="869.064,159.404,877.016,181.452" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="877.010,159.404,885.074,181.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="885.072,159.404,899.168,181.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="899.166,159.404,908.366,181.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="908.370,159.404,915.282,181.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="915.283,159.404,919.139,181.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="919.142,159.404,927.206,181.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="927.205,159.404,931.061,181.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="931.064,159.404,940.248,181.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="940.251,159.404,944.939,181.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="944.939,159.404,952.203,181.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="952.203,159.404,958.187,181.452" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,136.604,958.266,158.652">
<text font="OWDOPW+Georgia" bbox="533.000,136.604,538.520,158.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="538.523,136.604,547.723,158.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="547.726,136.604,561.822,158.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="561.821,136.604,568.733,158.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="568.734,136.604,574.254,158.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="574.258,136.604,578.114,158.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="578.117,136.604,585.381,158.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="585.382,136.604,594.006,158.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="594.008,136.604,603.464,158.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="603.461,136.604,611.605,158.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="611.610,136.604,620.810,158.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="620.813,136.604,628.541,158.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="628.547,136.604,632.403,158.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="632.406,136.604,646.502,158.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="646.501,136.604,654.565,158.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="654.563,136.604,662.707,158.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="662.712,136.604,672.168,158.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="672.165,136.604,676.853,158.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="676.853,136.604,683.765,158.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="683.766,136.604,688.086,158.652" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="688.078,136.604,691.934,158.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="691.938,136.604,702.674,158.652" size="22.048">A</text>
<text font="OWDOPW+Georgia" bbox="702.672,136.604,707.248,158.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="707.250,136.604,711.938,158.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="711.938,136.604,720.898,158.652" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="720.891,136.604,730.091,158.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="730.094,136.604,738.158,158.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="738.157,136.604,752.253,158.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="752.251,136.604,756.107,158.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="756.110,136.604,764.174,158.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="764.173,136.604,778.269,158.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="778.267,136.604,785.995,158.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="786.002,136.604,791.522,158.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="791.525,136.604,795.381,158.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="795.384,136.604,804.584,158.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="804.587,136.604,809.163,158.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="809.165,136.604,813.741,158.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="813.742,136.604,821.806,158.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="821.805,136.604,835.901,158.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="835.899,136.604,843.163,158.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="843.165,136.604,851.789,158.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="851.790,136.604,858.350,158.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="858.346,136.604,867.482,158.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="867.486,136.604,875.214,158.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="875.221,136.604,881.781,158.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="881.776,136.604,885.632,158.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="885.635,136.604,894.819,158.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="894.822,136.604,899.510,158.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="899.510,136.604,907.654,158.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="907.659,136.604,917.115,158.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="917.112,136.604,921.800,158.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="921.800,136.604,928.712,158.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="928.714,136.604,935.626,158.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="935.627,136.604,940.315,158.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="940.315,136.604,954.411,158.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="954.410,136.604,958.266,158.652" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,113.804,878.758,135.852">
<text font="OWDOPW+Georgia" bbox="533.000,113.804,547.096,135.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="547.094,113.804,555.718,135.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="555.720,113.804,560.296,135.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="560.298,113.804,568.026,135.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="568.032,113.804,574.944,135.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="574.946,113.804,580.466,135.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="580.469,113.804,585.157,135.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="585.157,113.804,592.885,135.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="592.891,113.804,597.211,135.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="597.203,113.804,601.059,135.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="601.062,113.804,607.974,135.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="607.976,113.804,615.704,135.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="615.710,113.804,624.894,135.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="624.898,113.804,628.754,135.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="628.757,113.804,642.853,135.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="642.851,113.804,651.475,135.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="651.477,113.804,656.053,135.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="656.054,113.804,660.630,135.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="660.632,113.804,665.320,135.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="665.320,113.804,672.232,135.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="672.234,113.804,676.554,135.852" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="676.546,113.804,680.402,135.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="680.405,113.804,690.309,135.852" size="22.048">T</text>
<text font="OWDOPW+Georgia" bbox="690.304,113.804,698.928,135.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="698.930,113.804,705.490,135.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="705.485,113.804,711.005,135.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="711.008,113.804,719.632,135.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="719.634,113.804,726.194,135.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="726.189,113.804,730.045,135.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="730.048,113.804,738.000,135.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="737.994,113.804,742.682,135.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="742.682,113.804,748.202,135.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="748.205,113.804,756.269,135.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="756.267,113.804,763.995,135.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="764.002,113.804,767.858,135.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="767.861,113.804,773.381,135.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="773.384,113.804,782.008,135.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="782.010,113.804,788.570,135.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="788.565,113.804,794.085,135.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="794.088,113.804,802.712,135.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="802.714,113.804,809.274,135.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="809.269,113.804,813.125,135.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="813.128,113.804,820.856,135.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="820.862,113.804,827.422,135.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="827.418,113.804,836.042,135.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="836.043,113.804,842.955,135.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="842.957,113.804,846.813,135.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="846.816,113.804,858.608,135.852" size="22.048">w</text>
<text font="OWDOPW+Georgia" bbox="858.613,113.804,863.301,135.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="863.301,113.804,870.213,135.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="870.214,113.804,874.902,135.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="874.902,113.804,878.758,135.852" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,91.004,935.203,113.052">
<text font="OWDOPW+Georgia" bbox="533.000,91.004,538.200,113.052" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="538.203,91.004,546.267,113.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="546.266,91.004,553.530,113.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="553.531,91.004,558.219,113.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="558.219,91.004,562.795,113.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="562.797,91.004,567.485,113.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="567.485,91.004,574.397,113.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="574.398,91.004,579.086,113.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="579.086,91.004,585.998,113.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="586.000,91.004,590.320,113.052" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="590.312,91.004,600.584,113.052" size="22.048">C</text>
<text font="OWDOPW+Georgia" bbox="600.586,91.004,609.210,113.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="609.211,91.004,618.667,113.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="618.664,91.004,625.576,113.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="625.578,91.004,633.306,113.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="633.312,91.004,640.576,113.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="640.578,91.004,646.098,113.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="646.101,91.004,653.829,113.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="653.835,91.004,659.355,113.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="659.358,91.004,668.558,113.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="668.562,91.004,676.290,113.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="676.296,91.004,682.856,113.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="682.851,91.004,686.707,113.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="686.710,91.004,694.774,113.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="694.773,91.004,701.333,113.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="701.328,91.004,708.592,113.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="708.594,91.004,717.794,113.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="717.797,91.004,721.653,113.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="721.656,91.004,726.344,113.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="726.344,91.004,735.480,113.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="735.485,91.004,742.397,113.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="742.398,91.004,751.598,113.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="751.602,91.004,765.698,113.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="765.696,91.004,769.552,113.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="769.555,91.004,778.179,113.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="778.181,91.004,784.741,113.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="784.736,91.004,794.192,113.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="794.189,91.004,802.253,113.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="802.251,91.004,808.811,113.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="808.806,91.004,816.534,113.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="816.541,91.004,820.397,113.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="820.400,91.004,829.536,113.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="829.541,91.004,837.269,113.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="837.275,91.004,841.851,113.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="841.853,91.004,846.429,113.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="846.430,91.004,854.158,113.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="854.165,91.004,863.621,113.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="863.618,91.004,869.138,113.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="869.141,91.004,876.869,113.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="876.875,91.004,883.787,113.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="883.789,91.004,892.749,113.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="892.742,91.004,901.942,113.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="901.946,91.004,909.674,113.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="909.680,91.004,913.536,113.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="913.539,91.004,921.491,113.052" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="921.485,91.004,929.213,113.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="929.219,91.004,935.203,113.052" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,68.204,962.675,90.252">
<text font="OWDOPW+Georgia" bbox="533.000,68.204,542.312,90.252" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="542.312,68.204,547.000,90.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="547.000,68.204,554.264,90.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="554.266,68.204,563.466,90.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="563.469,68.204,568.045,90.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="568.046,68.204,576.110,90.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="576.109,68.204,580.429,90.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="580.421,68.204,584.277,90.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="584.280,68.204,588.968,90.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="588.968,68.204,598.424,90.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="598.421,68.204,602.277,90.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="602.280,68.204,610.232,90.252" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="610.226,68.204,617.954,90.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="617.960,68.204,627.272,90.252" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="627.272,68.204,631.960,90.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="631.960,68.204,639.224,90.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="639.226,68.204,648.426,90.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="648.429,68.204,653.005,90.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="653.006,68.204,661.070,90.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="661.069,68.204,664.925,90.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="664.928,68.204,674.112,90.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="674.115,68.204,678.803,90.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="678.803,68.204,686.867,90.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="686.866,68.204,700.962,90.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="700.960,68.204,705.280,90.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="705.272,68.204,709.128,90.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="709.131,68.204,717.755,90.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="717.757,68.204,724.317,90.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="724.312,68.204,733.768,90.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="733.765,68.204,741.829,90.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="741.827,68.204,748.387,90.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="748.382,68.204,756.110,90.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="756.117,68.204,759.973,90.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="759.976,68.204,774.072,90.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="774.070,68.204,782.134,90.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="782.133,68.204,790.277,90.252" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="790.282,68.204,799.738,90.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="799.734,68.204,807.798,90.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="807.797,68.204,811.653,90.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="811.656,68.204,819.384,90.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="819.390,68.204,825.950,90.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="825.946,68.204,834.010,90.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="834.008,68.204,839.528,90.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="839.531,68.204,843.387,90.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="843.390,68.204,848.590,90.252" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="848.594,68.204,856.322,90.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="856.328,68.204,860.904,90.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="860.906,68.204,865.594,90.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="865.594,68.204,872.506,90.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="872.507,68.204,876.363,90.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="876.366,68.204,888.158,90.252" size="22.048">w</text>
<text font="OWDOPW+Georgia" bbox="888.163,68.204,892.851,90.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="892.851,68.204,899.763,90.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="899.765,68.204,904.453,90.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="904.453,68.204,908.309,90.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="908.312,68.204,916.376,90.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="916.374,68.204,920.230,90.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="920.234,68.204,926.794,90.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="926.789,68.204,931.477,90.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="931.477,68.204,938.389,90.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="938.390,68.204,947.590,90.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="947.594,68.204,954.506,90.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="954.507,68.204,958.827,90.252" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="958.819,68.204,962.675,90.252" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,45.404,905.304,67.452">
<text font="OWDOPW+Georgia" bbox="533.000,45.404,541.288,67.452" size="22.048">J</text>
<text font="OWDOPW+Georgia" bbox="541.282,45.404,550.482,67.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="550.485,45.404,557.397,67.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="557.398,45.404,562.918,67.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="562.922,45.404,571.546,67.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="571.547,45.404,575.403,67.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="575.406,45.404,580.606,67.452" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="580.610,45.404,588.338,67.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="588.344,45.404,594.904,67.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="594.899,45.404,608.995,67.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="608.994,45.404,616.722,67.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="616.728,45.404,626.184,67.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="626.181,45.404,631.701,67.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="631.704,45.404,640.904,67.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="640.907,45.404,655.003,67.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="655.002,45.404,658.858,67.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="658.861,45.404,663.549,67.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="663.549,45.404,672.733,67.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="672.736,45.404,677.056,67.452" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="677.048,45.404,680.904,67.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="680.907,45.404,695.739,67.452" size="22.048">M</text>
<text font="OWDOPW+Georgia" bbox="695.742,45.404,703.806,67.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="703.805,45.404,708.381,67.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="708.382,45.404,716.110,67.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="716.117,45.404,723.029,67.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="723.030,45.404,732.230,67.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="732.234,45.404,740.298,67.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="740.296,45.404,749.480,67.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="749.483,45.404,757.547,67.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="757.546,45.404,761.402,67.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="761.405,45.404,769.133,67.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="769.139,45.404,773.715,67.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="773.717,45.404,781.445,67.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="781.451,45.404,786.139,67.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="786.139,45.404,791.339,67.452" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="791.342,45.404,799.070,67.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="799.077,45.404,808.533,67.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="808.530,45.404,817.714,67.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="817.717,45.404,822.037,67.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="822.029,45.404,825.885,67.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="825.888,45.404,831.408,67.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="831.411,45.404,840.035,67.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="840.037,45.404,846.597,67.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="846.592,45.404,852.112,67.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="852.115,45.404,860.739,67.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="860.741,45.404,867.301,67.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="867.296,45.404,871.152,67.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="871.155,45.404,878.883,67.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="878.890,45.404,885.450,67.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="885.445,45.404,894.069,67.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="894.070,45.404,900.982,67.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="900.984,45.404,905.304,67.452" size="22.048">.</text>
<text>
</text>
</textline>
</textbox>
<textbox id="10" bbox="965.738,18.003,973.005,35.917">
<textline bbox="965.738,18.003,973.005,35.917">
<text font="OWDOPW+Georgia" bbox="965.738,18.003,973.005,35.917" size="17.914">2</text>
<text>
</text>
</textline>
</textbox>
<rect linewidth="0" bbox="0.000,0.000,1024.000,748.000" />
<rect linewidth="0" bbox="0.000,0.000,1024.000,748.000" />
<curve linewidth="0" bbox="50.000,40.000,488.000,516.000" pts="50.000,44.760,50.000,511.240,50.000,513.869,52.131,516.000,54.760,516.000,483.240,516.000,485.869,516.000,488.000,513.869,488.000,511.240,488.000,44.760,488.000,42.131,485.869,40.000,483.240,40.000,54.760,40.000,52.131,40.000,50.000,42.131,50.000,44.760,50.000,44.760"/>
<curve linewidth="0" bbox="50.000,40.000,488.000,516.000" pts="50.000,44.760,50.000,511.240,50.000,513.869,52.131,516.000,54.760,516.000,483.240,516.000,485.869,516.000,488.000,513.869,488.000,511.240,488.000,44.760,488.000,42.131,485.869,40.000,483.240,40.000,54.760,40.000,52.131,40.000,50.000,42.131,50.000,44.760,50.000,44.760"/>
<line linewidth="0" bbox="66.000,471.750,472.000,471.750" />
<line linewidth="0" bbox="50.000,680.750,490.000,680.750" />
<line linewidth="0" bbox="512.000,40.000,512.000,708.000" />
<layout>
<textgroup bbox="50.000,18.003,975.579,711.808">
<textgroup bbox="50.000,208.404,461.323,711.808">
<textgroup bbox="50.000,639.509,182.264,711.808">
<textbox id="0" bbox="50.000,687.004,133.447,711.808" />
<textbox id="1" bbox="50.000,639.509,182.264,689.117" />
</textgroup>
<textgroup bbox="66.250,208.404,461.323,502.808">
<textbox id="2" bbox="66.250,478.004,181.273,502.808" />
<textgroup bbox="66.250,208.404,461.323,464.808">
<textgroup bbox="66.250,268.804,453.354,464.808">
<textbox id="3" bbox="66.250,354.404,453.354,464.808" />
<textbox id="4" bbox="66.250,268.804,450.208,344.008" />
</textgroup>
<textgroup bbox="66.250,208.404,461.323,258.408">
<textbox id="5" bbox="66.250,233.604,461.323,258.408" />
<textbox id="6" bbox="96.000,208.404,398.182,233.208" />
</textgroup>
</textgroup>
</textgroup>
</textgroup>
<textgroup bbox="533.000,18.003,975.579,711.052">
<textgroup bbox="533.000,45.404,975.579,711.052">
<textgroup bbox="533.000,196.204,975.579,711.052">
<textbox id="7" bbox="533.000,461.004,974.035,711.052" />
<textbox id="8" bbox="533.000,196.204,975.579,446.252" />
</textgroup>
<textbox id="9" bbox="533.000,45.404,962.675,181.452" />
</textgroup>
<textbox id="10" bbox="965.738,18.003,973.005,35.917" />
</textgroup>
</textgroup>
</layout>
</page>
<page id="4" bbox="0.000,0.000,1024.000,748.000" rotate="0">
<textbox id="0" bbox="50.000,461.004,491.035,711.052">
<textline bbox="50.000,689.004,491.035,711.052">
<text font="OWDOPW+Georgia" bbox="50.000,689.004,59.664,711.052" size="22.048">L</text>
<text font="OWDOPW+Georgia" bbox="59.656,689.004,68.280,711.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="68.282,689.004,74.842,711.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="74.837,689.004,82.565,711.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="82.571,689.004,96.667,711.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="96.666,689.004,100.522,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="100.525,689.004,105.213,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="105.213,689.004,114.349,711.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="114.354,689.004,121.266,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="121.267,689.004,130.467,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="130.470,689.004,144.566,711.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="144.565,689.004,148.421,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="148.424,689.004,157.608,711.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="157.611,689.004,166.235,711.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="166.237,689.004,170.813,711.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="170.814,689.004,179.438,711.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="179.440,689.004,186.000,711.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="185.995,689.004,189.851,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="189.854,689.004,196.766,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="196.768,689.004,201.456,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="201.456,689.004,206.976,711.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="206.979,689.004,210.835,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="210.838,689.004,218.902,711.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="218.901,689.004,232.997,711.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="232.995,689.004,240.723,711.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="240.730,689.004,246.250,711.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="246.253,689.004,250.573,711.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="250.565,689.004,254.421,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="254.424,689.004,259.000,711.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="259.002,689.004,263.690,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="263.690,689.004,271.834,711.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="271.838,689.004,281.038,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="281.042,689.004,285.618,711.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="285.619,689.004,293.683,711.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="293.682,689.004,297.538,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="297.541,689.004,304.453,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="304.454,689.004,313.654,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="313.658,689.004,320.570,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="320.571,689.004,329.707,711.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="329.712,689.004,337.440,711.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="337.446,689.004,346.902,711.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="346.899,689.004,356.083,711.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="356.086,689.004,360.774,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="360.774,689.004,367.686,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="367.688,689.004,374.600,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="374.602,689.004,382.330,711.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="382.336,689.004,386.192,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="386.195,689.004,395.651,711.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="395.648,689.004,404.848,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="404.851,689.004,409.427,711.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="409.429,689.004,414.005,711.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="414.006,689.004,422.070,711.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="422.069,689.004,425.925,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="425.928,689.004,435.064,711.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="435.069,689.004,441.629,711.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="441.624,689.004,449.352,711.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="449.358,689.004,454.878,711.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="454.882,689.004,459.570,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="459.570,689.004,468.770,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="468.773,689.004,482.869,711.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="482.867,689.004,487.187,711.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="487.179,689.004,491.035,711.052" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,666.204,486.851,688.252">
<text font="OWDOPW+Georgia" bbox="50.000,666.204,56.560,688.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="56.555,666.204,65.867,688.252" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="65.867,666.204,74.491,688.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="74.493,666.204,83.949,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="83.946,666.204,91.210,688.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="91.211,666.204,100.411,688.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="100.414,666.204,107.326,688.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="107.328,666.204,111.184,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="111.187,666.204,116.707,688.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="116.710,666.204,124.438,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="124.445,666.204,138.541,688.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="138.539,666.204,147.675,688.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="147.680,666.204,156.304,688.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="156.306,666.204,162.866,688.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="162.861,666.204,166.717,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="166.720,666.204,175.856,688.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="175.861,666.204,180.437,688.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="180.438,666.204,188.502,688.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="188.501,666.204,195.765,688.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="195.766,666.204,203.494,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="203.501,666.204,210.061,688.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="210.056,666.204,218.120,688.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="218.118,666.204,223.638,688.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="223.642,666.204,227.498,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="227.501,666.204,232.701,688.252" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="232.704,666.204,240.432,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="240.438,666.204,246.998,688.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="246.994,666.204,261.090,688.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="261.088,666.204,268.816,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="268.822,666.204,278.278,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="278.275,666.204,283.795,688.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="283.798,666.204,292.998,688.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="293.002,666.204,307.098,688.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="307.096,666.204,311.416,688.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="311.408,666.204,315.264,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="315.267,666.204,322.995,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="323.002,666.204,332.458,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="332.454,666.204,337.142,688.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="337.142,666.204,351.238,688.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="351.237,666.204,355.093,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="355.096,666.204,359.784,688.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="359.784,666.204,369.240,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="369.237,666.204,374.757,688.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="374.760,666.204,382.488,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="382.494,666.204,390.638,688.252" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="390.643,666.204,398.371,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="398.378,666.204,404.938,688.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="404.933,666.204,408.789,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="408.792,666.204,416.856,688.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="416.854,666.204,426.038,688.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="426.042,666.204,429.898,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="429.901,666.204,437.853,688.252" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="437.846,666.204,445.574,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="445.581,666.204,452.493,688.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="452.494,666.204,458.014,688.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="458.018,666.204,462.706,688.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="462.706,666.204,471.666,688.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="471.667,666.204,480.867,688.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="480.867,666.204,486.851,688.252" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="50.000,643.404,457.275,665.452">
<text font="OWDOPW+Georgia" bbox="50.000,643.404,54.576,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="54.578,643.404,63.778,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="63.781,643.404,77.877,665.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="77.875,643.404,81.731,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="81.734,643.404,89.686,665.452" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="89.680,643.404,98.304,665.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="98.306,643.404,102.882,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="102.883,643.404,112.083,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="112.086,643.404,117.606,665.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="117.610,643.404,126.746,665.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="126.750,643.404,134.814,665.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="134.813,643.404,140.333,665.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="140.336,643.404,144.656,665.452" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="144.648,643.404,148.504,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="148.507,643.404,160.779,665.452" size="22.048">N</text>
<text font="OWDOPW+Georgia" bbox="160.781,643.404,165.469,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="165.469,643.404,172.381,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="172.382,643.404,176.958,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="176.960,643.404,180.816,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="180.819,643.404,187.379,665.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="187.374,643.404,196.686,665.452" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="196.686,643.404,205.310,665.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="205.312,643.404,214.768,665.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="214.765,643.404,222.029,665.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="222.030,643.404,231.230,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="231.234,643.404,238.146,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="238.147,643.404,242.003,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="242.006,643.404,247.526,665.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="247.530,643.404,256.730,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="256.733,643.404,263.293,665.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="263.288,643.404,272.424,665.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="272.429,643.404,277.117,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="277.117,643.404,284.029,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="284.030,643.404,287.886,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="287.890,643.404,295.618,665.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="295.624,643.404,302.536,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="302.538,643.404,308.058,665.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="308.061,643.404,312.381,665.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="312.373,643.404,316.229,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="316.232,643.404,324.184,665.452" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="324.178,643.404,331.906,665.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="331.912,643.404,336.488,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="336.490,643.404,340.346,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="340.349,643.404,348.077,665.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="348.083,643.404,352.659,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="352.661,643.404,357.349,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="357.349,643.404,362.869,665.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="362.872,643.404,367.192,665.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="367.184,643.404,371.040,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="371.043,643.404,378.307,665.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="378.309,643.404,386.933,665.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="386.934,643.404,396.390,665.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="396.387,643.404,404.531,665.452" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="404.536,643.404,413.736,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="413.739,643.404,421.467,665.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="421.474,643.404,425.330,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="425.333,643.404,437.125,665.452" size="22.048">w</text>
<text font="OWDOPW+Georgia" bbox="437.130,643.404,441.818,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="441.818,643.404,448.730,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="448.731,643.404,453.419,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="453.419,643.404,457.275,665.452" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,620.604,475.619,642.652">
<text font="OWDOPW+Georgia" bbox="50.000,620.604,57.728,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="57.734,620.604,67.190,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="67.187,620.604,71.875,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="71.875,620.604,85.971,642.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="85.970,620.604,89.826,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="89.829,620.604,99.285,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="99.282,620.604,108.482,642.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="108.485,620.604,117.941,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="117.938,620.604,125.202,642.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="125.203,620.604,129.059,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="129.062,620.604,138.262,642.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="138.266,620.604,142.842,642.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="142.843,620.604,148.363,642.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="148.366,620.604,154.926,642.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="154.922,620.604,159.610,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="159.610,620.604,166.874,642.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="166.875,620.604,171.563,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="171.563,620.604,179.291,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="179.298,620.604,186.210,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="186.211,620.604,190.067,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="190.070,620.604,196.982,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="196.984,620.604,201.672,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="201.672,620.604,207.192,642.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="207.195,620.604,211.515,642.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="211.507,620.604,215.363,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="215.366,620.604,229.462,642.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="229.461,620.604,237.525,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="237.523,620.604,245.667,642.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="245.672,620.604,255.128,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="255.125,620.604,263.189,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="263.187,620.604,267.043,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="267.046,620.604,272.566,642.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="272.570,620.604,277.258,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="277.258,620.604,286.714,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="286.710,620.604,293.974,642.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="293.976,620.604,298.664,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="298.664,620.604,307.848,642.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="307.851,620.604,317.051,642.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="317.054,620.604,326.510,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="326.507,620.604,332.027,642.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="332.030,620.604,336.350,642.652" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="336.342,620.604,340.198,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="340.202,620.604,355.034,642.652" size="22.048">M</text>
<text font="OWDOPW+Georgia" bbox="355.037,620.604,363.101,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="363.099,620.604,370.827,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="370.834,620.604,378.098,642.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="378.099,620.604,385.827,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="385.834,620.604,395.290,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="395.286,620.604,403.350,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="403.349,620.604,410.261,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="410.262,620.604,414.118,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="414.122,620.604,422.186,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="422.184,620.604,426.760,642.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="426.762,620.604,431.450,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="431.450,620.604,440.410,642.652" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="440.403,620.604,449.603,642.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="449.606,620.604,457.670,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="457.669,620.604,471.765,642.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="471.763,620.604,475.619,642.652" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,597.804,487.476,619.852">
<text font="OWDOPW+Georgia" bbox="50.000,597.804,64.096,619.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="64.094,597.804,72.158,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="72.157,597.804,79.885,619.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="79.891,597.804,87.155,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="87.157,597.804,94.885,619.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="94.891,597.804,104.347,619.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="104.344,597.804,112.408,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="112.406,597.804,119.318,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="119.320,597.804,123.176,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="123.179,597.804,127.755,619.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="127.757,597.804,132.445,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="132.445,597.804,140.589,619.852" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="140.594,597.804,149.794,619.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="149.797,597.804,154.373,619.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="154.374,597.804,162.438,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="162.437,597.804,166.293,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="166.296,597.804,175.752,619.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="175.749,597.804,184.373,619.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="184.374,597.804,191.286,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="191.288,597.804,196.808,619.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="196.811,597.804,203.371,619.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="203.366,597.804,211.430,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="211.429,597.804,215.749,619.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="215.741,597.804,219.597,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="219.600,597.804,227.664,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="227.662,597.804,234.926,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="234.928,597.804,242.192,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="242.194,597.804,251.394,619.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="251.397,597.804,265.493,619.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="265.491,597.804,272.403,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="272.405,597.804,280.469,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="280.467,597.804,289.923,619.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="289.920,597.804,293.776,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="293.779,597.804,299.299,619.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="299.302,597.804,307.366,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="307.365,597.804,314.629,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="314.630,597.804,319.318,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="319.318,597.804,324.838,619.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="324.842,597.804,329.530,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="329.530,597.804,333.850,619.852" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="333.842,597.804,337.698,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="337.701,597.804,346.677,619.852" size="22.048">S</text>
<text font="OWDOPW+Georgia" bbox="346.677,597.804,355.301,619.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="355.302,597.804,362.566,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="362.568,597.804,367.256,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="367.256,597.804,371.944,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="371.944,597.804,378.856,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="378.858,597.804,382.714,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="382.717,597.804,396.813,619.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="396.811,597.804,404.875,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="404.874,597.804,414.074,619.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="414.077,597.804,420.637,619.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="420.632,597.804,425.320,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="425.320,597.804,432.232,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="432.234,597.804,436.090,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="436.093,597.804,440.781,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="440.781,597.804,450.237,619.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="450.234,597.804,454.090,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="454.093,597.804,458.781,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="458.781,597.804,468.237,619.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="468.234,597.804,473.754,619.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="473.757,597.804,481.485,619.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="481.492,597.804,487.476,619.852" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="50.000,575.004,480.798,597.052">
<text font="OWDOPW+Georgia" bbox="50.000,575.004,58.144,597.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="58.149,575.004,65.877,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="65.883,575.004,72.443,597.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="72.438,575.004,76.758,597.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="76.750,575.004,80.606,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="80.610,575.004,88.674,597.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="88.672,575.004,92.528,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="92.531,575.004,101.715,597.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="101.718,575.004,110.342,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="110.344,575.004,114.920,597.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="114.922,575.004,123.546,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="123.547,575.004,130.107,597.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="130.102,575.004,133.958,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="133.962,575.004,143.418,597.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="143.414,575.004,151.142,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="151.149,575.004,156.669,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="156.672,575.004,165.872,597.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="165.875,575.004,172.787,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="172.789,575.004,176.645,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="176.648,575.004,186.104,597.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="186.101,575.004,194.725,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="194.726,575.004,204.182,597.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="204.179,575.004,208.035,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="208.038,575.004,217.222,597.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="217.226,575.004,226.426,597.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="226.429,575.004,231.117,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="231.117,575.004,234.973,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="234.976,575.004,243.040,597.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="243.038,575.004,247.614,597.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="247.616,575.004,252.304,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="252.304,575.004,261.264,597.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="261.258,575.004,270.458,597.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="270.461,575.004,278.189,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="278.195,575.004,283.715,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="283.718,575.004,288.038,597.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="288.030,575.004,291.886,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="291.890,575.004,298.802,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="298.803,575.004,306.867,597.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="306.866,575.004,315.010,597.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="315.014,575.004,319.702,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="319.702,575.004,325.222,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="325.226,575.004,330.746,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="330.749,575.004,335.437,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="335.437,575.004,342.349,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="342.350,575.004,346.206,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="346.210,575.004,351.410,597.052" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="351.413,575.004,359.141,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="359.147,575.004,363.723,597.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="363.725,575.004,368.413,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="368.413,575.004,375.325,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="375.326,575.004,379.182,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="379.186,575.004,386.098,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="386.099,575.004,394.723,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="394.725,575.004,403.909,597.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="403.912,575.004,411.976,597.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="411.974,575.004,416.550,597.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="416.552,575.004,424.280,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="424.286,575.004,431.198,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="431.200,575.004,435.520,597.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="435.512,575.004,439.368,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="439.371,575.004,448.555,597.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="448.558,575.004,457.182,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="457.184,575.004,461.760,597.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="461.762,575.004,470.386,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="470.387,575.004,476.947,597.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="476.942,575.004,480.798,597.052" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,552.204,467.882,574.252">
<text font="OWDOPW+Georgia" bbox="50.000,552.204,56.912,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="56.914,552.204,65.538,574.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="65.539,552.204,72.803,574.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="72.805,552.204,77.493,574.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="77.493,552.204,82.181,574.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="82.181,552.204,89.093,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="89.094,552.204,92.950,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="92.954,552.204,107.050,574.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="107.048,552.204,115.112,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="115.110,552.204,124.310,574.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="124.314,552.204,130.874,574.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="130.869,552.204,135.557,574.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="135.557,552.204,142.469,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="142.470,552.204,146.790,574.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="146.782,552.204,150.638,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="150.642,552.204,158.594,574.252" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="158.587,552.204,166.315,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="166.322,552.204,170.898,574.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="170.899,552.204,174.755,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="174.758,552.204,182.486,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="182.493,552.204,191.693,574.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="191.696,552.204,195.552,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="195.555,552.204,203.283,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="203.290,552.204,210.202,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="210.203,552.204,215.723,574.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="215.726,552.204,219.582,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="219.586,552.204,224.162,574.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="224.163,552.204,228.851,574.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="228.851,552.204,237.811,574.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="237.813,552.204,245.541,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="245.547,552.204,252.107,574.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="252.102,552.204,260.726,574.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="260.728,552.204,264.584,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="264.587,552.204,271.851,574.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="271.853,552.204,278.413,574.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="278.408,552.204,286.472,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="286.470,552.204,293.382,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="293.384,552.204,297.704,574.252" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="297.696,552.204,301.552,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="301.555,552.204,307.795,574.252" size="22.048">I</text>
<text font="OWDOPW+Georgia" bbox="307.789,552.204,317.245,574.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="317.242,552.204,322.762,574.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="322.765,552.204,330.493,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="330.499,552.204,337.059,574.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="337.054,552.204,346.238,574.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="346.242,552.204,355.442,574.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="355.445,552.204,369.541,574.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="369.539,552.204,373.395,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="373.398,552.204,381.462,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="381.461,552.204,386.981,574.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="386.984,552.204,391.304,574.252" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="391.296,552.204,395.152,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="395.155,552.204,405.603,574.252" size="22.048">E</text>
<text font="OWDOPW+Georgia" bbox="405.608,552.204,413.752,574.252" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="413.757,552.204,421.485,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="421.491,552.204,427.011,574.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="427.014,552.204,430.870,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="430.874,552.204,440.186,574.252" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="440.186,552.204,448.250,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="448.248,552.204,457.208,574.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="457.210,552.204,461.898,574.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="461.898,552.204,467.882,574.252" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="50.000,529.404,476.086,551.452">
<text font="OWDOPW+Georgia" bbox="50.000,529.404,55.520,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="55.523,529.404,63.587,551.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="63.586,529.404,70.498,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="70.499,529.404,77.411,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="77.413,529.404,85.141,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="85.147,529.404,89.003,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="89.006,529.404,96.734,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="96.741,529.404,101.317,551.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="101.318,529.404,109.046,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="109.053,529.404,123.149,551.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="123.147,529.404,130.875,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="130.882,529.404,140.338,551.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="140.334,529.404,145.854,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="145.858,529.404,155.058,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="155.061,529.404,169.157,551.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="169.155,529.404,173.011,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="173.014,529.404,180.742,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="180.749,529.404,187.661,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="187.662,529.404,193.182,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="193.186,529.404,197.506,551.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="197.498,529.404,201.354,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="201.357,529.404,206.045,551.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="206.045,529.404,215.181,551.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="215.186,529.404,222.098,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="222.099,529.404,231.299,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="231.302,529.404,245.398,551.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="245.397,529.404,249.253,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="249.256,529.404,258.392,551.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="258.397,529.404,267.597,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="267.600,529.404,274.160,551.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="274.155,529.404,283.355,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="283.358,529.404,290.270,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="290.272,529.404,294.128,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="294.131,529.404,303.267,551.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="303.272,529.404,311.000,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="311.006,529.404,320.190,551.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="320.194,529.404,327.922,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="327.928,529.404,331.784,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="331.787,529.404,340.923,551.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="340.928,529.404,349.552,551.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="349.554,529.404,356.114,551.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="356.109,529.404,361.629,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="361.632,529.404,367.152,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="367.155,529.404,371.843,551.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="371.843,529.404,377.363,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="377.366,529.404,385.990,551.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="385.992,529.404,392.552,551.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="392.547,529.404,396.403,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="396.406,529.404,403.670,551.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="403.672,529.404,408.248,551.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="408.250,529.404,416.314,551.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="416.312,529.404,423.224,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="423.226,529.404,430.138,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="430.139,529.404,434.459,551.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="434.451,529.404,438.307,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="438.310,529.404,447.510,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="447.514,529.404,453.034,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="453.037,529.404,456.893,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="456.896,529.404,461.472,551.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="461.474,529.404,470.098,551.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="470.102,529.404,476.086,551.452" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="50.000,506.604,471.680,528.652">
<text font="OWDOPW+Georgia" bbox="50.000,506.604,56.560,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="56.555,506.604,64.283,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="64.290,506.604,78.386,528.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="78.384,506.604,82.240,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="82.243,506.604,90.307,528.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="90.306,506.604,99.490,528.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="99.493,506.604,104.181,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="104.181,506.604,113.317,528.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="113.322,506.604,118.010,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="118.010,506.604,124.922,528.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="124.923,506.604,132.187,528.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="132.189,506.604,136.877,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="136.877,506.604,146.333,528.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="146.330,506.604,154.474,528.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="154.478,506.604,158.798,528.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="158.790,506.604,162.646,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="162.650,506.604,170.714,528.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="170.712,506.604,175.288,528.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="175.290,506.604,179.978,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="179.978,506.604,188.938,528.652" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="188.931,506.604,198.131,528.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="198.134,506.604,205.862,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="205.869,506.604,211.389,528.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="211.392,506.604,215.248,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="215.251,506.604,222.163,528.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="222.165,506.604,229.893,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="229.899,506.604,239.083,528.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="239.086,506.604,242.942,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="242.946,506.604,251.010,528.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="251.008,506.604,260.208,528.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="260.211,506.604,267.475,528.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="267.477,506.604,272.997,528.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="273.000,506.604,281.624,528.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="281.626,506.604,288.186,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="288.181,506.604,292.501,528.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="292.493,506.604,296.349,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="296.352,506.604,301.040,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="301.040,506.604,315.136,528.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="315.134,506.604,324.270,528.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="324.275,506.604,332.003,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="332.010,506.604,338.570,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="338.565,506.604,347.749,528.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="347.752,506.604,352.440,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="352.440,506.604,360.168,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="360.174,506.604,365.694,528.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="365.698,506.604,369.554,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="369.557,506.604,377.621,528.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="377.619,506.604,384.179,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="384.174,506.604,391.438,528.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="391.440,506.604,400.640,528.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="400.643,506.604,404.499,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="404.502,506.604,413.638,528.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="413.643,506.604,421.371,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="421.378,506.604,427.938,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="427.933,506.604,431.789,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="431.792,506.604,440.976,528.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="440.979,506.604,445.667,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="445.667,506.604,453.731,528.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="453.730,506.604,467.826,528.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="467.824,506.604,471.680,528.652" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,483.804,455.820,505.852">
<text font="OWDOPW+Georgia" bbox="50.000,483.804,59.184,505.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="59.187,483.804,67.251,505.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="67.250,483.804,76.386,505.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="76.390,483.804,81.078,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="81.078,483.804,90.038,505.852" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="90.040,483.804,99.240,505.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="99.243,483.804,106.155,505.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="106.157,483.804,110.013,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="110.016,483.804,114.592,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="114.594,483.804,119.282,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="119.282,483.804,128.242,505.852" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="128.243,483.804,135.971,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="135.978,483.804,142.538,505.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="142.533,483.804,151.157,505.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="151.158,483.804,155.014,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="155.018,483.804,164.202,505.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="164.205,483.804,173.405,505.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="173.408,483.804,178.096,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="178.096,483.804,185.008,505.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="185.010,483.804,189.330,505.852" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="189.322,483.804,193.178,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="193.181,483.804,203.629,505.852" size="22.048">E</text>
<text font="OWDOPW+Georgia" bbox="203.634,483.804,213.090,505.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="213.086,483.804,217.774,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="217.774,483.804,231.870,505.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="231.869,483.804,235.725,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="235.728,483.804,243.456,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="243.462,483.804,250.022,505.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="250.018,483.804,258.642,505.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="258.643,483.804,265.555,505.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="265.557,483.804,269.413,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="269.416,483.804,274.104,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="274.104,483.804,283.560,505.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="283.557,483.804,287.413,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="287.416,483.804,295.368,505.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="295.362,483.804,303.090,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="303.096,483.804,307.672,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="307.674,483.804,311.994,505.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="311.986,483.804,315.842,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="315.845,483.804,323.797,505.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="323.790,483.804,332.414,505.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="332.416,483.804,336.992,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="336.994,483.804,346.194,505.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="346.197,483.804,351.717,505.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="351.720,483.804,360.856,505.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="360.861,483.804,368.925,505.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="368.923,483.804,374.443,505.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="374.446,483.804,378.302,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="378.306,483.804,387.762,505.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="387.758,483.804,395.486,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="395.493,483.804,402.757,505.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="402.758,483.804,406.614,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="406.618,483.804,415.754,505.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="415.758,483.804,423.486,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="423.493,483.804,428.069,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="428.070,483.804,432.646,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="432.648,483.804,440.376,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="440.382,483.804,449.838,505.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="449.836,483.804,455.820,505.852" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="50.000,461.004,325.235,483.052">
<text font="OWDOPW+Georgia" bbox="50.000,461.004,55.520,483.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="55.523,461.004,63.251,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="63.258,461.004,70.170,483.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="70.171,461.004,79.131,483.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="79.125,461.004,88.325,483.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="88.328,461.004,96.056,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="96.062,461.004,99.918,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="99.922,461.004,104.498,483.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="104.499,461.004,112.227,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="112.234,461.004,120.858,483.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="120.859,461.004,125.179,483.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="125.171,461.004,129.027,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="129.030,461.004,134.550,483.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="134.554,461.004,142.282,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="142.288,461.004,156.384,483.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="156.382,461.004,165.518,483.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="165.523,461.004,174.147,483.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="174.149,461.004,180.709,483.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="180.704,461.004,185.392,483.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="185.392,461.004,194.352,483.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="194.354,461.004,203.554,483.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="203.557,461.004,210.469,483.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="210.470,461.004,214.326,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="214.330,461.004,221.242,483.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="221.243,461.004,228.507,483.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="228.509,461.004,236.237,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="236.243,461.004,240.819,483.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="240.821,461.004,248.549,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="248.555,461.004,255.115,483.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="255.110,461.004,259.798,483.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="259.798,461.004,266.710,483.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="266.712,461.004,275.672,483.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="275.666,461.004,284.866,483.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="284.869,461.004,292.597,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="292.603,461.004,296.459,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="296.462,461.004,305.918,483.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="305.915,461.004,313.643,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="313.650,461.004,320.914,483.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="320.915,461.004,325.235,483.052" size="22.048">.</text>
<text>
</text>
</textline>
</textbox>
<textbox id="1" bbox="50.000,59.404,493.509,446.252">
<textline bbox="50.000,424.204,469.910,446.252">
<text font="OWDOPW+Georgia" bbox="50.000,424.204,60.736,446.252" size="22.048">A</text>
<text font="OWDOPW+Georgia" bbox="60.734,424.204,67.998,446.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="68.000,424.204,71.856,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="71.859,424.204,81.043,446.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="81.046,424.204,89.670,446.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="89.672,424.204,94.248,446.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="94.250,424.204,102.874,446.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="102.875,424.204,109.435,446.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="109.430,424.204,113.286,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="113.290,424.204,121.354,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="121.352,424.204,128.616,446.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="128.618,424.204,132.474,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="132.477,424.204,140.541,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="140.539,424.204,149.723,446.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="149.726,424.204,154.414,446.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="154.414,424.204,163.550,446.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="163.555,424.204,168.243,446.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="168.243,424.204,175.155,446.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="175.157,424.204,182.421,446.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="182.422,424.204,187.110,446.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="187.110,424.204,196.566,446.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="196.563,424.204,204.707,446.252" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="204.712,424.204,208.568,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="208.571,424.204,216.635,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="216.634,424.204,230.730,446.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="230.728,424.204,238.456,446.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="238.462,424.204,243.982,446.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="243.986,424.204,247.842,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="247.845,424.204,256.805,446.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="256.806,424.204,261.494,446.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="261.494,424.204,270.454,446.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="270.456,424.204,278.184,446.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="278.190,424.204,287.646,446.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="287.643,424.204,296.827,446.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="296.830,424.204,306.030,446.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="306.034,424.204,320.130,446.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="320.128,424.204,323.984,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="323.987,424.204,333.443,446.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="333.440,424.204,342.640,446.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="342.643,424.204,347.219,446.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="347.221,424.204,351.797,446.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="351.798,424.204,359.862,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="359.861,424.204,373.957,446.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="373.955,424.204,378.275,446.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="378.267,424.204,382.123,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="382.126,424.204,396.222,446.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="396.221,424.204,404.285,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="404.283,424.204,411.195,446.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="411.197,424.204,418.109,446.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="418.110,424.204,426.174,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="426.173,424.204,430.029,446.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="430.032,424.204,434.608,446.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="434.610,424.204,442.674,446.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="442.672,424.204,449.936,446.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="449.938,424.204,459.138,446.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="459.141,424.204,466.053,446.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="466.054,424.204,469.910,446.252" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,401.404,481.691,423.452">
<text font="OWDOPW+Georgia" bbox="50.000,401.404,64.096,423.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="64.094,401.404,72.718,423.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="72.720,401.404,77.296,423.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="77.298,401.404,85.026,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="85.032,401.404,91.944,423.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="91.946,401.404,97.466,423.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="97.469,401.404,102.157,423.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="102.157,401.404,109.885,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="109.891,401.404,113.747,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="113.750,401.404,122.950,423.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="122.954,401.404,128.474,423.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="128.477,401.404,132.333,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="132.336,401.404,136.912,423.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="136.914,401.404,141.602,423.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="141.602,401.404,150.562,423.452" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="150.563,401.404,158.291,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="158.298,401.404,164.858,423.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="164.853,401.404,173.477,423.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="173.478,401.404,177.334,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="177.338,401.404,186.794,423.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="186.790,401.404,194.518,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="194.525,401.404,201.789,423.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="201.790,401.404,206.110,423.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="206.102,401.404,209.958,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="209.962,401.404,219.146,423.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="219.149,401.404,223.837,423.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="223.837,401.404,231.901,423.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="231.899,401.404,245.995,423.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="245.994,401.404,249.850,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="249.853,401.404,257.581,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="257.587,401.404,263.107,423.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="263.110,401.404,267.430,423.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="267.422,401.404,271.278,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="271.282,401.404,280.418,423.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="280.422,401.404,289.734,423.452" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="289.734,401.404,297.798,423.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="297.797,401.404,304.357,423.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="304.352,401.404,312.080,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="312.086,401.404,317.606,423.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="317.610,401.404,324.170,423.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="324.165,401.404,332.229,423.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="332.227,401.404,336.083,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="336.086,401.404,342.998,423.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="343.000,401.404,351.624,423.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="351.626,401.404,360.810,423.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="360.813,401.404,368.877,423.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="368.875,401.404,373.451,423.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="373.453,401.404,381.181,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="381.187,401.404,388.099,423.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="388.101,401.404,391.957,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="391.960,401.404,399.688,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="399.694,401.404,407.838,423.452" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="407.843,401.404,415.571,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="415.578,401.404,421.098,423.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="421.101,401.404,425.421,423.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="425.413,401.404,429.269,423.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="429.272,401.404,434.472,423.452" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="434.475,401.404,442.203,423.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="442.210,401.404,451.410,423.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="451.413,401.404,459.557,423.452" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="459.562,401.404,464.250,423.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="464.250,401.404,472.314,423.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="472.312,401.404,477.832,423.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="477.835,401.404,481.691,423.452" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,378.604,454.290,400.652">
<text font="OWDOPW+Georgia" bbox="50.000,378.604,59.200,400.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="59.203,378.604,63.779,400.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="63.781,378.604,68.357,400.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="68.358,378.604,76.422,400.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="76.421,378.604,90.517,400.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="90.515,378.604,97.779,400.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="97.781,378.604,106.405,400.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="106.406,378.604,112.966,400.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="112.962,378.604,122.098,400.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="122.102,378.604,129.830,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="129.837,378.604,136.397,400.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="136.392,378.604,140.248,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="140.251,378.604,144.939,400.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="144.939,378.604,154.123,400.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="154.126,378.604,157.982,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="157.986,378.604,163.506,400.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="163.509,378.604,171.237,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="171.243,378.604,185.339,400.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="185.338,378.604,194.474,400.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="194.478,378.604,203.102,400.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="203.104,378.604,209.664,400.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="209.659,378.604,213.515,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="213.518,378.604,221.246,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="221.253,378.604,229.397,400.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="229.402,378.604,237.130,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="237.136,378.604,242.656,400.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="242.659,378.604,246.515,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="246.518,378.604,251.206,400.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="251.206,378.604,260.390,400.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="260.394,378.604,264.250,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="264.253,378.604,272.205,400.652" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="272.198,378.604,276.886,400.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="276.886,378.604,282.406,400.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="282.410,378.604,290.474,400.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="290.472,378.604,298.200,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="298.206,378.604,302.526,400.652" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="302.518,378.604,306.374,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="306.378,378.604,321.210,400.652" size="22.048">M</text>
<text font="OWDOPW+Georgia" bbox="321.213,378.604,329.277,400.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="329.275,378.604,338.475,400.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="338.478,378.604,345.038,400.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="345.034,378.604,349.722,400.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="349.722,378.604,356.634,400.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="356.635,378.604,360.491,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="360.494,378.604,369.630,400.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="369.635,378.604,376.195,400.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="376.190,378.604,383.918,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="383.925,378.604,389.445,400.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="389.448,378.604,394.136,400.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="394.136,378.604,403.336,400.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="403.339,378.604,417.435,400.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="417.434,378.604,421.290,400.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="421.293,378.604,429.021,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="429.027,378.604,437.171,400.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="437.176,378.604,444.904,400.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="444.910,378.604,450.430,400.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="450.434,378.604,454.290,400.652" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,355.804,476.554,377.852">
<text font="OWDOPW+Georgia" bbox="50.000,355.804,58.064,377.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="58.062,355.804,62.638,377.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="62.640,355.804,67.328,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="67.328,355.804,76.288,377.852" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="76.282,355.804,85.482,377.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="85.485,355.804,93.213,377.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="93.219,355.804,98.739,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="98.742,355.804,103.062,377.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="103.054,355.804,106.910,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="106.914,355.804,111.490,377.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="111.491,355.804,119.219,377.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="119.226,355.804,126.490,377.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="126.491,355.804,132.011,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="132.014,355.804,141.214,377.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="141.218,355.804,148.130,377.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="148.131,355.804,151.987,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="151.990,355.804,157.510,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="157.514,355.804,162.202,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="162.202,355.804,171.658,377.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="171.654,355.804,178.918,377.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="178.920,355.804,183.608,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="183.608,355.804,192.792,377.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="192.795,355.804,201.995,377.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="201.998,355.804,211.454,377.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="211.451,355.804,216.971,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="216.974,355.804,221.294,377.852" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="221.286,355.804,225.142,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="225.146,355.804,234.906,377.852" size="22.048">P</text>
<text font="OWDOPW+Georgia" bbox="234.904,355.804,243.528,377.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="243.530,355.804,250.090,377.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="250.085,355.804,255.605,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="255.608,355.804,261.128,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="261.131,355.804,265.819,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="265.819,355.804,271.339,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="271.342,355.804,279.966,377.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="279.968,355.804,286.528,377.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="286.523,355.804,290.379,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="290.382,355.804,304.478,377.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="304.477,355.804,313.101,377.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="313.102,355.804,317.678,377.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="317.680,355.804,322.256,377.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="322.258,355.804,326.946,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="326.946,355.804,333.858,377.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="333.859,355.804,337.715,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="337.718,355.804,342.406,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="342.406,355.804,356.502,377.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="356.501,355.804,365.637,377.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="365.642,355.804,373.370,377.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="373.376,355.804,379.936,377.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="379.931,355.804,389.115,377.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="389.118,355.804,393.806,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="393.806,355.804,401.534,377.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="401.541,355.804,407.061,377.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="407.064,355.804,410.920,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="410.923,355.804,415.499,377.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="415.501,355.804,420.189,377.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="420.189,355.804,429.149,377.852" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="429.150,355.804,436.878,377.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="436.885,355.804,443.445,377.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="443.440,355.804,452.064,377.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="452.066,355.804,455.922,377.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="455.925,355.804,462.837,377.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="462.838,355.804,470.566,377.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="470.570,355.804,476.554,377.852" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="50.000,333.004,486.320,355.052">
<text font="OWDOPW+Georgia" bbox="50.000,333.004,59.456,355.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="59.453,333.004,67.181,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="67.187,333.004,74.451,355.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="74.453,333.004,79.973,355.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="79.976,333.004,89.176,355.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="89.179,333.004,96.091,355.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="96.093,333.004,99.949,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="99.952,333.004,109.088,355.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="109.093,333.004,118.293,355.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="118.296,333.004,122.872,355.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="122.874,333.004,130.826,355.052" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="130.819,333.004,135.507,355.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="135.507,333.004,144.963,355.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="144.960,333.004,153.024,355.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="153.022,333.004,159.582,355.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="159.578,333.004,163.898,355.052" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="163.890,333.004,167.746,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="167.749,333.004,178.197,355.052" size="22.048">E</text>
<text font="OWDOPW+Georgia" bbox="178.202,333.004,183.722,355.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="183.725,333.004,188.413,355.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="188.413,333.004,196.477,355.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="196.475,333.004,210.571,355.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="210.570,333.004,214.426,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="214.429,333.004,228.525,355.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="228.523,333.004,237.147,355.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="237.149,333.004,241.725,355.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="241.726,333.004,249.454,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="249.461,333.004,256.373,355.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="256.374,333.004,261.894,355.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="261.898,333.004,266.586,355.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="266.586,333.004,274.314,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="274.320,333.004,278.176,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="278.179,333.004,292.275,355.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="292.274,333.004,300.338,355.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="300.336,333.004,309.536,355.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="309.539,333.004,316.099,355.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="316.094,333.004,320.782,355.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="320.782,333.004,327.694,355.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="327.696,333.004,331.552,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="331.555,333.004,336.131,355.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="336.133,333.004,340.821,355.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="340.821,333.004,348.965,355.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="348.970,333.004,358.170,355.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="358.173,333.004,362.749,355.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="362.750,333.004,370.814,355.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="370.813,333.004,374.669,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="374.672,333.004,382.400,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="382.406,333.004,390.550,355.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="390.555,333.004,398.283,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="398.290,333.004,403.810,355.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="403.813,333.004,407.669,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="407.672,333.004,412.248,355.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="412.250,333.004,420.314,355.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="420.312,333.004,428.936,355.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="428.938,333.004,435.498,355.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="435.493,333.004,443.221,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="443.227,333.004,450.955,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="450.962,333.004,456.482,355.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="456.485,333.004,460.805,355.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="460.797,333.004,464.653,355.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="464.656,333.004,472.608,355.052" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="472.602,333.004,480.330,355.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="480.336,333.004,486.320,355.052" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="50.000,310.204,473.386,332.252">
<text font="OWDOPW+Georgia" bbox="50.000,310.204,59.312,332.252" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="59.312,310.204,64.000,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="64.000,310.204,71.264,332.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="71.266,310.204,80.466,332.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="80.469,310.204,85.045,332.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="85.046,310.204,93.110,332.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="93.109,310.204,96.965,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="96.968,310.204,104.696,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="104.702,310.204,109.278,332.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="109.280,310.204,117.008,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="117.014,310.204,121.702,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="121.702,310.204,126.902,332.252" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="126.906,310.204,134.634,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="134.640,310.204,144.096,332.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="144.093,310.204,153.277,332.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="153.280,310.204,157.600,332.252" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="157.592,310.204,161.448,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="161.451,310.204,172.683,332.252" size="22.048">R</text>
<text font="OWDOPW+Georgia" bbox="172.678,310.204,180.406,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="180.413,310.204,189.549,332.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="189.554,310.204,197.282,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="197.288,310.204,201.864,332.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="201.866,310.204,206.442,332.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="206.443,310.204,214.507,332.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="214.506,310.204,220.026,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="220.029,310.204,223.885,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="223.888,310.204,232.512,332.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="232.514,310.204,239.074,332.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="239.069,310.204,246.333,332.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="246.334,310.204,251.022,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="251.022,310.204,254.878,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="254.882,310.204,262.610,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="262.616,310.204,270.760,332.252" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="270.765,310.204,278.493,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="278.499,310.204,284.019,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="284.022,310.204,287.878,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="287.882,310.204,295.610,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="295.616,310.204,302.176,332.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="302.171,310.204,310.235,332.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="310.234,310.204,315.754,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="315.757,310.204,319.613,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="319.616,310.204,327.344,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="327.350,310.204,332.870,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="332.874,310.204,337.194,332.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="337.186,310.204,341.042,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="341.045,310.204,347.957,332.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="347.958,310.204,355.686,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="355.693,310.204,369.789,332.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="369.787,310.204,373.643,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="373.646,310.204,380.910,332.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="380.912,310.204,390.112,332.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="390.115,310.204,404.211,332.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="404.210,310.204,408.530,332.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="408.522,310.204,412.378,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="412.381,310.204,421.581,332.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="421.584,310.204,426.160,332.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="426.162,310.204,431.682,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="431.685,310.204,438.245,332.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="438.240,310.204,442.928,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="442.928,310.204,450.192,332.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="450.194,310.204,454.882,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="454.882,310.204,462.610,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="462.616,310.204,469.528,332.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="469.530,310.204,473.386,332.252" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,287.404,492.579,309.452">
<text font="OWDOPW+Georgia" bbox="50.000,287.404,56.912,309.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="56.914,287.404,65.538,309.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="65.539,287.404,70.115,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="70.117,287.404,74.693,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="74.694,287.404,79.382,309.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="79.382,287.404,86.646,309.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="86.648,287.404,91.336,309.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="91.336,287.404,96.856,309.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="96.859,287.404,106.059,309.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="106.062,287.404,115.246,309.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="115.250,287.404,119.938,309.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="119.938,287.404,129.394,309.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="129.390,287.404,133.246,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="133.250,287.404,141.314,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="141.312,287.404,155.408,309.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="155.406,287.404,163.134,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="163.141,287.404,168.661,309.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="168.664,287.404,172.520,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="172.523,287.404,180.251,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="180.258,287.404,184.834,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="184.835,287.404,192.563,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="192.570,287.404,197.258,309.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="197.258,287.404,202.458,309.452" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="202.461,287.404,210.189,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="210.195,287.404,219.651,309.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="219.648,287.404,228.832,309.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="228.835,287.404,232.691,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="232.694,287.404,241.878,309.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="241.882,287.404,250.506,309.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="250.507,287.404,255.083,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="255.085,287.404,263.709,309.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="263.710,287.404,270.270,309.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="270.266,287.404,274.122,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="274.125,287.404,283.581,309.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="283.578,287.404,292.778,309.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="292.781,287.404,297.357,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="297.358,287.404,301.934,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="301.936,287.404,310.000,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="309.998,287.404,324.094,309.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="324.093,287.404,327.949,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="327.952,287.404,335.680,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="335.686,287.404,342.246,309.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="342.242,287.404,350.306,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="350.304,287.404,355.824,309.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="355.827,287.404,360.147,309.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="360.139,287.404,363.995,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="363.998,287.404,378.094,309.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="378.093,287.404,386.157,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="386.155,287.404,390.731,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="390.733,287.404,398.461,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="398.467,287.404,405.379,309.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="405.381,287.404,414.581,309.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="414.584,287.404,422.648,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="422.646,287.404,431.830,309.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="431.834,287.404,439.898,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="439.896,287.404,443.752,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="443.755,287.404,451.483,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="451.490,287.404,458.402,309.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="458.403,287.404,463.923,309.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="463.926,287.404,467.782,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="467.786,287.404,472.362,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="472.363,287.404,480.091,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="480.098,287.404,488.722,309.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="488.723,287.404,492.579,309.452" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,264.604,482.642,286.652">
<text font="OWDOPW+Georgia" bbox="50.000,264.604,58.064,286.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="58.062,264.604,65.326,286.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="65.328,264.604,69.648,286.652" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="69.640,264.604,73.496,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="73.499,264.604,84.171,286.652" size="22.048">V</text>
<text font="OWDOPW+Georgia" bbox="84.163,264.604,92.227,286.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="92.226,264.604,98.786,286.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="98.781,264.604,103.469,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="103.469,264.604,112.669,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="112.672,264.604,119.584,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="119.586,264.604,123.442,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="123.445,264.604,132.901,286.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="132.898,264.604,140.962,286.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="140.960,264.604,146.480,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="146.483,264.604,155.107,286.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="155.109,264.604,164.069,286.652" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="164.062,264.604,173.262,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="173.266,264.604,180.994,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="181.000,264.604,184.856,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="184.859,264.604,190.379,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="190.382,264.604,199.582,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="199.586,264.604,206.146,286.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="206.141,264.604,215.277,286.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="215.282,264.604,219.970,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="219.970,264.604,226.882,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="226.883,264.604,230.739,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="230.742,264.604,238.470,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="238.477,264.604,243.053,286.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="243.054,264.604,250.782,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="250.789,264.604,264.885,286.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="264.883,264.604,272.611,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="272.618,264.604,282.074,286.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="282.070,264.604,287.590,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="287.594,264.604,296.794,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="296.797,264.604,310.893,286.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="310.891,264.604,314.747,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="314.750,264.604,322.478,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="322.485,264.604,329.397,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="329.398,264.604,334.918,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="334.922,264.604,339.242,286.652" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="339.234,264.604,343.090,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="343.093,264.604,355.077,286.652" size="22.048">D</text>
<text font="OWDOPW+Georgia" bbox="355.077,264.604,364.277,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="364.280,264.604,368.968,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="368.968,264.604,375.880,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="375.882,264.604,379.738,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="379.741,264.604,393.837,286.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="393.835,264.604,402.459,286.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="402.461,264.604,411.917,286.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="411.914,264.604,417.434,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="417.437,264.604,425.165,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="425.171,264.604,432.083,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="432.085,264.604,436.405,286.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="436.397,264.604,440.253,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="440.256,264.604,445.776,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="445.779,264.604,453.507,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="453.514,264.604,458.090,286.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="458.091,264.604,462.667,286.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="462.669,264.604,471.869,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="471.872,264.604,478.784,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="478.786,264.604,482.642,286.652" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,241.804,466.056,263.852">
<text font="OWDOPW+Georgia" bbox="50.000,241.804,54.576,263.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="54.578,241.804,63.202,263.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="63.203,241.804,72.163,263.852" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="72.165,241.804,80.789,263.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="80.790,241.804,87.350,263.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="87.346,241.804,92.866,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="92.869,241.804,97.557,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="97.557,241.804,104.469,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="104.470,241.804,108.326,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="108.330,241.804,112.906,263.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="112.907,241.804,120.971,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="120.970,241.804,128.234,263.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="128.235,241.804,137.435,263.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="137.438,241.804,144.350,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="144.352,241.804,148.208,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="148.211,241.804,156.275,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="156.274,241.804,170.370,263.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="170.368,241.804,178.096,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="178.102,241.804,183.622,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="183.626,241.804,187.482,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="187.485,241.804,195.549,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="195.547,241.804,202.107,263.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="202.102,241.804,209.366,263.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="209.368,241.804,218.568,263.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="218.571,241.804,222.427,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="222.430,241.804,230.158,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="230.165,241.804,235.685,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="235.688,241.804,240.008,263.852" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="240.000,241.804,243.856,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="243.859,241.804,250.099,263.852" size="22.048">I</text>
<text font="OWDOPW+Georgia" bbox="250.093,241.804,259.549,263.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="259.546,241.804,263.402,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="263.405,241.804,271.357,263.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="271.350,241.804,276.038,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="276.038,241.804,281.558,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="281.562,241.804,289.626,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="289.624,241.804,297.352,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="297.358,241.804,301.214,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="301.218,241.804,309.170,263.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="309.163,241.804,316.891,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="316.898,241.804,321.474,263.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="321.475,241.804,325.795,263.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="325.787,241.804,329.643,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="329.646,241.804,341.438,263.852" size="22.048">w</text>
<text font="OWDOPW+Georgia" bbox="341.443,241.804,346.131,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="346.131,241.804,353.043,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="353.045,241.804,357.733,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="357.733,241.804,361.589,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="361.592,241.804,369.656,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="369.654,241.804,375.174,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="375.178,241.804,379.498,263.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="379.490,241.804,383.346,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="383.349,241.804,388.037,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="388.037,241.804,397.221,263.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="397.224,241.804,401.080,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="401.083,241.804,410.219,263.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="410.224,241.804,416.784,263.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="416.779,241.804,424.843,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="424.842,241.804,432.570,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="432.576,241.804,439.488,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="439.490,241.804,447.218,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="447.224,241.804,456.680,263.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="456.677,241.804,462.197,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="462.200,241.804,466.056,263.852" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,219.004,479.765,241.052">
<text font="OWDOPW+Georgia" bbox="50.000,219.004,58.960,241.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="58.962,219.004,63.650,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="63.650,219.004,72.610,241.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="72.611,219.004,80.339,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="80.346,219.004,89.802,241.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="89.798,219.004,98.982,241.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="98.986,219.004,108.186,241.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="108.189,219.004,122.285,241.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="122.283,219.004,126.139,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="126.142,219.004,130.718,241.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="130.720,219.004,135.408,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="135.408,219.004,144.368,241.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="144.370,219.004,152.098,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="152.104,219.004,158.664,241.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="158.659,219.004,167.283,241.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="167.285,219.004,171.141,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="171.144,219.004,176.344,241.052" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="176.347,219.004,184.411,241.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="184.410,219.004,193.610,241.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="193.613,219.004,200.877,241.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="200.878,219.004,205.566,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="205.566,219.004,214.526,241.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="214.528,219.004,223.728,241.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="223.731,219.004,230.643,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="230.645,219.004,234.501,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="234.504,219.004,243.640,241.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="243.645,219.004,252.269,241.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="252.270,219.004,258.830,241.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="258.826,219.004,264.346,241.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="264.349,219.004,272.413,241.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="272.411,219.004,276.267,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="276.270,219.004,283.998,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="284.005,219.004,292.149,241.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="292.154,219.004,299.882,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="299.888,219.004,306.800,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="306.802,219.004,312.322,241.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="312.325,219.004,320.389,241.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="320.387,219.004,327.299,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="327.301,219.004,331.621,241.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="331.613,219.004,335.469,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="335.472,219.004,344.432,241.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="344.426,219.004,353.626,241.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="353.629,219.004,358.317,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="358.317,219.004,365.229,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="365.230,219.004,374.190,241.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="374.184,219.004,383.384,241.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="383.387,219.004,391.115,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="391.122,219.004,394.978,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="394.981,219.004,404.117,241.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="404.122,219.004,410.682,241.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="410.677,219.004,418.741,241.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="418.739,219.004,426.467,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="426.474,219.004,433.386,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="433.387,219.004,441.115,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="441.122,219.004,450.578,241.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="450.574,219.004,456.094,241.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="456.098,219.004,459.954,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="459.957,219.004,464.645,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="464.645,219.004,473.781,241.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="473.781,219.004,479.765,241.052" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="50.000,196.204,493.509,218.252">
<text font="OWDOPW+Georgia" bbox="50.000,196.204,56.912,218.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="56.914,196.204,66.114,218.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="66.117,196.204,80.213,218.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="80.211,196.204,84.067,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="84.070,196.204,89.270,218.252" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="89.274,196.204,97.002,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="97.008,196.204,103.568,218.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="103.563,196.204,117.659,218.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="117.658,196.204,125.386,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="125.392,196.204,134.848,218.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="134.845,196.204,140.365,218.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="140.368,196.204,149.568,218.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="149.571,196.204,163.667,218.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="163.666,196.204,167.522,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="167.525,196.204,176.661,218.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="176.666,196.204,181.242,218.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="181.243,196.204,189.307,218.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="189.306,196.204,196.570,218.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="196.571,196.204,204.299,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="204.306,196.204,210.866,218.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="210.861,196.204,218.925,218.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="218.923,196.204,224.443,218.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="224.446,196.204,228.302,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="228.306,196.204,233.826,218.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="233.829,196.204,241.557,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="241.563,196.204,255.659,218.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="255.658,196.204,264.794,218.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="264.798,196.204,273.422,218.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="273.424,196.204,279.984,218.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="279.979,196.204,284.299,218.252" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="284.291,196.204,288.147,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="288.150,196.204,298.422,218.252" size="22.048">C</text>
<text font="OWDOPW+Georgia" bbox="298.424,196.204,307.624,218.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="307.627,196.204,314.187,218.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="314.182,196.204,322.246,218.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="322.245,196.204,331.205,218.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="331.206,196.204,335.894,218.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="335.894,196.204,341.414,218.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="341.418,196.204,350.618,218.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="350.621,196.204,357.181,218.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="357.176,196.204,361.032,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="361.035,196.204,369.099,218.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="369.098,196.204,378.298,218.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="378.301,196.204,385.565,218.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="385.566,196.204,391.086,218.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="391.090,196.204,399.714,218.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="399.715,196.204,406.275,218.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="406.270,196.204,410.590,218.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="410.582,196.204,414.438,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="414.442,196.204,422.170,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="422.176,196.204,428.736,218.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="428.731,196.204,436.795,218.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="436.794,196.204,442.314,218.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="442.317,196.204,446.173,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="446.176,196.204,460.272,218.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="460.270,196.204,468.894,218.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="468.896,196.204,473.472,218.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="473.474,196.204,478.050,218.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="478.051,196.204,482.739,218.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="482.739,196.204,489.651,218.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="489.653,196.204,493.509,218.252" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,173.404,486.950,195.452">
<text font="OWDOPW+Georgia" bbox="50.000,173.404,56.912,195.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="56.914,173.404,64.642,195.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="64.648,173.404,73.832,195.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="73.835,173.404,77.691,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="77.694,173.404,82.894,195.452" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="82.898,173.404,92.098,195.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="92.101,173.404,99.013,195.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="99.014,173.404,106.278,195.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="106.280,173.404,114.008,195.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="114.014,173.404,118.334,195.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="118.326,173.404,122.182,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="122.186,173.404,127.706,195.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="127.709,173.404,136.909,195.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="136.912,173.404,143.472,195.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="143.467,173.404,152.603,195.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="152.608,173.404,157.296,195.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="157.296,173.404,164.208,195.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="164.210,173.404,168.066,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="168.069,173.404,176.021,195.452" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="176.014,173.404,180.702,195.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="180.702,173.404,188.654,195.452" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="188.648,173.404,196.712,195.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="196.710,173.404,210.806,195.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="210.805,173.404,220.005,195.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="220.008,173.404,226.920,195.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="226.922,173.404,230.778,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="230.781,173.404,238.845,195.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="238.843,173.404,242.699,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="242.702,173.404,251.886,195.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="251.890,173.404,256.578,195.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="256.578,173.404,263.842,195.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="263.843,173.404,269.363,195.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="269.366,173.404,278.566,195.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="278.570,173.404,292.666,195.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="292.664,173.404,299.576,195.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="299.578,173.404,305.098,195.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="305.101,173.404,308.957,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="308.960,173.404,316.224,195.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="316.226,173.404,324.850,195.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="324.851,173.404,334.307,195.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="334.304,173.404,342.448,195.452" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="342.453,173.404,351.653,195.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="351.656,173.404,359.384,195.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="359.390,173.404,363.246,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="363.250,173.404,377.346,195.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="377.344,173.404,385.408,195.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="385.406,173.404,393.550,195.452" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="393.555,173.404,403.011,195.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="403.008,173.404,407.696,195.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="407.696,173.404,414.608,195.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="414.610,173.404,418.930,195.452" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="418.922,173.404,422.778,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="422.781,173.404,433.517,195.452" size="22.048">A</text>
<text font="OWDOPW+Georgia" bbox="433.515,173.404,438.091,195.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="438.093,173.404,442.781,195.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="442.781,173.404,451.741,195.452" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="451.734,173.404,460.934,195.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="460.938,173.404,469.002,195.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="469.000,173.404,483.096,195.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="483.094,173.404,486.950,195.452" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,150.604,487.016,172.652">
<text font="OWDOPW+Georgia" bbox="50.000,150.604,58.064,172.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="58.062,150.604,72.158,172.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="72.157,150.604,79.885,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="79.891,150.604,85.411,172.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="85.414,150.604,89.270,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="89.274,150.604,98.474,172.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="98.477,150.604,103.053,172.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="103.054,150.604,107.630,172.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="107.632,150.604,115.696,172.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="115.694,150.604,129.790,172.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="129.789,150.604,137.053,172.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="137.054,150.604,145.678,172.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="145.680,150.604,152.240,172.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="152.235,150.604,161.371,172.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="161.376,150.604,169.104,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="169.110,150.604,175.670,172.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="175.666,150.604,179.522,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="179.525,150.604,188.709,172.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="188.712,150.604,193.400,172.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="193.400,150.604,201.544,172.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="201.549,150.604,211.005,172.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="211.002,150.604,215.690,172.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="215.690,150.604,222.602,172.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="222.603,150.604,229.515,172.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="229.517,150.604,234.205,172.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="234.205,150.604,248.301,172.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="248.299,150.604,252.155,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="252.158,150.604,266.254,172.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="266.253,150.604,274.877,172.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="274.878,150.604,279.454,172.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="279.456,150.604,287.184,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="287.190,150.604,294.102,172.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="294.104,150.604,299.624,172.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="299.627,150.604,304.315,172.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="304.315,150.604,312.043,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="312.050,150.604,316.370,172.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="316.362,150.604,320.218,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="320.221,150.604,327.133,172.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="327.134,150.604,334.862,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="334.869,150.604,344.053,172.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="344.056,150.604,347.912,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="347.915,150.604,362.011,172.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="362.010,150.604,370.634,172.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="370.635,150.604,375.211,172.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="375.213,150.604,379.789,172.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="379.790,150.604,384.478,172.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="384.478,150.604,391.390,172.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="391.392,150.604,395.712,172.652" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="395.704,150.604,399.560,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="399.563,150.604,409.467,172.652" size="22.048">T</text>
<text font="OWDOPW+Georgia" bbox="409.462,150.604,418.086,172.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="418.088,150.604,424.648,172.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="424.643,150.604,430.163,172.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="430.166,150.604,438.790,172.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="438.792,150.604,445.352,172.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="445.347,150.604,449.203,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="449.206,150.604,457.158,172.652" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="457.152,150.604,461.840,172.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="461.840,150.604,467.360,172.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="467.363,150.604,475.427,172.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="475.426,150.604,483.154,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="483.160,150.604,487.016,172.652" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,127.804,479.593,149.852">
<text font="OWDOPW+Georgia" bbox="50.000,127.804,55.520,149.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="55.523,127.804,64.147,149.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="64.149,127.804,70.709,149.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="70.704,127.804,76.224,149.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="76.227,127.804,84.851,149.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="84.853,127.804,91.413,149.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="91.408,127.804,95.264,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="95.267,127.804,102.995,149.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="103.002,127.804,109.562,149.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="109.557,127.804,118.181,149.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="118.182,127.804,125.094,149.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="125.096,127.804,128.952,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="128.955,127.804,140.747,149.852" size="22.048">w</text>
<text font="OWDOPW+Georgia" bbox="140.752,127.804,145.440,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="145.440,127.804,152.352,149.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="152.354,127.804,157.042,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="157.042,127.804,160.898,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="160.901,127.804,166.101,149.852" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="166.104,127.804,174.168,149.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="174.166,127.804,181.430,149.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="181.432,127.804,186.120,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="186.120,127.804,190.696,149.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="190.698,127.804,195.386,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="195.386,127.804,202.298,149.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="202.299,127.804,206.987,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="206.987,127.804,213.899,149.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="213.901,127.804,218.221,149.852" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="218.213,127.804,222.069,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="222.072,127.804,232.344,149.852" size="22.048">C</text>
<text font="OWDOPW+Georgia" bbox="232.346,127.804,240.970,149.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="240.971,127.804,250.427,149.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="250.424,127.804,257.336,149.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="257.338,127.804,265.066,149.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="265.072,127.804,272.336,149.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="272.338,127.804,277.858,149.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="277.861,127.804,285.589,149.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="285.595,127.804,291.115,149.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="291.118,127.804,300.318,149.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="300.322,127.804,308.050,149.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="308.056,127.804,314.616,149.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="314.611,127.804,318.467,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="318.470,127.804,326.534,149.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="326.533,127.804,333.093,149.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="333.088,127.804,340.352,149.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="340.354,127.804,349.554,149.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="349.557,127.804,353.413,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="353.416,127.804,358.104,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="358.104,127.804,367.240,149.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="367.245,127.804,374.157,149.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="374.158,127.804,383.358,149.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="383.362,127.804,397.458,149.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="397.456,127.804,401.312,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="401.315,127.804,409.939,149.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="409.941,127.804,416.501,149.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="416.496,127.804,425.952,149.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="425.949,127.804,434.013,149.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="434.011,127.804,440.571,149.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="440.566,127.804,448.294,149.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="448.301,127.804,452.157,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="452.160,127.804,461.296,149.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="461.301,127.804,469.029,149.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="469.035,127.804,473.611,149.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="473.609,127.804,479.593,149.852" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="50.000,105.004,480.730,127.052">
<text font="OWDOPW+Georgia" bbox="50.000,105.004,54.576,127.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="54.578,105.004,62.306,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="62.312,105.004,71.768,127.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="71.765,105.004,77.285,127.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="77.288,105.004,85.016,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="85.022,105.004,91.934,127.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="91.936,105.004,100.896,127.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="100.890,105.004,110.090,127.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="110.093,105.004,117.821,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="117.827,105.004,121.683,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="121.686,105.004,129.638,127.052" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="129.632,105.004,137.360,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="137.366,105.004,146.678,127.052" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="146.678,105.004,151.366,127.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="151.366,105.004,158.630,127.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="158.632,105.004,167.832,127.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="167.835,105.004,172.411,127.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="172.413,105.004,180.477,127.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="180.475,105.004,184.795,127.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="184.787,105.004,188.643,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="188.646,105.004,193.334,127.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="193.334,105.004,202.790,127.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="202.787,105.004,206.643,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="206.646,105.004,214.598,127.052" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="214.592,105.004,222.320,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="222.326,105.004,231.638,127.052" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="231.638,105.004,236.326,127.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="236.326,105.004,243.590,127.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="243.592,105.004,252.792,127.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="252.795,105.004,257.371,127.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="257.373,105.004,265.437,127.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="265.435,105.004,269.291,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="269.294,105.004,278.478,127.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="278.482,105.004,283.170,127.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="283.170,105.004,291.234,127.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="291.232,105.004,305.328,127.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="305.326,105.004,309.646,127.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="309.638,105.004,313.494,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="313.498,105.004,322.122,127.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="322.123,105.004,328.683,127.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="328.678,105.004,338.134,127.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="338.131,105.004,346.195,127.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="346.194,105.004,352.754,127.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="352.749,105.004,360.477,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="360.483,105.004,364.339,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="364.342,105.004,378.438,127.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="378.437,105.004,386.501,127.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="386.499,105.004,394.643,127.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="394.648,105.004,404.104,127.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="404.101,105.004,412.165,127.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="412.163,105.004,416.019,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="416.022,105.004,423.750,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="423.757,105.004,430.317,127.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="430.312,105.004,438.376,127.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="438.374,105.004,443.894,127.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="443.898,105.004,447.754,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="447.757,105.004,452.957,127.052" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="452.960,105.004,460.688,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="460.694,105.004,465.270,127.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="465.272,105.004,469.960,127.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="469.960,105.004,476.872,127.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="476.874,105.004,480.730,127.052" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,82.204,474.464,104.252">
<text font="OWDOPW+Georgia" bbox="50.000,82.204,61.792,104.252" size="22.048">w</text>
<text font="OWDOPW+Georgia" bbox="61.797,82.204,66.485,104.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="66.485,82.204,73.397,104.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="73.398,82.204,78.086,104.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="78.086,82.204,81.942,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="81.946,82.204,90.010,104.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="90.008,82.204,93.864,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="93.867,82.204,100.427,104.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="100.422,82.204,105.110,104.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="105.110,82.204,112.022,104.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="112.024,82.204,121.224,104.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="121.227,82.204,128.139,104.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="128.141,82.204,132.461,104.252" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="132.453,82.204,136.309,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="136.312,82.204,144.600,104.252" size="22.048">J</text>
<text font="OWDOPW+Georgia" bbox="144.594,82.204,153.794,104.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="153.797,82.204,160.709,104.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="160.710,82.204,166.230,104.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="166.234,82.204,174.858,104.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="174.859,82.204,178.715,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="178.718,82.204,183.918,104.252" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="183.922,82.204,191.650,104.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="191.656,82.204,198.216,104.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="198.211,82.204,212.307,104.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="212.306,82.204,220.034,104.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="220.040,82.204,229.496,104.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="229.493,82.204,235.013,104.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="235.016,82.204,244.216,104.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="244.219,82.204,258.315,104.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="258.314,82.204,262.170,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="262.173,82.204,266.861,104.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="266.861,82.204,276.045,104.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="276.048,82.204,280.368,104.252" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="280.360,82.204,284.216,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="284.219,82.204,299.051,104.252" size="22.048">M</text>
<text font="OWDOPW+Georgia" bbox="299.054,82.204,307.118,104.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="307.117,82.204,311.693,104.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="311.694,82.204,319.422,104.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="319.429,82.204,326.341,104.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="326.342,82.204,335.542,104.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="335.546,82.204,343.610,104.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="343.608,82.204,352.792,104.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="352.795,82.204,360.859,104.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="360.858,82.204,364.714,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="364.717,82.204,372.445,104.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="372.451,82.204,377.027,104.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="377.029,82.204,384.757,104.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="384.763,82.204,389.451,104.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="389.451,82.204,394.651,104.252" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="394.654,82.204,402.382,104.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="402.389,82.204,411.845,104.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="411.842,82.204,421.026,104.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="421.029,82.204,425.349,104.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="425.341,82.204,429.197,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="429.200,82.204,434.720,104.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="434.723,82.204,443.347,104.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="443.349,82.204,449.909,104.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="449.904,82.204,455.424,104.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="455.427,82.204,464.051,104.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="464.053,82.204,470.613,104.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="470.608,82.204,474.464,104.252" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="50.000,59.404,462.414,81.452">
<text font="OWDOPW+Georgia" bbox="50.000,59.404,64.096,81.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="64.094,59.404,72.718,81.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="72.720,59.404,77.296,81.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="77.298,59.404,85.026,81.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="85.032,59.404,91.944,81.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="91.946,59.404,97.466,81.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="97.469,59.404,102.157,81.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="102.157,59.404,109.885,81.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="109.891,59.404,114.211,81.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="114.203,59.404,118.059,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="118.062,59.404,126.126,81.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="126.125,59.404,129.981,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="129.984,59.404,135.184,81.452" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="135.187,59.404,144.387,81.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="144.390,59.404,151.302,81.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="151.304,59.404,158.568,81.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="158.570,59.404,166.298,81.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="166.304,59.404,170.160,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="170.163,59.404,178.227,81.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="178.226,59.404,182.082,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="182.085,59.404,190.037,81.452" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="190.030,59.404,197.758,81.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="197.765,59.404,202.341,81.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="202.342,59.404,206.198,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="206.202,59.404,213.930,81.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="213.936,59.404,219.456,81.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="219.459,59.404,223.779,81.452" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="223.771,59.404,227.627,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="227.630,59.404,242.462,81.452" size="22.048">M</text>
<text font="OWDOPW+Georgia" bbox="242.466,59.404,250.530,81.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="250.528,59.404,259.728,81.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="259.731,59.404,266.291,81.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="266.286,59.404,270.974,81.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="270.974,59.404,277.886,81.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="277.888,59.404,281.744,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="281.747,59.404,289.811,81.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="289.810,59.404,295.330,81.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="295.333,59.404,299.189,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="299.192,59.404,306.104,81.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="306.106,59.404,315.306,81.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="315.309,59.404,322.221,81.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="322.222,59.404,331.358,81.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="331.363,59.404,339.091,81.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="339.098,59.404,348.554,81.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="348.550,59.404,357.734,81.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="357.738,59.404,362.426,81.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="362.426,59.404,369.338,81.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="369.339,59.404,376.251,81.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="376.253,59.404,383.981,81.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="383.987,59.404,388.307,81.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="388.299,59.404,392.155,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="392.158,59.404,401.614,81.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="401.611,59.404,409.339,81.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="409.346,59.404,418.306,81.452" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="418.299,59.404,427.499,81.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="427.502,59.404,435.230,81.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="435.237,59.404,439.093,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="439.096,59.404,447.160,81.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="447.158,59.404,451.734,81.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="451.736,59.404,456.424,81.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="456.430,59.404,462.414,81.452" size="22.048">-</text>
<text>
</text>
</textline>
</textbox>
<textbox id="2" bbox="533.000,347.004,974.926,711.052">
<textline bbox="533.000,689.004,973.374,711.052">
<text font="OWDOPW+Georgia" bbox="533.000,689.004,541.960,711.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="541.954,689.004,551.154,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="551.157,689.004,559.221,711.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="559.219,689.004,573.315,711.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="573.314,689.004,577.170,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="577.173,689.004,582.373,711.052" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="582.376,689.004,590.440,711.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="590.438,689.004,599.638,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="599.642,689.004,606.906,711.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="606.907,689.004,611.595,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="611.595,689.004,620.555,711.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="620.557,689.004,629.757,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="629.760,689.004,636.672,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="636.674,689.004,640.530,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="640.533,689.004,648.597,711.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="648.595,689.004,657.779,711.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="657.782,689.004,662.470,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="662.470,689.004,671.606,711.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="671.611,689.004,676.299,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="676.299,689.004,683.211,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="683.213,689.004,690.477,711.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="690.478,689.004,695.166,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="695.166,689.004,704.622,711.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="704.619,689.004,712.763,711.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="712.768,689.004,717.088,711.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="717.080,689.004,720.936,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="720.939,689.004,728.891,711.052" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="728.885,689.004,733.573,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="733.573,689.004,741.525,711.052" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="741.518,689.004,749.582,711.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="749.581,689.004,763.677,711.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="763.675,689.004,772.875,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="772.878,689.004,779.790,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="779.792,689.004,783.648,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="783.651,689.004,788.339,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="788.339,689.004,797.795,711.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="797.792,689.004,802.112,711.052" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="802.104,689.004,805.960,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="805.963,689.004,821.579,711.052" size="22.048">W</text>
<text font="OWDOPW+Georgia" bbox="821.573,689.004,826.261,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="826.261,689.004,833.173,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="833.174,689.004,837.862,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="837.862,689.004,841.718,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="841.722,689.004,855.818,711.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="855.816,689.004,863.880,711.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="863.878,689.004,869.398,711.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="869.402,689.004,874.922,711.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="874.925,689.004,879.613,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="879.613,689.004,886.525,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="886.526,689.004,890.382,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="890.386,689.004,894.962,711.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="894.963,689.004,902.691,711.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="902.698,689.004,911.322,711.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="911.323,689.004,915.179,711.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="915.182,689.004,922.094,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="922.096,689.004,931.296,711.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="931.299,689.004,938.211,711.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="938.213,689.004,945.477,711.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="945.478,689.004,950.166,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="950.166,689.004,959.302,711.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="959.307,689.004,963.995,711.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="963.995,689.004,969.515,711.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="969.518,689.004,973.374,711.052" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,666.204,970.992,688.252">
<text font="OWDOPW+Georgia" bbox="533.000,666.204,542.456,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="542.453,666.204,550.181,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="550.187,666.204,557.451,688.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="557.453,666.204,561.309,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="561.312,666.204,569.376,688.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="569.374,666.204,583.470,688.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="583.469,666.204,591.197,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="591.203,666.204,596.723,688.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="596.726,666.204,601.046,688.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="601.038,666.204,604.894,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="604.898,666.204,614.354,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="614.350,666.204,619.038,688.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="619.038,666.204,625.950,688.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="625.952,666.204,630.528,688.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="630.530,666.204,634.386,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="634.389,666.204,639.589,688.252" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="639.592,666.204,647.320,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="647.326,666.204,653.886,688.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="653.882,666.204,667.978,688.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="667.976,666.204,675.704,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="675.710,666.204,685.166,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="685.163,666.204,690.683,688.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="690.686,666.204,699.886,688.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="699.890,666.204,713.986,688.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="713.984,666.204,717.840,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="717.843,666.204,723.363,688.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="723.366,666.204,731.094,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="731.101,666.204,745.197,688.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="745.195,666.204,754.331,688.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="754.336,666.204,762.960,688.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="762.962,666.204,769.522,688.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="769.517,666.204,773.373,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="773.376,666.204,781.440,688.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="781.438,666.204,788.702,688.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="788.704,666.204,792.560,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="792.563,666.204,800.627,688.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="800.626,666.204,804.946,688.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="804.938,666.204,808.794,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="808.797,666.204,816.861,688.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="816.859,666.204,826.059,688.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="826.062,666.204,834.206,688.252" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="834.211,666.204,843.411,688.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="843.414,666.204,851.142,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="851.149,666.204,855.005,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="855.008,666.204,859.696,688.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="859.696,666.204,869.152,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="869.149,666.204,873.005,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="873.008,666.204,880.736,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="880.742,666.204,885.318,688.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="885.320,666.204,893.048,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="893.054,666.204,897.742,688.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="897.742,666.204,902.942,688.252" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="902.946,666.204,910.674,688.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="910.680,666.204,920.136,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="920.133,666.204,929.317,688.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="929.320,666.204,933.176,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="933.179,666.204,937.867,688.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="937.867,666.204,947.323,688.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="947.320,666.204,951.176,688.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="951.179,666.204,955.867,688.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="955.867,666.204,965.003,688.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="965.008,666.204,970.992,688.252" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,643.404,964.781,665.452">
<text font="OWDOPW+Georgia" bbox="533.000,643.404,539.912,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="539.914,643.404,549.114,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="549.117,643.404,563.213,665.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="563.211,643.404,567.067,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="567.070,643.404,575.022,665.452" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="575.016,643.404,582.744,665.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="582.750,643.404,592.206,665.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="592.203,643.404,599.931,665.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="599.938,643.404,609.394,665.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="609.390,643.404,617.454,665.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="617.453,643.404,622.973,665.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="622.976,643.404,627.664,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="627.664,643.404,634.576,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="634.578,643.404,638.898,665.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="638.890,643.404,642.746,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="642.749,643.404,650.013,665.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="650.014,643.404,656.574,665.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="656.570,643.404,664.634,665.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="664.632,643.404,671.544,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="671.546,643.404,675.402,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="675.405,643.404,682.317,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="682.318,643.404,687.006,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="687.006,643.404,692.526,665.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="692.530,643.404,696.386,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="696.389,643.404,701.077,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="701.077,643.404,710.261,665.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="710.264,643.404,714.120,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="714.123,643.404,718.811,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="718.811,643.404,728.267,665.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="728.264,643.404,732.120,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="732.123,643.404,740.075,665.452" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="740.069,643.404,747.797,665.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="747.803,643.404,754.715,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="754.717,643.404,760.237,665.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="760.240,643.404,764.928,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="764.928,643.404,773.888,665.452" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="773.890,643.404,783.090,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="783.093,643.404,787.669,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="787.670,643.404,796.870,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="796.874,643.404,810.970,665.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="810.968,643.404,814.824,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="814.827,643.404,820.027,665.452" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="820.030,643.404,827.758,665.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="827.765,643.404,832.341,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="832.342,643.404,837.030,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="837.030,643.404,843.942,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="843.944,643.404,847.800,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="847.803,643.404,852.491,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="852.491,643.404,861.947,665.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="861.944,643.404,866.264,665.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="866.256,643.404,870.112,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="870.115,643.404,877.027,665.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="877.029,643.404,884.757,665.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="884.763,643.404,893.947,665.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="893.950,643.404,897.806,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="897.810,643.404,902.386,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="902.387,643.404,907.075,665.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="907.075,643.404,915.219,665.452" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="915.224,643.404,924.424,665.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="924.427,643.404,929.003,665.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="929.005,643.404,937.069,665.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="937.067,643.404,941.387,665.452" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="941.379,643.404,945.235,665.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="945.238,643.404,951.478,665.452" size="22.048">I</text>
<text font="OWDOPW+Georgia" bbox="951.472,643.404,960.928,665.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="960.925,643.404,964.781,665.452" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,620.604,963.570,642.652">
<text font="OWDOPW+Georgia" bbox="533.000,620.604,539.912,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="539.914,620.604,548.538,642.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="548.539,620.604,557.723,642.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="557.726,620.604,565.790,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="565.789,620.604,570.365,642.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="570.366,620.604,578.094,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="578.101,620.604,585.013,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="585.014,620.604,588.870,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="588.874,620.604,595.786,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="595.787,620.604,604.987,642.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="604.990,620.604,611.902,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="611.904,620.604,621.040,642.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="621.045,620.604,628.773,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="628.779,620.604,638.235,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="638.232,620.604,647.416,642.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="647.419,620.604,652.107,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="652.107,620.604,659.019,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="659.021,620.604,665.933,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="665.934,620.604,673.662,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="673.669,620.604,677.525,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="677.528,620.604,691.624,642.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="691.622,620.604,699.686,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="699.685,620.604,708.885,642.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="708.888,620.604,715.448,642.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="715.443,620.604,720.131,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="720.131,620.604,727.043,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="727.045,620.604,730.901,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="730.904,620.604,739.864,642.652" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="739.858,620.604,749.058,642.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="749.061,620.604,757.125,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="757.123,620.604,771.219,642.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="771.218,620.604,775.074,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="775.077,620.604,782.805,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="782.811,620.604,788.331,642.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="788.334,620.604,793.022,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="793.022,620.604,801.086,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="801.085,620.604,815.181,642.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="815.179,620.604,819.035,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="819.038,620.604,826.766,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="826.773,620.604,833.333,642.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="833.328,620.604,841.392,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="841.390,620.604,846.910,642.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="846.914,620.604,851.234,642.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="851.226,620.604,855.082,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="855.085,620.604,864.045,642.652" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="864.038,620.604,873.238,642.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="873.242,620.604,877.930,642.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="877.930,620.604,885.994,642.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="885.992,620.604,889.848,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="889.851,620.604,895.371,642.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="895.374,620.604,903.102,642.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="903.109,620.604,907.685,642.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="907.686,620.604,912.262,642.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="912.264,620.604,921.464,642.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="921.467,620.604,928.379,642.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="928.381,620.604,932.237,642.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="932.240,620.604,939.504,642.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="939.506,620.604,948.130,642.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="948.131,620.604,957.587,642.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="957.586,620.604,963.570,642.652" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,597.804,963.539,619.852">
<text font="OWDOPW+Georgia" bbox="533.000,597.804,540.952,619.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="540.946,597.804,549.010,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="549.008,597.804,553.584,619.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="553.586,597.804,558.162,619.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="558.163,597.804,562.851,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="562.851,597.804,569.763,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="569.765,597.804,573.621,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="573.624,597.804,581.352,619.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="581.358,597.804,587.918,619.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="587.914,597.804,596.538,619.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="596.539,597.804,603.451,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="603.453,597.804,607.309,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="607.312,597.804,613.872,619.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="613.867,597.804,623.179,619.852" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="623.179,597.804,631.803,619.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="631.805,597.804,641.261,619.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="641.258,597.804,648.522,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="648.523,597.804,657.723,619.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="657.726,597.804,664.638,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="664.640,597.804,668.496,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="668.499,597.804,677.683,619.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="677.686,597.804,682.374,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="682.374,597.804,690.438,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="690.437,597.804,704.533,619.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="704.531,597.804,708.387,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="708.390,597.804,717.014,619.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="717.016,597.804,723.576,619.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="723.571,597.804,730.835,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="730.837,597.804,735.525,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="735.525,597.804,739.845,619.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="739.837,597.804,743.693,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="743.696,597.804,752.832,619.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="752.837,597.804,761.461,619.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="761.462,597.804,768.022,619.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="768.018,597.804,773.538,619.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="773.541,597.804,781.605,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="781.603,597.804,785.459,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="785.462,597.804,790.038,619.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="790.040,597.804,797.768,619.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="797.774,597.804,805.038,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="805.040,597.804,810.560,619.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="810.563,597.804,819.763,619.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="819.766,597.804,826.678,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="826.680,597.804,830.536,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="830.539,597.804,838.267,619.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="838.274,597.804,845.186,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="845.187,597.804,852.099,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="852.101,597.804,859.829,619.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="859.835,597.804,863.691,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="863.694,597.804,871.758,619.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="871.757,597.804,880.941,619.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="880.944,597.804,885.632,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="885.632,597.804,894.768,619.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="894.773,597.804,899.461,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="899.461,597.804,906.373,619.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="906.374,597.804,913.638,619.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="913.640,597.804,918.328,619.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="918.328,597.804,927.784,619.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="927.781,597.804,935.925,619.852" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="935.930,597.804,939.786,619.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="939.789,597.804,948.925,619.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="948.930,597.804,957.554,619.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="957.555,597.804,963.539,619.852" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,575.004,964.216,597.052">
<text font="OWDOPW+Georgia" bbox="533.000,575.004,539.912,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="539.914,575.004,549.114,597.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="549.117,575.004,556.845,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="556.851,575.004,563.411,597.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="563.406,575.004,571.134,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="571.141,575.004,574.997,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="575.000,575.004,582.728,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="582.734,575.004,588.254,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="588.258,575.004,592.578,597.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="592.570,575.004,596.426,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="596.429,575.004,605.885,597.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="605.882,575.004,610.570,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="610.570,575.004,617.482,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="617.483,575.004,622.059,597.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="622.061,575.004,625.917,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="625.920,575.004,633.984,597.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="633.982,575.004,640.542,597.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="640.538,575.004,647.802,597.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="647.803,575.004,657.003,597.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="657.006,575.004,660.862,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="660.866,575.004,668.818,597.052" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="668.811,575.004,673.499,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="673.499,575.004,679.019,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="679.022,575.004,687.086,597.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="687.085,575.004,694.813,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="694.819,575.004,698.675,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="698.678,575.004,703.254,597.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="703.256,575.004,711.320,597.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="711.318,575.004,719.942,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="719.944,575.004,726.504,597.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="726.499,575.004,734.227,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="734.234,575.004,741.962,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="741.968,575.004,747.488,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="747.491,575.004,751.811,597.052" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="751.803,575.004,755.659,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="755.662,575.004,770.494,597.052" size="22.048">M</text>
<text font="OWDOPW+Georgia" bbox="770.498,575.004,779.122,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="779.123,575.004,785.683,597.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="785.678,575.004,794.638,597.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="794.640,575.004,799.328,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="799.328,575.004,803.184,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="803.187,575.004,807.875,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="807.875,575.004,817.331,597.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="817.328,575.004,822.848,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="822.851,575.004,830.579,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="830.586,575.004,838.730,597.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="838.734,575.004,846.462,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="846.469,575.004,853.029,597.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="853.024,575.004,856.880,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="856.883,575.004,870.979,597.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="870.978,575.004,879.602,597.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="879.603,575.004,884.179,597.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="884.181,575.004,891.909,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="891.915,575.004,898.827,597.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="898.829,575.004,904.349,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="904.352,575.004,909.040,597.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="909.040,575.004,916.768,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="916.774,575.004,921.094,597.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="921.086,575.004,924.942,597.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="924.946,575.004,933.010,597.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="933.008,575.004,947.104,597.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="947.102,575.004,954.830,597.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="954.837,575.004,960.357,597.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="960.360,575.004,964.216,597.052" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,552.204,974.926,574.252">
<text font="OWDOPW+Georgia" bbox="533.000,552.204,539.912,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="539.914,552.204,549.114,574.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="549.117,552.204,556.029,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="556.030,552.204,565.166,574.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="565.171,552.204,572.899,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="572.906,552.204,582.362,574.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="582.358,552.204,591.542,574.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="591.546,552.204,596.234,574.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="596.234,552.204,603.146,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="603.147,552.204,610.059,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="610.061,552.204,617.789,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="617.795,552.204,621.651,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="621.654,552.204,635.750,574.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="635.749,552.204,644.373,574.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="644.374,552.204,650.934,574.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="650.930,552.204,659.890,574.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="659.891,552.204,664.579,574.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="664.579,552.204,668.899,574.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="668.891,552.204,672.747,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="672.750,552.204,680.814,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="680.813,552.204,694.909,574.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="694.907,552.204,702.635,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="702.642,552.204,708.162,574.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="708.165,552.204,712.021,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="712.024,552.204,726.120,574.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="726.118,552.204,734.182,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="734.181,552.204,741.909,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="741.915,552.204,749.179,574.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="749.181,552.204,756.909,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="756.915,552.204,766.371,574.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="766.368,552.204,774.432,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="774.430,552.204,781.342,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="781.344,552.204,785.664,574.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="785.656,552.204,789.512,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="789.515,552.204,797.579,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="797.578,552.204,801.434,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="801.437,552.204,815.533,574.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="815.531,552.204,823.595,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="823.594,552.204,831.322,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="831.328,552.204,838.592,574.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="838.594,552.204,846.322,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="846.328,552.204,855.784,574.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="855.781,552.204,863.845,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="863.843,552.204,870.755,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="870.757,552.204,874.613,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="874.616,552.204,888.712,574.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="888.710,552.204,896.774,574.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="896.773,552.204,905.973,574.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="905.976,552.204,912.536,574.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="912.531,552.204,917.219,574.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="917.219,552.204,924.131,574.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="924.133,552.204,927.989,574.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="927.992,552.204,937.448,574.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="937.445,552.204,945.173,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="945.179,552.204,954.139,574.252" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="954.133,552.204,963.333,574.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="963.336,552.204,971.064,574.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="971.070,552.204,974.926,574.252" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,529.404,957.394,551.452">
<text font="OWDOPW+Georgia" bbox="533.000,529.404,542.136,551.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="542.141,529.404,548.701,551.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="548.696,529.404,557.320,551.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="557.322,529.404,562.010,551.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="562.010,529.404,571.466,551.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="571.462,529.404,575.318,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="575.322,529.404,584.778,551.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="584.774,529.404,589.462,551.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="589.462,529.404,596.374,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="596.376,529.404,600.952,551.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="600.954,529.404,604.810,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="604.813,529.404,618.909,551.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="618.907,529.404,627.531,551.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="627.533,529.404,632.109,551.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="632.110,529.404,636.686,551.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="636.688,529.404,641.376,551.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="641.376,529.404,648.288,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="648.290,529.404,652.610,551.452" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="652.602,529.404,656.458,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="656.461,529.404,665.437,551.452" size="22.048">S</text>
<text font="OWDOPW+Georgia" bbox="665.437,529.404,674.637,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="674.640,529.404,681.552,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="681.554,529.404,688.818,551.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="688.819,529.404,693.507,551.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="693.507,529.404,702.643,551.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="702.648,529.404,707.336,551.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="707.336,529.404,712.856,551.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="712.859,529.404,716.715,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="716.718,529.404,726.174,551.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="726.171,529.404,733.899,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="733.906,529.404,741.170,551.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="741.171,529.404,745.027,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="745.030,529.404,754.486,551.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="754.483,529.404,762.211,551.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="762.218,529.404,769.482,551.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="769.483,529.404,773.339,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="773.342,529.404,777.918,551.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="777.920,529.404,782.608,551.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="782.608,529.404,790.752,551.452" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="790.757,529.404,799.957,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="799.960,529.404,804.536,551.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="804.538,529.404,812.602,551.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="812.600,529.404,816.456,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="816.459,529.404,821.147,551.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="821.147,529.404,830.283,551.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="830.288,529.404,837.200,551.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="837.202,529.404,846.402,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="846.405,529.404,860.501,551.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="860.499,529.404,864.355,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="864.358,529.404,872.982,551.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="872.984,529.404,879.544,551.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="879.539,529.404,886.803,551.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="886.805,529.404,891.493,551.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="891.493,529.404,895.349,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="895.352,529.404,904.808,551.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="904.805,529.404,914.005,551.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="914.008,529.404,918.584,551.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="918.586,529.404,923.162,551.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="923.163,529.404,931.227,551.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="931.226,529.404,935.546,551.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="935.538,529.404,939.394,551.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="939.397,529.404,944.085,551.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="944.085,529.404,953.541,551.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="953.538,529.404,957.394,551.452" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,506.604,948.625,528.652">
<text font="OWDOPW+Georgia" bbox="533.000,506.604,537.576,528.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="537.578,506.604,546.202,528.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="546.203,506.604,552.763,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="552.758,506.604,560.486,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="560.493,506.604,574.589,528.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="574.587,506.604,578.443,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="578.446,506.604,583.134,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="583.134,506.604,592.270,528.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="592.275,506.604,599.187,528.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="599.189,506.604,608.389,528.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="608.392,506.604,622.488,528.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="622.486,506.604,626.342,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="626.346,506.604,635.482,528.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="635.486,506.604,644.110,528.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="644.112,506.604,651.024,528.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="651.026,506.604,660.226,528.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="660.229,506.604,667.957,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="667.963,506.604,674.523,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="674.518,506.604,682.246,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="682.253,506.604,686.109,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="686.112,506.604,695.312,528.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="695.315,506.604,700.835,528.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="700.838,506.604,704.694,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="704.698,506.604,713.658,528.652" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="713.651,506.604,722.851,528.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="722.854,506.604,727.542,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="727.542,506.604,734.454,528.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="734.456,506.604,738.312,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="738.315,506.604,747.515,528.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="747.518,506.604,752.094,528.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="752.096,506.604,757.616,528.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="757.619,506.604,764.179,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="764.174,506.604,768.862,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="768.862,506.604,776.126,528.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="776.128,506.604,783.856,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="783.862,506.604,790.774,528.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="790.776,506.604,795.096,528.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="795.088,506.604,798.944,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="798.947,506.604,803.523,528.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="803.525,506.604,811.253,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="811.259,506.604,818.523,528.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="818.525,506.604,824.045,528.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="824.048,506.604,833.248,528.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="833.251,506.604,840.163,528.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="840.165,506.604,844.021,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="844.024,506.604,851.752,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="851.758,506.604,859.902,528.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="859.907,506.604,867.635,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="867.642,506.604,873.162,528.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="873.165,506.604,877.021,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="877.024,506.604,886.160,528.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="886.165,506.604,892.725,528.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="892.720,506.604,897.408,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="897.408,506.604,911.504,528.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="911.502,506.604,916.190,528.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="916.190,506.604,923.102,528.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="923.104,506.604,926.960,528.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="926.963,506.604,934.915,528.652" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="934.909,506.604,942.637,528.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="942.641,506.604,948.625,528.652" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,483.804,973.031,505.852">
<text font="OWDOPW+Georgia" bbox="533.000,483.804,542.312,505.852" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="542.312,483.804,547.000,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="547.000,483.804,554.264,505.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="554.266,483.804,563.466,505.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="563.469,483.804,568.045,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="568.046,483.804,576.110,505.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="576.109,483.804,579.965,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="579.968,483.804,587.920,505.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="587.914,483.804,595.642,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="595.648,483.804,600.224,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="600.226,483.804,604.914,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="604.914,483.804,610.434,505.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="610.437,483.804,614.293,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="614.296,483.804,623.608,505.852" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="623.608,483.804,631.672,505.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="631.670,483.804,638.582,505.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="638.584,483.804,646.312,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="646.318,483.804,650.894,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="650.896,483.804,655.472,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="655.474,483.804,664.674,505.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="664.677,483.804,671.589,505.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="671.590,483.804,675.446,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="675.450,483.804,680.026,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="680.027,483.804,687.755,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="687.762,483.804,695.026,505.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="695.027,483.804,700.547,505.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="700.550,483.804,709.750,505.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="709.754,483.804,716.666,505.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="716.667,483.804,720.987,505.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="720.979,483.804,724.835,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="724.838,483.804,732.790,505.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="732.784,483.804,740.512,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="740.518,483.804,747.430,505.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="747.432,483.804,752.952,505.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="752.955,483.804,757.643,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="757.643,483.804,766.603,505.852" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="766.605,483.804,775.805,505.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="775.808,483.804,780.384,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="780.386,483.804,789.586,505.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="789.589,483.804,803.685,505.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="803.683,483.804,807.539,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="807.542,483.804,816.166,505.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="816.168,483.804,822.728,505.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="822.723,483.804,829.987,505.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="829.989,483.804,834.677,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="834.677,483.804,838.533,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="838.536,483.804,843.112,505.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="843.114,483.804,851.178,505.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="851.176,483.804,859.800,505.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="859.802,483.804,866.362,505.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="866.357,483.804,874.085,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="874.091,483.804,881.819,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="881.826,483.804,887.346,505.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="887.349,483.804,891.205,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="891.208,483.804,895.896,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="895.896,483.804,905.352,505.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="905.349,483.804,912.613,505.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="912.614,483.804,920.342,505.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="920.349,483.804,929.485,505.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="929.490,483.804,935.010,505.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="935.013,483.804,943.637,505.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="943.638,483.804,950.550,505.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="950.552,483.804,954.408,505.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="954.411,483.804,962.363,505.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="962.357,483.804,967.045,505.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="967.047,483.804,973.031,505.852" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,461.004,973.250,483.052">
<text font="OWDOPW+Georgia" bbox="533.000,461.004,538.520,483.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="538.523,461.004,546.587,483.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="546.590,461.004,554.318,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="554.322,461.004,558.642,483.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="558.629,461.004,562.485,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="562.488,461.004,570.552,483.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="570.555,461.004,576.075,483.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="576.078,461.004,579.934,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="579.938,461.004,587.202,483.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="587.205,461.004,595.829,483.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="595.832,461.004,605.288,483.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="605.291,461.004,612.203,483.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="612.206,461.004,619.934,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="619.938,461.004,627.202,483.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="627.205,461.004,632.725,483.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="632.728,461.004,640.456,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="640.459,461.004,645.979,483.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="645.982,461.004,655.182,483.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="655.186,461.004,662.914,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="662.917,461.004,669.477,483.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="669.464,461.004,673.320,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="673.323,461.004,681.387,483.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="681.390,461.004,695.486,483.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="695.490,461.004,703.218,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="703.221,461.004,708.741,483.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="708.744,461.004,712.600,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="712.603,461.004,720.331,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="720.334,461.004,725.854,483.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="725.858,461.004,729.714,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="729.717,461.004,736.981,483.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="736.984,461.004,745.608,483.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="745.611,461.004,755.067,483.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="755.070,461.004,761.982,483.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="761.986,461.004,769.714,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="769.717,461.004,776.981,483.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="776.984,461.004,782.504,483.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="782.507,461.004,790.235,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="790.238,461.004,795.758,483.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="795.762,461.004,804.962,483.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="804.965,461.004,812.693,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="812.696,461.004,819.256,483.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="819.243,461.004,823.563,483.052" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="823.550,461.004,827.406,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="827.410,461.004,837.682,483.052" size="22.048">C</text>
<text font="OWDOPW+Georgia" bbox="837.685,461.004,846.309,483.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="846.312,461.004,855.768,483.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="855.771,461.004,863.915,483.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="863.918,461.004,873.118,483.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="873.122,461.004,880.850,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="880.853,461.004,884.709,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="884.712,461.004,893.848,483.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="893.851,461.004,902.475,483.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="902.478,461.004,909.038,483.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="909.026,461.004,914.546,483.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="914.549,461.004,922.613,483.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="922.616,461.004,926.472,483.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="926.475,461.004,933.387,483.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="933.390,461.004,940.654,483.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="940.658,461.004,948.386,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="948.389,461.004,952.965,483.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="952.968,461.004,960.696,483.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="960.699,461.004,967.259,483.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="967.266,461.004,973.250,483.052" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,438.204,964.963,460.252">
<text font="OWDOPW+Georgia" bbox="533.000,438.204,537.688,460.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="537.688,438.204,544.600,460.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="544.602,438.204,553.562,460.252" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="553.555,438.204,562.755,460.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="562.758,438.204,570.486,460.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="570.493,438.204,574.349,460.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="574.352,438.204,583.488,460.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="583.493,438.204,590.053,460.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="590.048,438.204,598.112,460.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="598.110,438.204,605.838,460.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="605.845,438.204,612.757,460.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="612.758,438.204,620.486,460.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="620.493,438.204,629.949,460.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="629.946,438.204,635.466,460.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="635.469,438.204,639.325,460.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="639.328,438.204,647.392,460.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="647.390,438.204,652.910,460.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="652.914,438.204,657.234,460.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="657.226,438.204,661.082,460.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="661.085,438.204,665.661,460.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="665.662,438.204,673.726,460.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="673.725,438.204,680.989,460.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="680.990,438.204,690.190,460.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="690.194,438.204,697.106,460.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="697.107,438.204,700.963,460.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="700.966,438.204,708.918,460.252" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="708.912,438.204,716.640,460.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="716.646,438.204,723.558,460.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="723.560,438.204,729.080,460.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="729.083,438.204,733.771,460.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="733.771,438.204,742.731,460.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="742.733,438.204,751.933,460.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="751.936,438.204,756.512,460.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="756.514,438.204,765.714,460.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="765.717,438.204,779.813,460.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="779.811,438.204,783.667,460.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="783.670,438.204,791.398,460.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="791.405,438.204,796.925,460.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="796.928,438.204,800.784,460.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="800.787,438.204,808.851,460.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="808.850,438.204,814.370,460.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="814.373,438.204,818.229,460.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="818.232,438.204,827.416,460.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="827.419,438.204,832.107,460.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="832.107,438.204,840.251,460.252" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="840.256,438.204,849.712,460.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="849.709,438.204,854.397,460.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="854.397,438.204,861.309,460.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="861.310,438.204,868.222,460.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="868.224,438.204,872.912,460.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="872.912,438.204,887.008,460.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="887.006,438.204,890.862,460.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="890.866,438.204,898.130,460.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="898.131,438.204,904.691,460.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="904.686,438.204,912.750,460.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="912.749,438.204,919.661,460.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="919.662,438.204,923.518,460.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="923.522,438.204,932.722,460.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="932.725,438.204,939.285,460.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="939.280,438.204,948.736,460.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="948.733,438.204,956.797,460.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="956.795,438.204,961.115,460.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="961.107,438.204,964.963,460.252" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,415.404,970.586,437.452">
<text font="OWDOPW+Georgia" bbox="533.000,415.404,541.064,437.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="541.062,415.404,550.518,437.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="550.515,415.404,556.035,437.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="556.038,415.404,563.766,437.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="563.773,415.404,567.629,437.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="567.632,415.404,574.896,437.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="574.898,415.404,583.522,437.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="583.523,415.404,592.979,437.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="592.976,415.404,600.928,437.452" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="600.922,415.404,608.986,437.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="608.984,415.404,613.560,437.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="613.562,415.404,618.138,437.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="618.139,415.404,622.827,437.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="622.827,415.404,629.739,437.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="629.741,415.404,633.597,437.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="633.600,415.404,639.120,437.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="639.123,415.404,648.323,437.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="648.326,415.404,654.886,437.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="654.882,415.404,664.018,437.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="664.022,415.404,668.710,437.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="668.710,415.404,675.622,437.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="675.624,415.404,679.480,437.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="679.483,415.404,688.667,437.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="688.670,415.404,697.870,437.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="697.874,415.404,702.562,437.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="702.562,415.404,709.474,437.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="709.475,415.404,713.331,437.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="713.334,415.404,717.910,437.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="717.912,415.404,725.640,437.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="725.646,415.404,732.910,437.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="732.912,415.404,738.432,437.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="738.435,415.404,747.635,437.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="747.638,415.404,754.550,437.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="754.552,415.404,758.408,437.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="758.411,415.404,765.323,437.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="765.325,415.404,773.053,437.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="773.059,415.404,782.243,437.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="782.246,415.404,786.102,437.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="786.106,415.404,794.170,437.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="794.168,415.404,798.744,437.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="798.746,415.404,803.434,437.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="803.434,415.404,812.394,437.452" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="812.387,415.404,821.587,437.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="821.590,415.404,829.318,437.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="829.325,415.404,834.845,437.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="834.848,415.404,839.168,437.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="839.160,415.404,843.016,437.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="843.019,415.404,851.083,437.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="851.082,415.404,856.602,437.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="856.605,415.404,860.461,437.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="860.464,415.404,865.984,437.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="865.987,415.404,873.715,437.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="873.722,415.404,887.818,437.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="887.816,415.404,896.952,437.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="896.957,415.404,906.157,437.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="906.160,415.404,913.072,437.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="913.074,415.404,916.930,437.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="916.933,415.404,924.661,437.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="924.667,415.404,930.187,437.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="930.190,415.404,934.046,437.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="934.050,415.404,943.250,437.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="943.253,415.404,947.829,437.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="947.830,415.404,953.350,437.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="953.354,415.404,959.914,437.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="959.909,415.404,964.597,437.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="964.602,415.404,970.586,437.452" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,392.604,974.896,414.652">
<text font="OWDOPW+Georgia" bbox="533.000,392.604,540.264,414.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="540.266,392.604,544.954,414.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="544.954,392.604,552.682,414.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="552.688,392.604,559.600,414.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="559.602,392.604,563.922,414.652" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="563.914,392.604,567.770,414.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="567.773,392.604,578.221,414.652" size="22.048">E</text>
<text font="OWDOPW+Georgia" bbox="578.226,392.604,584.786,414.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="584.781,392.604,593.405,414.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="593.406,392.604,600.318,414.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="600.320,392.604,604.176,414.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="604.179,392.604,611.091,414.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="611.093,392.604,619.717,414.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="619.718,392.604,626.982,414.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="626.984,392.604,631.672,414.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="631.672,392.604,636.360,414.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="636.360,392.604,643.272,414.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="643.274,392.604,647.130,414.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="647.133,392.604,654.397,414.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="654.398,392.604,663.598,414.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="663.602,392.604,670.162,414.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="670.157,392.604,677.069,414.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="677.070,392.604,686.270,414.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="686.274,392.604,693.186,414.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="693.187,392.604,697.043,414.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="697.046,392.604,706.502,414.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="706.499,392.604,714.227,414.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="714.234,392.604,721.498,414.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="721.499,392.604,725.355,414.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="725.358,392.604,734.670,414.652" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="734.670,392.604,742.734,414.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="742.733,392.604,756.829,414.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="756.827,392.604,764.555,414.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="764.562,392.604,774.018,414.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="774.014,392.604,782.078,414.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="782.077,392.604,789.805,414.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="789.811,392.604,798.435,414.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="798.437,392.604,805.349,414.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="805.350,392.604,809.206,414.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="809.210,392.604,818.394,414.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="818.397,392.604,823.085,414.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="823.085,392.604,831.229,414.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="831.234,392.604,840.690,414.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="840.686,392.604,845.374,414.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="845.374,392.604,852.286,414.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="852.288,392.604,859.200,414.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="859.202,392.604,863.890,414.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="863.890,392.604,877.986,414.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="877.984,392.604,886.608,414.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="886.610,392.604,893.522,414.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="893.523,392.604,897.379,414.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="897.382,392.604,902.070,414.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="902.070,392.604,916.166,414.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="916.165,392.604,925.301,414.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="925.306,392.604,933.034,414.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="933.040,392.604,939.600,414.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="939.595,392.604,948.779,414.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="948.782,392.604,953.470,414.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="953.470,392.604,961.198,414.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="961.205,392.604,966.725,414.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="966.728,392.604,971.048,414.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="971.040,392.604,974.896,414.652" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,369.804,946.518,391.852">
<text font="OWDOPW+Georgia" bbox="533.000,369.804,537.576,391.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="537.578,369.804,546.778,391.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="546.781,369.804,554.045,391.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="554.046,369.804,559.566,391.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="559.570,369.804,568.770,391.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="568.773,369.804,575.685,391.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="575.686,369.804,579.542,391.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="579.546,369.804,587.610,391.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="587.608,369.804,594.872,391.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="594.874,369.804,598.730,391.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="598.733,369.804,606.461,391.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="606.467,369.804,613.027,391.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="613.022,369.804,621.646,391.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="621.648,369.804,628.560,391.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="628.562,369.804,632.418,391.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="632.421,369.804,639.333,391.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="639.334,369.804,647.062,391.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="647.069,369.804,656.253,391.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="656.256,369.804,660.112,391.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="660.115,369.804,669.299,391.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="669.302,369.804,677.926,391.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="677.928,369.804,682.504,391.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="682.506,369.804,691.130,391.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="691.131,369.804,697.691,391.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="697.686,369.804,701.542,391.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="701.546,369.804,709.274,391.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="709.280,369.804,716.192,391.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="716.194,369.804,721.714,391.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="721.717,369.804,725.573,391.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="725.576,369.804,732.488,391.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="732.490,369.804,740.218,391.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="740.224,369.804,749.408,391.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="749.411,369.804,753.267,391.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="753.270,369.804,767.366,391.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="767.365,369.804,775.429,391.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="775.427,369.804,782.339,391.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="782.341,369.804,789.253,391.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="789.254,369.804,797.318,391.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="797.317,369.804,801.173,391.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="801.176,369.804,809.128,391.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="809.122,369.804,816.850,391.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="816.856,369.804,823.768,391.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="823.770,369.804,829.290,391.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="829.293,369.804,833.981,391.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="833.981,369.804,842.941,391.852" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="842.942,369.804,852.142,391.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="852.146,369.804,856.722,391.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="856.723,369.804,865.923,391.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="865.926,369.804,880.022,391.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="880.021,369.804,884.341,391.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="884.333,369.804,888.189,391.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="888.192,369.804,892.768,391.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="892.770,369.804,901.394,391.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="901.395,369.804,910.355,391.852" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="910.357,369.804,918.981,391.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="918.982,369.804,925.542,391.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="925.538,369.804,931.058,391.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="931.061,369.804,935.749,391.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="935.749,369.804,942.661,391.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="942.662,369.804,946.518,391.852" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,347.004,908.579,369.052">
<text font="OWDOPW+Georgia" bbox="533.000,347.004,541.064,369.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="541.062,347.004,550.246,369.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="550.250,347.004,554.938,369.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="554.938,347.004,564.074,369.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="564.078,347.004,568.766,369.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="568.766,347.004,575.678,369.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="575.680,347.004,582.944,369.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="582.946,347.004,587.634,369.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="587.634,347.004,597.090,369.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="597.086,347.004,605.230,369.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="605.235,347.004,609.091,369.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="609.094,347.004,618.230,369.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="618.235,347.004,624.795,369.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="624.790,347.004,632.854,369.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="632.853,347.004,640.581,369.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="640.587,347.004,647.499,369.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="647.501,347.004,655.229,369.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="655.235,347.004,664.691,369.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="664.688,347.004,670.208,369.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="670.211,347.004,674.531,369.052" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="674.523,347.004,678.379,369.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="678.382,347.004,690.654,369.052" size="22.048">N</text>
<text font="OWDOPW+Georgia" bbox="690.656,347.004,698.384,369.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="698.390,347.004,705.654,369.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="705.656,347.004,709.512,369.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="709.515,347.004,717.243,369.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="717.250,347.004,723.810,369.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="723.805,347.004,732.429,369.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="732.430,347.004,739.342,369.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="739.344,347.004,743.200,369.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="743.203,347.004,750.931,369.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="750.938,347.004,760.138,369.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="760.141,347.004,763.997,369.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="764.000,347.004,770.560,369.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="770.555,347.004,775.243,369.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="775.243,347.004,784.427,369.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="784.430,347.004,789.118,369.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="789.118,347.004,796.382,369.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="796.384,347.004,805.584,369.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="805.587,347.004,810.163,369.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="810.165,347.004,819.365,369.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="819.368,347.004,826.280,369.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="826.282,347.004,830.138,369.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="830.141,347.004,834.717,369.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="834.718,347.004,839.406,369.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="839.406,347.004,848.366,369.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="848.368,347.004,856.096,369.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="856.102,347.004,862.662,369.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="862.658,347.004,871.282,369.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="871.283,347.004,875.139,369.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="875.142,347.004,880.342,369.052" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="880.346,347.004,888.074,369.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="888.080,347.004,892.656,369.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="892.658,347.004,897.346,369.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="897.346,347.004,904.258,369.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="904.259,347.004,908.579,369.052" size="22.048">.</text>
<text>
</text>
</textline>
</textbox>
<textbox id="3" bbox="533.000,59.404,978.648,332.252">
<textline bbox="533.000,310.204,978.648,332.252">
<text font="OWDOPW+Georgia" bbox="533.000,310.204,544.984,332.252" size="22.048">D</text>
<text font="OWDOPW+Georgia" bbox="544.984,310.204,553.608,332.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="553.610,310.204,563.066,332.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="563.062,310.204,570.790,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="570.797,310.204,578.061,332.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="578.062,310.204,581.918,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="581.922,310.204,589.986,332.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="589.984,310.204,596.544,332.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="596.539,310.204,603.803,332.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="603.805,310.204,613.005,332.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="613.008,310.204,616.864,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="616.867,310.204,623.427,332.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="623.422,310.204,628.110,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="628.110,310.204,635.022,332.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="635.024,310.204,644.224,332.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="644.227,310.204,651.139,332.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="651.141,310.204,654.997,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="655.000,310.204,664.184,332.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="664.187,310.204,668.875,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="668.875,310.204,676.939,332.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="676.938,310.204,691.034,332.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="691.032,310.204,694.888,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="694.891,310.204,702.955,332.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="702.954,310.204,717.050,332.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="717.048,310.204,724.776,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="724.782,310.204,730.302,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="730.306,310.204,734.162,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="734.165,310.204,741.077,332.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="741.078,310.204,745.766,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="745.766,310.204,751.286,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="751.290,310.204,755.610,332.252" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="755.602,310.204,759.458,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="759.461,310.204,769.733,332.252" size="22.048">C</text>
<text font="OWDOPW+Georgia" bbox="769.734,310.204,778.358,332.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="778.360,310.204,787.816,332.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="787.813,310.204,795.957,332.252" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="795.962,310.204,805.162,332.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="805.165,310.204,812.893,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="812.899,310.204,816.755,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="816.758,310.204,822.278,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="822.282,310.204,830.906,332.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="830.907,310.204,837.467,332.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="837.462,310.204,842.982,332.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="842.986,310.204,851.610,332.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="851.611,310.204,858.171,332.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="858.166,310.204,862.022,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="862.026,310.204,869.290,332.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="869.291,310.204,878.491,332.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="878.494,310.204,885.054,332.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="885.050,310.204,891.962,332.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="891.963,310.204,901.163,332.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="901.166,310.204,908.078,332.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="908.080,310.204,911.936,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="911.939,310.204,918.499,332.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="918.494,310.204,923.182,332.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="923.182,310.204,930.094,332.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="930.096,310.204,939.296,332.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="939.299,310.204,946.211,332.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="946.213,310.204,950.069,332.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="950.072,310.204,958.024,332.252" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="958.018,310.204,965.746,332.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="965.752,310.204,972.664,332.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="972.664,310.204,978.648,332.252" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,287.404,972.172,309.452">
<text font="OWDOPW+Georgia" bbox="533.000,287.404,538.520,309.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="538.523,287.404,543.211,309.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="543.211,287.404,552.171,309.452" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="552.173,287.404,561.373,309.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="561.376,287.404,565.952,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="565.954,287.404,575.154,309.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="575.157,287.404,589.253,309.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="589.251,287.404,593.107,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="593.110,287.404,600.374,309.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="600.376,287.404,609.000,309.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="609.002,287.404,623.098,309.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="623.096,287.404,637.192,309.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="637.190,287.404,645.814,309.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="645.816,287.404,655.000,309.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="655.003,287.404,663.627,309.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="663.629,287.404,667.485,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="667.488,287.404,676.944,309.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="676.941,287.404,681.629,309.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="681.629,287.404,688.541,309.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="688.542,287.404,693.118,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="693.120,287.404,697.440,309.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="697.432,287.404,701.288,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="701.291,287.404,705.867,309.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="705.869,287.404,715.069,309.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="715.072,287.404,722.336,309.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="722.338,287.404,727.858,309.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="727.861,287.404,737.061,309.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="737.064,287.404,743.976,309.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="743.978,287.404,747.834,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="747.837,287.404,755.901,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="755.899,287.404,765.099,309.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="765.102,287.404,773.246,309.452" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="773.251,287.404,782.451,309.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="782.454,287.404,790.182,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="790.189,287.404,794.045,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="794.048,287.404,802.112,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="802.110,287.404,816.206,309.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="816.205,287.404,823.933,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="823.939,287.404,829.459,309.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="829.462,287.404,833.318,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="833.322,287.404,842.282,309.452" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="842.275,287.404,851.475,309.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="851.478,287.404,856.166,309.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="856.166,287.404,863.078,309.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="863.080,287.404,866.936,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="866.939,287.404,875.003,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="875.002,287.404,882.730,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="882.736,287.404,892.192,309.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="892.189,287.404,899.917,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="899.923,287.404,907.987,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="907.986,287.404,917.442,309.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="917.438,287.404,921.294,309.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="921.298,287.404,935.394,309.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="935.392,287.404,943.456,309.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="943.454,287.404,951.182,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="951.189,287.404,958.453,309.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="958.454,287.404,966.182,309.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="966.188,287.404,972.172,309.452" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,264.604,959.426,286.652">
<text font="OWDOPW+Georgia" bbox="533.000,264.604,542.456,286.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="542.453,264.604,550.517,286.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="550.515,264.604,557.427,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="557.429,264.604,561.285,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="561.288,264.604,568.200,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="568.202,264.604,572.890,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="572.890,264.604,578.410,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="578.413,264.604,582.733,286.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="582.725,264.604,586.581,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="586.584,264.604,595.768,286.652" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="595.771,264.604,604.395,286.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="604.397,264.604,613.853,286.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="613.850,264.604,621.578,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="621.584,264.604,628.848,286.652" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="628.850,264.604,632.706,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="632.709,264.604,640.661,286.652" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="640.654,264.604,648.382,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="648.389,264.604,652.965,286.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="652.966,264.604,657.654,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="657.654,264.604,663.174,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="663.178,264.604,667.034,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="667.037,264.604,671.725,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="671.725,264.604,680.925,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="680.928,264.604,687.840,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="687.842,264.604,693.362,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="693.365,264.604,701.989,286.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="701.990,264.604,706.310,286.652" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="706.302,264.604,710.158,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="710.162,264.604,724.258,286.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="724.256,264.604,732.880,286.652" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="732.882,264.604,739.442,286.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="739.437,264.604,748.397,286.652" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="748.398,264.604,753.086,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="753.086,264.604,756.942,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="756.946,264.604,762.146,286.652" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="762.149,264.604,769.877,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="769.883,264.604,774.459,286.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="774.461,264.604,779.149,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="779.149,264.604,786.061,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="786.062,264.604,789.918,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="789.922,264.604,797.650,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="797.656,264.604,802.232,286.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="802.234,264.604,806.922,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="806.922,264.604,812.442,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="812.445,264.604,816.301,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="816.304,264.604,824.032,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="824.038,264.604,829.558,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="829.562,264.604,833.418,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="833.421,264.604,842.877,286.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="842.874,264.604,847.562,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="847.562,264.604,856.522,286.652" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="856.523,264.604,865.835,286.652" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="865.835,264.604,870.155,286.652" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="870.147,264.604,874.003,286.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="874.006,264.604,884.678,286.652" size="22.048">V</text>
<text font="OWDOPW+Georgia" bbox="884.670,264.604,892.398,286.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="892.405,264.604,899.317,286.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="899.318,264.604,904.838,286.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="904.842,264.604,909.530,286.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="909.530,264.604,918.490,286.652" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="918.491,264.604,927.691,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="927.694,264.604,932.270,286.652" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="932.272,264.604,941.472,286.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="941.475,264.604,955.571,286.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="955.570,264.604,959.426,286.652" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,241.804,976.509,263.852">
<text font="OWDOPW+Georgia" bbox="533.000,241.804,540.952,263.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="540.946,241.804,549.570,263.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="549.571,241.804,554.147,263.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="554.149,241.804,563.349,263.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="563.352,241.804,568.872,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="568.875,241.804,578.011,263.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="578.016,241.804,586.080,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="586.078,241.804,591.598,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="591.602,241.804,595.458,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="595.461,241.804,604.645,263.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="604.648,241.804,613.848,263.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="613.851,241.804,618.539,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="618.539,241.804,622.395,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="622.398,241.804,626.974,263.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="626.976,241.804,635.040,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="635.038,241.804,642.302,263.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="642.304,241.804,651.504,263.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="651.507,241.804,658.419,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="658.421,241.804,662.277,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="662.280,241.804,669.544,263.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="669.546,241.804,678.170,263.852" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="678.171,241.804,687.627,263.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="687.624,241.804,694.536,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="694.538,241.804,702.266,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="702.272,241.804,709.536,263.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="709.538,241.804,715.058,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="715.061,241.804,722.789,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="722.795,241.804,728.315,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="728.318,241.804,737.518,263.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="737.522,241.804,745.250,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="745.256,241.804,751.816,263.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="751.811,241.804,756.131,263.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="756.123,241.804,759.979,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="759.982,241.804,774.078,263.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="774.077,241.804,782.141,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="782.139,241.804,791.339,263.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="791.342,241.804,797.902,263.852" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="797.898,241.804,802.586,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="802.586,241.804,809.498,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="809.499,241.804,813.355,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="813.358,241.804,821.422,263.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="821.421,241.804,826.941,263.852" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="826.944,241.804,830.800,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="830.803,241.804,837.715,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="837.717,241.804,846.917,263.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="846.920,241.804,853.832,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="853.834,241.804,862.970,263.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="862.974,241.804,870.702,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="870.709,241.804,880.165,263.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="880.162,241.804,889.346,263.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="889.349,241.804,894.037,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="894.037,241.804,900.949,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="900.950,241.804,907.862,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="907.864,241.804,915.592,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="915.598,241.804,919.918,263.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="919.910,241.804,923.766,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="923.770,241.804,931.498,263.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="931.504,241.804,940.704,263.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="940.707,241.804,944.563,263.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="944.566,241.804,956.358,263.852" size="22.048">w</text>
<text font="OWDOPW+Georgia" bbox="956.363,241.804,961.051,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="961.051,241.804,967.963,263.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="967.965,241.804,972.653,263.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="972.653,241.804,976.509,263.852" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,219.004,972.968,241.052">
<text font="OWDOPW+Georgia" bbox="533.000,219.004,539.560,241.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="539.555,219.004,548.867,241.052" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="548.867,219.004,557.491,241.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="557.493,219.004,566.949,241.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="566.946,219.004,574.210,241.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="574.211,219.004,583.411,241.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="583.414,219.004,590.326,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="590.328,219.004,594.184,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="594.187,219.004,601.915,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="601.922,219.004,610.066,241.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="610.070,219.004,617.798,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="617.805,219.004,623.325,241.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="623.328,219.004,627.184,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="627.187,219.004,636.643,241.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="636.640,219.004,641.328,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="641.328,219.004,650.288,241.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="650.290,219.004,659.602,241.052" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="659.602,219.004,663.458,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="663.461,219.004,671.413,241.052" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="671.406,219.004,679.134,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="679.141,219.004,683.717,241.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="683.718,219.004,688.406,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="688.406,219.004,693.926,241.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="693.930,219.004,698.250,241.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="698.242,219.004,702.098,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="702.101,219.004,709.829,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="709.835,219.004,717.979,241.052" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="717.984,219.004,725.712,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="725.718,219.004,731.238,241.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="731.242,219.004,735.098,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="735.101,219.004,744.237,241.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="744.242,219.004,752.866,241.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="752.867,219.004,759.779,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="759.781,219.004,768.981,241.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="768.984,219.004,776.712,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="776.718,219.004,783.278,241.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="783.274,219.004,791.002,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="791.008,219.004,794.864,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="794.867,219.004,801.779,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="801.781,219.004,809.509,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="809.515,219.004,823.611,241.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="823.610,219.004,827.466,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="827.469,219.004,832.157,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="832.157,219.004,841.613,241.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="841.610,219.004,845.466,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="845.469,219.004,853.533,241.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="853.531,219.004,857.387,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="857.390,219.004,864.302,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="864.304,219.004,868.992,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="868.992,219.004,874.512,241.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="874.515,219.004,878.835,241.052" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="878.827,219.004,882.683,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="882.686,219.004,891.662,241.052" size="22.048">S</text>
<text font="OWDOPW+Georgia" bbox="891.662,219.004,900.286,241.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="900.288,219.004,907.552,241.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="907.554,219.004,912.242,241.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="912.242,219.004,920.866,241.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="920.867,219.004,927.779,241.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="927.781,219.004,936.741,241.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="936.734,219.004,945.934,241.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="945.938,219.004,949.794,241.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="949.797,219.004,959.253,241.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="959.250,219.004,966.978,241.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="966.984,219.004,972.968,241.052" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,196.204,975.363,218.252">
<text font="OWDOPW+Georgia" bbox="533.000,196.204,538.520,218.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="538.523,196.204,547.723,218.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="547.726,196.204,554.638,218.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="554.640,196.204,558.496,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="558.499,196.204,565.411,218.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="565.413,196.204,573.141,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="573.147,196.204,587.243,218.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="587.242,196.204,596.378,218.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="596.382,196.204,604.110,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="604.117,196.204,610.677,218.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="610.672,196.204,614.528,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="614.531,196.204,622.595,218.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="622.594,196.204,630.322,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="630.328,196.204,639.784,218.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="639.781,196.204,647.509,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="647.515,196.204,655.579,218.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="655.578,196.204,665.034,218.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="665.030,196.204,668.886,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="668.890,196.204,675.802,218.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="675.803,196.204,685.003,218.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="685.006,196.204,691.918,218.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="691.920,196.204,701.056,218.252" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="701.061,196.204,708.789,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="708.795,196.204,718.251,218.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="718.248,196.204,727.432,218.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="727.435,196.204,732.123,218.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="732.123,196.204,739.035,218.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="739.037,196.204,745.949,218.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="745.950,196.204,753.678,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="753.685,196.204,757.541,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="757.544,196.204,766.728,218.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="766.731,196.204,771.419,218.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="771.419,196.204,778.683,218.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="778.685,196.204,784.205,218.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="784.208,196.204,793.408,218.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="793.411,196.204,807.507,218.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="807.506,196.204,811.826,218.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="811.818,196.204,815.674,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="815.677,196.204,823.741,218.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="823.739,196.204,830.299,218.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="830.294,196.204,837.558,218.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="837.560,196.204,846.760,218.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="846.763,196.204,850.619,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="850.622,196.204,858.350,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="858.357,196.204,867.813,218.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="867.810,196.204,872.498,218.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="872.498,196.204,886.594,218.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="886.592,196.204,890.448,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="890.451,196.204,897.715,218.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="897.717,196.204,906.341,218.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="906.342,196.204,915.798,218.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="915.795,196.204,924.995,218.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="924.998,196.204,933.958,218.252" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="933.960,196.204,938.648,218.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="938.648,196.204,946.712,218.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="946.710,196.204,950.566,218.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="950.570,196.204,955.146,218.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="955.147,196.204,962.875,218.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="962.882,196.204,971.506,218.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="971.507,196.204,975.363,218.252" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,173.404,975.173,195.452">
<text font="OWDOPW+Georgia" bbox="533.000,173.404,542.456,195.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="542.453,173.404,551.653,195.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="551.656,173.404,556.232,195.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="556.234,173.404,560.810,195.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="560.811,173.404,568.875,195.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="568.874,173.404,572.730,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="572.733,173.404,580.797,195.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="580.795,173.404,588.059,195.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="588.061,173.404,591.917,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="591.920,173.404,601.376,195.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="601.373,173.404,606.061,195.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="606.061,173.404,615.021,195.452" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="615.022,173.404,624.334,195.452" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="624.334,173.404,628.654,195.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="628.646,173.404,632.502,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="632.506,173.404,641.642,195.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="641.646,173.404,650.846,195.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="650.850,173.404,657.410,195.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="657.405,173.404,666.605,195.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="666.608,173.404,673.520,195.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="673.522,173.404,677.378,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="677.381,173.404,686.693,195.452" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="686.693,173.404,694.421,195.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="694.427,173.404,703.883,195.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="703.880,173.404,713.064,195.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="713.067,173.404,719.627,195.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="719.622,173.404,727.350,195.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="727.357,173.404,733.917,195.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="733.912,173.404,738.600,195.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="738.600,173.404,744.120,195.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="744.123,173.404,747.979,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="747.982,173.404,757.182,195.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="757.186,173.404,762.706,195.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="762.709,173.404,766.565,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="766.568,173.404,780.664,195.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="780.662,173.404,788.726,195.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="788.725,173.404,794.245,195.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="794.248,173.404,799.768,195.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="799.771,173.404,804.459,195.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="804.459,173.404,811.371,195.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="811.373,173.404,815.229,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="815.232,173.404,824.688,195.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="824.685,173.404,832.413,195.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="832.419,173.404,839.683,195.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="839.685,173.404,843.541,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="843.544,173.404,857.640,195.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="857.638,173.404,865.702,195.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="865.701,173.404,873.429,195.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="873.435,173.404,880.699,195.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="880.701,173.404,888.429,195.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="888.435,173.404,897.891,195.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="897.888,173.404,905.952,195.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="905.950,173.404,912.862,195.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="912.864,173.404,917.184,195.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="917.176,173.404,921.032,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="921.035,173.404,929.995,195.452" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="929.989,173.404,939.189,195.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="939.192,173.404,947.816,195.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="947.818,173.404,951.674,195.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="951.677,173.404,959.741,195.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="959.739,173.404,967.003,195.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="967.005,173.404,971.325,195.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="971.317,173.404,975.173,195.452" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,150.604,960.211,172.652">
<text font="OWDOPW+Georgia" bbox="533.000,150.604,540.952,172.652" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="540.946,150.604,545.634,172.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="545.634,150.604,553.586,172.652" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="553.579,150.604,561.643,172.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="561.642,150.604,575.738,172.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="575.736,150.604,584.936,172.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="584.939,150.604,591.851,172.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="591.853,150.604,595.709,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="595.712,150.604,604.848,172.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="604.853,150.604,611.413,172.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="611.408,150.604,619.472,172.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="619.470,150.604,627.198,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="627.205,150.604,634.117,172.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="634.118,150.604,641.846,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="641.853,150.604,651.309,172.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="651.306,150.604,656.826,172.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="656.829,150.604,660.685,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="660.688,150.604,674.784,172.652" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="674.782,150.604,682.510,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="682.517,150.604,688.037,172.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="688.040,150.604,697.240,172.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="697.243,150.604,704.155,172.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="704.157,150.604,708.013,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="708.016,150.604,715.744,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="715.750,150.604,723.894,172.652" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="723.899,150.604,731.627,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="731.634,150.604,737.154,172.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="737.157,150.604,741.013,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="741.016,150.604,748.968,172.652" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="748.962,150.604,753.650,172.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="753.650,150.604,761.602,172.652" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="761.595,150.604,769.323,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="769.330,150.604,775.890,172.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="775.885,150.604,782.445,172.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="782.440,150.604,790.504,172.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="790.502,150.604,794.358,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="794.362,150.604,802.426,172.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="802.424,150.604,811.880,172.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="811.877,150.604,817.397,172.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="817.400,150.604,825.128,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="825.134,150.604,829.454,172.652" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="829.446,150.604,833.302,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="833.306,150.604,848.138,172.652" size="22.048">M</text>
<text font="OWDOPW+Georgia" bbox="848.141,150.604,856.205,172.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="856.203,150.604,865.403,172.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="865.406,150.604,871.966,172.652" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="871.962,150.604,876.650,172.652" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="876.650,150.604,883.562,172.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="883.563,150.604,887.419,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="887.422,150.604,895.486,172.652" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="895.485,150.604,901.005,172.652" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="901.008,150.604,904.864,172.652" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="904.867,150.604,911.779,172.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="911.781,150.604,920.981,172.652" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="920.984,150.604,927.896,172.652" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="927.898,150.604,937.034,172.652" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="937.038,150.604,944.766,172.652" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="944.773,150.604,954.229,172.652" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="954.227,150.604,960.211,172.652" size="22.048">-</text>
<text>
</text>
</textline>
<textline bbox="533.000,127.804,949.592,149.852">
<text font="OWDOPW+Georgia" bbox="533.000,127.804,542.184,149.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="542.187,127.804,546.875,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="546.875,127.804,553.787,149.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="553.789,127.804,560.701,149.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="560.702,127.804,568.430,149.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="568.437,127.804,572.757,149.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="572.749,127.804,576.605,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="576.608,127.804,586.064,149.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="586.061,127.804,593.789,149.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="593.795,127.804,602.755,149.852" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="602.749,127.804,611.949,149.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="611.952,127.804,619.680,149.852" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="619.686,127.804,623.542,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="623.546,127.804,631.610,149.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="631.608,127.804,636.184,149.852" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="636.186,127.804,640.874,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="640.874,127.804,649.834,149.852" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="649.827,127.804,659.027,149.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="659.030,127.804,667.094,149.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="667.093,127.804,681.189,149.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="681.187,127.804,685.043,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="685.046,127.804,690.246,149.852" size="22.048">f</text>
<text font="OWDOPW+Georgia" bbox="690.250,127.804,698.314,149.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="698.312,127.804,707.512,149.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="707.515,127.804,714.779,149.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="714.781,127.804,719.469,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="719.469,127.804,728.429,149.852" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="728.430,127.804,737.630,149.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="737.634,127.804,744.546,149.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="744.547,127.804,748.403,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="748.406,127.804,756.470,149.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="756.469,127.804,765.653,149.852" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="765.656,127.804,770.344,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="770.344,127.804,779.480,149.852" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="779.485,127.804,784.173,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="784.173,127.804,791.085,149.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="791.086,127.804,798.350,149.852" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="798.352,127.804,803.040,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="803.040,127.804,812.496,149.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="812.493,127.804,820.637,149.852" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="820.642,127.804,824.962,149.852" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="824.954,127.804,828.810,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="828.813,127.804,836.765,149.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="836.758,127.804,841.446,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="841.446,127.804,849.398,149.852" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="849.392,127.804,857.456,149.852" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="857.454,127.804,871.550,149.852" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="871.549,127.804,880.749,149.852" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="880.752,127.804,887.664,149.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="887.666,127.804,891.522,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="891.525,127.804,896.213,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="896.213,127.804,905.669,149.852" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="905.666,127.804,909.986,149.852" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="909.978,127.804,913.834,149.852" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="913.837,127.804,929.453,149.852" size="22.048">W</text>
<text font="OWDOPW+Georgia" bbox="929.446,127.804,934.134,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="934.134,127.804,941.046,149.852" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="941.048,127.804,945.736,149.852" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="945.736,127.804,949.592,149.852" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,105.004,953.722,127.052">
<text font="OWDOPW+Georgia" bbox="533.000,105.004,547.096,127.052" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="547.094,105.004,555.158,127.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="555.157,105.004,560.677,127.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="560.680,105.004,566.200,127.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="566.203,105.004,570.891,127.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="570.891,105.004,577.803,127.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="577.805,105.004,581.661,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="581.664,105.004,586.240,127.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="586.242,105.004,593.970,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="593.976,105.004,602.600,127.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="602.602,105.004,606.922,127.052" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="606.914,105.004,610.770,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="610.773,105.004,623.045,127.052" size="22.048">N</text>
<text font="OWDOPW+Georgia" bbox="623.046,105.004,631.110,127.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="631.109,105.004,636.629,127.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="636.632,105.004,645.256,127.052" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="645.258,105.004,654.218,127.052" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="654.211,105.004,663.411,127.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="663.414,105.004,671.142,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="671.149,105.004,675.005,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="675.008,105.004,684.144,127.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="684.149,105.004,688.725,127.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="688.726,105.004,696.790,127.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="696.789,105.004,704.053,127.052" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="704.054,105.004,711.782,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="711.789,105.004,718.349,127.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="718.344,105.004,726.408,127.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="726.406,105.004,731.926,127.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="731.930,105.004,735.786,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="735.789,105.004,742.701,127.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="742.702,105.004,750.430,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="750.437,105.004,759.621,127.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="759.624,105.004,763.480,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="763.483,105.004,770.395,127.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="770.397,105.004,775.085,127.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="775.085,105.004,780.605,127.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="780.608,105.004,784.464,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="784.467,105.004,793.779,127.052" size="22.048">h</text>
<text font="OWDOPW+Georgia" bbox="793.779,105.004,801.507,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="801.514,105.004,810.970,127.052" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="810.966,105.004,820.150,127.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="820.154,105.004,826.714,127.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="826.709,105.004,834.437,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="834.443,105.004,841.003,127.052" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="840.998,105.004,845.686,127.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="845.686,105.004,851.206,127.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="851.210,105.004,855.530,127.052" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="855.522,105.004,859.378,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="859.381,105.004,868.565,127.052" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="868.568,105.004,876.632,127.052" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="876.630,105.004,885.766,127.052" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="885.771,105.004,890.459,127.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="890.459,105.004,899.419,127.052" size="22.048">b</text>
<text font="OWDOPW+Georgia" bbox="899.421,105.004,908.621,127.052" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="908.624,105.004,915.536,127.052" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="915.538,105.004,919.394,127.052" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="919.397,105.004,927.349,127.052" size="22.048">v</text>
<text font="OWDOPW+Georgia" bbox="927.342,105.004,935.070,127.052" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="935.077,105.004,939.653,127.052" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="939.654,105.004,944.342,127.052" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="944.342,105.004,949.862,127.052" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="949.866,105.004,953.722,127.052" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,82.204,951.336,104.252">
<text font="OWDOPW+Georgia" bbox="533.000,82.204,547.096,104.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="547.094,82.204,555.718,104.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="555.720,82.204,560.296,104.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="560.298,82.204,568.026,104.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="568.032,82.204,574.944,104.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="574.946,82.204,580.466,104.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="580.469,82.204,585.157,104.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="585.157,82.204,593.221,104.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="593.219,82.204,600.947,104.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="600.954,82.204,604.810,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="604.813,82.204,609.389,104.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="609.390,82.204,617.118,104.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="617.125,82.204,625.749,104.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="625.750,82.204,629.606,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="629.610,82.204,637.674,104.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="637.672,82.204,641.992,104.252" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="641.984,82.204,645.840,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="645.843,82.204,655.043,104.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="655.046,82.204,660.566,104.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="660.570,82.204,664.426,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="664.429,82.204,669.005,104.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="669.006,82.204,677.630,104.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="677.632,82.204,684.192,104.252" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="684.187,82.204,691.915,104.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="691.922,82.204,706.018,104.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="706.016,82.204,709.872,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="709.875,82.204,716.787,104.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="716.789,82.204,721.477,104.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="721.477,82.204,726.997,104.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="727.000,82.204,730.856,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="730.859,82.204,738.587,104.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="738.594,82.204,744.114,104.252" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="744.117,82.204,747.973,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="747.976,82.204,752.552,104.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="752.554,82.204,760.618,104.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="760.616,82.204,767.880,104.252" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="767.882,82.204,777.082,104.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="777.085,82.204,783.997,104.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="783.998,82.204,787.854,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="787.858,82.204,795.922,104.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="795.920,82.204,800.496,104.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="800.498,82.204,805.186,104.252" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="805.186,82.204,814.146,104.252" size="22.048">q</text>
<text font="OWDOPW+Georgia" bbox="814.139,82.204,823.339,104.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="823.342,82.204,831.406,104.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="831.405,82.204,845.501,104.252" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="845.499,82.204,849.819,104.252" size="22.048">.</text>
<text font="OWDOPW+Georgia" bbox="849.811,82.204,853.667,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="853.670,82.204,862.646,104.252" size="22.048">S</text>
<text font="OWDOPW+Georgia" bbox="862.646,82.204,871.270,104.252" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="871.272,82.204,880.456,104.252" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="880.459,82.204,888.523,104.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="888.522,82.204,893.098,104.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="893.099,82.204,900.827,104.252" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="900.834,82.204,907.746,104.252" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="907.747,82.204,911.603,104.252" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="911.606,82.204,921.062,104.252" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="921.059,82.204,930.259,104.252" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="930.262,82.204,934.838,104.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="934.840,82.204,939.416,104.252" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="939.418,82.204,947.482,104.252" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="947.480,82.204,951.336,104.252" size="22.048"> </text>
<text>
</text>
</textline>
<textline bbox="533.000,59.404,921.635,81.452">
<text font="OWDOPW+Georgia" bbox="533.000,59.404,541.064,81.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="541.062,59.404,550.518,81.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="550.515,59.404,556.035,81.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="556.038,59.404,563.766,81.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="563.773,59.404,567.629,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="567.632,59.404,575.696,81.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="575.694,59.404,584.894,81.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="584.898,59.404,592.162,81.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="592.163,59.404,597.683,81.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="597.686,59.404,606.310,81.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="606.312,59.404,612.872,81.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="612.867,59.404,616.723,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="616.726,59.404,624.454,81.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="624.461,59.404,632.541,81.452" size="22.048">x</text>
<text font="OWDOPW+Georgia" bbox="632.539,59.404,639.803,81.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="639.805,59.404,647.533,81.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="647.539,59.404,656.675,81.452" size="22.048">p</text>
<text font="OWDOPW+Georgia" bbox="656.680,59.404,662.200,81.452" size="22.048">t</text>
<text font="OWDOPW+Georgia" bbox="662.203,59.404,671.403,81.452" size="22.048">u</text>
<text font="OWDOPW+Georgia" bbox="671.406,59.404,677.966,81.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="677.962,59.404,682.650,81.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="682.650,59.404,686.506,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="686.509,59.404,698.301,81.452" size="22.048">w</text>
<text font="OWDOPW+Georgia" bbox="698.306,59.404,702.994,81.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="702.994,59.404,709.906,81.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="709.907,59.404,714.595,81.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="714.595,59.404,718.915,81.452" size="22.048">,</text>
<text font="OWDOPW+Georgia" bbox="718.907,59.404,722.763,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="722.766,59.404,731.950,81.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="731.954,59.404,740.578,81.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="740.579,59.404,745.155,81.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="745.157,59.404,753.781,81.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="753.782,59.404,760.342,81.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="760.338,59.404,764.194,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="764.197,59.404,768.773,81.452" size="22.048">l</text>
<text font="OWDOPW+Georgia" bbox="768.774,59.404,776.838,81.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="776.837,59.404,784.101,81.452" size="22.048">c</text>
<text font="OWDOPW+Georgia" bbox="784.102,59.404,788.790,81.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="788.790,59.404,798.246,81.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="798.243,59.404,802.931,81.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="802.931,59.404,810.995,81.452" size="22.048">a</text>
<text font="OWDOPW+Georgia" bbox="810.994,59.404,814.850,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="814.853,59.404,824.037,81.452" size="22.048">d</text>
<text font="OWDOPW+Georgia" bbox="824.040,59.404,828.728,81.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="828.728,59.404,836.872,81.452" size="22.048">g</text>
<text font="OWDOPW+Georgia" bbox="836.877,59.404,846.333,81.452" size="22.048">n</text>
<text font="OWDOPW+Georgia" bbox="846.330,59.404,851.018,81.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="851.018,59.404,857.930,81.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="857.931,59.404,864.843,81.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="864.845,59.404,869.533,81.452" size="22.048">i</text>
<text font="OWDOPW+Georgia" bbox="869.533,59.404,883.629,81.452" size="22.048">m</text>
<text font="OWDOPW+Georgia" bbox="883.627,59.404,887.483,81.452" size="22.048"> </text>
<text font="OWDOPW+Georgia" bbox="887.486,59.404,895.214,81.452" size="22.048">e</text>
<text font="OWDOPW+Georgia" bbox="895.221,59.404,901.781,81.452" size="22.048">r</text>
<text font="OWDOPW+Georgia" bbox="901.776,59.404,910.400,81.452" size="22.048">o</text>
<text font="OWDOPW+Georgia" bbox="910.402,59.404,917.314,81.452" size="22.048">s</text>
<text font="OWDOPW+Georgia" bbox="917.315,59.404,921.635,81.452" size="22.048">.</text>
<text>
</text>
</textline>
</textbox>
<textbox id="4" bbox="965.827,18.003,973.003,35.917">
<textline bbox="965.827,18.003,973.003,35.917">
<text font="OWDOPW+Georgia" bbox="965.827,18.003,973.003,35.917" size="17.914">3</text>
<text>
</text>
</textline>
</textbox>
<rect linewidth="0" bbox="0.000,0.000,1024.000,748.000" />
<rect linewidth="0" bbox="0.000,0.000,1024.000,748.000" />
<line linewidth="0" bbox="512.000,40.000,512.000,708.000" />
<layout>
<textgroup bbox="50.000,18.003,978.648,711.052">
<textgroup bbox="50.000,59.404,493.509,711.052">
<textbox id="0" bbox="50.000,461.004,491.035,711.052" />
<textbox id="1" bbox="50.000,59.404,493.509,446.252" />
</textgroup>
<textgroup bbox="533.000,18.003,978.648,711.052">
<textgroup bbox="533.000,59.404,978.648,711.052">
<textbox id="2" bbox="533.000,347.004,974.926,711.052" />
<textbox id="3" bbox="533.000,59.404,978.648,332.252" />
</textgroup>
<textbox id="4" bbox="965.827,18.003,973.003,35.917" />
</textgroup>
</textgroup>
</layout>
</page>
</pages>
    """
    b = book(file)
    print ("[%s]" % b.toJson())
