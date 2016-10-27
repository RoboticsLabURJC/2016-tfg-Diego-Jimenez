##MAVProxy

This is a MAVLink ground station written in python. 

##MAVProxy-Server
MAVProxy-Server is the same mavproxy with one addition feature:

You can run mavproxy as a Tcp/Udp server which allows you to read/write mavlink commands remotely.

###Usage 

To run a TCP server:

```
	mavproxy.py --tcp=0.0.0.0:5234	
```

To run a UDP server:

```
	mavproxy.py --udp=0.0.0.0:5234
```

>You can run both TCP and UDP servers simultaneously, but only the UDP server will be able to write mavlink commands. This is not advised.

###Test
To test the connection, connect to the server using `nc`.

Example to connect to TCP server from the same machine:

```
	nc 127.0.0.1 5234 -v
```

> Add -u option to connect to UDP server

###Implementation
See [my blog](http://nasa.z-proj.com/mavproxy-server-implementation) for how this was created.

----

Please see http://Dronecode.github.io/MAVProxy/ for more information

This ground station was developed as part of the CanberraUAV OBC team
entry

###License

MAVProxy is released under the GNU General Public License v3 or later
MAVProxy-Server is released under the GNU General Public License v3 or later

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Dronecode/MAVProxy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)