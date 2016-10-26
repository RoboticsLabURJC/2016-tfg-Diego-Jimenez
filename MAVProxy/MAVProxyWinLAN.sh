cd ..
python setup.py build install --user
#python ./MAVProxy/mavproxy.py --master=192.168.1.3:14550 --console
python ./MAVProxy/mavproxy.py --master=10.1.1.191:14550 --console
