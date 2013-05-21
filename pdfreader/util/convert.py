#!/usr/bin/python
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter


class converter(object):

    def usage(self):
        print ('usage: %s [-d] [-p pagenos] [-m maxpages] [-P password] [-o output] [-C] '
               '[-n] [-A] [-V] [-M char_margin] [-L line_margin] [-W word_margin] [-F boxes_flow] '
               '[-Y layout_mode] [-O output_dir] [-t text|html|xml|tag] [-c codec] [-s scale] file ...' % self._argv[0])
        return 100

    def __init__(self):
        # debug option
        self._debug = 0
        # input option
        self._password = ''
        self._pagenos = set()
        self._maxpages = 0
        # output option
        self._outfile = None
        self._outtype = None
        self._imagewriter = None
        self._layoutmode = 'normal'
        self._codec = 'utf-8'
        self._pageno = 1
        self._scale = 1
        self._caching = True
        self._showpageno = True
        self._laparams = LAParams()
        self._argv = ['convert.py']
        self._args = []

    def mainIniter(self, argv):
        import getopt
        try:
            (opts, args) = getopt.getopt(argv[1:], 'dp:m:P:o:CnAVM:L:W:F:Y:O:t:c:s:')
        except getopt.GetoptError:
            return self.usage()
        if not args: return self.usage()
        for (k, v) in opts:
            if k == '-d': self._debug += 1
            elif k == '-p': self._pagenos.update( int(x)-1 for x in v.split(',') )
            elif k == '-m': self._maxpages = int(v)
            elif k == '-P': self._password = v
            elif k == '-o': self._outfile = v
            elif k == '-C': self._caching = False
            elif k == '-n': self._laparams = None
            elif k == '-A': self._laparams.all_texts = True
            elif k == '-V': self._laparams.detect_vertical = True
            elif k == '-M': self._laparams.char_margin = float(v)
            elif k == '-L': self._laparams.line_margin = float(v)
            elif k == '-W': self._laparams.word_margin = float(v)
            elif k == '-F': self._laparams.boxes_flow = float(v)
            elif k == '-Y': self._layoutmode = v
            elif k == '-O': self._imagewriter = ImageWriter(v)
            elif k == '-t': self._outtype = v
            elif k == '-c': self._codec = v
            elif k == '-s': self._scale = float(v)
        #
        self._argv = argv
        self._args = args
        #
        PDFDocument.debug = self._debug
        PDFParser.debug = self._debug
        CMapDB.debug = self._debug
        PDFResourceManager.debug = self._debug
        PDFPageInterpreter.debug = self._debug
        PDFDevice.debug = self._debug
        return self.run()

    """
    Output options
    """
    def with_debug(self, todo=True):
        self._debug = 1 if todo else 0
        return self

    def as_text(self, todo=True):
        self._outtype = 'text' if todo else None
        return self

    def as_xml(self, todo=True):
        self._outtype = 'xml' if todo else None
        return self

    def as_html(self, todo=True):
        self._outtype = 'html' if todo else None
        return self

    def as_tag(self, todo=True):
        self._outtype = 'tag' if todo else None
        return self

    def add_input_file(self, filename):
        self._args.append(filename)
        return self

    """
    Process the pdf file(s)
    """
    def run(self):
        rsrcmgr = PDFResourceManager(caching=self._caching)
        if not self._outtype:
            self._outtype = 'text'
            if __name__ == '__main__':
                if self._outfile:
                    if self._outfile.endswith('.htm') or self._outfile.endswith('.html'):
                        self._outtype = 'html'
                    elif self._outfile.endswith('.xml'):
                        self._outtype = 'xml'
                    elif self._outfile.endswith('.tag'):
                        self._outtype = 'tag'
        if __name__ == '__main__':
            if self._outfile:
                outfp = file(self._outfile, 'w')
            else:
                outfp = sys.stdout
        else:
            from cStringIO import StringIO
            outfp = StringIO()
        if self._outtype == 'text':
            device = TextConverter(rsrcmgr, outfp, codec=self._codec, laparams=self._laparams, imagewriter=self._imagewriter)
        elif self._outtype == 'xml':
            device = XMLConverter(rsrcmgr, outfp, codec=self._codec, laparams=self._laparams, imagewriter=self._imagewriter)
        elif self._outtype == 'html':
            device = HTMLConverter(rsrcmgr, outfp, codec=self._codec, scale=self._scale, layoutmode=self._layoutmode, laparams=self._laparams, imagewriter=self._imagewriter)
        elif self._outtype == 'tag':
            device = TagExtractor(rsrcmgr, outfp, codec=self._codec)
        else:
            return usage()
        for fname in self._args:
            fp = file(fname, 'rb')
            process_pdf(rsrcmgr, device, fp, self._pagenos, maxpages=self._maxpages, password=self._password, caching=self._caching, check_extractable=True)
            fp.close()
        device.close()
        if __name__ == '__main__':
            outfp.close()
        else:
            return outfp.getvalue()




if __name__ == '__main__':
    import sys
    sys.exit(converter().mainIniter(sys.argv))