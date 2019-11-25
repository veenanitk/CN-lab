sudo ip netns add one 
sudo ip netns add two 
sudo ip netns add r1
sudo ip netns add r2

sudo ip link add name mid0 type veth peer name mid1
sudo ip link add name mid2 type veth peer name mid3

# veth btw routers

sudo ip link add name mid4 type veth peer name mid5

sudo ip link set mid0 netns one
sudo ip link set mid3 netns two

sudo ip link set mid1 netns r1
sudo ip link set mid2 netns r2

sudo ip link set mid4 netns r1
sudo ip link set mid5 netns r2

sudo ip netns exec one ip link set lo up
sudo ip netns exec two ip link set lo up
sudo ip netns exec r1 ip link set lo up
sudo ip netns exec r2 ip link set lo up

sudo ip netns exec one ip link set mid0 up
sudo ip netns exec r1 ip link set mid1 up
sudo ip netns exec two ip link set mid3 up
sudo ip netns exec r2 ip link set mid2 up
sudo ip netns exec r1 ip link set mid4 up
sudo ip netns exec r2 ip link set mid5 up

sudo ip netns exec one ip address add 10.0.0.1/24 dev mid0
sudo ip netns exec r1 ip address add 10.0.0.2/24 dev mid1

sudo ip netns exec two ip address add 10.0.2.1/24 dev mid3
sudo ip netns exec r2 ip address add 10.0.2.2/24 dev mid2

sudo ip netns exec r1 ip address add 10.0.3.1/24 dev mid4
sudo ip netns exec r2 ip address add 10.0.3.2/24 dev mid5

sudo ip netns exec one ip route add default via 10.0.0.2 dev mid0
sudo ip netns exec two ip route add default via 10.0.2.2 dev mid3

sudo ip netns exec r1 ip route add default via 10.0.3.2 dev mid4
sudo ip netns exec r2 ip route add default via 10.0.3.1 dev mid5

sudo ip netns exec r1 sysctl -w net.ipv4.ip_forward=1

sudo ip netns exec r2 sysctl -w net.ipv4.ip_forward=1

sudo ip netns exec one ping -c 5 10.0.2.1

# sudo ip netns exec one tc qdisc add dev mid0 root netem delay 100ms
# sudo ip netns exec r1 tc qdisc add dev mid1 root netem delay 100ms
# sudo ip netns exec one tc qdisc add dev eth0 root netem delay 100ms

sudo ip netns exec r1 tc qdisc change dev mid1 root tbf rate 100mbit latency 5ms burst 1kb
sudo ip netns exec r2 tc qdisc change dev mid2 root tbf rate 100mbit latency 5ms burst 1kb
sudo ip netns exec one tc qdisc change dev mid0 root tbf rate 100mbit latency 5ms burst 1kb
sudo ip netns exec two tc qdisc change dev mid3 root tbf rate 100mbit latency 5ms burst 1kb
sudo ip netns exec r2 tc qdisc change dev mid5 root tbf rate 100mbit latency 5ms burst 1kb
sudo ip netns exec r1 tc qdisc change dev mid4 root tbf rate 100mbit latency 5ms burst 1kb

# sudo ip netns exec one tc qdisc change dev mid0 root tbf rate 10mbit latency 40ms burst 1kb

sudo ip netns exec one ping -c 5 10.0.2.1