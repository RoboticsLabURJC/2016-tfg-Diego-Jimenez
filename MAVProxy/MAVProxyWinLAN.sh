cd ..

rm -r build
rm /home/diego/.local/lib/python3.5/site-packages/MAVProxy-1.4.38-py3.5.egg

python3.5 setup.py build install --user
#python3.5 ./MAVProxy/mavproxy.py --master=10.1.1.191:14550 --console
python3.5 ./MAVProxy/mavproxy.py --master=0.0.0.0:14550 --console
