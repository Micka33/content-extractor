mkdir install02500809
cd install02500809
# We suppose that the system has apt-get command already installed (if pdfimages is not available)
# We suppose that the system has curl command already installed
# We chech that pip exist on the system
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

# psd-tools dependencies
echo "Installing psd-tools dependecies\n"
echo "Now installing packbits\n"
sudo pip install packbits
echo "Now installing Pillow\n"
sudo pip install Pillow
echo "Now installing docops\n"
sudo pip install docopt
echo "Done psd-tools dependecies\n"

# Installing psd-tools
echo "Installing psd-tools\n"
sudo pip install psd-tools
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
sudo pip install beautifulsoup4
echo "Done beautifulsoup\n"

# If pdfimages is not available we install the lib poppler-utils which contains it 
echo "Checking pdfimages\n"
type pdfimages >/dev/null 2>&1 || {
                                    echo "pdfimages unavaliable\nNow installing poppler-utils\n"
                                    sudo apt-get install poppler-utils
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
