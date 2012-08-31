cp -a ~/dvizshok .
cd ~/ps4a
./android.py build ../frogs release install
cd ~/frogs
rm -rf dvizshok
rm -rf *.pyo
