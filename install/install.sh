mkdir install02500809
cd install02500809
echo "changing mode of /usr/local/etc to 775\n"
sudo chmod 775 /usr/local/etc
# We check the python2 avalaibility
echo "Checking python2 availability\n"
type python2 >/dev/null 2>&1 || { 
                                    echo "python2 unavaliable\nNow creating python2 as alias of python\n"
                                    alias python2="python"
                                }
echo "Done python2\n"
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
                                rm -rf pipInstall
                            }
echo "Done pip\n"

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
mkdir lcmsextract
tar xzf ../lcms-1.19.tar.gz --directory=./lcmsextract
cd lcmsextract/lcms-1.19
./configure
make
sudo make install
cd ../..
rm -rf lcmsextract
echo "Done pil dependecies\n"

# psd-tools dependencies
echo "Installing psd-tools dependecies\n"
echo "Now installing packbits\n"
sudo pip install -U packbits
echo "Now installing docops\n"
sudo pip install -U docopt
echo "Now installing pil\n"
sudo pip install -U pil
echo "Done psd-tools dependecies\n"


# Installing psd-tools
echo "Installing psd-tools\n"
sudo pip install -U psd-tools
echo "Done psd-tools\n"

# Installing pdfminer
echo "Installing pdfminer\n"
mkdir pdfminerInstall
cd pdfminerInstall
curl -O https://codeload.github.com/euske/pdfminer/zip/master
unzip master
cd pdfminer-master
make cmap
sudo python setup.py install
cd ../..
rm -rf pdfminerInstall
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
                                                                                                        brew install fontconfig
                                                                                                        brew link --overwrite fontconfig
                                                                                                        brew install poppler
                                                                                                        brew link --overwrite poppler
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
                                    rm -rf imagemagickInstall
                                }
echo "Done convert\n"
cd ..
rm -rf install02500809
