sudo ip netns del red
sudo ip netns del blue
sudo ip netns del green

sudo ip netns add red
sudo ip netns add blue
sudo ip netns add green

sudo ip link add veth0 type veth peer name veth1 
sudo ip link add veth2 type veth peer name veth3 
sudo ip link add veth4 type veth peer name veth5 

sudo ip link add b0 type veth peer name b1
sudo ip link add b2 type veth peer name b3
sudo ip link add b4 type veth peer name b5

sudo ip link set veth0 netns red
sudo ip link set veth2 netns blue
sudo ip link set veth4 netns green

sudo ip netns exec red ip link set lo up
sudo ip netns exec blue ip link set lo up
sudo ip netns exec green ip link set lo up

sudo ip netns exec red ip link set veth0 up
sudo ip netns exec blue ip link set veth2 up
sudo ip netns exec green ip link set veth4 up

sudo ip netns exec red ip address add 10.0.0.1/24 dev veth0 
sudo ip netns exec blue ip address add 10.0.0.3/24 dev veth2 
sudo ip netns exec green ip address add 10.0.0.5/24 dev veth4 

sudo ip link add name br0 type bridge
sudo ip link set dev br0 up
sudo ip link set veth1 master br0

sudo ip link add name br1 type bridge
sudo ip link set dev br1 up
sudo ip link set veth3 master br1

sudo ip link add name br2 type bridge
sudo ip link set dev br2 up
sudo ip link set veth5 master br2

sudo ip link set b0 master br0
sudo ip link set b1 master br1
sudo ip link set b2 master br2
sudo ip link set b3 master br0
sudo ip link set b4 master br1
sudo ip link set b5 master br2


sudo ip link set dev b0 up
sudo ip link set dev b1 up
sudo ip link set dev b2 up
sudo ip link set dev b3 up
sudo ip link set dev b4 up
sudo ip link set dev b5 up


sudo ip link set dev veth1 up
sudo ip link set dev veth3 up
sudo ip link set dev veth5 up

sudo ip netns exec red ping 10.0.0.5
