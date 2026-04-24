from mininet.topo import Topo

class SingleSwitchTopo(Topo):
    def build(self, n=2):

        # Create one switch (acts like router)
        s1 = self.addSwitch('s1')

        # Create n hosts dynamically
        for i in range(1, n + 1):
            host = self.addHost('h%s' % i)
            self.addLink(host, s1)

topos = {'single': SingleSwitchTopo}
