sudo ip netns add a
sudo ip netns add r

sudo ip link add 1 type veth peer name 2

sudo ip link set 1 netns a
sudo ip link set 2 netns r

sudo ip netns exec a ip link set lo up


sudo ip netns exec a ip link set 1 up
sudo ip netns exec r ip link set 2 up

sudo ip netns exec a ip address add 10.0.0.1/24 dev 1
sudo ip netns exec r ip address add 10.0.2.1/24 dev 2

//router

sudo ip netns exec a ip route add default via 10.0.2.1 dev 1

sudo ip netns exec r sysctl -w net.ipv4.ip_forward=1

sudo ip netns exec a tc qdisc add dev 2 root tbf rate 100mbit latency 2ms burst 10kb

sudo ip netns exec a ping -c 5 10.0.0.1

//bridge

sudo ip link add name br type bridge
sudo ip link set dev br up
sudo ip link set 2 master br