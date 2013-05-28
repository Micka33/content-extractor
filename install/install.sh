mkdir install02500809
cd install02500809
# We suppose that the system has apt-get command already installed (if pdfimages is not available)
# We suppose that the system has curl command already installed
# We check that pip exist on the system
echo "Checking pip availability\n"
type pip >/dev/null 2>&1 || { 
                                echo "pip unavaliable\nNow installing pip\n"
                                mkdir pipInstall
                                cd pipInstall
                                curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
                                sudo python get-pip.py
                                cd ..
                                sudo rm -rf pipInstall
                            }
echo "Done pip\n"
# We check that easy_install exist on the system
echo "Checking easy_install availability\n"
type easy_install >/dev/null 2>&1 || {
                                        echo "easy_install unavailable\nNow installing easy_install"
                                        mkdir easy_install
                                        cd easy_install
                                        curl -O https://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg
                                        sudo sh setuptools-0.6c9-py2.4.egg
                                        cd ..
                                        sudo rm -rf easy_install
                                     }
echo "Done easy_install\n"

# pil dependencies
echo "Installing pil dependecies\n"
type apt-get >/dev/null 2>&1 && {
                                    sudo apt-get install libjpeg libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
                                 } || {
                                    type brew >/dev/null 2>&1 && {
                                                                    brew install jpeg freetype
                                                                    brew tap homebrew/dupes
                                                                    brew install zlib
                                                                 }
                                 }

ls -la
mkdir lcmsextract
tar xzf ../lcms-1.19.tar.gz --directory=./lcmsextract
cd lcmsextract/lcms-1.19
./configure
make
sudo make install
cd ../..
sudo rm -rf lcmsextract
echo "Done pil dependecies\n"

# psd-tools dependencies
echo "Installing psd-tools dependecies\n"
echo "Now installing packbits\n"
sudo pip install -U packbits
echo "Now installing Pillow\n"
sudo pip install -U Pillow
echo "Now installing docops\n"
sudo pip install -U docopt
echo "Now installing pil\n"
sudo easy_install pil
echo "Done psd-tools dependecies\n"


# Installing psd-tools
echo "Installing psd-tools\n"
sudo pip install -U psd-tools
echo "Done psd-tools\n"

# Installing pdfminer
echo "Installing pdfminer\n"
mkdir pdfminerInstall
cd pdfminerInstall
curl -O  https://pypi.python.org/packages/source/p/pdfminer/pdfminer-20110515.tar.gz
tar xvfz pdfminer-20110515.tar.gz
cd pdfminer-20110515
make cmap
sudo python setup.py install
cd ../..
sudo rm -rf pdfminerInstall
echo "Done pdfminer\n"

# Installing beautifullsoup
echo "Installing beautifulsoup\n"
sudo pip install -U beautifulsoup4
echo "Done beautifulsoup\n"

# If pdfimages is not available we install the lib poppler-utils which contains it 
echo "Checking pdfimages\n"
type pdfimages >/dev/null 2>&1 || {
                                    echo "pdfimages unavaliable\nNow installing poppler-utils\n"
                                    type apt-get >/dev/null 2>&1 && {
                                                                        sudo apt-get install poppler-utils
                                                                     } || {
                                                                        type brew >/dev/null 2>&1 && {
                                                                                                        brew install xpdf
                                                                                                        brew install poppler
                                                                                                     }
                                                                     }
                                  }
echo "Done pdfimages\n"

#If convert is not avalable we install the lib imagemagick which contains it
echo "Checking convert\n"
type convert >/dev/null 2>&1 || { 
                                    echo "convert unavaliable\nNow installing imagemagick\n"
                                    mkdir imagemagickInstall
                                    cd imagemagickInstall
                                    curl -O http://www.imagemagick.org/download/ImageMagick.tar.gz
                                    tar xvfz ImageMagick.tar.gz
                                    cd ImageMagick-6.8.5-8
                                    ./configure
                                    make
                                    sudo make install
                                    sudo ldconfig /usr/local/lib
                                    cd ../..
                                    sudo rm -rf imagemagickInstall
                                }
echo "Done convert\n"
cd ..
sudo rm -rf install02500809
