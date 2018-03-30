__author__='goldi'

class Network:
    def cable(self):
        print('I am the cable')
    def router(self):
        print('I am the router')
    def switch(self):
        print('I am the switch')
    def wifi(self):
        print('I am a wireless router,cable doesnt matter')

class TokenRing(Network):
    def cable(self):
        print('I am a token ring network cable')
    def router(self):
        print('I am a token ring network router')
class Ethernet(Network):
    def cable(self):
        print('I am ethernet cable')
    def router(self):
        print('I am ethernet router')
    def wifi(self):
        print('I am wifi for mac only')
def main():
    windows=TokenRing()
    mac=Ethernet()

    for obj in (windows, mac):
     obj.cable()
     obj.router()
     obj.wifi()
main()