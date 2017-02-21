cd ..

rm -r build
rm /home/diego/.local/lib/python3.5/site-packages/MAVProxy-1.4.38-py3.5.egg

python3.5 setup.py build install --user
python3.5 ./MAVProxy/MAVLinkServer.py --master=192.168.1.3:14550 --console
