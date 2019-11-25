sudo ip netns del red1
sudo ip netns del blue1
sudo ip netns del green1

sudo ip netns add red1
sudo ip netns add blue1
sudo ip netns add green1

sudo ip link add eth1 type veth peer name eth2
sudo ip link add eth3 type veth peer name eth4
sudo ip link add eth5 type veth peer name eth6

sudo ip link add ethb0 type veth peer name ethb1
sudo ip link add ethb2 type veth peer name ethb3
sudo ip link add ethb4 type veth peer name ethb5


# sudo ip netns exec red1 ip link set eth1 netns 1
# sudo ip netns exec blue1 ip link set eth3 netns 1
# sudo ip netns exec green1 ip link set eth5 netns 1

sudo ip link set eth1 netns red1
sudo ip link set eth3 netns blue1
sudo ip link set eth5 netns green1

sudo ip netns exec red1 ip link set lo up
sudo ip netns exec blue1 ip link set lo up
sudo ip netns exec green1 ip link set lo up

sudo ip netns exec red1 ip link set eth1 up
sudo ip netns exec blue1 ip link set eth3 up
sudo ip netns exec green1 ip link set eth5 up

sudo ip netns exec red1 ip address add 10.0.0.1/24 dev eth1
sudo ip netns exec blue1 ip address add 10.0.0.3/24 dev eth3
sudo ip netns exec green1 ip address add 10.0.0.5/24 dev eth5

sudo ip link add name br1 type bridge
sudo ip link set dev br1 up

sudo ip link add name br2 type bridge
sudo ip link set dev br2 up

sudo ip link add name br3 type bridge
sudo ip link set dev br3 up


sudo ip link set eth2 master br1
sudo ip link set eth4 master br2
sudo ip link set eth6 master br3

sudo ip link set ethb0 master br1
sudo ip link set ethb1 master br2
sudo ip link set ethb2 master br2
sudo ip link set ethb3 master br3

sudo ip link set dev eth2 up
sudo ip link set dev eth4 up
sudo ip link set dev eth6 up
sudo ip link set dev ethb0 up
sudo ip link set dev ethb1 up
sudo ip link set dev ethb2 up
sudo ip link set dev ethb3 up

sudo ip netns exec red1 ping 10.0.0.3