from main import Main
from facter import facter
import libvirt
import json


class Host:
    def __init__(self, connection=Main().connection()):
        self.connection = connection

    def info(self):
        info = {}
        info.update(facter())
        info['model']      = self.connection.getInfo()[0]
        info['virtualizationType']    = self.connection.getType()
        info['libVersion']            = str(self.connection.getLibVersion())
        info['canonicalURI']          = self.connection.getURI()
        encrypted = self.connection.isEncrypted()
        if encrypted == 1:
            info['isConnectionEncrypted'] = True
        elif encrypted == 0:
            info['isConnectionEncrypted'] = False
        else:
            info['isConnectionEncrypted'] = 'unknown'
        secure = self.connection.isSecure()
        if secure == 1:
            info['isConnectionSecure'] = True
        elif secure == 0:
            info['isConnectionSecure'] = False
        else:
            info['isConnectionSecure'] = 'unknown'
        alive = self.connection.isAlive()
        if alive == 1:
            info['isConnectionAlive'] = True
        elif alive == 0:
            info['isConnectionAlive'] = False
        else:
            info['isConnectionAlive'] = 'unknown'

        #from xml.dom import minidom
        #xml = self.connection.getSysinfo()
        #xml_ = minidom.parseString(xml)
        #print(xml)

        self.connection.close()
        return info


    def metrics(self):
        pass


host = Host()

#print(host.info())
print(json.dumps(host.info(), indent=4, sort_keys=True))