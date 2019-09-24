# CN-lab

https://www.nsnam.org/wiki/Installation#Ubuntu.2FDebian.2FMint


Configure ns-3 using command: ./waf configure --enable-examples
Build ns-3 using command: ./waf

Pyviz

$ python3 waf configure --enable-examples --enable-tests

$ ./waf clean
$ ./waf configure
$ ./build.py 
$ cd ns-allinone-3.30/netanim-3.108
$ ./waf --pyrun src/flow-monitor/examples/wifi-olsr-flowmon.py --vis

NetAnim
$ sudo apt-get install qt5-default mercurial
$ sudo synaptic

Valgrind
$ ./waf configure --disable-gtk --enable-examples --enable-tests
## ./waf --command-template="valgrind --leak-check=full --show-reachable=yes --track-origins=yes %s --suite=isotropic-antenna-model" --run scratch/first

https://www.nsnam.org/docs/manual/html/test-framework.html
$./test.py
