cd ..

python2.7 setup.py build install --user
python2.7 ./MAVProxy/mavproxy.py uav_viewer_py.yml --master=10.1.1.191:14550 --console
#python2.7 ./MAVProxy/mavproxy.py --master=0.0.0.0:14550 --console
